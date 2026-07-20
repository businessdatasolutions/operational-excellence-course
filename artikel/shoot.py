"""Schiet schone screenshots van het OE-gate-systeem voor het artikel.

Schieten en annoteren zijn bewust twee scripts. Opnieuw schieten na een
UI-wijziging mag de annotaties niet overschrijven, en een rechthoekje tekenen
hoort geen draaiende browser en geen draaiende stack te vergen.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys

from playwright.sync_api import Page, sync_playwright

ROOT = pathlib.Path(__file__).parent
RAW = ROOT / "figures" / "raw"

# De capability-links komen uit de omgeving, nooit uit manifest.json: dat bestand
# gaat de git-geschiedenis in, en wie de link heeft is die student. Zie de
# module-toelichting in oe-gate-system/frontend/src/auth.ts.
LINK_ENV = {"student": "OE_LINK_STUDENT", "docent": "OE_LINK_DOCENT"}


def login(page: Page, base: str, rol: str) -> str:
    """Wissel het fragment-credential in; geef het team-id terug dat de server toekent.

    Er is geen netwerkrespons om op te wachten. Het credential staat in het
    URL-fragment, dat de browser nooit verstuurt: main.tsx leest het voor React
    mount en stript het uit de adresbalk. Het enige waarneembare signaal dat de
    inwisseling gelukt is, is dat /toegang ons wegstuurt.
    """
    credential = os.environ.get(LINK_ENV[rol])
    if not credential:
        sys.exit(f"Zet {LINK_ENV[rol]} in de omgeving. Zie .env.example.")

    page.goto(f"{base}/toegang#t={credential}")
    page.wait_for_url(lambda url: "/toegang" not in url, timeout=15_000)

    # OwnTeamGuard corrigeert :teamId naar wat het credential zegt, dus het
    # team-id uit de redirect is gezaghebbend en hoeft hier niet te staan.
    match = re.search(r"/team/([^/?#]+)", page.url)
    return match.group(1) if match else ""


def run_actions(page: Page, actions: list[dict]) -> None:
    """Breng de pagina in de toestand die de figuur moet tonen.

    Sommige schermen tonen pas iets na een handeling. Het kwaliteitsrapport is
    een leeg formulier tot je op genereren klikt, en het cohortveld staat
    standaard op een cohort waar de ingelogde docent niet bij hoort, dus zonder
    de fill levert de klik een 403 op in plaats van een rapport.
    """
    for action in actions:
        if "fill" in action:
            page.get_by_label(action["fill"]).fill(action["value"])
        elif "click" in action:
            page.click(action["click"])


# Documentcoordinaten, niet viewportcoordinaten: een full_page-schot begint bij
# de top van het document, dus de scrollpositie moet erbij. Voor een
# viewport-schot is scrollX/Y nul zolang we niet scrollen, dus dezelfde formule
# klopt in beide gevallen.
RECT_JS = """el => {
  const r = el.getBoundingClientRect();
  return {x: r.x + window.scrollX, y: r.y + window.scrollY, w: r.width, h: r.height};
}"""


def clip_rect(page: Page, selectors: list[str], pad: int = 24) -> dict:
    """Rechthoek van de bovenkant van het eerste element tot de onderkant van het tweede."""
    top = page.locator(selectors[0]).first.evaluate(RECT_JS)
    bottom = page.locator(selectors[1]).first.evaluate(RECT_JS)
    width = page.evaluate("() => document.documentElement.clientWidth")
    return {
        "x": 0,
        "y": max(0, top["y"] - pad),
        "width": width,
        "height": bottom["y"] + bottom["h"] - top["y"] + pad * 2,
    }


def measure(page: Page, fig: dict) -> list[dict]:
    """Lees de omhullende rechthoek van elke callout-target uit de levende DOM.

    Dit vervangt met de hand ingeschatte coordinaten. Die waren niet alleen
    monnikenwerk, ze verlopen ook stil: verschuift de UI een blok, dan wijst een
    ingetikt getal naar het verkeerde element zonder dat iets faalt. Een selector
    wijst na een herschot vanzelf weer het goede element aan, of hij knalt.
    """
    # Waar het kader relatief aan is, hangt af van wat er geschoten wordt: bij
    # `clip_to` is de oorsprong die uitsnede, niet de pagina. Zonder deze tak
    # wijzen alle callouts op zo'n figuur naar de verkeerde plek, en dat valt
    # pas op als je het beeld opent.
    origin = {"x": 0.0, "y": 0.0}
    if clip := fig.get("clip_to"):
        rect = page.locator(clip).first.evaluate(RECT_JS)
        size = {"w": rect["w"], "h": rect["h"]}
        origin = {"x": rect["x"], "y": rect["y"]}
    elif rng := fig.get("clip_range"):
        rect = clip_rect(page, rng)
        size = {"w": rect["width"], "h": rect["height"]}
        origin = {"x": rect["x"], "y": rect["y"]}
    elif fig.get("full_page"):
        size = page.evaluate(
            "() => ({w: document.documentElement.scrollWidth,"
            " h: document.documentElement.scrollHeight})"
        )
    else:
        size = {"w": page.viewport_size["width"], "h": page.viewport_size["height"]}

    boxes = []
    for callout in fig.get("callouts", []):
        target = page.locator(callout["target"]).first
        target.wait_for(state="attached", timeout=10_000)
        rect = target.evaluate(RECT_JS)
        rect = {**rect, "x": rect["x"] - origin["x"], "y": rect["y"] - origin["y"]}
        # Alleen geometrie, bewust geen badge-kant: waar de badge staat is een
        # presentatiekeuze en die hoort in het manifest. Zou hij hier meeliften,
        # dan vergde het verplaatsen van een badge een herschot met browser en
        # draaiende stack -- precies wat het splitsen van shoot en annotate moet
        # voorkomen. `target` gaat mee zodat annotate.py kan controleren dat hij
        # bij hetzelfde manifest hoort.
        boxes.append(
            {
                "target": callout["target"],
                "box": [
                    rect["x"] / size["w"],
                    rect["y"] / size["h"],
                    (rect["x"] + rect["w"]) / size["w"],
                    (rect["y"] + rect["h"]) / size["h"],
                ],
            }
        )
    return boxes


def shoot(page: Page, base: str, fig: dict, team: str, default_viewport: dict) -> None:
    # Een figuur mag een hogere viewport vragen. Dat is het alternatief voor
    # full_page op schermen waar de interessante blokken bovenaan staan en er
    # daaronder nog een halve pagina volgt die het argument niet dient: liever
    # het kader passend maken dan achteraf een lap wegsnijden. Altijd zetten,
    # ook zonder override: de viewport leeft op de page, dus zonder deze regel
    # erft de volgende figuur stilzwijgend de maat van de vorige.
    page.set_viewport_size(fig.get("viewport", default_viewport))

    # Een `url` is een volledige, externe bron (de publieke wiki); een `path`
    # hangt aan de lokale stack. De wiki is een aparte site met een eigen adres,
    # dus die base-url uit het manifest geldt daar niet.
    page.goto(fig.get("url") or base + fig["path"].replace("{team}", team))
    run_actions(page, fig.get("actions", []))

    # Bewust geen wait_until="networkidle": CheckpointView pollt elke 5 seconden
    # zolang gate A op 'assessing' staat, dus daar wordt het netwerk nooit stil
    # en verloopt de wachttijd. En `ready` is nooit een <h1>: die rendert hier
    # uit de route-params, dus hij staat er al terwijl de fetch nog loopt en het
    # scherm "Laden..." toont. Alleen een selector die de data zelf nodig heeft
    # bewijst dat de pagina af is.
    page.wait_for_selector(fig["ready"], state="visible", timeout=15_000)

    # `clip_to` snijdt de figuur af op een element in plaats van op de viewport.
    # Nodig zodra de bron een lange pagina is waarvan maar een sectie het
    # argument draagt: een schot van 4000 px waarin de lezer moet zoeken bewijst
    # minder dan een uitsnede van de alinea zelf.
    if fig.get("clip_to"):
        page.locator(fig["clip_to"]).first.screenshot(path=RAW / f"{fig['id']}.png")
    elif rng := fig.get("clip_range"):
        # Van de bovenkant van het ene element tot de onderkant van het andere.
        # Nodig omdat een markdown-pagina geen omhullend element per sectie
        # heeft: koppen en lijsten staan plat naast elkaar, dus er is niets om
        # op te clippen. Twee ankers beschrijven de sectie wel exact.
        page.screenshot(path=RAW / f"{fig['id']}.png", full_page=True, clip=clip_rect(page, rng))
    else:
        page.screenshot(path=RAW / f"{fig['id']}.png", full_page=fig.get("full_page", False))

    # De maten gaan naast de PNG mee. annotate.py hoeft dan geen browser te
    # openen en blijft een pure beeldstap.
    (RAW / f"{fig['id']}.boxes.json").write_text(json.dumps(measure(page, fig), indent=2))
    print(f"  {fig['id']}.png")


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text())
    base = os.environ.get("OE_BASE_URL", manifest["base_url"]).rstrip("/")
    RAW.mkdir(parents=True, exist_ok=True)

    # Optioneel: alleen deze figuur-id's schieten. Handig als er een figuur
    # bijkomt en de rest al klopt, en noodzakelijk voor de publieke wiki, die
    # geen draaiende stack nodig heeft terwijl de andere vijf dat wel doen.
    only = set(sys.argv[1:])
    if only:
        unknown = only - {f["id"] for f in manifest["figures"]}
        if unknown:
            sys.exit(f"onbekende figuur-id's: {', '.join(sorted(unknown))}")
        manifest["figures"] = [f for f in manifest["figures"] if f["id"] in only]

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        # "publiek" is de openbare wiki: een aparte site, zonder inlog. Die staat
        # bewust in dezelfde pijplijn en niet in een eigen scriptje, want het is
        # dezelfde beeldset met dezelfde legenda's en dezelfde audit.
        for rol in ("student", "docent", "publiek"):
            figures = [f for f in manifest["figures"] if f["rol"] == rol]
            if not figures:
                continue
            print(f"{rol}:")
            # Een context per rol. sessionStorage is per context, en de app houdt
            # bewust een credential per tab aan, ongeacht de rol (auth.ts). Twee
            # rollen in een context zouden elkaars credential overschrijven.
            context = browser.new_context(
                viewport=manifest["viewport"],
                device_scale_factor=2,  # scherp op retina en in de LinkedIn-feed
                reduced_motion="reduce",  # geen half-ingelopen transities in beeld
            )
            page = context.new_page()
            team = "" if rol == "publiek" else login(page, base, rol)
            for fig in figures:
                shoot(page, base, fig, team, manifest["viewport"])
            context.close()
        browser.close()


if __name__ == "__main__":
    main()
