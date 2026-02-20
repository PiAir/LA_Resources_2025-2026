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
    -   Gebruik Python-scripts voor batch-acties (downloaden, screenshots, tekstextractie).

---

## 9. Template voor Toekomstige "Live Markdown Resource Hub" Projecten
Als dit project wordt hergebruikt voor een andere cursus, volg dan sterk de volgende architectuur en conventies:

### 9.1. Technische Architectuur & Core Stack
*   **Webapp:** Enkelvoudige `index.html` gebouwd met Vanilla HTML, CSS en JavaScript. Geen complexe frameworks (zoals React/Vue) tenzij expliciet verzocht.
*   **Markdown Parsing:** Gebruik `marked.js` om het centrale referentie Markdown (`.md`) bestand live via het client-side script om te zetten naar HTML. URL-encodeer spaties in markdown-links handmatig via RegEx vòòrdat `marked.js` ze parseert ter voorkoming van fouten in bestandsnamen met spaties.
*   **Python Tooling:** Gebruik Python-scripts uitsluitend voor eenmalige/iteratieve *dataverrijking* (door scripts in een `scripts/` map) in plaats van het lokaal draaien als een dynamische webserver backend.

### 9.2. UI/UX & Layout Eisen (in `index.html`)
*   **Structuur:** Bouw een responsieve layout (bijv. zijbalk navigatie links + scrollende content box rechts). Geef sectiekoppen (`<h2>`) een duidelijke contrastkleurige achtergrond.
*   **Kaarten Componenten (Cards):** Transformeer Markdown opsommingslijsten (`<ul>`) met bron-links realtime via DOM-manipulatie naar dynamische "Cards":
    *   *Thumbnails:* Controleer of het LI element al een markdown afbeelding bevat (`![alt](img)`). Zo nee, fallback naar een URL/PDF-bestandsnaam match in de `thumbnails/` map.
    *   *Titel en Beschrijving:* Gebruik de eerste link als fallback-titel. Zoek indien mogelijk naar rijkere titels (bijv. APA stijl cursieve tekst in `*italics*`)  in het tekstknooppunt van het lijst-item. Behoud de correcte HTML opmaak in de object-beschrijving.
    *   *Footer Tags*: Ontleed alle gevonden anker-tags. Scheid links naar documenten (`.pdf`) en normale externe hyperlinks visueel in losse download/link knoppen onderin de kaart.
*   **Uitzondering/Opt-out:** Sta lijsten toe om te ontsnappen uit de kaart-weergave als zij direct zijn voorafgegaan door, of de HTML snippet `<!-- no-cards -->` bevatten. Toon deze als platte HTML lijst.

### 9.3. Interactie & Navigatie
*   **TOC & Scroll-Spy:** Genereer het zijbalkmenu (Table of Contents) dynamisch op basis van de geneste `<h2>` koppen. Implementeer een JavaScript `IntersectionObserver` in de content box die de actuele scroll-view locatie identificeert en de overeenkomstige menu-item nav-link een actieve styling-class geeft.
*   **Realtime Zoeken:** Implementeer een invulveld in het menu dat de `.card` view list iteratief verbergt (`display: none`) zodra hun inhoud geen match vormt met de zoektekst in de invoer.
*   **Back-to-Top:** Voeg een verborgen "naar boven" knop toe via Fixed CSS placement, verschijnend on-scroll via JavaScript en met browser-native smooth scrolling ondersteuning.

### 9.4. Beheer & GitHub Delivery
*   Zorg altijd voor een zorgvuldige `.gitignore` die auteursrechtelijk beschermde PDF's blokkeert voordat een Git Repo ge-init wordt. 
*   Plaats als fallback in de uitgesloten data mappen altijd een losse `README.md` met uitleg + de filenamen als bestellijst.
*   Documenteer prominent in de Project README.md dat drag & drop of bestands-dubbelklikken door lokale `file://` CORS restricties onmogelijk is en localhost rendering via een webserver vereist.
