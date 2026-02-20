# Handleiding: Learning Analytics Webapp (V3 Live)

Deze map bevat de *Learning Analytics 2025-2026* webapplicatie. Deze applicatie is zo opgebouwd dat hij live de inhoud van een Markdown bestand (`.md`) inleest en omzet naar een mooie webpagina met "kaarten" (cards). 

Hieronder volgt een uitleg hoe je zelf de inhoud kunt aanpassen, nieuwe secties kunt tovoegen, en afbeeldingen of PDF's kunt beheren.

---

## 🚀 2. Lokale Installatie & Openen (CORS)

> ⚠️ **LET OP: Ontbrekende PDF-bestanden**
> Omdat dit project op een openbare GitHub repository (of vergelijkbare plek) staat, zijn de academische `.pdf` documenten niet meegeleverd wegens auteursrecht. Je moet deze zelf verzamelen en in de map `processed_content/pdfs/` plaatsen (zie `processed_content/pdfs/README.md` voor de ontbrekende namen). De webapp zal wel werken zonder de PDF's, maar de 'Download PDF' knoppen zullen resulteren in "bestand niet gevonden" (404) fouten tot je de pdf's in de map plaatst.

Omdat moderne webbrowsers om veiligheidsredenen (CORS restricties) niet toestaan dat scripts lokale bestanden uitlezen via het `file://` protocol, **werkt het niet meer als je simpelweg dubbelklikt op `index.html`**. Je krijgt dan een rood foutbericht in beeld.

**De Oplossing (Lokaal testen):**
Draai een lokale webserver.
1. **VS Code**: Open deze map (`processed_content` of de hoofdmap) in VS Code, installeer de extensie "Live Server" en klik rechtsonder op "Go Live" wanneer je `index.html` open hebt staan.
2. **Python**: Open Command Prompt (CMD) of PowerShell in de map `processed_content` en typ:  
   `python -m http.server`  
   Ga vervolgens in je browser naar: `http://localhost:8000`

*Tip: Als je deze inhoud online zet op een standaard webserver (bijv. een server van de HAN of GitHub Pages), dan werkt alles direct zonder deze stappen!*

---

## 📝 2. Inhoud Aanpassen (Het `.md` bestand)

Alle teksten, links en verwijzingen in de webapplicatie staan opgeslagen in één bestand:
👉 **`processed_content/LA-2025-2026 bronnen.md`**

Je kunt dit bestand openen met een teksteditor, zoals kladblok, of nog beter: in Visual Studio Code. De applicatie leest dit bestand de volgende keer dat je de webpagina ververst (refresh/F5) meteen in!

### Hoe de opmaak werkt (Markdown Basics)
Markdown is een simpele manier om tekst op te maken. De webapplicatie gebruikt deze opmaak om de kaarten en het menu te genereren.

*   `# Hoofdtitel` (Koppeniveau 1, bovenaan de pagina)
*   `## Nieuwe Sectie` (Koppeniveau 2, **belangrijk**: dit maakt automatisch een nieuw item in het linkermenu aan!)
*   `* ` (Een sterretje of streepje maakt een lijst-item. De applicatie zoekt naar links ín deze lijsten om kaarten te maken).
*   `[Naam van link](verwijzing.pdf)` of `[Naam van link](http://www.google.nl)` (Dit is de code om een link te maken).

---

## ➕ 3. Nieuwe Secties en Bronnen Toevoegen

Om de mooie "kaarten" of "cards" in de webapp te krijgen, moet je een hele specifieke structuur hanteren in Markdown: **een lijst met een link erin**.

### Voorbeeld: Een gewone weblink toevoegen
Zo voeg je een nieuwe sectie toe en zet je er een weblink in.

```markdown
## Mijn Nieuwe Sectie Toevoegen

Hier is een korte introductie tekst over dit onderwerp.

* [Website van Npuls](https://npuls.nl)
  Dit is de beschrijving die ónder de titel op de kaart komt te staan.
```

✅ **Resultaat:** 
1. Het menu links krijgt de optie "Mijn Nieuwe Sectie Toevoegen".
2. Er komt een titel en tekst in het hoofdscherm.
3. Er wordt een 'Card' (kaartje) gegenereerd getiteld "Website van Npuls", met een standaardafbeelding en daaronder de beschrijving.

### Voorbeeld: Een nieuw PDF-bestand toevoegen
Als je een PDF lokaal wilt aanbieden met een thumbnail-afbeelding (een kleine weergave van de eerste pagina), volg dan deze stappen.

**Stap 1: Zet de bestanden in de juiste mappen**
1. Kopieer je nieuwe PDF (bijv. `MijnNieuweRapport.pdf`) in de map `processed_content/pdfs/`.
2. Zorg voor een thumbnail afbeelding. Dit *moet* een `.png` bestand zijn dat **exact dezelfde naam** heeft als de PDF, met daaraan vast `.png`. 
   > Dus de thumbnail voor `MijnNieuweRapport.pdf` **moet heten**: `MijnNieuweRapport.pdf.png`.
3. Plaats deze afbeelding in de map `processed_content/thumbnails/`.

*(Opmerking: je kunt evtueel ook het python script `scripts/generate_thumbnails.py` uitvoeren om automatisch voor álle nieuwe PDF's de thumbnails te laten maken).*

**Stap 2: Zet de link in het Markdown bestand!**
```markdown
## PDF Sectie

* [Dit is het Nieuwe Rapport](pdfs/MijnNieuweRapport.pdf)
  Plaats hier een korte samenvatting van het rapport voor op de kaart.
```

✅ **Resultaat:** 
De applicatie herkent dat de link eindigt op `.pdf`. Hij maakt er een rode PDF-badge van en hij gaat automatisch op zoek naar afbeeling `thumbnails/MijnNieuweRapport.pdf.png`. Als hij de afbeelding niet kan vinden, toont hij een standaard-icoon.

### Voorbeeld: Een link met een eigen gekozen afbeelding
Als je een specifieke externe link hebt (zoals een website) en je wilt zélf bepalen welke afbeelding er op de kaart verschijnt, dan kun je een afbeelding direct in het lijst-item plaatsen! De webapp pakt deze afbeelding dan als 'thumbnail' voor de kaart.

```markdown
* ![Mijn Plaatje](media/mijn_afbeelding.jpg) [Website van het Ethiekkompas](https://wijzer.kennisnet.nl/ethiekkompas)
  Online tool waarmee je als team het gesprek kunt ondersteunen als het gaat om ethiek en data.
```

---

## 4. Uitzonderingen: Géén kaarten genereren

Soms wil je gewoon een simpele, ouderwetse opsommingslijst met linkjes maken, zonder dat de webapp er grote kaarten van probeert te maken.

Dat kan heel eenvoudig! Plaats de tekst `<!-- no-cards -->` ergens in of direct boven je opsommingslijst. De webapp zal deze lijst dan negeren en gewoon als platte tekst/links weergeven.

```markdown
<!-- no-cards -->
* [Normale link 1](https://google.nl)
* [Normale link 2](https://nu.nl)
```

---

## 🛠️ 5. Samenvattend: Regels voor de Kaarten
1. **De bron MOET een link zijn in een "opsomming" (`* ` of `- `).** 
2. De tekst van de link wordt de **titel** van de kaart.
3. Wil je een eigen afbeelding? Plaats deze dan als Markdown afbeelding `![alt](str)` in hetzelfde lijst-item.
4. De regel(s) tekst onder de link vormen de **beschrijving**.
5. Spaties in je bestandsnamen mogen gewoon. *(bijv. `pdfs/Mijn document.pdf` werkt prima).*
6. Om een lijst NIET om te zetten naar kaarten, voeg je `<!-- no-cards -->` toe aan de lijst.

**Vergeet na het opslaan van het `.md` bestand niet je browser met app te vernieuwen (F5)!**
