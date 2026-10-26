# -*- coding: utf-8 -*-
"""Spanish content for the parselex.app landing (docs ES terminology)."""

C = {
    "lang": "es",
    "meta_title": "Parselex — Plataforma de Inteligencia Documental Legal",
    "meta_desc": ("Parselex automatiza el ciclo completo del documento legal: OCR inteligente, análisis "
                  "multilingüe, redacción de borradores y la puntuación de preparación del caso (0–100). Producto "
                  "en producción con 7 categorías de inteligencia y 4 regiones. Seguridad Zero-Trust por "
                  "arquitectura."),
    "nav": {"platform": "Plataforma", "score": "Puntuación del caso", "security": "Seguridad", "product": "Producto",
            "metrics": "Métricas", "pricing": "Precios", "docs": "Documentación", "cta": "Abrir Parselex"},
    "hero": {
        "badge": "Producto en producción — casos reales en curso",
        "h1": "Plataforma de <span class='accent'>Inteligencia Documental</span> Legal",
        "sub": ("Parselex automatiza el ciclo de vida completo del documento legal — ingesta desde cualquier "
                "fuente, análisis profundo, redacción y una puntuación objetiva de preparación del caso. Un único "
                "sistema que razona el caso junto al abogado, no solo busca texto."),
        "cta1": "Abrir Parselex",
        "cta2": "Leer la documentación",
        "note": "parselex.app · arquitectura independiente del proveedor · 2026",
        "stats": [("99,6%", "procesamientos con éxito"), ("7", "categorías de inteligencia"),
                  ("4", "jurisdicciones en un caso real"), ("2.500+", "documentos en pipelines de producción")],
    },
    "problem": {
        "kicker": "El desafío",
        "title": "Los equipos legales se ahogan en documentos",
        "lead": ("El procesamiento manual crea cuellos de botella críticos, multiplica el riesgo de error humano y "
                 "ralentiza cada decisión importante."),
        "cards": [
            {"num": "01", "t": "Volumen de datos explosivo",
             "d": ("Un solo caso penal puede abarcar de 200 a 2.000 documentos. Cada año se generan millones de "
                   "archivos legales que requieren análisis y clasificación.")},
            {"num": "02", "t": "Trabajo manual",
             "d": ("Los abogados dedican hasta el 40% de su jornada a tareas documentales. El análisis completo de "
                   "un caso complejo toma semanas — a menudo meses.")},
            {"num": "03", "t": "Errores y riesgos",
             "d": ("El factor humano provoca pruebas omitidas, contradicciones en declaraciones y discrepancias en "
                   "registros financieros — precisamente las brechas que deciden el resultado.")},
        ],
        "why_title": "Por qué la IA genérica no lo resuelve",
        "why": [
            {"icon": "⊗", "t": "Respuestas superficiales y alucinaciones",
             "d": ("Los chatbots de propósito general producen resultados plausibles pero falsos: precisión del "
                   "42–65% y tasas de alucinación de hasta el 33%. Verificar sus respuestas toma más tiempo que "
                   "redactar el documento desde cero.")},
            {"icon": "❄", "t": "Sin enfoque sistémico",
             "d": ("Las herramientas puntuales procesan consultas aisladas — nunca ven el caso completo ni "
                   "conectan fuentes como correo, mensajería y escaneos.")},
            {"icon": "⚿", "t": "Riesgos de confidencialidad",
             "d": ("Subir datos sensibles del caso a modelos de IA públicos crea riesgos de fuga; la mayoría de "
                   "las herramientas no garantiza ningún aislamiento de datos.")},
        ],
    },
    "platform": {
        "kicker": "La plataforma",
        "title": "Una plataforma de IA legal de ciclo completo",
        "lead": ("Parselex acompaña el caso durante todo su ciclo de vida: desde la ingesta de documentos de "
                 "cualquier fuente hasta el análisis profundo, la redacción y una evaluación objetiva de "
                 "preparación. Un único sistema que razona junto al abogado — con una arquitectura independiente "
                 "del proveedor: la cascada de modelos se adapta y el flujo de trabajo permanece intacto."),
        "c1t": "Ingeniería documental",
        "c1": ["OCR inteligente — documentos escaneados, chats de WhatsApp y Telegram",
               "Clasificación automática con puntuación de relevancia",
               "Traducción jurídica multilingüe con control de calidad en tres etapas",
               "Verificación de integridad — cronología, referencias cruzadas, aritmética, semántica",
               "Generación de borradores judiciales listos para presentar"],
        "c2t": "Analítica y experticia de IA",
        "c2": ["Búsqueda con IA en todo el corpus — respuestas con citas a documentos concretos",
               "Análisis multi-etapa — coherencia, contradicciones, narrativa, pruebas",
               "Puntuación de preparación del caso (0–100) — vínculo de cargos y análisis de brechas",
               "Ciclo cerrado: Clasificación → Análisis → Evaluación → Informe",
               "Fijación forense de pruebas — la integridad de cada archivo queda preservada"],
    },
    "sectors": {
        "kicker": "Áreas de práctica",
        "title": "Construido sobre práctica real, no hipótesis",
        "lead": ("Cada categoría nace de la carga real de casos — del tipo de asuntos donde cada documento es "
                 "prueba potencial."),
        "cards": [
            {"icon": "⛨", "tag": "FINREG", "t": "Fraude bancario",
             "d": ("Acceso no autorizado y sustracción de fondos: extractos, registros de pagos, reclamaciones y "
                   "correspondencia. Verificación automática de aritmética y cronología, detección de "
                   "contradicciones entre declaraciones.")},
            {"icon": "$", "tag": "Caso FIR real", "t": "Fraude con criptomonedas",
             "d": ("Casos de criptofraude e investigación blockchain. Un caso transfronterizo demostrado: un "
                   "esquema organizado con 9 acusados en 4 jurisdicciones — 91 documentos procesados por la "
                   "plataforma.")},
            {"icon": "⚖", "tag": "AML · KYC", "t": "Antilavado de dinero",
             "d": ("Análisis de esquemas de lavado: cadenas de transacciones, origen de fondos, documentación de "
                   "cumplimiento. Un dominio propio de la plataforma junto a la práctica penal y civil.")},
            {"icon": "▦", "tag": "Civil", "t": "Conflictos laborales",
             "d": ("Expedientes de RRHH, contratos, órdenes y correspondencia interna. Detección de "
                   "contradicciones entre documentos y preparación de la posición para el juicio.")},
        ],
        "strip": ("<b>7 categorías de inteligencia</b> — Criminal · Civil · COMM (comercial internacional) · ECOM "
                  "(comercio electrónico y protección al consumidor) · FINREG (regulación financiera y AML) · IP · "
                  "Litigation Support — en <b>4 regiones</b>: América/EE. UU., Europa, Asia, India. Ampliable según "
                  "la práctica del cliente."),
    },
    "score": {
        "kicker": "Capacidad insignia",
        "title": "Puntuación de preparación del caso — de 0 a 100",
        "lead": ("No es generación de texto — es experticia del caso. Una evaluación numérica con vínculo "
                 "automático de pruebas y análisis de brechas, única en el mercado actual."),
        "big": "0–100",
        "big_label": "puntuación numérica de preparación del caso",
        "dims": [
            {"t": "Base probatoria", "d": "completitud y fiabilidad de cada prueba"},
            {"t": "Vínculo de cargos", "d": "pruebas asignadas a cargos y puntos concretos"},
            {"t": "Análisis de brechas", "d": "pruebas faltantes y puntos débiles detectados automáticamente"},
            {"t": "Teoría del caso", "d": "coherencia interna y solidez de la narrativa"},
            {"t": "Líneas de riesgo", "d": "vías probables de ataque de la defensa"},
        ],
        "steps_title": "Dentro del análisis de IA en 8 etapas",
        "steps": ["Coherencia y conectividad de los documentos",
                  "Detección de contradicciones entre declaraciones",
                  "Análisis contextual — secuencia y lógica",
                  "Evaluación de la calidad de las pruebas",
                  "Conformidad con las normas legales",
                  "Corrección de la terminología jurídica",
                  "Evaluación de riesgos y vulnerabilidades",
                  "Dictamen final de preparación"],
        "ribbon": ("Ventaja clave: una puntuación numérica de preparación del caso (0–100). Ningún competidor del "
                   "mercado ofrece un equivalente."),
    },
    "security": {
        "kicker": "Seguridad",
        "title": "Seguridad por arquitectura, no por promesa",
        "lead": ("Parselex está diseñado para los requisitos de confidencialidad de la práctica jurídica y "
                 "bancaria: acceso Zero-Trust, anonimización en el dispositivo y despliegue dentro de su propio "
                 "perímetro."),
        "cards": [
            {"icon": "⛨", "t": "LexZTNA — acceso Zero-Trust",
             "d": ("Sin endpoints públicos. Los espacios de trabajo solo son accesibles mediante el cliente seguro "
                   "LexZTNA — túneles mesh cifrados, verificación de dispositivos y acceso con privilegios "
                   "mínimos.")},
            {"icon": "⚿", "t": "Cortafuegos ético — redacción de PII",
             "d": ("Nombres, identificadores y números de cuenta se sustituyen por tokens deterministas en su "
                   "dispositivo antes de la transmisión — un valor se convierte en un token, de modo que la IA "
                   "conserva la coherencia de las entidades. La reidentificación ocurre localmente en el retorno.")},
            {"icon": "⚙", "t": "Despliegue on-premise",
             "d": ("Modelos de pesos abiertos se ejecutan dentro de su infraestructura: la inferencia y la "
                   "búsqueda semántica nunca llaman a APIs de IA externas y los documentos nunca salen de su "
                   "perímetro.")},
            {"icon": "✓", "t": "Cumplimiento y auditoría",
             "d": ("Aislamiento de datos por usuario, registro completo de acciones y verificación de permisos en "
                   "cada operación — integrable en las políticas de seguridad de la información. Minimización de "
                   "datos alineada con GDPR, CCPA y ABA Model Rule 1.6.")},
        ],
        "pilot": ("→ <b>Piloto en 4–8 semanas</b> — con sus documentos, dentro de su perímetro seguro → puntuación "
                  "de preparación del caso (0–100) → contrato Professional o Enterprise"),
    },
    "arch": {
        "kicker": "Bajo el capó",
        "title": "Un sistema de IA multinivel",
        "lead": ("Una cascada de modelos de IA sin dependencia de un único proveedor — desde embeddings y "
                 "recuperación hasta generación de texto y puntuación de casos."),
        "pipeline_title": "El pipeline de procesamiento de 7 etapas",
        "pipeline": ["Ingest", "OCR", "Classification", "Validation", "RAG Analysis", "AI Translation", "Report"],
        "cascade_title": "Una cascada de 4 niveles que nunca se detiene",
        "cascade": [
            {"n": "01", "t": "Modelo cloud principal", "d": "Rápido y rentable para la carga diaria"},
            {"n": "02", "t": "Segundo proveedor cloud", "d": "Conmutación automática — el trabajo nunca se detiene"},
            {"n": "03", "t": "Modelo local on-premise", "d": "Se ejecuta en su perímetro con coste cero por consulta"},
            {"n": "04", "t": "Reserva adicional", "d": "Continuidad del servicio incluso ante caídas del proveedor"},
        ],
        "strip": ("Búsqueda semántica multilingüe — EN · RU · HI · NP · KZ · TR — con selección automática de "
                  "jurisdicción. <b>Despliegue dentro de su perímetro:</b> modelos de pesos abiertos, sin llamadas "
                  "a APIs de IA externas, documentos nunca enviados a servicios de terceros."),
    },
    "modules": {
        "kicker": "Producto",
        "title": "Un espacio de trabajo para todo el ciclo del caso",
        "lead": ("Una única interfaz web desde la carga de documentos hasta la evaluación de preparación — doce "
                 "módulos cubren el ciclo completo."),
        "tiles": [
            {"icon": "◌", "t": "Chat IA del caso", "d": "respuestas con citas a documentos concretos"},
            {"icon": "▤", "t": "Documentos", "d": "carga, búsqueda y gestión documental del caso"},
            {"icon": "▦", "t": "Biblioteca", "d": "catálogo categorizado de documentos legales"},
            {"icon": "✎", "t": "Redacción", "d": "borradores de documentos legales con asistente de IA"},
            {"icon": "▦", "t": "Análisis", "d": "análisis de ciclo cerrado con seguimiento de iteraciones"},
            {"icon": "✓", "t": "Puntuación del caso", "d": "0–100, vínculo de pruebas, análisis de brechas"},
            {"icon": "◯", "t": "Jurisdicción", "d": "7 dominios: penal, civil, AML/KYC, IP"},
            {"icon": "✿", "t": "Pipeline", "d": "procesamiento masivo: estado e historial"},
            {"icon": "▦", "t": "Módulos", "d": "extensiones flexibles según el cliente"},
            {"icon": "⚙", "t": "Opciones", "d": "configuración de la plataforma por práctica"},
            {"icon": "♟", "t": "Usuarios", "d": "gestión de accesos y registro de acciones"},
            {"icon": "▦", "t": "Analítica del corpus", "d": "estadísticas y monitoreo del procesamiento"},
        ],
    },
    "metrics": {
        "kicker": "Evidencias",
        "title": "Probado en casos reales",
        "lead": "Cifras de producción con cargas reales — no condiciones de demostración.",
        "stats": [("99,6%", "procesamientos con éxito"), ("95%", "metadatos extraídos automáticamente"),
                  ("2.500+", "documentos en pipelines de producción"), ("2.309", "verificaciones automáticas por release"),
                  ("7", "categorías de inteligencia"), ("4", "jurisdicciones en un caso real")],
        "case": {
            "tag": "Caso real destacado",
            "title": "Persecución transfronteriza por criptofraude",
            "desc": ("Un esquema organizado de fraude investigado en cuatro jurisdicciones a la vez — el caso "
                     "completo corre por la plataforma: desde la ingesta hasta la evaluación de preparación."),
            "rows": [("Acusados", "9 · 4 jurisdicciones"), ("Documentos procesados", "91"),
                     ("Fragmentos en la base de conocimiento", "792 · todo consultable por IA"),
                     ("Documentos relevantes aislados", "52"), ("Dominio", "penal · blockchain")],
        },
        "quality_title": "Ingeniería de calidad",
        "quality": ["Autoverificación de releases — cada versión pasa el ciclo completo de comprobaciones",
                    "Suite de pruebas automatizadas — 2.309 verificaciones de código",
                    "Comprobaciones automáticas de escenarios clave de la interfaz",
                    "Medición semanal de la calidad de búsqueda en producción"],
    },
    "compare": {
        "kicker": "Panorama competitivo",
        "title": "Dónde se sitúa Parselex",
        "lead": "El mercado se divide en tres grupos — y cada uno se detiene donde empieza el trabajo real del caso.",
        "rows": [
            {"grp": "Gigantes del LegalTech", "who": "Thomson Reuters (Westlaw, CoCounsel) · LexisNexis",
             "lim": "Enfoque en bases de datos e investigación; precisión del 42–65% y alucinaciones de hasta el 33%.",
             "win_t": "Experticia profunda del caso en lugar de búsqueda —",
             "win_d": "el sistema evalúa la preparación del caso, no solo encuentra documentos."},
            {"grp": "Asistentes de IA para abogados", "who": "Harvey · Spellbook · Kannon",
             "lim": "Profundidad limitada a la generación; sin evaluación del caso; integraciones a menudo estrechas.",
             "win_t": "Análisis autónomo y análisis de brechas —",
             "win_d": "experticia que detecta puntos débiles sin una persona en cada paso."},
            {"grp": "Plataformas de automatización", "who": "LexCheck · Luminance · Ironclad",
             "lim": "Principalmente contratos y due diligence; cobertura de jurisdicciones limitada.",
             "win_t": "7 dominios legales y 4 regiones —",
             "win_d": "penal, civil, comercial, AML y más, con las especificidades regionales integradas."},
        ],
        "ribbon": ("Ventaja clave: la puntuación numérica de preparación del caso (0–100) — ningún competidor "
                   "ofrece un equivalente."),
    },
    "pricing": {
        "kicker": "Monetización",
        "title": "Modelo híbrido, listo para la empresa",
        "lead": ("Suscripciones SaaS para equipos y soluciones corporativas con despliegue on-premise y "
                 "entrenamiento personalizado de modelos — optimizadas para cada segmento del mercado legal."),
        "tiers": [
            {"name": "Starter", "for": "Para pilotos y equipos pequeños",
             "features": ["Corpus de hasta 500 documentos", "Búsqueda con IA y clasificación documental",
                          "Verificaciones automáticas básicas", "Soporte por correo"],
             "cta": "Iniciar un piloto"},
            {"name": "Professional", "for": "Para equipos legales en operación",
             "pop": "Recomendado", "hot": True,
             "features": ["Corpus de hasta 5.000 documentos", "Todos los módulos de la plataforma",
                          "Puntuación de preparación del caso", "Soporte prioritario"],
             "cta": "Solicitar precio"},
            {"name": "Enterprise", "for": "Para instituciones y bancos",
             "features": ["Corpus ilimitado", "Despliegue on-premise dentro de su perímetro",
                          "Ajuste fino de modelos para el cliente", "Soporte dedicado con SLA",
                          "Integraciones personalizadas"],
             "cta": "Hablar con nosotros"},
        ],
        "note": "Canales de venta: ventas directas · proyectos piloto · red de socios. Precios a petición.",
    },
    "market": {
        "kicker": "Mercado",
        "title": "Un mercado que crece exponencialmente",
        "lead": ("El LegalTech global escala con rapidez y Parselex ocupa un nicho único en la intersección de la "
                 "IA y la analítica documental legal."),
        "cards": [
            {"t": "TAM — mercado total", "n": "$300 MM para 2028",
             "d": ("El LegalTech global alcanzó $49 MM en 2024 con proyección de $300 MM para 2028 (CAGR 9,4%) — "
                   "incluyendo analítica documental, cumplimiento y automatización.")},
            {"t": "SAM — mercado servible", "n": "El segmento de mayor crecimiento",
             "d": ("La analítica documental con IA. Parselex apunta a 7+ dominios legales y 4 regiones clave — "
                   "cientos de miles de despachos, organismos investigadores y consultoras en todo el mundo.")},
            {"t": "SOM — cabeza de playa", "n": "Primero India y la CEI",
             "d": ("Un segmento concreto y medible donde el producto ya está validado — primeros ingresos vía "
                   "pilotos y suscripciones Professional / Enterprise, luego escala por regiones.")},
        ],
    },
    "roadmap": {
        "kicker": "Trayectoria",
        "title": "Dinámica de desarrollo",
        "lead": "Del inicio del proyecto a los pipelines de producción en un solo año — con una ruta clara de escalado.",
        "items": [
            {"yr": "2026", "t": "Inicio del proyecto", "d": "La plataforma se concibe alrededor de casos reales."},
            {"yr": "2026", "t": "Primer release", "d": "Producto en funcionamiento con suite de pruebas automatizadas."},
            {"yr": "2026", "t": "Hub unificado de IA", "d": "40 herramientas para agentes bajo una única capa de orquestación."},
            {"yr": "2026", "t": "2.500+ documentos en producción", "d": "Pipelines reales del cliente procesando cargas reales."},
            {"yr": "2027", "t": "Escalado SaaS multi-tenant", "d": "Nuevos mercados, integraciones y aplicación móvil."},
        ],
    },
    "cta": {
        "title": "Empiece con Parselex",
        "sub": ("Pase su primer caso por la plataforma o comience con la documentación de arquitectura — "
                "los análisis profundos viven en docs.parselex.app."),
        "primary": "Abrir Parselex",
        "secondary": "Explorar la documentación",
    },
    "footer": {
        "tagline": "Plataforma de Inteligencia Documental Legal — desde cualquier fuente hasta una puntuación objetiva de preparación del caso.",
        "docs_note": "La investigación de arquitectura, seguridad y el benchmark RAG viven en",
        "col_platform_title": "Plataforma",
        "col_platform": ["Abrir la aplicación", "Documentación", "Arquitectura de seguridad", "Benchmark RAG"],
        "col_legal_title": "Legal",
        "legal": {"privacy": "Privacidad", "personal_data": "Uso de datos personales", "cookies": "Cookies",
                  "terms": "Términos del servicio", "payments": "Pagos recurrentes", "disclaimer": "Aviso de IA"},
        "contact": "Soporte",
        "copyright": "© 2026 Parselex — Plataforma de Inteligencia Documental Legal",
    },
}
