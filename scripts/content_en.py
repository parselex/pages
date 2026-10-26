# -*- coding: utf-8 -*-
"""English (canonical) content for the parselex.app landing."""

C = {
    "lang": "en",
    "meta_title": "Parselex — Legal Document Intelligence Platform",
    "meta_desc": ("Parselex automates the full legal document lifecycle — intelligent OCR, multilingual analysis, "
                  "drafting and the Case Readiness Score (0–100). Working product across 7 intelligence categories "
                  "and 4 regions. Zero-Trust security by architecture."),
    "nav": {"platform": "Platform", "score": "Case Score", "security": "Security", "product": "Product",
            "metrics": "Metrics", "pricing": "Pricing", "docs": "Docs", "cta": "Open Parselex"},
    "hero": {
        "badge": "Working product — live cases in production",
        "h1": "Legal Document <span class='accent'>Intelligence</span> Platform",
        "sub": ("Parselex automates the full legal document lifecycle — ingestion from any source, deep analysis, "
                "drafting, and an objective Case Readiness Score. One system that thinks through the case with the "
                "lawyer, not just a text search."),
        "cta1": "Open Parselex",
        "cta2": "Read the documentation",
        "note": "parselex.app · Provider-independent architecture · 2026",
        "stats": [("99.6%", "processing success"), ("7", "intelligence categories"),
                  ("4", "jurisdictions in one live case"), ("2,500+", "documents in production pipelines")],
    },
    "problem": {
        "kicker": "The challenge",
        "title": "Legal teams are drowning in documents",
        "lead": ("Manual processing creates critical bottlenecks, multiplies the risk of human error and slows "
                 "every decision that matters."),
        "cards": [
            {"num": "01", "t": "Explosive data volume",
             "d": ("A single criminal case can span 200 to 2,000 documents. Millions of legal files are generated "
                   "worldwide every year — each one requiring analysis and classification.")},
            {"num": "02", "t": "Manual routine",
             "d": ("Lawyers spend up to 40% of their working time on document handling. A full analysis of one "
                   "complex case takes weeks — often months.")},
            {"num": "03", "t": "Errors and risk",
             "d": ("The human factor causes missed evidence, contradictions in testimony and discrepancies in "
                   "financial records — precisely the gaps that decide outcomes.")},
        ],
        "why_title": "Why generic AI doesn't solve it",
        "why": [
            {"icon": "⊗", "t": "Superficial answers and hallucinations",
             "d": ("General-purpose chatbots produce plausible but false results: 42–65% accuracy and hallucination "
                   "rates up to 33%. Verifying their output takes longer than drafting the document from scratch.")},
            {"icon": "❄", "t": "No systemic approach",
             "d": ("Point tools process isolated queries — they never see the whole case and don't connect sources "
                   "such as email, messengers and scans.")},
            {"icon": "⚿", "t": "Confidentiality risks",
             "d": ("Uploading sensitive case data to public AI models creates leakage risks; most tools offer no "
                   "data isolation guarantees at all.")},
        ],
    },
    "platform": {
        "kicker": "The platform",
        "title": "A full-cycle legal AI platform",
        "lead": ("Parselex carries a case through its entire lifecycle: from ingesting documents from any source to "
                 "deep analytics, drafting and an objective readiness assessment. One system that thinks through the "
                 "case with the lawyer — with a provider-independent architecture, so the model cascade adapts while "
                 "your workflow stays intact."),
        "c1t": "Document engineering",
        "c1": ["Intelligent OCR — scanned files, WhatsApp and Telegram chats",
               "Automatic classification with relevance scoring",
               "Multilingual legal translation with three-stage quality control",
               "Integrity checks — timeline, cross-references, arithmetic, semantics",
               "Court-ready draft generation"],
        "c2t": "AI analytics &amp; expertise",
        "c2": ["Corpus-wide AI search — answers with citations to specific documents",
               "Multi-stage analysis — coherence, contradictions, narrative, evidence",
               "Case Readiness Score (0–100) — charge mapping and gap analysis",
               "Closed loop: Classification → Analysis → Assessment → Report",
               "Forensic evidence capture — the integrity of every file is preserved"],
    },
    "sectors": {
        "kicker": "Practice areas",
        "title": "Built on live practice, not hypotheses",
        "lead": ("Every category comes from the real caseload — the kinds of matters where each document is "
                 "potential evidence."),
        "cards": [
            {"icon": "⛨", "tag": "FINREG", "t": "Banking fraud",
             "d": ("Unauthorized access and theft of funds: statements, payment logs, claims and correspondence. "
                   "Automated arithmetic and timeline verification, contradiction detection across testimony.")},
            {"icon": "$", "tag": "Live FIR case", "t": "Cryptocurrency fraud",
             "d": ("Crypto-fraud and blockchain-investigation matters. A proven cross-border case: an organized "
                   "scheme with 9 defendants across 4 jurisdictions — 91 documents processed by the platform.")},
            {"icon": "⚖", "tag": "AML · KYC", "t": "Anti-money laundering",
             "d": ("Analysis of laundering schemes: transaction chains, sources of funds, compliance documentation. "
                   "A dedicated platform domain alongside criminal and civil practice.")},
            {"icon": "▦", "tag": "Civil", "t": "Employment disputes",
             "d": ("Labor disputes: HR files, contracts, orders and internal correspondence. Cross-document "
                   "contradiction detection and court-ready position preparation.")},
        ],
        "strip": ("<b>7 intelligence categories</b> — Criminal · Civil · COMM (International Commercial) · ECOM "
                  "(E-Commerce &amp; Consumer Protection) · FINREG (Financial Regulation &amp; AML) · IP · Litigation "
                  "Support — across <b>4 regions</b>: Americas/US, Europe, Asia, India. Extended per client practice."),
    },
    "score": {
        "kicker": "Flagship capability",
        "title": "Case Readiness Score — from 0 to 100",
        "lead": ("Not text generation — case expertise. A numeric readiness assessment with automatic evidence "
                 "mapping and gap analysis, unique on the market today."),
        "big": "0–100",
        "big_label": "numeric case readiness score",
        "dims": [
            {"t": "Evidence base", "d": "completeness and reliability of every piece of evidence"},
            {"t": "Charge mapping", "d": "evidence tied to specific charges and counts"},
            {"t": "Gap analysis", "d": "missing evidence and weak points surfaced automatically"},
            {"t": "Case theory", "d": "internal coherence and persuasiveness of the narrative"},
            {"t": "Risk lines", "d": "likely avenues of attack for the defense"},
        ],
        "steps_title": "Inside the 8-stage AI analysis",
        "steps": ["Coherence and connectivity of documents",
                  "Contradiction detection across testimony",
                  "Contextual analysis — sequence and logic",
                  "Evidence quality assessment",
                  "Statutory compliance",
                  "Legal terminology correctness",
                  "Risk and vulnerability assessment",
                  "Final readiness verdict"],
        "ribbon": ("Key advantage: a numeric Case Readiness Score (0–100). No competitor on the market offers "
                   "the equivalent."),
    },
    "security": {
        "kicker": "Security",
        "title": "Security by architecture, not by promise",
        "lead": ("Parselex is engineered for the confidentiality requirements of legal and banking practice: "
                 "Zero-Trust access, on-device anonymization and deployment inside your own perimeter."),
        "cards": [
            {"icon": "⛨", "t": "LexZTNA — Zero-Trust access",
             "d": ("No public endpoints. Workspaces are reachable only through the LexZTNA secure client — "
                   "encrypted mesh tunnels, device verification and least-privilege access.")},
            {"icon": "⚿", "t": "Ethics Firewall — PII redaction",
             "d": ("Names, identifiers and account numbers are replaced with deterministic tokens on your device "
                   "before transmission — one value maps to one token, so the AI keeps entity coherence. "
                   "Re-identification happens locally on return.")},
            {"icon": "⚙", "t": "On-premise deployment",
             "d": ("Open-weight models run inside your infrastructure: inference and semantic search never call "
                   "external AI APIs, and documents never leave your perimeter.")},
            {"icon": "✓", "t": "Compliance and audit",
             "d": ("Per-user data isolation, a full action journal and permission checks on every operation — "
                   "designed to slot into information-security policies. Data minimization aligned with GDPR, "
                   "CCPA and ABA Model Rule 1.6.")},
        ],
        "pilot": ("→ <b>Pilot in 4–8 weeks</b> — on your documents, inside your secure perimeter → Case Readiness "
                  "Score (0–100) → Professional or Enterprise engagement"),
    },
    "arch": {
        "kicker": "Under the hood",
        "title": "A multi-level AI system",
        "lead": ("A cascade of AI models with no single-vendor lock-in — from embedding and retrieval to text "
                 "generation and case scoring."),
        "pipeline_title": "The 7-stage processing pipeline",
        "pipeline": ["Ingest", "OCR", "Classification", "Validation", "RAG Analysis", "AI Translation", "Report"],
        "cascade_title": "A 4-level model cascade that never stalls",
        "cascade": [
            {"n": "01", "t": "Primary cloud model", "d": "Fast and cost-efficient for the everyday workload"},
            {"n": "02", "t": "Second cloud provider", "d": "Automatic failover — the work never stops"},
            {"n": "03", "t": "Local on-premise model", "d": "Runs inside your perimeter at zero per-query cost"},
            {"n": "04", "t": "Additional reserve", "d": "Continuity of service even during provider outages"},
        ],
        "strip": ("Multilingual semantic search — EN · RU · HI · NP · KZ · TR — with automatic jurisdiction "
                  "selection. <b>Deploy inside your perimeter:</b> open-weight models, no external AI API calls, "
                  "documents never transmitted to third-party services."),
    },
    "modules": {
        "kicker": "Product",
        "title": "One workspace for the entire case lifecycle",
        "lead": ("A single web interface from document upload to readiness assessment — twelve modules covering "
                 "the full cycle."),
        "tiles": [
            {"icon": "◌", "t": "AI Case Chat", "d": "answers on the case with document-level citations"},
            {"icon": "▤", "t": "Documents", "d": "upload, search and case document management"},
            {"icon": "▦", "t": "Library", "d": "categorized catalog of legal documents"},
            {"icon": "✎", "t": "Drafting", "d": "drafts of legal documents with an AI assistant"},
            {"icon": "▦", "t": "Analysis", "d": "closed-loop analysis with iteration tracking"},
            {"icon": "✓", "t": "Case Score", "d": "0–100 score, evidence mapping, gap analysis"},
            {"icon": "◯", "t": "Jurisdiction", "d": "7 domains: criminal, civil, AML/KYC, IP"},
            {"icon": "✿", "t": "Pipeline", "d": "bulk document processing: status and history"},
            {"icon": "▦", "t": "Modules", "d": "flexible extensions for client workloads"},
            {"icon": "⚙", "t": "Options", "d": "platform configuration per practice"},
            {"icon": "♟", "t": "Users", "d": "access management and action log"},
            {"icon": "▦", "t": "Corpus Analytics", "d": "processing statistics and monitoring"},
        ],
    },
    "metrics": {
        "kicker": "Proof",
        "title": "Proven on real cases",
        "lead": "Production numbers from live caseloads — not demo conditions.",
        "stats": [("99.6%", "successful processing runs"), ("95%", "metadata extracted automatically"),
                  ("2,500+", "documents in production pipelines"), ("2,309", "automated checks per release"),
                  ("7", "intelligence categories"), ("4", "jurisdictions in one live case")],
        "case": {
            "tag": "Featured live case",
            "title": "Cross-border crypto-fraud prosecution",
            "desc": ("An organized fraud scheme investigated across four jurisdictions — the entire case runs "
                     "through the platform, from ingestion to readiness assessment."),
            "rows": [("Defendants", "9 · 4 jurisdictions"), ("Documents processed", "91"),
                     ("Knowledge chunks", "792 · fully AI-searchable"), ("Relevant documents isolated", "52"),
                     ("Domain", "Criminal · blockchain")],
        },
        "quality_title": "Quality engineering",
        "quality": ["Release auto-verification — every release passes the full check cycle",
                    "Automated test suite — 2,309 code checks",
                    "Automated UI scenario checks for key workflows",
                    "Weekly search-quality measurement in production"],
    },
    "compare": {
        "kicker": "Competitive landscape",
        "title": "Where Parselex stands",
        "lead": "The market splits into three groups — each one stops where the actual case work begins.",
        "rows": [
            {"grp": "LegalTech giants", "who": "Thomson Reuters (Westlaw, CoCounsel) · LexisNexis",
             "lim": "Database and research focus; accuracy 42–65% with hallucination rates up to 33%.",
             "win_t": "Deep case expertise instead of search —",
             "win_d": "the system assesses case readiness, not just documents or questions."},
            {"grp": "AI assistants for lawyers", "who": "Harvey · Spellbook · Kannon",
             "lim": "Depth limited to generation; no case assessment; often narrow integrations.",
             "win_t": "Autonomous analysis and gap analysis —",
             "win_d": "expertise that surfaces weak points without a human in every step."},
            {"grp": "Automation platforms", "who": "LexCheck · Luminance · Ironclad",
             "lim": "Mostly contracts and due diligence; jurisdiction coverage usually limited.",
             "win_t": "7 legal domains and 4 regions —",
             "win_d": "criminal, civil, commercial, AML and more, with regional specifics built in."},
        ],
        "ribbon": ("Key advantage: the numeric Case Readiness Score (0–100) — none of the competitors offers "
                   "the equivalent."),
    },
    "pricing": {
        "kicker": "Monetization",
        "title": "Hybrid model, enterprise-ready",
        "lead": ("SaaS subscriptions for teams and corporate solutions with on-premise deployment and custom "
                 "model training — optimized for different segments of the legal market."),
        "tiers": [
            {"name": "Starter", "for": "For pilots and small teams",
             "features": ["Corpus of up to 500 documents", "AI search and document classification",
                          "Core automated checks", "Email support"],
             "cta": "Start a pilot"},
            {"name": "Professional", "for": "For working legal teams",
             "pop": "Most popular", "hot": True,
             "features": ["Corpus of up to 5,000 documents", "All platform modules",
                          "Case Readiness Score", "Priority support"],
             "cta": "Request pricing"},
            {"name": "Enterprise", "for": "For institutions and banks",
             "features": ["Unlimited corpus", "On-premise deployment inside your perimeter",
                          "Custom model fine-tuning", "Dedicated support with SLA", "Custom integrations"],
             "cta": "Talk to us"},
        ],
        "note": "Sales channels: direct sales · pilot projects · partner network. Pricing on request.",
    },
    "market": {
        "kicker": "Market",
        "title": "A market growing exponentially",
        "lead": ("Global LegalTech is scaling fast, and Parselex occupies a unique niche at the intersection of "
                 "AI and legal document analytics."),
        "cards": [
            {"t": "TAM — total market", "n": "$300B by 2028",
             "d": ("Global LegalTech reached $49B in 2024 and is projected to $300B by 2028 at 9.4% CAGR — "
                   "document analytics, compliance and automation included.")},
            {"t": "SAM — serviceable market", "n": "Fastest-growing segment",
             "d": ("AI-driven document intelligence. Parselex targets 7+ legal domains and 4 key regions — "
                   "hundreds of thousands of firms, investigative bodies and consultancies worldwide.")},
            {"t": "SOM — beachhead", "n": "India &amp; CIS first",
             "d": ("A concrete, measurable segment where the product is already validated — first revenue through "
                   "pilots and Professional / Enterprise subscriptions, then scale across regions.")},
        ],
    },
    "roadmap": {
        "kicker": "Trajectory",
        "title": "Development dynamics",
        "lead": "From project start to production pipelines within a single year — and a clear scale-up path next.",
        "items": [
            {"yr": "2026", "t": "Project start", "d": "The platform is conceived and scoped around live caseloads."},
            {"yr": "2026", "t": "First release", "d": "A working product shipped with an automated test suite."},
            {"yr": "2026", "t": "Unified AI hub", "d": "40 tools for agents under one orchestration layer."},
            {"yr": "2026", "t": "2,500+ documents in production", "d": "Live client pipelines processing real caseloads."},
            {"yr": "2027", "t": "Multi-tenant SaaS scale-up", "d": "New markets, integrations and a mobile application."},
        ],
    },
    "cta": {
        "title": "Get started with Parselex",
        "sub": ("Run your first case through the platform, or start with the architecture documentation — "
                "the deep dives live on docs.parselex.app."),
        "primary": "Open Parselex",
        "secondary": "Explore the docs",
    },
    "footer": {
        "tagline": "Legal Document Intelligence Platform — from any source to an objective Case Readiness Score.",
        "docs_note": "Architecture research, security deep dives and the RAG benchmark live on",
        "col_platform_title": "Platform",
        "col_platform": ["Open the app", "Documentation", "Security architecture", "RAG benchmark"],
        "col_legal_title": "Legal",
        "legal": {"privacy": "Privacy Policy", "personal_data": "Personal Data Use", "cookies": "Cookies",
                  "terms": "Terms of Service", "payments": "Recurring Payments", "disclaimer": "AI Disclaimer"},
        "contact": "Support",
        "copyright": "© 2026 Parselex — Legal Document Intelligence Platform",
    },
}
