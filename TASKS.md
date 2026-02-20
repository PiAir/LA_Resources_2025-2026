# TASKS.md - Project Doelen en Taken

## Hoofddoel
Het consolideren van verspreide bronmaterialen (PDF's en Xerte modules) tot een overzichtelijke, mobiel-vriendelijke webapplicatie die eenvoudig te distribueren is via een ZIP-bestand.

## Takenlijst

- [ ] **Inventarisatie & Analyse**
    - [ ] Mappenstructuur en bestandsnamen verifiëren (`Phd Mayari` en `LA_MOVEL_..`)
    - [ ] Inhoud van Xerte export analyseren (structuur van data/html)

- [ ] **Data Verwerking**
    - [ ] Map `pdfs` aanmaken
    - [ ] PDF's uit `Phd Mayari` indexeren en kopiëren naar `pdfs/`
    - [ ] Relevante data (afbeeldingen, links) extraheren uit `LA_MOVEL_..` (Xerte export)
    - [ ] Alle bronnen samenvoegen in `LA-2025-2026 bronnen.md` (Markdown format)

- [ ] **Webapp Ontwikkeling**
    - [ ] Ontwerp maken voor de Single Page Interface (HTML/CSS/JS)
    - [ ] `index.html` genereren op basis van de content in de Markdown lijst
    - [ ] Functionaliteit toevoegen (zoeken/filteren, responsiviteit)

- [ ] **Oplevering**
    - [ ] Structuur controleren (`index.html`, `pdfs/` map, eventuele andere assets)
    - [ ] Alles inpakken in een ZIP-bestand
    - [ ] Validatie van de werking van het ZIP-bestand
