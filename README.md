# Ortogon – web stavební a developerské firmy (koncept)

Interaktivní koncept webu brněnské stavební firmy, která dělá i development.

- 3D model stavby po fázích (three.js r128 z cdnjs), písmo Poppins
- reference s filtrem, výběr bytu v Nové Ponávce, kalkulačka ceny stavby, postup spolupráce, poptávkový formulář

Celý web je jeden soubor `index.html`. Zdroj je `src/artifact.html` (formát pro Claude artefakt, bez `<html>/<head>` obalu); `python3 build.py` z něj složí `index.html`.

Názvy projektů, čísla, ceny a kontakty jsou ilustrační. Formulář zatím nikam neodesílá.
