"""Behind-the-numbers markdown blocks merged into COPY in src.i18n."""

from __future__ import annotations

METHODS: dict[str, dict[str, str]] = {
    "en": {
        "page_methods": "Behind the numbers",
        "about_intro": (
            "Methods, sources, glossary, and limits for people who want to "
            "peek under the hood."
        ),
        "methods_heading": "How the numbers are built",
        "sources_heading": "Where the data comes from",
        "limits_heading": "Care and limits",
        "glossary_heading": "Words we use on purpose",
        "methods_md": """- **Join key:** SNP rsIDs (never free-text trait names).
- **Panel:** 1000 Genomes Project phase 3, chromosome 22 genotypes + super-population labels.
- **Trait layer:** 15 curated non-medical GWAS Catalog associations on chr22 (discovery N typically > 10,000).
- **Dosage:** 0 / 1 / 2 copies of the effect allele from the uploaded genotype.
- **Trait score:** `dosage × {+1, −1, 0}` effect direction. Transparent rule, not an ML trait model.
- **Ancestry sketch:** Random Forest on the same 15 dosages → AFR / AMR / EAS / EUR / SAS labels, with feature-importance drivers.
- **Demo mode:** bundled panel counts + committed `models/ancestry_clf.joblib` when Postgres is absent.

More detail lives in `docs/methods.md` and `docs/CONCEPTS.md`.
""",
        "sources_md": """- **1000 Genomes Project phase 3**, chr22 multi-sample VCF and sample panel (EBI FTP public release)
- **GWAS Catalog**, curated non-medical SNP–trait pairs on chr22
- **Bundled demo genotypes** in `data/sample/` for UI walkthroughs without a personal kit export
""",
        "limits_md": """- Public research aggregates and educational uploads only; not a clinical test
- Fifteen markers cannot replace consumer ancestry products (hundreds of thousands of SNPs)
- Chromosome 22 scope: classic traits on other chromosomes are out of range on purpose
- Research ancestry labels are study constructs, not modern nationality claims
- This is a **portfolio learning project**, not a hospital, lab, or consumer-genomics product

Longer biology primer: `docs/CONCEPTS.md`.
""",
        "glossary_md": """| Term | Plain meaning |
|------|----------------|
| **SNP** | A common single-letter DNA difference between people |
| **Allele** | One possible letter at a SNP (for example A or G) |
| **Dosage** | How many copies of the effect allele (0, 1, or 2) |
| **MAF** | How common the rarer letter is in a group (0 to 0.5) |
| **rsID** | Public catalogue name for a SNP (always starts with `rs`) |
| **Super-population** | Broad 1000 Genomes research label (AFR, AMR, EAS, EUR, SAS) |
| **Association** | Population correlation from GWAS, not proof of personal causation |
""",
    },
    "fr": {
        "page_methods": "Derrière les chiffres",
        "about_intro": (
            "Méthodes, sources, glossaire et limites pour qui veut regarder sous le capot."
        ),
        "methods_heading": "Comment les chiffres sont construits",
        "sources_heading": "D’où viennent les données",
        "limits_heading": "Précautions et limites",
        "glossary_heading": "Mots que nous utilisons à dessein",
        "methods_md": """- **Clé de jointure :** rsID des SNP (jamais des noms de traits en texte libre).
- **Panel :** 1000 Genomes phase 3, génotypes du chromosome 22 + libellés de super-population.
- **Couche traits :** 15 associations non médicales du GWAS Catalog sur chr22 (N de découverte souvent > 10 000).
- **Dosage :** 0 / 1 / 2 copies de l’allèle d’effet depuis le fichier chargé.
- **Score de trait :** `dosage × {+1, −1, 0}`. Règle transparente, pas un modèle ML de trait.
- **Esquisse d’ancestralité :** forêt aléatoire sur les 15 dosages → libellés AFR / AMR / EAS / EUR / SAS, avec drivers d’importance.
- **Mode démo :** totaux de panel fournis + `models/ancestry_clf.joblib` si Postgres est absent.

Plus de détail dans `docs/methods.md` et `docs/CONCEPTS.md`.
""",
        "sources_md": """- **1000 Genomes Project phase 3**, VCF multi-échantillons chr22 et panel (FTP EBI)
- **GWAS Catalog**, paires SNP–trait non médicales sur chr22
- **Génotypes de démo** dans `data/sample/` pour parcourir l’UI sans kit personnel
""",
        "limits_md": """- Agrégats de recherche publics et chargements éducatifs seulement ; pas un test clinique
- Quinze marqueurs ne remplacent pas les tests d’ancestralité grand public
- Périmètre chromosome 22 : les traits classiques sur d’autres chromosomes sont hors champ volontairement
- Les libellés d’ancestralité de recherche ne sont pas des nationalités modernes
- **Projet d’apprentissage portfolio**, pas un produit hôpital / labo / génomique grand public

Primer biologie : `docs/CONCEPTS.md`.
""",
        "glossary_md": """| Terme | Sens simple |
|------|-------------|
| **SNP** | Différence d’ADN d’une lettre, fréquente entre individus |
| **Allèle** | Une lettre possible à un SNP (par ex. A ou G) |
| **Dosage** | Nombre de copies de l’allèle d’effet (0, 1 ou 2) |
| **MAF** | Fréquence de la lettre plus rare dans un groupe (0 à 0,5) |
| **rsID** | Nom catalogue public d’un SNP (commence par `rs`) |
| **Super-population** | Grand libellé 1000 Genomes (AFR, AMR, EAS, EUR, SAS) |
| **Association** | Corrélation populationnelle GWAS, pas une preuve individuelle |
""",
    },
    "de": {
        "page_methods": "Hinter den Zahlen",
        "about_intro": (
            "Methoden, Quellen, Glossar und Grenzen für alle, die unter die Haube schauen wollen."
        ),
        "methods_heading": "So entstehen die Zahlen",
        "sources_heading": "Woher die Daten kommen",
        "limits_heading": "Sorgfalt und Grenzen",
        "glossary_heading": "Wörter, die wir bewusst verwenden",
        "methods_md": """- **Join-Schlüssel:** SNP-rsIDs (nie freie Merkmalsnamen).
- **Panel:** 1000 Genomes Phase 3, Chr22-Genotypen + Superpopulations-Labels.
- **Merkmalslayer:** 15 kuratierte nicht-medizinische GWAS-Catalog-Assoziationen auf Chr22.
- **Dosage:** 0 / 1 / 2 Kopien des Effektallels aus der hochgeladenen Datei.
- **Merkmalsscore:** `dosage × {+1, −1, 0}`. Transparente Regel, kein ML-Merkmalsmodell.
- **Ancestry-Skizze:** Random Forest auf denselben 15 Dosages → AFR / AMR / EAS / EUR / SAS.
- **Demo-Modus:** gebündelte Panelzahlen + committed `models/ancestry_clf.joblib` ohne Postgres.

Mehr in `docs/methods.md` und `docs/CONCEPTS.md`.
""",
        "sources_md": """- **1000 Genomes Project Phase 3**, Chr22-VCF und Sample-Panel (EBI-FTP)
- **GWAS Catalog**, nicht-medizinische SNP–Merkmal-Paare auf Chr22
- **Demo-Genotypen** in `data/sample/` für UI-Demos ohne persönlichen Kit-Export
""",
        "limits_md": """- Nur öffentliche Forschungsaggregate und Bildungs-Uploads; kein klinischer Test
- Fünfzehn Marker ersetzen keine Consumer-Ancestry-Produkte
- Nur Chromosom 22: klassische Merkmale auf anderen Chromosomen bewusst ausgelassen
- Forschungs-Ancestry-Labels sind Studienkonstrukte, keine modernen Nationalitäten
- **Portfolio-Lernprojekt**, kein Klinik-/Labor-/Consumer-Genomik-Produkt

Biologie-Primer: `docs/CONCEPTS.md`.
""",
        "glossary_md": """| Begriff | Kurz erklärt |
|---------|--------------|
| **SNP** | Häufiger Ein-Buchstaben-Unterschied in der DNA |
| **Allel** | Mögliche DNA-Buchstabe an einem SNP |
| **Dosage** | Anzahl Kopien des Effektallels (0, 1 oder 2) |
| **MAF** | Häufigkeit des selteneren Allels in einer Gruppe |
| **rsID** | Öffentlicher Katalogname eines SNP (beginnt mit `rs`) |
| **Superpopulation** | Breites 1000-Genomes-Label (AFR, AMR, EAS, EUR, SAS) |
| **Assoziation** | Populationskorrelation aus GWAS, kein individueller Kausalnachweis |
""",
    },
    "it": {
        "page_methods": "Dietro i numeri",
        "about_intro": (
            "Metodi, fonti, glossario e limiti per chi vuole guardare sotto il cofano."
        ),
        "methods_heading": "Come sono costruiti i numeri",
        "sources_heading": "Da dove arrivano i dati",
        "limits_heading": "Cautela e limiti",
        "glossary_heading": "Parole che usiamo di proposito",
        "methods_md": """- **Chiave di join:** rsID degli SNP (mai nomi di tratti in testo libero).
- **Panel:** 1000 Genomes fase 3, genotipi del cromosoma 22 + etichette di super-popolazione.
- **Layer tratti:** 15 associazioni non mediche del GWAS Catalog su chr22.
- **Dosage:** 0 / 1 / 2 copie dell’allele di effetto dal file caricato.
- **Punteggio tratto:** `dosage × {+1, −1, 0}`. Regola trasparente, non un modello ML.
- **Bozza di ancestry:** Random Forest sugli stessi 15 dosage → AFR / AMR / EAS / EUR / SAS.
- **Modalità demo:** conteggi panel in bundle + `models/ancestry_clf.joblib` senza Postgres.

Dettagli in `docs/methods.md` e `docs/CONCEPTS.md`.
""",
        "sources_md": """- **1000 Genomes Project fase 3**, VCF multi-campione chr22 e panel (FTP EBI)
- **GWAS Catalog**, coppie SNP–tratto non mediche su chr22
- **Genotipi demo** in `data/sample/` per l’UI senza export personale
""",
        "limits_md": """- Solo aggregati di ricerca pubblici e upload educativi; non un test clinico
- Quindici marcatori non sostituiscono i test ancestry consumer
- Ambito cromosoma 22: tratti classici su altri cromosomi esclusi di proposito
- Le etichette ancestry di ricerca non sono nazionalità moderne
- **Progetto portfolio didattico**, non un prodotto ospedale / laboratorio / genomica consumer

Primer di biologia: `docs/CONCEPTS.md`.
""",
        "glossary_md": """| Termine | Significato semplice |
|---------|----------------------|
| **SNP** | Differenza DNA di una lettera, comune tra le persone |
| **Allele** | Una lettera possibile a uno SNP |
| **Dosage** | Copie dell’allele di effetto (0, 1 o 2) |
| **MAF** | Quanto è comune la lettera più rara in un gruppo |
| **rsID** | Nome catalogo pubblico di uno SNP (inizia con `rs`) |
| **Super-popolazione** | Etichetta ampia 1000 Genomes (AFR, AMR, EAS, EUR, SAS) |
| **Associazione** | Correlazione di popolazione da GWAS, non prova causale individuale |
""",
    },
    "pt": {
        "page_methods": "Por trás dos números",
        "about_intro": (
            "Métodos, fontes, glossário e limites para quem quer olhar por baixo do capô."
        ),
        "methods_heading": "Como os números são construídos",
        "sources_heading": "De onde vêm os dados",
        "limits_heading": "Cuidados e limites",
        "glossary_heading": "Palavras que usamos de propósito",
        "methods_md": """- **Chave de junção:** rsIDs dos SNPs (nunca nomes de traços em texto livre).
- **Painel:** 1000 Genomes fase 3, genótipos do cromossomo 22 + rótulos de superpopulação.
- **Camada de traços:** 15 associações não médicas do GWAS Catalog no chr22.
- **Dosage:** 0 / 1 / 2 cópias do alelo de efeito a partir do arquivo carregado.
- **Pontuação de traço:** `dosage × {+1, −1, 0}`. Regra transparente, não um modelo ML.
- **Esboço de ancestralidade:** Random Forest nos mesmos 15 dosages → AFR / AMR / EAS / EUR / SAS.
- **Modo demo:** totais do painel + `models/ancestry_clf.joblib` sem Postgres.

Mais detalhe em `docs/methods.md` e `docs/CONCEPTS.md`.
""",
        "sources_md": """- **1000 Genomes Project fase 3**, VCF multi-amostra chr22 e painel (FTP EBI)
- **GWAS Catalog**, pares SNP–traço não médicos no chr22
- **Genótipos demo** em `data/sample/` para a UI sem export pessoal
""",
        "limits_md": """- Apenas agregados públicos de pesquisa e uploads educativos; não é teste clínico
- Quinze marcadores não substituem testes de ancestralidade de consumo
- Âmbito cromossomo 22: traços clássicos noutros cromossomos ficam de fora de propósito
- Rótulos de ancestralidade de pesquisa não são nacionalidades modernas
- **Projeto portfolio educativo**, não um produto hospitalar / laboratorial / genómica de consumo

Primer de biologia: `docs/CONCEPTS.md`.
""",
        "glossary_md": """| Termo | Significado simples |
|-------|---------------------|
| **SNP** | Diferença comum de uma letra no DNA entre pessoas |
| **Alelo** | Uma letra possível num SNP |
| **Dosage** | Cópias do alelo de efeito (0, 1 ou 2) |
| **MAF** | Quão comum é a letra mais rara num grupo |
| **rsID** | Nome de catálogo público de um SNP (começa por `rs`) |
| **Superpopulação** | Rótulo amplo do 1000 Genomes (AFR, AMR, EAS, EUR, SAS) |
| **Associação** | Correlação populacional de GWAS, não prova causal individual |
""",
    },
    "es": {
        "page_methods": "Detrás de las cifras",
        "about_intro": (
            "Métodos, fuentes, glosario y límites para quien quiera mirar bajo el capó."
        ),
        "methods_heading": "Cómo se construyen los números",
        "sources_heading": "De dónde salen los datos",
        "limits_heading": "Cuidado y límites",
        "glossary_heading": "Palabras que usamos a propósito",
        "methods_md": """- **Clave de unión:** rsID de los SNP (nunca nombres de rasgos en texto libre).
- **Panel:** 1000 Genomes fase 3, genotipos del cromosoma 22 + etiquetas de superpoblación.
- **Capa de rasgos:** 15 asociaciones no médicas del GWAS Catalog en chr22.
- **Dosage:** 0 / 1 / 2 copias del alelo de efecto desde el archivo cargado.
- **Puntuación de rasgo:** `dosage × {+1, −1, 0}`. Regla transparente, no un modelo ML.
- **Boceto de ancestría:** Random Forest sobre los mismos 15 dosages → AFR / AMR / EAS / EUR / SAS.
- **Modo demo:** totales del panel + `models/ancestry_clf.joblib` sin Postgres.

Más detalle en `docs/methods.md` y `docs/CONCEPTS.md`.
""",
        "sources_md": """- **1000 Genomes Project fase 3**, VCF multi-muestra chr22 y panel (FTP EBI)
- **GWAS Catalog**, pares SNP–rasgo no médicos en chr22
- **Genotipos demo** en `data/sample/` para la UI sin exportación personal
""",
        "limits_md": """- Solo agregados públicos de investigación y cargas educativas; no es una prueba clínica
- Quince marcadores no sustituyen los tests de ancestría de consumo
- Ámbito cromosoma 22: rasgos clásicos en otros cromosomas quedan fuera a propósito
- Las etiquetas de ancestría de investigación no son nacionalidades modernas
- **Proyecto portfolio educativo**, no un producto hospital / laboratorio / genómica de consumo

Primer de biología: `docs/CONCEPTS.md`.
""",
        "glossary_md": """| Término | Significado sencillo |
|---------|----------------------|
| **SNP** | Diferencia común de una letra de ADN entre personas |
| **Alelo** | Una letra posible en un SNP |
| **Dosage** | Copias del alelo de efecto (0, 1 o 2) |
| **MAF** | Qué tan común es la letra más rara en un grupo |
| **rsID** | Nombre de catálogo público de un SNP (empieza por `rs`) |
| **Superpoblación** | Etiqueta amplia de 1000 Genomes (AFR, AMR, EAS, EUR, SAS) |
| **Asociación** | Correlación poblacional de GWAS, no prueba causal individual |
""",
    },
    "ar": {
        "page_methods": "خلف الأرقام",
        "about_intro": (
            "المنهجية والمصادر والمصطلحات والحدود لمن يريد النظر تحت الغطاء."
        ),
        "methods_heading": "كيف تُبنى الأرقام",
        "sources_heading": "من أين تأتي البيانات",
        "limits_heading": "العناية والحدود",
        "glossary_heading": "كلمات نستخدمها عن قصد",
        "methods_md": """- **مفتاح الربط:** معرّفات rsID للـ SNP (وليس أسماء السمات كنص حر).
- **اللوحة:** مشروع ألف جينوم المرحلة 3، أنماط كروموسوم 22 + تسميات المجموعات الكبرى.
- **طبقة السمات:** 15 ارتباطاً غير طبي من كتالوج GWAS على الكروموسوم 22.
- **الجرعة:** 0 / 1 / 2 نسخ من أليل التأثير من الملف المرفوع.
- **درجة السمة:** `dosage × {+1, −1, 0}`. قاعدة شفافة وليست نموذجاً للتعلم الآلي.
- **رسم نسب الأصل:** غابة عشوائية على الجرعات الخمس عشرة نفسها → AFR / AMR / EAS / EUR / SAS.
- **وضع العرض:** مجاميع اللوحة المضمّنة + `models/ancestry_clf.joblib` عند غياب Postgres.

المزيد في `docs/methods.md` و`docs/CONCEPTS.md`.
""",
        "sources_md": """- **مشروع ألف جينوم المرحلة 3**، ملف VCF للكروموسوم 22 ولوحة العينات (FTP لـ EBI)
- **كتالوج GWAS**، أزواج SNP–سمة غير طبية على الكروموسوم 22
- **أنماط جينية للعرض** في `data/sample/` لتجربة الواجهة دون تصدير شخصي
""",
        "limits_md": """- مجاميع بحث عامة وتحميلات تعليمية فقط؛ ليست اختباراً سريرياً
- خمسة عشر معلماً لا تحل محل اختبارات نسب الأصل التجارية
- نطاق الكروموسوم 22: السمات الكلاسيكية على كروموسومات أخرى خارج النطاق عمداً
- تسميات نسب الأصل البحثية ليست جنسيات حديثة
- **مشروع محفظة تعليمي**، وليس منتج مستشفى أو مختبر أو جينوميات استهلاكية

مقدمة الأحياء: `docs/CONCEPTS.md`.
""",
        "glossary_md": """| المصطلح | المعنى البسيط |
|---------|----------------|
| **SNP** | اختلاف شائع بحرف واحد في الحمض النووي بين الأشخاص |
| **الأليل** | حرف ممكن عند موقع SNP |
| **الجرعة** | عدد نسخ أليل التأثير (0 أو 1 أو 2) |
| **MAF** | مدى شيوع الحرف الأندر في مجموعة |
| **rsID** | اسم الكتالوج العام لـ SNP (يبدأ بـ `rs`) |
| **المجموعة الكبرى** | تسمية بحثية واسعة من ألف جينوم (AFR, AMR, EAS, EUR, SAS) |
| **الارتباط** | ارتباط سكاني من GWAS، وليس إثباتاً سببياً فردياً |
""",
    },
    "zh": {
        "page_methods": "数字背后",
        "about_intro": "方法、来源、术语与局限，适合想看清底层逻辑的人。",
        "methods_heading": "数字如何构建",
        "sources_heading": "数据从哪里来",
        "limits_heading": "注意事项与局限",
        "glossary_heading": "我们刻意使用的词",
        "methods_md": """- **关联键：** SNP 的 rsID（从不用自由文本性状名）。
- **队列：** 千人基因组计划第 3 期，22 号染色体基因型 + 超级人群标签。
- **性状层：** GWAS Catalog 上 chr22 的 15 个非医学关联。
- **剂量：** 上传文件中效应等位基因的 0 / 1 / 2 拷贝。
- **性状得分：** `dosage × {+1, −1, 0}`。透明规则，不是机器学习性状模型。
- **祖先草图：** 同样在这 15 个剂量上的随机森林 → AFR / AMR / EAS / EUR / SAS。
- **演示模式：** 无 Postgres 时使用捆绑队列计数 + 已提交的 `models/ancestry_clf.joblib`。

详见 `docs/methods.md` 与 `docs/CONCEPTS.md`。
""",
        "sources_md": """- **千人基因组计划第 3 期**，chr22 多样本 VCF 与样本面板（EBI FTP）
- **GWAS Catalog**，chr22 上的非医学 SNP–性状对
- **演示基因型** `data/sample/`，无需个人试剂盒导出即可浏览界面
""",
        "limits_md": """- 仅限公开研究汇总与教育性上传；不是临床检测
- 15 个位点不能替代消费级祖先检测（数十万标记）
- 仅限 22 号染色体：其他染色体上的经典性状有意不在范围内
- 研究用祖先标签不是现代国籍主张
- **作品集学习项目**，不是医院 / 实验室 / 消费基因组产品

生物学入门：`docs/CONCEPTS.md`。
""",
        "glossary_md": """| 术语 | 简明含义 |
|------|----------|
| **SNP** | 人与人之间常见的单碱基 DNA 差异 |
| **等位基因** | 某个 SNP 上可能的字母 |
| **剂量** | 效应等位基因拷贝数（0、1 或 2） |
| **MAF** | 较罕见字母在群体中的频率 |
| **rsID** | SNP 的公开目录名（以 `rs` 开头） |
| **超级人群** | 千人基因组宽标签（AFR、AMR、EAS、EUR、SAS） |
| **关联** | GWAS 的群体相关，不是个人因果证明 |
""",
    },
    "ru": {
        "page_methods": "За цифрами",
        "about_intro": (
            "Методы, источники, словарь и ограничения для тех, кто хочет заглянуть под капот."
        ),
        "methods_heading": "Как строятся цифры",
        "sources_heading": "Откуда данные",
        "limits_heading": "Осторожность и ограничения",
        "glossary_heading": "Слова, которые мы используем намеренно",
        "methods_md": """- **Ключ соединения:** rsID SNP (никогда свободные названия признаков).
- **Панель:** 1000 Genomes фаза 3, генотипы 22-й хромосомы + метки суперпопуляций.
- **Слой признаков:** 15 курируемых немедицинских ассоциаций GWAS Catalog на chr22.
- **Dosage:** 0 / 1 / 2 копии аллеля эффекта из загруженного файла.
- **Оценка признака:** `dosage × {+1, −1, 0}`. Прозрачное правило, не ML-модель признака.
- **Набросок происхождения:** Random Forest на тех же 15 dosage → AFR / AMR / EAS / EUR / SAS.
- **Демо-режим:** счётчики панели + `models/ancestry_clf.joblib` без Postgres.

Подробнее в `docs/methods.md` и `docs/CONCEPTS.md`.
""",
        "sources_md": """- **1000 Genomes Project фаза 3**, multi-sample VCF chr22 и панель (EBI FTP)
- **GWAS Catalog**, немедицинские пары SNP–признак на chr22
- **Демо-генотипы** в `data/sample/` для UI без личного экспорта
""",
        "limits_md": """- Только открытые исследовательские агрегаты и учебные загрузки; не клинический тест
- Пятнадцать маркеров не заменяют потребительские тесты происхождения
- Только 22-я хромосома: классические признаки на других хромосомах намеренно вне охвата
- Исследовательские метки происхождения не равны современным национальностям
- **Учебный портфолио-проект**, не продукт больницы / лаборатории / потребительской геномики

Биологический праймер: `docs/CONCEPTS.md`.
""",
        "glossary_md": """| Термин | Простой смысл |
|--------|----------------|
| **SNP** | Распространённое различие ДНК в одну букву |
| **Аллель** | Возможная буква в позиции SNP |
| **Dosage** | Число копий аллеля эффекта (0, 1 или 2) |
| **MAF** | Насколько редкая буква часта в группе |
| **rsID** | Публичное каталожное имя SNP (начинается с `rs`) |
| **Суперпопуляция** | Широкая метка 1000 Genomes (AFR, AMR, EAS, EUR, SAS) |
| **Ассоциация** | Популяционная корреляция GWAS, не доказательство личной причинности |
""",
    },
}
