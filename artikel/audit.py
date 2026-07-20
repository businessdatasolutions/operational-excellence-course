"""Controleer dat de artikelen en het manifest niet uit elkaar zijn gelopen.

Draai dit voor publicatie, niet alleen na het schrijven. De controle is bewust
gesloten over het manifest: hij vangt losgeraakte legenda's en ontbrekende
figuren, maar kan niet weten dat de werkelijkheid is veranderd. Daarvoor is de
feitencontrole (zie README).
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
BESTANDEN = {
    (1, "nl"): "artikel-1-criteria-nl.md",
    (1, "en"): "artikel-1-criteria-en.md",
    (2, "nl"): "artikel-2-docent-nl.md",
    (2, "en"): "artikel-2-docent-en.md",
}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text())
    fouten: list[str] = []
    alle_ids = {f["id"] for f in manifest["figures"]}

    for (nummer, taal), naam in BESTANDEN.items():
        pad = ROOT / naam
        if not pad.exists():
            fouten.append(f"{naam}: ontbreekt")
            continue
        tekst = pad.read_text()
        figuren = [f for f in manifest["figures"] if f["artikel"] == nummer]

        verwacht = [f["id"] for f in figuren]
        gevonden = re.findall(r"!\[\]\(figures/([a-z0-9-]+)\.png\)", tekst)
        if gevonden != verwacht:
            fouten.append(f"{naam}: figuren {gevonden} != {verwacht}")

        for fig in figuren:
            if not (ROOT / "figures" / f"{fig['id']}.png").exists():
                fouten.append(f"{naam}: figures/{fig['id']}.png ontbreekt")
            for i, regel in enumerate(fig["legend"][taal], 1):
                if norm(regel) not in norm(tekst):
                    fouten.append(f"{naam}: legenda {fig['id']}#{i} staat niet in de tekst")

        # Em-dashes zijn in het Engels toegestaan; die regel is Nederlands.
        if taal == "nl" and (n := tekst.count("—")):
            fouten.append(f"{naam}: {n} em-dash(es), zie taalredactie sectie E")

        body = sum(
            len(r.split()) for r in tekst.split("\n")
            if not r.startswith(("**Fig", "#", "![", "*"))
        )
        print(f"  {naam:28} {len(gevonden)} figuren   {body:>5} woorden")

    wees = [p.name for p in (ROOT / "figures").glob("*.png") if p.stem not in alle_ids]
    if wees:
        fouten.append(f"weesbestanden in figures/: {wees}")

    if fouten:
        print("\nFOUTEN:")
        for f in fouten:
            print(f"  - {f}")
        sys.exit(1)
    print("\nAlles sluit.")


if __name__ == "__main__":
    main()
