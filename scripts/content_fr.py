# -*- coding: utf-8 -*-
"""French content for the parselex.app landing (docs FR terminology)."""

C = {
    "lang": "fr",
    "meta_title": "Parselex — Plateforme d'Intelligence Documentaire Juridique",
    "meta_desc": ("Parselex automatise le cycle de vie complet du document juridique : OCR intelligent, analyse "
                  "multilingue, rédaction et score de préparation du dossier (0–100). Produit en production, "
                  "7 catégories d'intelligence, 4 régions. Sécurité Zero-Trust par l'architecture."),
    "nav": {"platform": "Plateforme", "score": "Score du dossier", "security": "Sécurité", "product": "Produit",
            "metrics": "Métriques", "pricing": "Tarifs", "docs": "Documentation", "cta": "Ouvrir Parselex"},
    "hero": {
        "badge": "Produit en production — dossiers réels en cours",
        "h1": "Plateforme d'<span class='accent'>Intelligence Documentaire</span> Juridique",
        "sub": ("Parselex automatise le cycle de vie complet du document juridique — ingestion depuis toute "
                "source, analyse approfondie, rédaction et un score objectif de préparation du dossier. Un système "
                "unique qui raisonne le dossier avec l'avocat, au-delà de la simple recherche de texte."),
        "cta1": "Ouvrir Parselex",
        "cta2": "Lire la documentation",
        "note": "parselex.app · architecture indépendante des fournisseurs · 2026",
        "stats": [("99,6 %", "traitements réussis"), ("7", "catégories d'intelligence"),
                  ("4", "juridictions dans un dossier réel"), ("2 500+", "documents dans les pipelines de production")],
    },
    "problem": {
        "kicker": "Le défi",
        "title": "Les équipes juridiques se noient sous les documents",
        "lead": ("Le traitement manuel crée des goulots d'étranglement critiques, multiplie le risque d'erreur "
                 "humaine et ralentit chaque décision qui compte."),
        "cards": [
            {"num": "01", "t": "Volume de données explosif",
             "d": ("Une seule affaire pénale peut compter de 200 à 2 000 documents. Des millions de fichiers "
                   "juridiques sont générés chaque année dans le monde — chacun exigeant analyse et "
                   "classification.")},
            {"num": "02", "t": "Routine manuelle",
             "d": ("Les juristes consacrent jusqu'à 40 % de leur temps au traitement documentaire. L'analyse "
                   "complète d'une affaire complexe prend des semaines, souvent des mois.")},
            {"num": "03", "t": "Erreurs et risques",
             "d": ("Le facteur humain entraîne des preuves manquées, des contradictions dans les témoignages et "
                   "des écarts dans les pièces financières — précisément les lacunes qui décident de l'issue.")},
        ],
        "why_title": "Pourquoi l'IA générique n'y répond pas",
        "why": [
            {"icon": "⊗", "t": "Réponses superficielles et hallucinations",
             "d": ("Les chatbots généralistes produisent des résultats plausibles mais faux : précision de 42–65 %, "
                   "taux d'hallucination jusqu'à 33 %. Vérifier leurs réponses prend plus de temps que rédiger le "
                   "document de zéro.")},
            {"icon": "❄", "t": "Aucune approche systémique",
             "d": ("Les outils ponctuels traitent des requêtes isolées — ils ne voient jamais l'affaire dans son "
                   "ensemble et ne relient pas les sources : e-mails, messageries, scans.")},
            {"icon": "⚿", "t": "Risques de confidentialité",
             "d": ("Téléverser des données sensibles vers des modèles d'IA publics crée des risques de fuite ; la "
                   "plupart des outils ne garantissent aucun isolement des données.")},
        ],
    },
    "platform": {
        "kicker": "La plateforme",
        "title": "Une plateforme d'IA juridique à cycle complet",
        "lead": ("Parselex accompagne le dossier sur tout son cycle de vie : de l'ingestion des documents depuis "
                 "toute source à l'analyse approfondie, la rédaction et une évaluation objective de la "
                 "préparation. Un système unique qui raisonne avec l'avocat — avec une architecture indépendante "
                 "des fournisseurs : la cascade de modèles s'adapte, votre flux de travail reste intact."),
        "c1t": "Ingénierie documentaire",
        "c1": ["OCR intelligent — documents scannés, chats WhatsApp et Telegram",
               "Classification automatique avec score de pertinence",
               "Traduction juridique multilingue avec contrôle qualité en trois étapes",
               "Contrôles d'intégrité — chronologie, références croisées, arithmétique, sémantique",
               "Génération de projets d'actes prêts à être déposés"],
        "c2t": "Analytique et expertise IA",
        "c2": ["Recherche IA sur tout le corpus — réponses avec citations des documents précis",
               "Analyse multi-étapes — cohérence, contradictions, narratif, preuves",
               "Score de préparation du dossier (0–100) — rattachement des chefs et analyse des lacunes",
               "Boucle fermée : Classification → Analyse → Évaluation → Rapport",
               "Scellé forensique des preuves — l'intégrité de chaque fichier est préservée"],
    },
    "sectors": {
        "kicker": "Domaines de pratique",
        "title": "Construit sur la pratique réelle, pas sur des hypothèses",
        "lead": ("Chaque catégorie naît de la charge réelle de dossiers — ce type d'affaires où chaque document "
                 "est une preuve potentielle."),
        "cards": [
            {"icon": "⛨", "tag": "FINREG", "t": "Fraude bancaire",
             "d": ("Accès non autorisé et détournement de fonds : relevés, journaux de paiements, réclamations et "
                   "correspondance. Vérification automatique de l'arithmétique et de la chronologie, détection des "
                   "contradictions entre témoignages.")},
            {"icon": "$", "tag": "Dossier FIR réel", "t": "Fraude aux cryptomonnaies",
             "d": ("Affaires de cryptofraude et d'investigations blockchain. Un cas transfrontalier démontré : un "
                   "schéma organisé avec 9 prévenus dans 4 juridictions — 91 documents traités par la "
                   "plateforme.")},
            {"icon": "⚖", "tag": "AML · KYC", "t": "Lutte anti-blanchiment",
             "d": ("Analyse des schémas de blanchiment : chaînes de transactions, origine des fonds, documentation "
                   "de conformité. Un domaine à part entière de la plateforme aux côtés du pénal et du civil.")},
            {"icon": "▦", "tag": "Civil", "t": "Litiges du travail",
             "d": ("Dossiers RH, contrats, notes de service et correspondance interne. Détection des "
                   "contradictions entre documents et préparation de la position pour le procès.")},
        ],
        "strip": ("<b>7 catégories d'intelligence</b> — Criminal · Civil · COMM (commercial international) · ECOM "
                  "(e-commerce et protection du consommateur) · FINREG (régulation financière et AML) · IP · "
                  "Litigation Support — sur <b>4 régions</b> : Amérique/États-Unis, Europe, Asie, Inde. Extensible "
                  "selon la pratique du client."),
    },
    "score": {
        "kicker": "Capacité phare",
        "title": "Score de préparation du dossier — de 0 à 100",
        "lead": ("Pas de la génération de texte — de l'expertise de dossier. Une évaluation numérique avec "
                 "rattachement automatique des preuves et analyse des lacunes, unique sur le marché actuel."),
        "big": "0–100",
        "big_label": "score numérique de préparation du dossier",
        "dims": [
            {"t": "Base probatoire", "d": "complétude et fiabilité de chaque preuve"},
            {"t": "Rattachement des chefs", "d": "preuves liées à des chefs d'accusation précis"},
            {"t": "Analyse des lacunes", "d": "preuves manquantes et points faibles détectés automatiquement"},
            {"t": "Théorie du dossier", "d": "cohérence interne et force de persuasion du narratif"},
            {"t": "Lignes de risque", "d": "axes d'attaque probables de la défense"},
        ],
        "steps_title": "Au cœur de l'analyse IA en 8 étapes",
        "steps": ["Cohérence et connectivité des documents",
                  "Détection des contradictions entre témoignages",
                  "Analyse contextuelle — séquence et logique",
                  "Évaluation de la qualité des preuves",
                  "Conformité aux normes légales",
                  "Exactitude de la terminologie juridique",
                  "Évaluation des risques et vulnérabilités",
                  "Verdict final de préparation"],
        "ribbon": ("Avantage clé : un score numérique de préparation du dossier (0–100). Aucun concurrent sur le "
                   "marché n'en propose l'équivalent."),
    },
    "security": {
        "kicker": "Sécurité",
        "title": "La sécurité par l'architecture, pas par la promesse",
        "lead": ("Parselex est conçu pour les exigences de confidentialité de la pratique juridique et bancaire : "
                 "accès Zero-Trust, anonymisation sur l'appareil et déploiement dans votre propre périmètre."),
        "cards": [
            {"icon": "⛨", "t": "LexZTNA — accès Zero-Trust",
             "d": ("Aucun endpoint public. Les espaces de travail ne sont accessibles que via le client sécurisé "
                   "LexZTNA — tunnels mesh chiffrés, vérification des appareils et accès aux privilèges "
                   "minimaux.")},
            {"icon": "⚿", "t": "Pare-feu éthique — anonymisation des PII",
             "d": ("Noms, identifiants et numéros de compte sont remplacés par des jetons déterministes sur votre "
                   "appareil avant transmission — une valeur correspond à un jeton, si bien que l'IA conserve la "
                   "cohérence des entités. La réidentification s'effectue localement au retour.")},
            {"icon": "⚙", "t": "Déploiement on-premise",
             "d": ("Des modèles à poids ouverts s'exécutent dans votre infrastructure : l'inférence et la "
                   "recherche sémantique n'appellent jamais d'API d'IA externes et les documents ne quittent "
                   "jamais votre périmètre.")},
            {"icon": "✓", "t": "Conformité et audit",
             "d": ("Isolement des données par utilisateur, journal complet des actions et contrôle des droits à "
                   "chaque opération — s'intègre aux politiques de sécurité de l'information. Minimisation des "
                   "données alignée sur le RGPD, le CCPA et l'ABA Model Rule 1.6.")},
        ],
        "pilot": ("→ <b>Pilote en 4–8 semaines</b> — sur vos documents, dans votre périmètre sécurisé → score de "
                  "préparation du dossier (0–100) → engagement Professional ou Enterprise"),
    },
    "arch": {
        "kicker": "Sous le capot",
        "title": "Un système d'IA multi-niveaux",
        "lead": ("Une cascade de modèles d'IA sans dépendre d'un fournisseur unique — de l'embedding et de la "
                 "recherche à la génération de texte et au scoring des dossiers."),
        "pipeline_title": "Le pipeline de traitement en 7 étapes",
        "pipeline": ["Ingest", "OCR", "Classification", "Validation", "RAG Analysis", "AI Translation", "Report"],
        "cascade_title": "Une cascade de modèles à 4 niveaux qui ne s'arrête jamais",
        "cascade": [
            {"n": "01", "t": "Modèle cloud principal", "d": "Rapide et économique pour la charge quotidienne"},
            {"n": "02", "t": "Second fournisseur cloud", "d": "Bascule automatique — le travail ne s'interrompt jamais"},
            {"n": "03", "t": "Modèle local on-premise", "d": "S'exécute dans votre périmètre, coût par requête nul"},
            {"n": "04", "t": "Réserve supplémentaire", "d": "Continuité de service même en cas de panne fournisseur"},
        ],
        "strip": ("Recherche sémantique multilingue — EN · RU · HI · NP · KZ · TR — avec sélection automatique de "
                  "la juridiction. <b>Déploiement dans votre périmètre :</b> modèles à poids ouverts, aucun appel "
                  "à des API d'IA externes, documents jamais transmis à des tiers."),
    },
    "modules": {
        "kicker": "Produit",
        "title": "Un espace de travail pour tout le cycle du dossier",
        "lead": ("Une interface web unique, du téléversement des documents à l'évaluation de préparation — douze "
                 "modules couvrent le cycle complet."),
        "tiles": [
            {"icon": "◌", "t": "Chat IA du dossier", "d": "réponses avec citations des documents précis"},
            {"icon": "▤", "t": "Documents", "d": "téléversement, recherche et gestion des pièces"},
            {"icon": "▦", "t": "Bibliothèque", "d": "catalogue catégorisé de documents juridiques"},
            {"icon": "✎", "t": "Rédaction", "d": "projets d'actes assistés par IA"},
            {"icon": "▦", "t": "Analyse", "d": "analyse en boucle fermée avec suivi des itérations"},
            {"icon": "✓", "t": "Score du dossier", "d": "0–100, rattachement des preuves, analyse des lacunes"},
            {"icon": "◯", "t": "Juridiction", "d": "7 domaines : pénal, civil, AML/KYC, IP"},
            {"icon": "✿", "t": "Pipeline", "d": "traitement de masse : statut et historique"},
            {"icon": "▦", "t": "Modules", "d": "extensions flexibles selon les besoins"},
            {"icon": "⚙", "t": "Options", "d": "configuration de la plateforme par pratique"},
            {"icon": "♟", "t": "Utilisateurs", "d": "gestion des accès et journal des actions"},
            {"icon": "▦", "t": "Analytique du corpus", "d": "statistiques et supervision du traitement"},
        ],
    },
    "metrics": {
        "kicker": "Preuves",
        "title": "Démontré sur des dossiers réels",
        "lead": "Des chiffres de production sur des charges réelles — pas des conditions de démonstration.",
        "stats": [("99,6 %", "traitements réussis"), ("95 %", "métadonnées extraites automatiquement"),
                  ("2 500+", "documents dans les pipelines de production"), ("2 309", "contrôles automatisés par version"),
                  ("7", "catégories d'intelligence"), ("4", "juridictions dans un dossier réel")],
        "case": {
            "tag": "Dossier réel à la une",
            "title": "Poursuite transfrontalière pour cryptofraude",
            "desc": ("Un schéma organisé de fraude enquêté simultanément dans quatre juridictions — le dossier "
                     "entier passe par la plateforme : de l'ingestion à l'évaluation de préparation."),
            "rows": [("Prévenus", "9 · 4 juridictions"), ("Documents traités", "91"),
                     ("Fragments dans la base de connaissances", "792 · tout interrogeable par l'IA"),
                     ("Documents pertinents isolés", "52"), ("Domaine", "pénal · blockchain")],
        },
        "quality_title": "Ingénierie qualité",
        "quality": ["Auto-vérification des versions — chaque version passe le cycle complet de contrôles",
                    "Suite de tests automatisés — 2 309 contrôles de code",
                    "Contrôles automatiques des scénarios clés de l'interface",
                    "Mesure hebdomadaire de la qualité de recherche en production"],
    },
    "compare": {
        "kicker": "Paysage concurrentiel",
        "title": "Où se situe Parselex",
        "lead": "Le marché se divise en trois groupes — et chacun s'arrête là où commence le vrai travail du dossier.",
        "rows": [
            {"grp": "Géants du LegalTech", "who": "Thomson Reuters (Westlaw, CoCounsel) · LexisNexis",
             "lim": "Axés sur les bases de données et la recherche ; précision de 42–65 %, hallucinations jusqu'à 33 %.",
             "win_t": "L'expertise approfondie du dossier plutôt que la recherche —",
             "win_d": "le système évalue la préparation du dossier, pas seulement des documents."},
            {"grp": "Assistants IA pour juristes", "who": "Harvey · Spellbook · Kannon",
             "lim": "Profondeur limitée à la génération ; pas d'évaluation du dossier ; intégrations souvent étroites.",
             "win_t": "Analyse autonome et analyse des lacunes —",
             "win_d": "une expertise qui révèle les points faibles sans humain à chaque étape."},
            {"grp": "Plateformes d'automatisation", "who": "LexCheck · Luminance · Ironclad",
             "lim": "Essentiellement contrats et due diligence ; couverture juridictionnelle souvent limitée.",
             "win_t": "7 domaines juridiques et 4 régions —",
             "win_d": "pénal, civil, commercial, AML et plus encore, avec les spécificités régionales."},
        ],
        "ribbon": ("Avantage clé : le score numérique de préparation du dossier (0–100) — aucun concurrent n'en "
                   "propose l'équivalent."),
    },
    "pricing": {
        "kicker": "Monétisation",
        "title": "Modèle hybride, prêt pour l'entreprise",
        "lead": ("Abonnements SaaS pour les équipes et solutions d'entreprise avec déploiement on-premise et "
                 "entraînement de modèles sur mesure — optimisés pour chaque segment du marché juridique."),
        "tiers": [
            {"name": "Starter", "for": "Pour les pilotes et petites équipes",
             "features": ["Corpus jusqu'à 500 documents", "Recherche IA et classification documentaire",
                          "Contrôles automatiques de base", "Support par e-mail"],
             "cta": "Lancer un pilote"},
            {"name": "Professional", "for": "Pour les équipes juridiques en production",
             "pop": "Recommandé", "hot": True,
             "features": ["Corpus jusqu'à 5 000 documents", "Tous les modules de la plateforme",
                          "Score de préparation du dossier", "Support prioritaire"],
             "cta": "Demander un tarif"},
            {"name": "Enterprise", "for": "Pour les institutions et banques",
             "features": ["Corpus illimité", "Déploiement on-premise dans votre périmètre",
                          "Affinage de modèles sur mesure", "Support dédié avec SLA",
                          "Intégrations personnalisées"],
             "cta": "Nous parler"},
        ],
        "note": "Canaux de vente : ventes directes · projets pilotes · réseau de partenaires. Tarifs sur demande.",
    },
    "market": {
        "kicker": "Marché",
        "title": "Un marché en croissance exponentielle",
        "lead": ("Le LegalTech mondial monte en puissance et Parselex occupe une niche unique à l'intersection de "
                 "l'IA et de l'analytique documentaire juridique."),
        "cards": [
            {"t": "TAM — marché total", "n": "300 Md$ d'ici 2028",
             "d": ("Le LegalTech mondial a atteint 49 Md$ en 2024, avec une projection de 300 Md$ d'ici 2028 "
                   "(TCAC 9,4 %) — analytique documentaire, conformité et automatisation comprises.")},
            {"t": "SAM — marché adressable", "n": "Le segment à la plus forte croissance",
             "d": ("L'analytique documentaire par IA. Parselex cible 7+ domaines juridiques et 4 régions clés — "
                   "des centaines de milliers de cabinets, d'organismes d'enquête et de conseils dans le monde.")},
            {"t": "SOM — tête de pont", "n": "D'abord l'Inde et la CEI",
             "d": ("Un segment concret et mesurable où le produit est déjà validé — premiers revenus via les "
                   "pilotes et les abonnements Professional / Enterprise, puis montée en charge régionale.")},
        ],
    },
    "roadmap": {
        "kicker": "Trajectoire",
        "title": "Dynamique de développement",
        "lead": ("Du démarrage du projet aux pipelines de production en une seule année — et une trajectoire "
                 "claire de montée en échelle."),
        "items": [
            {"yr": "2026", "t": "Lancement du projet", "d": "La plateforme est conçue autour de dossiers réels."},
            {"yr": "2026", "t": "Première version", "d": "Produit opérationnel livré avec une suite de tests automatisés."},
            {"yr": "2026", "t": "Hub IA unifié", "d": "40 outils pour agents sous une couche d'orchestration unique."},
            {"yr": "2026", "t": "2 500+ documents en production", "d": "Pipelines clients réels traitant de vraies charges."},
            {"yr": "2027", "t": "Montée en échelle SaaS multi-tenant", "d": "Nouveaux marchés, intégrations et application mobile."},
        ],
    },
    "cta": {
        "title": "Commencez avec Parselex",
        "sub": ("Faites passer votre premier dossier par la plateforme, ou commencez par la documentation "
                "d'architecture — les analyses approfondies vivent sur docs.parselex.app."),
        "primary": "Ouvrir Parselex",
        "secondary": "Explorer la documentation",
    },
    "footer": {
        "tagline": "Plateforme d'Intelligence Documentaire Juridique — de toute source jusqu'à un score objectif de préparation du dossier.",
        "docs_note": "Les recherches d'architecture, la sécurité et le benchmark RAG vivent sur",
        "col_platform_title": "Plateforme",
        "col_platform": ["Ouvrir l'application", "Documentation", "Architecture de sécurité", "Benchmark RAG"],
        "col_legal_title": "Mentions légales",
        "legal": {"privacy": "Confidentialité", "personal_data": "Utilisation des données personnelles",
                  "cookies": "Cookies", "terms": "Conditions d'utilisation", "payments": "Paiements récurrents",
                  "disclaimer": "Avertissement IA"},
        "contact": "Support",
        "copyright": "© 2026 Parselex — Plateforme d'Intelligence Documentaire Juridique",
    },
}
