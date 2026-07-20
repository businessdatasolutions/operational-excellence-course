"""Teken genummerde callouts over de schone screenshots.

De tekst van een callout staat niet in de PNG maar in manifest.json, en gaat als
genummerde legenda onder de figuur het artikel in. Reden: tekst in pixels is niet
te vertalen zonder opnieuw te renderen, niet te doorzoeken, en onzichtbaar voor
een schermlezer. Zo draagt een beeldset zowel de Nederlandse als de Engelse versie.
"""
from __future__ import annotations

import json
import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).parent
RAW = ROOT / "figures" / "raw"
OUT = ROOT / "figures"

# Niet de huisstijlkleur. De UI gebruikt --han-pink (#e5007d) zelf voor
# gate-pending en groen voor gate-open, dus een annotatie in een van beide is
# niet te onderscheiden van de interface. Deze blauwtint komt in de UI nergens
# voor, en zegt daarmee vanzelf "dit is door de auteur toegevoegd".
CALLOUT = (11, 95, 255, 255)
HALO = (255, 255, 255, 255)

BADGE_R = 22  # straal in px, bij device_scale_factor=2
RING_W = 4
BOX_W = 4

FONT_CANDIDATES = [
    "/System/Library/Fonts/Helvetica.ttc",  # HAN-huisstijl is Arial/Helvetica
    "/Library/Fonts/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def load_font(size: int):
    for path in FONT_CANDIDATES:
        if pathlib.Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_badge(draw: ImageDraw.ImageDraw, x: int, y: int, n: int, font) -> None:
    # Witte ring buiten de badge: de callout landt soms op een lichte kaart en
    # soms op de bijna-zwarte footer. Een ring maakt hem op beide leesbaar
    # zonder per figuur een kleur te hoeven kiezen.
    draw.ellipse(
        [x - BADGE_R - RING_W, y - BADGE_R - RING_W, x + BADGE_R + RING_W, y + BADGE_R + RING_W],
        fill=HALO,
    )
    draw.ellipse([x - BADGE_R, y - BADGE_R, x + BADGE_R, y + BADGE_R], fill=CALLOUT)
    draw.text((x, y), str(n), font=font, fill=HALO, anchor="mm")


def badge_center(box: list[float], side: str, width: int, height: int) -> tuple[int, int]:
    """Zet de badge naast het kader, nooit erin.

    Een badge bovenop de inhoud dekt precies af wat hij moet aanwijzen, en dat
    is bij tekstblokken meteen een woord kwijt. Buiten de rand blijft het kader
    leesbaar en wijst de badge nog steeds ondubbelzinnig.
    """
    x0, y0, x1, y1 = box
    gap = (BADGE_R + RING_W * 2) / width
    if side == "right":
        return int((x1 + gap) * width), int((y0 + y1) / 2 * height)
    if side == "top":
        return int(x0 * width) + BADGE_R, int(y0 * height) - BADGE_R - RING_W * 2
    return int((x0 - gap) * width), int((y0 + y1) / 2 * height)


def annotate(fig: dict) -> None:
    src = RAW / f"{fig['id']}.png"
    boxes_path = RAW / f"{fig['id']}.boxes.json"
    if not src.exists() or not boxes_path.exists():
        raise SystemExit(f"{fig['id']}: schot of maten ontbreken. Draai eerst shoot.py.")

    image = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    width, height = image.size
    font = load_font(BADGE_R + 8)

    measured = json.loads(boxes_path.read_text())
    callouts = fig.get("callouts", [])
    if [m["target"] for m in measured] != [c["target"] for c in callouts]:
        raise SystemExit(
            f"{fig['id']}: de opgemeten targets wijken af van het manifest. "
            "Draai shoot.py opnieuw."
        )

    for index, (m, callout) in enumerate(zip(measured, callouts), start=1):
        # Geometrie komt uit de meting, de badge-kant uit het manifest. Zo is een
        # badge verplaatsen een kwestie van annotate.py opnieuw draaien.
        x0, y0, x1, y1 = m["box"]
        pad = BOX_W
        draw.rectangle(
            [x0 * width - pad, y0 * height - pad, x1 * width + pad, y1 * height + pad],
            outline=CALLOUT,
            width=BOX_W,
        )
        bx, by = badge_center(m["box"], callout.get("badge", "left"), width, height)
        draw_badge(draw, bx, by, index, font)

    Image.alpha_composite(image, overlay).convert("RGB").save(OUT / f"{fig['id']}.png")
    print(f"  {fig['id']}.png")


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    for fig in manifest["figures"]:
        annotate(fig)


if __name__ == "__main__":
    main()
