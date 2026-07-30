"""EN / FR / DE / IT / PT / ES / AR / ZH / RU micro-copy for the Streamlit demo.

Same language set and sidebar pattern as ICU Mortality and Where Needs Overlap.
"""

from __future__ import annotations

SUPPORTED_LANGS = ("en", "fr", "de", "it", "pt", "es", "ar", "zh", "ru")

LANGUAGE_LABELS: dict[str, str] = {
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "pt": "Português",
    "es": "Español",
    "ar": "العربية",
    "zh": "中文",
    "ru": "Русский",
}

# Super-population research labels (1000 Genomes).
SUPER_POP_KEYS = ("AFR", "AMR", "EAS", "EUR", "SAS")

COPY: dict[str, dict[str, str]] = {
    "en": {
        "lang": "Language",
        "sidebar_hint": "Switch language anytime. Everything on the page follows.",
        "sidebar_guide": "Explore the public panel, then load one genotype file for Trait profile and Ancestry.",
        "nav": "Pages",
        "page_explore": "Explore",
        "page_trait": "Trait profile",
        "page_ancestry": "Ancestry",
        "title": "SNP Trait Explorer",
        "subtitle": (
            "Turn raw SNP files into plain-English trait notes using public "
            "1000 Genomes genotypes and curated GWAS Catalog associations."
        ),
        "disclaimer_general": (
            "Learning tool on public research data. Not medical advice. "
            "Do not use it to make health decisions."
        ),
        "disclaimer_ancestry": (
            "An ancestry sketch from 15 SNPs is illustrative only. "
            "Consumer tests use hundreds of thousands of markers."
        ),
        "db_connected": "Connected to your database",
        "db_demo": "Demo mode (no database). Charts use public 1000 Genomes counts.",
        "file_ready_sidebar": "Genotype file ready for Trait profile and Ancestry.",
        "reset_session": "Clear loaded file",
        "upload_label": "Your genotype file",
        "upload_help": "23andMe raw .txt, or a CSV with columns rsid and genotype.",
        "upload_empty": "Load a sample, or upload your own file, to open a report.",
        "sample_button": "Try the sample file",
        "sample_loaded": "Sample file loaded. Trait profile and Ancestry share it.",
        "file_ready": "Using **{name}**. Clear it anytime.",
        "clear_file": "Clear file",
        "or_upload": "or upload your own",
        "parse_error": (
            "That file did not look like a genotype list. "
            "Use a 23andMe .txt export, or a CSV with rsid and genotype columns."
        ),
        "parse_empty": "No SNP rows found. Check the format and try again.",
        "reading_file": "Reading your file…",
        "building_profile": "Building your educational profile…",
        "comparing_ancestry": "Comparing your markers with 1000 Genomes patterns…",
        "markers_found": "Matched **{n}** of 15 educational markers in your file.",
        "trait_intro": (
            "Each card shows how many copies of a research-linked DNA letter "
            "appeared in your file. Grey on purpose: correlations, not good or bad scores."
        ),
        "trait_done": "Educational trait profile",
        "result_noncarrier": "Non-carrier",
        "result_one": "One copy",
        "result_two": "Two copies",
        "result_missing": "Missing",
        "ancestry_intro": (
            "The classifier compares your 15 marker dosages with allele-frequency "
            "patterns across continental research groups in 1000 Genomes."
        ),
        "ancestry_need_file": "Load a genotype file once; Trait profile and Ancestry share it.",
        "ancestry_result": "Closest match in this demo",
        "ancestry_proba": "Class probabilities across five research groups",
        "ancestry_drivers": "Markers that nudged this guess",
        "ancestry_top3": "Top three markers in plain words",
        "ancestry_driver_line": (
            "**{rsid}** near **{gene}**: your file has {copies} of the linked letter. "
            "This marker helps separate research ancestry groups."
        ),
        "copies_0": "no copies",
        "copies_1": "one copy",
        "copies_2": "two copies",
        "gene_fallback": "a nearby gene region",
        "model_missing": (
            "Ancestry model missing on disk. "
            "From the project folder run: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "No personal file needed. See who sits in the 1000 Genomes panel "
            "and how common the 15 curated markers are across research ancestry groups."
        ),
        "explore_tab_overview": "Who is in the data",
        "explore_tab_snp": "Compare one SNP",
        "explore_map_note": (
            "Map pins are illustrative country anchors for each research label, "
            "not a claim that a label equals a modern nation."
        ),
        "explore_snp_caption": (
            "Allele frequency is how often a DNA letter appears in a group. "
            "Pick a marker to compare research ancestry groups."
        ),
        "marker_select": "Marker",
        "chart_people": "People",
        "chart_counts_title": "People per research ancestry group",
        "chart_map_title": "Research labels on a map (illustrative)",
        "chart_maf_x": "How common the rarer letter is (MAF)",
        "chart_maf_y": "Number of markers",
        "chart_maf_title": "How rare or common the 15 markers are",
        "chart_af_y": "Frequency",
        "chart_af_title": "Alternate-letter frequency ({rsid})",
        "chart_proba_y": "Probability",
        "chart_contrib_x": "Relative nudge",
        "pop_AFR": "African",
        "pop_AMR": "Admixed American",
        "pop_EAS": "East Asian",
        "pop_EUR": "European",
        "pop_SAS": "South Asian",
        "snp_glossary": "SNP: a common single-letter DNA difference between people.",
    },
    "fr": {
        "lang": "Langue",
        "sidebar_hint": "Changez de langue à tout moment. Toute la page suit.",
        "sidebar_guide": "Explorez le panel public, puis chargez un fichier génotype pour le profil de traits et l'ancestralité.",
        "nav": "Pages",
        "page_explore": "Explorer",
        "page_trait": "Profil de traits",
        "page_ancestry": "Ancestralité",
        "title": "Explorateur de traits SNP",
        "subtitle": (
            "Transforme des fichiers SNP bruts en notes de traits en langage clair, "
            "avec les génotypes publics 1000 Genomes et des associations GWAS Catalog."
        ),
        "disclaimer_general": (
            "Outil pédagogique sur des données de recherche publiques. "
            "Pas un avis médical. Ne l'utilisez pas pour des décisions de santé."
        ),
        "disclaimer_ancestry": (
            "Une esquisse d'ancestralité à partir de 15 SNP est illustrative. "
            "Les tests grand public utilisent des centaines de milliers de marqueurs."
        ),
        "db_connected": "Connecté à votre base de données",
        "db_demo": "Mode démo (pas de base). Les graphiques utilisent les effectifs 1000 Genomes.",
        "file_ready_sidebar": "Fichier génotype prêt pour Profil de traits et Ancestralité.",
        "reset_session": "Effacer le fichier chargé",
        "upload_label": "Votre fichier génotype",
        "upload_help": "Export brut 23andMe (.txt), ou CSV avec colonnes rsid et genotype.",
        "upload_empty": "Chargez l'exemple, ou importez votre fichier, pour ouvrir un rapport.",
        "sample_button": "Essayer le fichier exemple",
        "sample_loaded": "Exemple chargé. Profil de traits et Ancestralité le partagent.",
        "file_ready": "Fichier **{name}**. Vous pouvez l'effacer à tout moment.",
        "clear_file": "Effacer",
        "or_upload": "ou importez le vôtre",
        "parse_error": (
            "Ce fichier ne ressemble pas à une liste de génotypes. "
            "Utilisez un export 23andMe .txt, ou un CSV avec rsid et genotype."
        ),
        "parse_empty": "Aucune ligne SNP trouvée. Vérifiez le format et réessayez.",
        "reading_file": "Lecture du fichier…",
        "building_profile": "Construction du profil pédagogique…",
        "comparing_ancestry": "Comparaison avec les motifs 1000 Genomes…",
        "markers_found": "**{n}** des 15 marqueurs pédagogiques trouvés dans votre fichier.",
        "trait_intro": (
            "Chaque carte indique combien de copies d'une lettre liée à la recherche "
            "apparaissent dans votre fichier. Gris volontairement: corrélations, pas de score bon/mauvais."
        ),
        "trait_done": "Profil de traits pédagogique",
        "result_noncarrier": "Non porteur",
        "result_one": "Une copie",
        "result_two": "Deux copies",
        "result_missing": "Manquant",
        "ancestry_intro": (
            "Le classifieur compare vos 15 dosages de marqueurs aux fréquences alléliques "
            "des groupes de recherche continentaux dans 1000 Genomes."
        ),
        "ancestry_need_file": "Chargez un fichier une fois; Profil de traits et Ancestralité le partagent.",
        "ancestry_result": "Correspondance la plus proche (démo)",
        "ancestry_proba": "Probabilités sur cinq groupes de recherche",
        "ancestry_drivers": "Marqueurs qui ont influencé cette estimation",
        "ancestry_top3": "Trois marqueurs principaux, en clair",
        "ancestry_driver_line": (
            "**{rsid}** près de **{gene}**: votre fichier a {copies} de la lettre liée. "
            "Ce marqueur aide à séparer les groupes d'ancestralité de recherche."
        ),
        "copies_0": "aucune copie",
        "copies_1": "une copie",
        "copies_2": "deux copies",
        "gene_fallback": "une région génique proche",
        "model_missing": (
            "Modèle d'ancestralité absent. "
            "Dans le dossier du projet: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "Aucun fichier personnel requis. Voyez qui compose le panel 1000 Genomes "
            "et à quel point les 15 marqueurs sont fréquents selon les groupes."
        ),
        "explore_tab_overview": "Qui est dans les données",
        "explore_tab_snp": "Comparer un SNP",
        "explore_map_note": (
            "Les points de carte sont des ancres pays illustratives pour chaque libellé de recherche, "
            "pas une équivalence avec une nation moderne."
        ),
        "explore_snp_caption": (
            "La fréquence allélique est la fréquence d'une lettre d'ADN dans un groupe. "
            "Choisissez un marqueur pour comparer les groupes."
        ),
        "marker_select": "Marqueur",
        "chart_people": "Personnes",
        "chart_counts_title": "Personnes par groupe d'ancestralité de recherche",
        "chart_map_title": "Libellés de recherche sur une carte (illustratif)",
        "chart_maf_x": "Fréquence de l'allèle rare (MAF)",
        "chart_maf_y": "Nombre de marqueurs",
        "chart_maf_title": "Rareté ou fréquence des 15 marqueurs",
        "chart_af_y": "Fréquence",
        "chart_af_title": "Fréquence de la lettre alternative ({rsid})",
        "chart_proba_y": "Probabilité",
        "chart_contrib_x": "Contribution relative",
        "pop_AFR": "Africain",
        "pop_AMR": "Américain admixed",
        "pop_EAS": "Est-asiatique",
        "pop_EUR": "Européen",
        "pop_SAS": "Sud-asiatique",
        "snp_glossary": "SNP: une différence d'ADN d'une lettre, fréquente entre individus.",
    },
    "de": {
        "lang": "Sprache",
        "sidebar_hint": "Sprache jederzeit wechseln. Die ganze Seite folgt.",
        "sidebar_guide": "Öffentliche Panel-Daten erkunden, dann eine Genotyp-Datei für Trait-Profil und Ancestry laden.",
        "nav": "Seiten",
        "page_explore": "Erkunden",
        "page_trait": "Merkmalsprofil",
        "page_ancestry": "Ancestry",
        "title": "SNP-Merkmals-Explorer",
        "subtitle": (
            "Wandelt rohe SNP-Dateien in verständliche Merkmalsnotizen um, "
            "mit öffentlichen 1000-Genomes-Genotypen und GWAS-Catalog-Assoziationen."
        ),
        "disclaimer_general": (
            "Lernwerkzeug auf öffentlichen Forschungsdaten. Keine medizinische Beratung. "
            "Nicht für Gesundheitsentscheidungen verwenden."
        ),
        "disclaimer_ancestry": (
            "Eine Ancestry-Skizze aus 15 SNPs ist nur illustrativ. "
            "Verbrauchertests nutzen Hunderttausende Marker."
        ),
        "db_connected": "Mit Ihrer Datenbank verbunden",
        "db_demo": "Demo-Modus (keine DB). Diagramme nutzen 1000-Genomes-Anzahlen.",
        "file_ready_sidebar": "Genotyp-Datei bereit für Merkmalsprofil und Ancestry.",
        "reset_session": "Geladene Datei löschen",
        "upload_label": "Ihre Genotyp-Datei",
        "upload_help": "23andMe-Rohdaten (.txt) oder CSV mit Spalten rsid und genotype.",
        "upload_empty": "Beispiel laden oder eigene Datei hochladen, um einen Bericht zu öffnen.",
        "sample_button": "Beispieldatei laden",
        "sample_loaded": "Beispiel geladen. Merkmalsprofil und Ancestry teilen sie.",
        "file_ready": "Datei **{name}**. Jederzeit löschbar.",
        "clear_file": "Löschen",
        "or_upload": "oder eigene Datei",
        "parse_error": (
            "Diese Datei sah nicht wie eine Genotyp-Liste aus. "
            "Nutzen Sie einen 23andMe-.txt-Export oder CSV mit rsid und genotype."
        ),
        "parse_empty": "Keine SNP-Zeilen gefunden. Format prüfen und erneut versuchen.",
        "reading_file": "Datei wird gelesen…",
        "building_profile": "Pädagogisches Profil wird erstellt…",
        "comparing_ancestry": "Vergleich mit 1000-Genomes-Mustern…",
        "markers_found": "**{n}** von 15 pädagogischen Markern in Ihrer Datei gefunden.",
        "trait_intro": (
            "Jede Karte zeigt, wie viele Kopien eines forschungsgebundenen DNA-Buchstabens "
            "in Ihrer Datei vorkommen. Grau absichtlich: Korrelationen, keine Gut/Schlecht-Scores."
        ),
        "trait_done": "Pädagogisches Merkmalsprofil",
        "result_noncarrier": "Kein Träger",
        "result_one": "Eine Kopie",
        "result_two": "Zwei Kopien",
        "result_missing": "Fehlend",
        "ancestry_intro": (
            "Der Klassifikator vergleicht Ihre 15 Marker-Dosierungen mit Allelfrequenz-Mustern "
            "kontinentaler Forschungsgruppen in 1000 Genomes."
        ),
        "ancestry_need_file": "Datei einmal laden; Merkmalsprofil und Ancestry teilen sie.",
        "ancestry_result": "Nächste Übereinstimmung in dieser Demo",
        "ancestry_proba": "Klassenwahrscheinlichkeiten über fünf Forschungsgruppen",
        "ancestry_drivers": "Marker, die diese Schätzung beeinflusst haben",
        "ancestry_top3": "Drei wichtigste Marker in Klartext",
        "ancestry_driver_line": (
            "**{rsid}** nahe **{gene}**: Ihre Datei hat {copies} des verknüpften Buchstabens. "
            "Dieser Marker hilft, Forschungs-Ancestry-Gruppen zu trennen."
        ),
        "copies_0": "keine Kopien",
        "copies_1": "eine Kopie",
        "copies_2": "zwei Kopien",
        "gene_fallback": "eine nahe Genregion",
        "model_missing": (
            "Ancestry-Modell fehlt. "
            "Im Projektordner: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "Keine persönliche Datei nötig. Sehen Sie, wer im 1000-Genomes-Panel ist "
            "und wie häufig die 15 Marker in Forschungsgruppen sind."
        ),
        "explore_tab_overview": "Wer steckt in den Daten",
        "explore_tab_snp": "Einen SNP vergleichen",
        "explore_map_note": (
            "Kartenpunkte sind illustrative Länderanker für Forschungs-Labels, "
            "keine Gleichsetzung mit modernen Staaten."
        ),
        "explore_snp_caption": (
            "Allelfrequenz ist, wie oft ein DNA-Buchstabe in einer Gruppe vorkommt. "
            "Wählen Sie einen Marker zum Vergleich."
        ),
        "marker_select": "Marker",
        "chart_people": "Personen",
        "chart_counts_title": "Personen je Forschungs-Ancestry-Gruppe",
        "chart_map_title": "Forschungslabels auf einer Karte (illustrativ)",
        "chart_maf_x": "Häufigkeit des selteneren Allels (MAF)",
        "chart_maf_y": "Anzahl Marker",
        "chart_maf_title": "Seltenheit oder Häufigkeit der 15 Marker",
        "chart_af_y": "Frequenz",
        "chart_af_title": "Frequenz des Alternativbuchstabens ({rsid})",
        "chart_proba_y": "Wahrscheinlichkeit",
        "chart_contrib_x": "Relativer Beitrag",
        "pop_AFR": "Afrikanisch",
        "pop_AMR": "Admixed American",
        "pop_EAS": "Ostasiatisch",
        "pop_EUR": "Europäisch",
        "pop_SAS": "Südasisch",
        "snp_glossary": "SNP: ein häufiger Ein-Buchstaben-Unterschied in der DNA zwischen Menschen.",
    },
    "it": {
        "lang": "Lingua",
        "sidebar_hint": "Cambia lingua quando vuoi. Tutta la pagina segue.",
        "sidebar_guide": "Esplora il panel pubblico, poi carica un file di genotipo per profilo tratti e ancestry.",
        "nav": "Pagine",
        "page_explore": "Esplora",
        "page_trait": "Profilo tratti",
        "page_ancestry": "Ancestry",
        "title": "Esploratore di tratti SNP",
        "subtitle": (
            "Trasforma file SNP grezzi in note sui tratti in linguaggio chiaro, "
            "con genotipi pubblici 1000 Genomes e associazioni GWAS Catalog."
        ),
        "disclaimer_general": (
            "Strumento didattico su dati di ricerca pubblici. Non è consiglio medico. "
            "Non usarlo per decisioni di salute."
        ),
        "disclaimer_ancestry": (
            "Uno schizzo di ancestry da 15 SNP è solo illustrativo. "
            "I test consumer usano centinaia di migliaia di marcatori."
        ),
        "db_connected": "Connesso al database",
        "db_demo": "Modalità demo (senza database). I grafici usano i conteggi 1000 Genomes.",
        "file_ready_sidebar": "File di genotipo pronto per Profilo tratti e Ancestry.",
        "reset_session": "Cancella file caricato",
        "upload_label": "Il tuo file di genotipo",
        "upload_help": "Export grezzo 23andMe (.txt), oppure CSV con colonne rsid e genotype.",
        "upload_empty": "Carica il campione, o il tuo file, per aprire un report.",
        "sample_button": "Prova il file di esempio",
        "sample_loaded": "Esempio caricato. Profilo tratti e Ancestry lo condividono.",
        "file_ready": "File **{name}**. Puoi cancellarlo in qualsiasi momento.",
        "clear_file": "Cancella",
        "or_upload": "oppure carica il tuo",
        "parse_error": (
            "Questo file non sembra un elenco di genotipi. "
            "Usa un export 23andMe .txt, o un CSV con rsid e genotype."
        ),
        "parse_empty": "Nessuna riga SNP trovata. Controlla il formato e riprova.",
        "reading_file": "Lettura del file…",
        "building_profile": "Creazione del profilo didattico…",
        "comparing_ancestry": "Confronto con i pattern 1000 Genomes…",
        "markers_found": "Trovati **{n}** dei 15 marcatori didattici nel tuo file.",
        "trait_intro": (
            "Ogni scheda mostra quante copie di una lettera DNA collegata alla ricerca "
            "compaiono nel file. Grigio di proposito: correlazioni, non punteggi buoni/cattivi."
        ),
        "trait_done": "Profilo tratti didattico",
        "result_noncarrier": "Non portatore",
        "result_one": "Una copia",
        "result_two": "Due copie",
        "result_missing": "Mancante",
        "ancestry_intro": (
            "Il classificatore confronta i tuoi 15 dosaggi di marcatori con le frequenze alleliche "
            "dei gruppi di ricerca continentali in 1000 Genomes."
        ),
        "ancestry_need_file": "Carica un file una volta; Profilo tratti e Ancestry lo condividono.",
        "ancestry_result": "Corrispondenza più vicina in questa demo",
        "ancestry_proba": "Probabilità di classe su cinque gruppi di ricerca",
        "ancestry_drivers": "Marcatori che hanno influenzato questa stima",
        "ancestry_top3": "Tre marcatori principali, in parole semplici",
        "ancestry_driver_line": (
            "**{rsid}** vicino a **{gene}**: il file ha {copies} della lettera collegata. "
            "Questo marcatore aiuta a separare i gruppi di ancestry di ricerca."
        ),
        "copies_0": "nessuna copia",
        "copies_1": "una copia",
        "copies_2": "due copie",
        "gene_fallback": "una regione genica vicina",
        "model_missing": (
            "Modello di ancestry assente. "
            "Nella cartella del progetto: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "Nessun file personale richiesto. Vedi chi è nel panel 1000 Genomes "
            "e quanto sono comuni i 15 marcatori tra i gruppi."
        ),
        "explore_tab_overview": "Chi è nei dati",
        "explore_tab_snp": "Confronta un SNP",
        "explore_map_note": (
            "I punti sulla mappa sono ancore paese illustrative per ogni etichetta di ricerca, "
            "non equivalgono a nazioni moderne."
        ),
        "explore_snp_caption": (
            "La frequenza allelica è quanto spesso una lettera DNA compare in un gruppo. "
            "Scegli un marcatore per confrontare."
        ),
        "marker_select": "Marcatore",
        "chart_people": "Persone",
        "chart_counts_title": "Persone per gruppo di ancestry di ricerca",
        "chart_map_title": "Etichette di ricerca su una mappa (illustrativo)",
        "chart_maf_x": "Quanto è comune l'allele raro (MAF)",
        "chart_maf_y": "Numero di marcatori",
        "chart_maf_title": "Rarità o frequenza dei 15 marcatori",
        "chart_af_y": "Frequenza",
        "chart_af_title": "Frequenza della lettera alternativa ({rsid})",
        "chart_proba_y": "Probabilità",
        "chart_contrib_x": "Contributo relativo",
        "pop_AFR": "Africano",
        "pop_AMR": "Americano admixed",
        "pop_EAS": "Est asiatico",
        "pop_EUR": "Europeo",
        "pop_SAS": "Sud asiatico",
        "snp_glossary": "SNP: una differenza DNA di una lettera, comune tra le persone.",
    },
    "es": {
        "lang": "Idioma",
        "sidebar_hint": "Cambie de idioma cuando quiera. Toda la página lo sigue.",
        "sidebar_guide": "Explore el panel público y luego cargue un archivo de genotipo para el perfil de rasgos y la ascendencia.",
        "nav": "Páginas",
        "page_explore": "Explorar",
        "page_trait": "Perfil de rasgos",
        "page_ancestry": "Ascendencia",
        "title": "Explorador de rasgos SNP",
        "subtitle": (
            "Convierte archivos SNP en bruto en notas de rasgos en lenguaje sencillo, "
            "usando genotipos públicos de 1000 Genomes y asociaciones seleccionadas del Catálogo GWAS."
        ),
        "disclaimer_general": (
            "Herramienta educativa sobre datos públicos de investigación. "
            "No es un consejo médico. No la use para tomar decisiones de salud."
        ),
        "disclaimer_ancestry": (
            "Un esbozo de ascendencia a partir de 15 SNP es solo ilustrativo. "
            "Las pruebas comerciales usan cientos de miles de marcadores."
        ),
        "db_connected": "Conectado a su base de datos",
        "db_demo": "Modo demo (sin base de datos). Los gráficos usan los recuentos públicos de 1000 Genomes.",
        "file_ready_sidebar": "Archivo de genotipo listo para Perfil de rasgos y Ascendencia.",
        "reset_session": "Borrar archivo cargado",
        "upload_label": "Su archivo de genotipo",
        "upload_help": "Exportación en bruto de 23andMe (.txt), o un CSV con las columnas rsid y genotype.",
        "upload_empty": "Cargue una muestra, o suba su propio archivo, para abrir un informe.",
        "sample_button": "Probar el archivo de muestra",
        "sample_loaded": "Archivo de muestra cargado. Perfil de rasgos y Ascendencia lo comparten.",
        "file_ready": "Usando **{name}**. Puede borrarlo cuando quiera.",
        "clear_file": "Borrar archivo",
        "or_upload": "o suba el suyo",
        "parse_error": (
            "Ese archivo no parecía una lista de genotipos. "
            "Use una exportación .txt de 23andMe, o un CSV con las columnas rsid y genotype."
        ),
        "parse_empty": "No se encontraron filas de SNP. Revise el formato e inténtelo de nuevo.",
        "reading_file": "Leyendo su archivo…",
        "building_profile": "Generando su perfil educativo…",
        "comparing_ancestry": "Comparando sus marcadores con los patrones de 1000 Genomes…",
        "markers_found": "Se encontraron **{n}** de 15 marcadores educativos en su archivo.",
        "trait_intro": (
            "Cada tarjeta muestra cuántas copias de una letra de ADN vinculada a la "
            "investigación aparecieron en su archivo. Gris a propósito: son correlaciones, "
            "no puntuaciones buenas o malas."
        ),
        "trait_done": "Perfil de rasgos educativo",
        "result_noncarrier": "No portador",
        "result_one": "Una copia",
        "result_two": "Dos copias",
        "result_missing": "Falta el dato",
        "ancestry_intro": (
            "El clasificador compara sus 15 dosis de marcadores con los patrones de "
            "frecuencia alélica de los grupos de investigación continentales en 1000 Genomes."
        ),
        "ancestry_need_file": "Cargue un archivo de genotipo una vez; Perfil de rasgos y Ascendencia lo comparten.",
        "ancestry_result": "Coincidencia más cercana en esta demo",
        "ancestry_proba": "Probabilidades de clase entre cinco grupos de investigación",
        "ancestry_drivers": "Marcadores que influyeron en esta estimación",
        "ancestry_top3": "Los tres marcadores principales en palabras sencillas",
        "ancestry_driver_line": (
            "**{rsid}** cerca de **{gene}**: su archivo tiene {copies} de la letra vinculada. "
            "Este marcador ayuda a separar los grupos de ascendencia de investigación."
        ),
        "copies_0": "ninguna copia",
        "copies_1": "una copia",
        "copies_2": "dos copias",
        "gene_fallback": "una región génica cercana",
        "model_missing": (
            "Falta el modelo de ascendencia en el disco. "
            "Desde la carpeta del proyecto ejecute: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "No se necesita ningún archivo personal. Vea quién forma parte del panel de "
            "1000 Genomes y qué tan comunes son los 15 marcadores seleccionados entre los "
            "grupos de ascendencia de investigación."
        ),
        "explore_tab_overview": "Quién está en los datos",
        "explore_tab_snp": "Comparar un SNP",
        "explore_map_note": (
            "Los marcadores del mapa son anclas de país ilustrativas para cada etiqueta de "
            "investigación, no una afirmación de que una etiqueta equivale a una nación moderna."
        ),
        "explore_snp_caption": (
            "La frecuencia alélica indica con qué frecuencia aparece una letra de ADN en "
            "un grupo. Elija un marcador para comparar los grupos de ascendencia de investigación."
        ),
        "marker_select": "Marcador",
        "chart_people": "Personas",
        "chart_counts_title": "Personas por grupo de ascendencia de investigación",
        "chart_map_title": "Etiquetas de investigación en un mapa (ilustrativo)",
        "chart_maf_x": "Qué tan común es la letra más rara (MAF)",
        "chart_maf_y": "Número de marcadores",
        "chart_maf_title": "Qué tan raros o comunes son los 15 marcadores",
        "chart_af_y": "Frecuencia",
        "chart_af_title": "Frecuencia de la letra alternativa ({rsid})",
        "chart_proba_y": "Probabilidad",
        "chart_contrib_x": "Contribución relativa",
        "pop_AFR": "Africana",
        "pop_AMR": "Americana mixta",
        "pop_EAS": "Asiática oriental",
        "pop_EUR": "Europea",
        "pop_SAS": "Asiática meridional",
        "snp_glossary": "SNP: una diferencia común de una sola letra de ADN entre personas.",
    },
    "ar": {
        "lang": "اللغة",
        "sidebar_hint": "يمكنك تغيير اللغة في أي وقت. تتبع الصفحة بأكملها هذا التغيير.",
        "sidebar_guide": "استكشف اللوحة العامة، ثم حمّل ملف نمط وراثي واحد لعرض ملف السمات ونسب الأصل.",
        "nav": "الصفحات",
        "page_explore": "استكشاف",
        "page_trait": "ملف السمات",
        "page_ancestry": "نسب الأصل",
        "title": "مستكشف سمات SNP",
        "subtitle": (
            "يحوّل ملفات SNP الخام إلى ملاحظات سمات بلغة بسيطة، باستخدام أنماط وراثية "
            "عامة من مشروع 1000 جينوم وارتباطات مختارة من كتالوج GWAS."
        ),
        "disclaimer_general": (
            "أداة تعليمية تعتمد على بيانات بحثية عامة. ليست استشارة طبية. "
            "لا تستخدمها لاتخاذ قرارات صحية."
        ),
        "disclaimer_ancestry": (
            "رسم تقريبي لنسب الأصل من 15 موضعًا وراثيًا (SNP) هو لأغراض توضيحية فقط. "
            "تستخدم الاختبارات الاستهلاكية مئات الآلاف من العلامات الوراثية."
        ),
        "db_connected": "متصل بقاعدة بياناتك",
        "db_demo": "وضع العرض التجريبي (بلا قاعدة بيانات). تستخدم الرسوم البيانية أعداد مشروع 1000 جينوم العامة.",
        "file_ready_sidebar": "ملف النمط الوراثي جاهز لملف السمات ونسب الأصل.",
        "reset_session": "مسح الملف المحمَّل",
        "upload_label": "ملف النمط الوراثي الخاص بك",
        "upload_help": "ملف 23andMe الخام بصيغة .txt، أو ملف CSV يحتوي على عمودي rsid وgenotype.",
        "upload_empty": "حمّل عينة، أو ارفع ملفك الخاص، لفتح تقرير.",
        "sample_button": "جرّب ملف العينة",
        "sample_loaded": "تم تحميل ملف العينة. يشترك فيه ملف السمات ونسب الأصل.",
        "file_ready": "يُستخدم الآن **{name}**. يمكنك مسحه في أي وقت.",
        "clear_file": "مسح الملف",
        "or_upload": "أو ارفع ملفك الخاص",
        "parse_error": (
            "لم يبدُ هذا الملف كقائمة أنماط وراثية. "
            "استخدم تصدير 23andMe بصيغة .txt، أو ملف CSV بعمودي rsid وgenotype."
        ),
        "parse_empty": "لم يُعثر على أي صفوف SNP. تحقق من الصيغة وحاول مرة أخرى.",
        "reading_file": "جارٍ قراءة ملفك…",
        "building_profile": "جارٍ إنشاء ملفك التعليمي…",
        "comparing_ancestry": "جارٍ مقارنة علاماتك الوراثية بأنماط مشروع 1000 جينوم…",
        "markers_found": "تمت مطابقة **{n}** من أصل 15 علامة تعليمية في ملفك.",
        "trait_intro": (
            "تُظهر كل بطاقة عدد نسخ حرف DNA المرتبط بالبحث العلمي الموجودة في ملفك. "
            "اللون الرمادي مقصود: هذه ارتباطات، وليست درجات جيدة أو سيئة."
        ),
        "trait_done": "ملف السمات التعليمي",
        "result_noncarrier": "غير حامل",
        "result_one": "نسخة واحدة",
        "result_two": "نسختان",
        "result_missing": "غير متوفر",
        "ancestry_intro": (
            "يقارن المصنِّف جرعات علاماتك الوراثية الخمس عشرة بأنماط تردد الأليل عبر "
            "مجموعات بحثية قارية في مشروع 1000 جينوم."
        ),
        "ancestry_need_file": "حمّل ملف النمط الوراثي مرة واحدة؛ يشترك فيه ملف السمات ونسب الأصل.",
        "ancestry_result": "أقرب تطابق في هذا العرض التجريبي",
        "ancestry_proba": "احتمالات الفئة عبر خمس مجموعات بحثية",
        "ancestry_drivers": "العلامات الوراثية التي أثّرت في هذا التخمين",
        "ancestry_top3": "أهم ثلاث علامات وراثية بكلمات بسيطة",
        "ancestry_driver_line": (
            "**{rsid}** بالقرب من **{gene}**: يحتوي ملفك على {copies} من الحرف المرتبط. "
            "تساعد هذه العلامة الوراثية في التمييز بين مجموعات نسب الأصل البحثية."
        ),
        "copies_0": "لا نسخ",
        "copies_1": "نسخة واحدة",
        "copies_2": "نسختان",
        "gene_fallback": "منطقة جينية قريبة",
        "model_missing": (
            "نموذج نسب الأصل غير موجود على القرص. "
            "من مجلد المشروع، شغّل: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "لا حاجة لأي ملف شخصي. اطّلع على تركيبة لوحة مشروع 1000 جينوم، ومدى شيوع "
            "العلامات الوراثية الخمس عشرة المختارة عبر مجموعات نسب الأصل البحثية."
        ),
        "explore_tab_overview": "من في البيانات",
        "explore_tab_snp": "قارن موضعًا وراثيًا واحدًا (SNP)",
        "explore_map_note": (
            "دبابيس الخريطة هي مراسي دول توضيحية لكل تصنيف بحثي، وليست ادعاءً بأن "
            "التصنيف يماثل دولة حديثة."
        ),
        "explore_snp_caption": (
            "تردد الأليل هو مدى تكرار ظهور حرف DNA في مجموعة ما. "
            "اختر علامة وراثية لمقارنة مجموعات نسب الأصل البحثية."
        ),
        "marker_select": "العلامة الوراثية",
        "chart_people": "الأشخاص",
        "chart_counts_title": "عدد الأشخاص لكل مجموعة نسب أصل بحثية",
        "chart_map_title": "التصنيفات البحثية على خريطة (توضيحي)",
        "chart_maf_x": "مدى شيوع الحرف الأندر (MAF)",
        "chart_maf_y": "عدد العلامات الوراثية",
        "chart_maf_title": "مدى ندرة أو شيوع العلامات الوراثية الخمس عشرة",
        "chart_af_y": "التردد",
        "chart_af_title": "تردد الحرف البديل ({rsid})",
        "chart_proba_y": "الاحتمال",
        "chart_contrib_x": "المساهمة النسبية",
        "pop_AFR": "أفريقية",
        "pop_AMR": "أمريكية مختلطة",
        "pop_EAS": "شرق آسيوية",
        "pop_EUR": "أوروبية",
        "pop_SAS": "جنوب آسيوية",
        "snp_glossary": "SNP: اختلاف شائع بحرف واحد في الحمض النووي بين الأشخاص.",
    },
    "zh": {
        "lang": "语言",
        "sidebar_hint": "可随时切换语言，整页内容会一起更新。",
        "sidebar_guide": "先浏览公开样本面板，再上传一份基因型文件，用于性状报告与祖先估计。",
        "nav": "页面",
        "page_explore": "浏览数据",
        "page_trait": "性状报告",
        "page_ancestry": "祖先估计",
        "title": "SNP 性状探索器",
        "subtitle": "把原始 SNP 文件变成通俗性状说明，基于公开的千人基因组数据与 GWAS Catalog 关联。",
        "disclaimer_general": "基于公开研究数据的学习工具，不是医疗建议，请勿据此做健康决策。",
        "disclaimer_ancestry": "仅用 15 个 SNP 做祖先估计只是示意。消费级检测通常使用数十万个位点。",
        "db_connected": "已连接数据库",
        "db_demo": "演示模式（无数据库）。图表使用千人基因组公开样本量。",
        "file_ready_sidebar": "基因型文件已就绪，可用于性状报告与祖先估计。",
        "reset_session": "清除已加载文件",
        "upload_label": "你的基因型文件",
        "upload_help": "23andMe 原始 .txt，或含 rsid、genotype 列的 CSV。",
        "upload_empty": "加载示例文件，或上传你自己的文件，以打开报告。",
        "sample_button": "试用示例文件",
        "sample_loaded": "示例已加载。性状报告与祖先估计共用该文件。",
        "file_ready": "正在使用 **{name}**。可随时清除。",
        "clear_file": "清除文件",
        "or_upload": "或上传自己的文件",
        "parse_error": "该文件不像基因型列表。请使用 23andMe .txt，或含 rsid 与 genotype 的 CSV。",
        "parse_empty": "未找到 SNP 行。请检查格式后重试。",
        "reading_file": "正在读取文件…",
        "building_profile": "正在生成教育性报告…",
        "comparing_ancestry": "正在与千人基因组模式比较…",
        "markers_found": "在你的文件中匹配到 **{n}** / 15 个教育性位点。",
        "trait_intro": "每张卡片显示研究相关 DNA 字母在你文件中的拷贝数。刻意使用灰色：这是相关，不是好坏评分。",
        "trait_done": "教育性性状报告",
        "result_noncarrier": "非携带",
        "result_one": "一个拷贝",
        "result_two": "两个拷贝",
        "result_missing": "缺失",
        "ancestry_intro": "分类器把你的 15 个位点剂量，与千人基因组各大洲研究群体的等位基因频率模式比较。",
        "ancestry_need_file": "加载一次基因型文件即可；性状报告与祖先估计共用。",
        "ancestry_result": "本演示中最接近的匹配",
        "ancestry_proba": "五个研究群体上的类别概率",
        "ancestry_drivers": "推动本次估计的位点",
        "ancestry_top3": "用白话看前三个位点",
        "ancestry_driver_line": "**{rsid}** 靠近 **{gene}**：你的文件中有{copies}相关字母。该位点有助于区分研究用祖先群体。",
        "copies_0": "零个拷贝",
        "copies_1": "一个拷贝",
        "copies_2": "两个拷贝",
        "gene_fallback": "附近基因区域",
        "model_missing": "磁盘上缺少祖先模型。请在项目目录运行：python ml/train_demo_model.py",
        "explore_intro": "无需个人文件。查看千人基因组面板构成，以及 15 个位点在各研究群体中的常见程度。",
        "explore_tab_overview": "数据里有谁",
        "explore_tab_snp": "比较一个 SNP",
        "explore_map_note": "地图锚点仅为各研究标签的示意国家，不等于现代国家身份。",
        "explore_snp_caption": "等位基因频率表示某个 DNA 字母在群体中出现的比例。选择一个位点进行比较。",
        "marker_select": "位点",
        "chart_people": "人数",
        "chart_counts_title": "各研究祖先群体人数",
        "chart_map_title": "研究标签示意地图",
        "chart_maf_x": "稀有等位基因频率 (MAF)",
        "chart_maf_y": "位点数",
        "chart_maf_title": "15 个位点的稀有/常见程度",
        "chart_af_y": "频率",
        "chart_af_title": "替代字母频率（{rsid}）",
        "chart_proba_y": "概率",
        "chart_contrib_x": "相对贡献",
        "pop_AFR": "非洲",
        "pop_AMR": "美洲混血",
        "pop_EAS": "东亚",
        "pop_EUR": "欧洲",
        "pop_SAS": "南亚",
        "snp_glossary": "SNP：人与人之间常见的单碱基 DNA 差异。",
    },
    "pt": {
        "lang": "Idioma",
        "sidebar_hint": "Mude o idioma a qualquer momento. A página inteira acompanha.",
        "sidebar_guide": "Explore o painel público e depois carregue um arquivo de genótipo para perfil de traços e ancestralidade.",
        "nav": "Páginas",
        "page_explore": "Explorar",
        "page_trait": "Perfil de traços",
        "page_ancestry": "Ancestralidade",
        "title": "Explorador de traços SNP",
        "subtitle": (
            "Converte arquivos SNP brutos em notas de traços em linguagem clara, "
            "com genótipos públicos do 1000 Genomes e associações do GWAS Catalog."
        ),
        "disclaimer_general": (
            "Ferramenta educativa com dados públicos de pesquisa. Não é conselho médico. "
            "Não use para decisões de saúde."
        ),
        "disclaimer_ancestry": (
            "Um esboço de ancestralidade com 15 SNPs é só ilustrativo. "
            "Testes comerciais usam centenas de milhares de marcadores."
        ),
        "db_connected": "Conectado à sua base de dados",
        "db_demo": "Modo demo (sem base). Os gráficos usam contagens do 1000 Genomes.",
        "file_ready_sidebar": "Arquivo de genótipo pronto para Perfil de traços e Ancestralidade.",
        "reset_session": "Limpar arquivo carregado",
        "upload_label": "Seu arquivo de genótipo",
        "upload_help": "Exportação bruta 23andMe (.txt), ou CSV com colunas rsid e genotype.",
        "upload_empty": "Carregue o exemplo, ou o seu arquivo, para abrir um relatório.",
        "sample_button": "Experimentar o arquivo de exemplo",
        "sample_loaded": "Exemplo carregado. Perfil de traços e Ancestralidade compartilham o arquivo.",
        "file_ready": "Usando **{name}**. Pode limpar a qualquer momento.",
        "clear_file": "Limpar",
        "or_upload": "ou envie o seu",
        "parse_error": (
            "Esse arquivo não parece uma lista de genótipos. "
            "Use um export 23andMe .txt, ou um CSV com rsid e genotype."
        ),
        "parse_empty": "Nenhuma linha SNP encontrada. Verifique o formato e tente de novo.",
        "reading_file": "Lendo o arquivo…",
        "building_profile": "Montando o perfil educativo…",
        "comparing_ancestry": "Comparando com padrões do 1000 Genomes…",
        "markers_found": "Encontrados **{n}** dos 15 marcadores educativos no seu arquivo.",
        "trait_intro": (
            "Cada cartão mostra quantas cópias de uma letra de DNA ligada à pesquisa "
            "aparecem no arquivo. Cinza de propósito: correlações, não notas bom/ruim."
        ),
        "trait_done": "Perfil de traços educativo",
        "result_noncarrier": "Não portador",
        "result_one": "Uma cópia",
        "result_two": "Duas cópias",
        "result_missing": "Ausente",
        "ancestry_intro": (
            "O classificador compara seus 15 dosages de marcadores com frequências alélicas "
            "dos grupos de pesquisa continentais no 1000 Genomes."
        ),
        "ancestry_need_file": "Carregue um arquivo uma vez; Perfil de traços e Ancestralidade compartilham.",
        "ancestry_result": "Correspondência mais próxima nesta demo",
        "ancestry_proba": "Probabilidades de classe em cinco grupos de pesquisa",
        "ancestry_drivers": "Marcadores que influenciaram esta estimativa",
        "ancestry_top3": "Três marcadores principais, em linguagem clara",
        "ancestry_driver_line": (
            "**{rsid}** perto de **{gene}**: seu arquivo tem {copies} da letra ligada. "
            "Este marcador ajuda a separar grupos de ancestralidade de pesquisa."
        ),
        "copies_0": "nenhuma cópia",
        "copies_1": "uma cópia",
        "copies_2": "duas cópias",
        "gene_fallback": "uma região gênica próxima",
        "model_missing": (
            "Modelo de ancestralidade ausente. "
            "Na pasta do projeto: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "Nenhum arquivo pessoal necessário. Veja quem está no painel 1000 Genomes "
            "e quão comuns são os 15 marcadores entre grupos."
        ),
        "explore_tab_overview": "Quem está nos dados",
        "explore_tab_snp": "Comparar um SNP",
        "explore_map_note": (
            "Os pontos no mapa são âncoras de país ilustrativas para cada rótulo de pesquisa, "
            "não equivalem a nações modernas."
        ),
        "explore_snp_caption": (
            "Frequência alélica é com que frequência uma letra de DNA aparece em um grupo. "
            "Escolha um marcador para comparar."
        ),
        "marker_select": "Marcador",
        "chart_people": "Pessoas",
        "chart_counts_title": "Pessoas por grupo de ancestralidade de pesquisa",
        "chart_map_title": "Rótulos de pesquisa em um mapa (ilustrativo)",
        "chart_maf_x": "Quão comum é o alelo raro (MAF)",
        "chart_maf_y": "Número de marcadores",
        "chart_maf_title": "Raridade ou frequência dos 15 marcadores",
        "chart_af_y": "Frequência",
        "chart_af_title": "Frequência da letra alternativa ({rsid})",
        "chart_proba_y": "Probabilidade",
        "chart_contrib_x": "Contribuição relativa",
        "pop_AFR": "Africano",
        "pop_AMR": "Americano admixed",
        "pop_EAS": "Leste asiático",
        "pop_EUR": "Europeu",
        "pop_SAS": "Sul asiático",
        "snp_glossary": "SNP: uma diferença comum de uma letra no DNA entre pessoas.",
    },
    "ru": {
        "lang": "Язык",
        "sidebar_hint": "Меняйте язык в любой момент. Вся страница обновится.",
        "sidebar_guide": "Изучите публичную панель, затем загрузите файл генотипов для профиля признаков и предков.",
        "nav": "Страницы",
        "page_explore": "Обзор",
        "page_trait": "Профиль признаков",
        "page_ancestry": "Происхождение",
        "title": "Исследователь признаков SNP",
        "subtitle": (
            "Превращает сырые SNP-файлы в понятные заметки о признаках "
            "на данных 1000 Genomes и ассоциациях GWAS Catalog."
        ),
        "disclaimer_general": (
            "Учебный инструмент на открытых исследовательских данных. Не медицинская рекомендация. "
            "Не используйте для решений о здоровье."
        ),
        "disclaimer_ancestry": (
            "Набросок происхождения по 15 SNP лишь иллюстративен. "
            "Потребительские тесты используют сотни тысяч маркеров."
        ),
        "db_connected": "Подключено к вашей базе данных",
        "db_demo": "Демо-режим (без БД). Графики используют численности 1000 Genomes.",
        "file_ready_sidebar": "Файл генотипов готов для профиля признаков и происхождения.",
        "reset_session": "Очистить загруженный файл",
        "upload_label": "Ваш файл генотипов",
        "upload_help": "Сырой экспорт 23andMe (.txt) или CSV со столбцами rsid и genotype.",
        "upload_empty": "Загрузите пример или свой файл, чтобы открыть отчёт.",
        "sample_button": "Попробовать пример",
        "sample_loaded": "Пример загружен. Профиль признаков и происхождение используют его вместе.",
        "file_ready": "Файл **{name}**. Можно очистить в любой момент.",
        "clear_file": "Очистить",
        "or_upload": "или загрузите свой",
        "parse_error": (
            "Файл не похож на список генотипов. "
            "Используйте экспорт 23andMe .txt или CSV с rsid и genotype."
        ),
        "parse_empty": "Строки SNP не найдены. Проверьте формат и попробуйте снова.",
        "reading_file": "Чтение файла…",
        "building_profile": "Сборка учебного профиля…",
        "comparing_ancestry": "Сравнение с паттернами 1000 Genomes…",
        "markers_found": "Найдено **{n}** из 15 учебных маркеров в вашем файле.",
        "trait_intro": (
            "Каждая карточка показывает, сколько копий исследовательской ДНК-буквы "
            "есть в файле. Серый цвет намеренно: корреляции, не оценки хорошо/плохо."
        ),
        "trait_done": "Учебный профиль признаков",
        "result_noncarrier": "Не носитель",
        "result_one": "Одна копия",
        "result_two": "Две копии",
        "result_missing": "Нет данных",
        "ancestry_intro": (
            "Классификатор сравнивает ваши 15 дозировок маркеров с частотами аллелей "
            "континентальных исследовательских групп в 1000 Genomes."
        ),
        "ancestry_need_file": "Загрузите файл один раз; профиль признаков и происхождение делят его.",
        "ancestry_result": "Ближайшее совпадение в этой демо",
        "ancestry_proba": "Вероятности классов по пяти исследовательским группам",
        "ancestry_drivers": "Маркеры, повлиявшие на эту оценку",
        "ancestry_top3": "Три главных маркера простыми словами",
        "ancestry_driver_line": (
            "**{rsid}** рядом с **{gene}**: в файле {copies} связанной буквы. "
            "Этот маркер помогает разделять исследовательские группы происхождения."
        ),
        "copies_0": "нет копий",
        "copies_1": "одна копия",
        "copies_2": "две копии",
        "gene_fallback": "близкая генная область",
        "model_missing": (
            "Модель происхождения отсутствует. "
            "В папке проекта: python ml/train_demo_model.py"
        ),
        "explore_intro": (
            "Личный файл не нужен. Посмотрите состав панели 1000 Genomes "
            "и насколько часты 15 маркеров в исследовательских группах."
        ),
        "explore_tab_overview": "Кто в данных",
        "explore_tab_snp": "Сравнить один SNP",
        "explore_map_note": (
            "Точки на карте — иллюстративные якоря стран для исследовательских меток, "
            "а не отождествление с современными государствами."
        ),
        "explore_snp_caption": (
            "Частота аллеля — как часто буква ДНК встречается в группе. "
            "Выберите маркер для сравнения."
        ),
        "marker_select": "Маркер",
        "chart_people": "Люди",
        "chart_counts_title": "Люди по исследовательским группам происхождения",
        "chart_map_title": "Исследовательские метки на карте (иллюстративно)",
        "chart_maf_x": "Насколько часта редкая буква (MAF)",
        "chart_maf_y": "Число маркеров",
        "chart_maf_title": "Редкость или частота 15 маркеров",
        "chart_af_y": "Частота",
        "chart_af_title": "Частота альтернативной буквы ({rsid})",
        "chart_proba_y": "Вероятность",
        "chart_contrib_x": "Относительный вклад",
        "pop_AFR": "Африканская",
        "pop_AMR": "Американская смешанная",
        "pop_EAS": "Восточноазиатская",
        "pop_EUR": "Европейская",
        "pop_SAS": "Южноазиатская",
        "snp_glossary": "SNP: распространённое различие ДНК в одну букву между людьми.",
    },
}


def normalize_lang(lang: str | None) -> str:
    """Return a supported language code from a control value."""
    if not lang:
        return "en"
    raw = str(lang).strip().lower()
    if raw in {"zh", "zh-cn", "zh-tw", "cn", "中文", "mandarin"}:
        return "zh"
    if raw in {"pt", "pt-br", "pt-pt", "portuguese", "português", "portugues"}:
        return "pt"
    if raw in {"ru", "ru-ru", "russian", "русский"}:
        return "ru"
    if raw in {"es", "es-es", "es-mx", "es-ar", "spanish", "español", "espanol"}:
        return "es"
    if raw in {"ar", "ar-sa", "ar-eg", "arabic", "العربية", "عربي"}:
        return "ar"
    code = raw[:2]
    if code in SUPPORTED_LANGS:
        return code
    return "en"


def t(key: str, lang: str = "en") -> str:
    """Look up a UI string; fall back to English, then the key itself."""
    lang = normalize_lang(lang)
    return COPY[lang].get(key, COPY["en"].get(key, key))


def tf(key: str, lang: str = "en", **kwargs: object) -> str:
    """Format a translated template string with keyword arguments."""
    return t(key, lang).format(**kwargs)


def population_label(code: str, lang: str = "en") -> str:
    """Return the localized label for a 1000 Genomes super-population code."""
    return t(f"pop_{code}", lang)


def dosage_result_label(dosage: int, lang: str = "en") -> str:
    """Map dosage 0/1/2 to a localized carrier label."""
    if dosage == 0:
        return t("result_noncarrier", lang)
    if dosage == 1:
        return t("result_one", lang)
    if dosage == 2:
        return t("result_two", lang)
    return t("result_missing", lang)


def copy_count_phrase(dosage: int, lang: str = "en") -> str:
    """Return a localized phrase for allele copy count."""
    key = {0: "copies_0", 1: "copies_1", 2: "copies_2"}.get(dosage)
    if key is None:
        return str(dosage)
    return t(key, lang)
