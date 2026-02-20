# AGENT.md - Project Principles

## Doelstelling
Het doel van dit project is het ontsluiten van bronmaterialen voor Learning Analytics (2025-2026) op een laagdrempelige en toegankelijke manier voor studenten.

## Uitgangspunten
1.  **Single Page Application (SPA):** Het eindresultaat is een webapplicatie die bestaat uit **één enkel HTML-bestand**.
2.  **Self-contained:** Alle CSS (styling) en JavaScript (logica) worden inline in het HTML-bestand opgenomen, zodat er geen externe afhankelijkheden zijn voor de werking van de app zelf (behalve de gelinkte bronbestanden).
3.  **Responsief Design:** De webapp moet volledig responsief zijn en goed werken op zowel desktop, tablet als mobiele apparaten.
4.  **Lokaal Opslaan:**
    -   Alle PDF-bronnen moeten lokaal worden opgeslagen in een submap (`pdfs/`).
    -   Indien een online bron een PDF betreft, wordt deze gedownload en lokaal aangeboden.
5.  **Visuele Rijkdom:**
    -   Alle items in de lijst moeten voorzien zijn van een afbeelding.
    -   Voor PDF's: Screenshot van de eerste pagina.
    -   Voor websites: Screenshot van de homepage.
    -   Gebruik tijdelijke Python-scripts waar nodig om deze screenshots te genereren.
6.  **Inhoudelijke Beschrijving:** Alle PDF-bestanden moeten voorzien zijn van een korte Nederlandse omschrijving.
7.  **Draagbaarheid:** Het eindproduct (HTML + bronbestanden) wordt aangeleverd als een **ZIP-bestand**.
8.  **Bronverwerking:** 
    -   Metadata wordt centraal beheerd (JSON in `index.html` of Markdown bronbestand).
    -   Gebruik Python-scripts voor batch-acties (downloaden, screenshots, tekstextractie).
