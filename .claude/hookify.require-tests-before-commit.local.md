---
name: require-tests-before-commit
enabled: true
event: bash
pattern: git\s+(commit|push)
action: warn
---

🚦 **Test-gate check — Operational Excellence buildplan**

Je staat op het punt te committen/pushen. Volgens `design-documents/buildplan.md` mag dat **alleen** nadat de test gate van de huidige main task succesvol is doorlopen — en pas ná een succesvolle push mag aan de volgende main task begonnen worden.

Bevestig, vóórdat je doorgaat:
1. Welke main task rondt deze commit af (zie `design-documents/buildplan.md`)?
2. Is de test gate van die main task **in dit gesprek** daadwerkelijk uitgevoerd en geslaagd — niet aangenomen, niet overgeslagen?
3. Is het bijbehorende taakvakje in `design-documents/buildplan.md` al afgevinkt (of vink je dat direct na deze commit af)?

Zo niet: voer eerst de tests van de huidige main task uit en los eventuele fouten op vóór je opnieuw commit/push probeert.

Deze waarschuwing blokkeert de actie niet automatisch — hookify kan geen testresultaten of exit-codes verifiëren, alleen het commando zelf herkennen. De verantwoordelijkheid om de test-gate-regel echt na te leven ligt bij jou als uitvoerende agent.
