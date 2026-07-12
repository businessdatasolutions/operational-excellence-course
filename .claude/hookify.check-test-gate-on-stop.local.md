---
name: check-test-gate-on-stop
enabled: true
event: stop
pattern: .*
action: warn
---

✅ **Voor je stopt — buildplan-checklist**

Als je zojuist aan een main task uit `design-documents/buildplan.md` hebt gewerkt, controleer voordat je stopt:

- [ ] Alle subtasks van deze main task zijn afgerond
- [ ] De test gate van deze main task is uitgevoerd en **geslaagd** (niet alleen gestart)
- [ ] De wijzigingen zijn gecommit én gepusht naar de remote
- [ ] Het taakvakje van deze main task in `design-documents/buildplan.md` is afgevinkt (`- [x]`)
- [ ] Je bent nog **niet** begonnen aan de volgende main task vóórdat de vorige gepusht was (sequentiële regel uit het buildplan)

Klopt een van deze niet? Rond dat eerst af, of meld expliciet en concreet aan de gebruiker wat nog open staat en waarom — verzin geen afgeronde status.
