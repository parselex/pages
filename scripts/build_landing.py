#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the parselex.app landing page in 6 languages (en/uk/ru/es/fr/hi).

Content sources:
  - v15 presentation "Parselex — презентация для банка" (16 slides)
  - international terminology of docs.parselex.app (LexZTNA, Ethics Firewall,
    Case Readiness Score, 7 intelligence categories, ...)
Constraints: no founder names, no screenshots, self-contained single-file pages.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content_en import C as EN  # noqa: E402
from content_uk import C as UK  # noqa: E402
from content_ru import C as RU  # noqa: E402
from content_es import C as ES  # noqa: E402
from content_fr import C as FR  # noqa: E402
from content_hi import C as HI  # noqa: E402

DEFAULT_OUT = "/home/z/my-project/download/parselex-landing"
LANGS = {"en": (EN, ""), "es": (ES, "es/"), "fr": (FR, "fr/"), "hi": (HI, "hi/"), "ru": (RU, "ru/"), "uk": (UK, "uk/")}
ORDER = ["en", "es", "fr", "hi", "ru", "uk"]
HOST = "https://parselex.app"
DOCS = "https://docs.parselex.app"
# Fleet services behind /login/. While the applications are in final
# development the sign-in cards link to the on-page waiting list (#waitlist);
# these direct URLs come back at launch.
# Studio = the main application, formerly "LexRegister" (renamed 2026-10).
APP = "https://lexregister.parselex.app"       # Studio
DASH = "https://dashboard.parselex.app/login"  # Admin Workspace
MCPHUB = "https://mcp-hub.parselex.app/login"  # MCP Hub
LOGIN = HOST + "/login/"
LINKEDIN = "https://www.linkedin.com/company/parselex"
CHANGELOG = HOST + "/changelog/"
OG_IMAGE = HOST + "/og.png"

# Site-level facts (same for every locale): founder/jurisdiction block and its labels.
ABOUT = {
    "en": {
        "kicker": "Who is behind Parselex", "title": "Built by a founder, not a committee",
        "tag": "Self-funded · Founder-led · Independent",
        "p1": ("Parselex is built and operated by a hands-on founder working directly with live legal "
               "caseloads — the product is shaped by real criminal, civil and financial cases, not market "
               "research. The platform grew from practice: every capability answers a problem encountered "
               "in production casework."),
        "p2": ("The project runs as a lean, self-funded operation with an unusually strong engineering culture: "
               "2,309 automated checks per release, weekly search-quality measurement and a multi-agent "
               "infrastructure (40 tools under one orchestration hub). The company is in the process of "
               "incorporation; legal entity details will be published on this page once finalized."),
        "cta": "Connect on LinkedIn",
    },
    "uk": {
        "kicker": "Хто стоїть за Parselex", "title": "Створено засновником, а не комітетом",
        "tag": "Самофінансування · Керується засновником · Незалежний",
        "p1": ("Parselex створює та розвиває практикуючий засновник, який працює з живими юридичними справами "
               "власноруч — продукт сформований реальними кримінальними, цивільними та фінансовими справами, "
               "а не маркетинговими дослідженнями. Платформа виросла з практики: кожна можливість відповідає "
               "на проблему, зустрінуту у бойовому провадженні."),
        "p2": ("Проєкт працює як компактна самофінансована операція з незвично сильною інженерною культурою: "
               "2 309 автоматичних перевірок на реліз, щотижневий замір якості пошуку та мультиагентна "
               "інфраструктура (40 інструментів під одним оркестратором). Компанія перебуває у процесі "
               "інкорпорації; реквізити юридичної особи буде опубліковано на цій сторінці після завершення."),
        "cta": "Напишіть у LinkedIn",
    },
    "ru": {
        "kicker": "Кто стоит за Parselex", "title": "Создано основателем, а не комитетом",
        "tag": "Самофинансирование · Развивается основателем · Независимый",
        "p1": ("Parselex создаёт и развивает практикующий основатель, работающий с живыми юридическими делами "
               "вручную — продукт сформирован реальными уголовными, гражданскими и финансовыми делами, "
               "а не маркетинговыми исследованиями. Платформа выросла из практики: каждая возможность "
               "отвечает на проблему, встреченную в боевом производстве."),
        "p2": ("Проект работает как компактная самофинансируемая операция с необычно сильной инженерной "
               "культурой: 2 309 автоматических проверок на релиз, еженедельный замер качества поиска и "
               "мультиагентная инфраструктура (40 инструментов под одним оркестратором). Компания находится "
               "в процессе инкорпорации; реквизиты юридического лица будут опубликованы на этой странице "
               "после завершения."),
        "cta": "Написать в LinkedIn",
    },
    "es": {
        "kicker": "Quién está detrás de Parselex", "title": "Creado por un fundador, no por un comité",
        "tag": "Autofinanciado · Dirigido por su fundador · Independiente",
        "p1": ("Parselex lo construye y opera un fundador que trabaja directamente con causas "
               "legales reales: el producto está forjado por casos penales, civiles y financieros reales, "
               "no por estudios de mercado. La plataforma nació de la práctica: cada capacidad responde a "
               "un problema encontrado en producción."),
        "p2": ("El proyecto opera como una operación compacta y autofinanciada con una cultura de ingeniería "
               "excepcionalmente sólida: 2 309 verificaciones automáticas por versión, medición semanal de la "
               "calidad de búsqueda e infraestructura multiagente (40 herramientas bajo un único orquestador). "
               "La sociedad está en proceso de constitución; los datos jurídicos se publicarán aquí."),
        "cta": "Conectar en LinkedIn",
    },
    "fr": {
        "kicker": "Qui se cache derrière Parselex", "title": "Conçu par un fondateur, pas par un comité",
        "tag": "Autofinancé · Porté par son fondateur · Indépendant",
        "p1": ("Parselex est construit et opéré par un fondateur qui travaille en direct sur des "
               "dossiers juridiques réels : le produit est façonné par des affaires pénales, civiles et "
               "financières concrètes, non par des études de marché. Chaque capacité répond à un problème "
               "rencontré en production."),
        "p2": ("Le projet fonctionne comme une operation compacte et autofinancée dotée d'une culture "
               "d'ingénierie remarquablement solide : 2 309 vérifications automatiques par version, mesure "
               "hebdomadaire de la qualité de recherche et infrastructure multi-agents (40 outils sous un "
               "seul orchestrateur). La société est en cours de constitution ; ses informations juridiques "
               "seront publiées ici."),
        "cta": "Échanger sur LinkedIn",
    },
    "hi": {
        "kicker": "Parselex के पीछे कौन है", "title": "एक संस्थापक का काम, समिति का नहीं",
        "tag": "स्व-वित्तपोषित · संस्थापक-नेतृत्व · स्वतंत्र",
        "p1": ("Parselex को एक अनुभवी संस्थापक स्वयं वास्तविक कानूनी मामलों के साथ काम करके बनाता और "
               "संचालित करता है — उत्पाद वास्तविक आपराधिक, सिविल और वित्तीय मामलों से आकार लिया है, बाज़ार "
               "अनुसंधान से नहीं। हर क्षमता उत्पादन-स्तर की समस्या का समाधान है।"),
        "p2": ("परियोजना एक तेज़, स्व-वित्तपोषित संचालन के रूप में चलती है, जिसमें असाधारण रूप से मज़बूत "
               "इंजीनियरिंग संस्कृति है: प्रति रिलीज़ 2,309 स्वचालित जाँचें, साप्ताहिक खोज-गुणवत्ता मापन और "
               "मल्टी-एजेंट इंफ्रास्ट्रक्चर (एक ही ऑर्केस्ट्रेटर के अंतर्गत 40 टूल)। कंपनी निगमीकरण की प्रक्रिया "
               "में है; कानूनी विवरण यहाँ प्रकाशित होंगे।"),
        "cta": "LinkedIn पर जुड़ें",
    },
}

CSS = """
:root{--navy:#1B2A4A;--navy2:#2C4270;--navyD:#0F1A33;--gold:#C9953C;--gold2:#D4A843;
--goldsoft:rgba(201,149,60,.14);--ink:#1F2937;--muted:#5B6B7F;--line:#E4E8EF;
--bg:#FFFFFF;--soft:#F6F8FB;--green:#1A7F4C;--red:#C62828}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;
background:var(--bg);color:var(--ink);line-height:1.6;font-size:15.5px}
a{color:inherit;text-decoration:none}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
section{padding:72px 0}
section.alt{background:var(--soft)}
.kicker{color:var(--gold);font-weight:700;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:10px}
h1{font-size:clamp(29px,4.6vw,54px);line-height:1.14;letter-spacing:-.02em;font-weight:800;overflow-wrap:break-word}
h2{font-size:clamp(25px,3.2vw,34px);line-height:1.2;letter-spacing:-.015em;font-weight:800;color:var(--navy)}
h3{font-size:16.5px;font-weight:700;color:var(--navy)}
.lead{color:var(--muted);font-size:17px;max-width:760px;margin-top:14px}
.accent{color:var(--gold2)}
.head{margin-bottom:38px}
/* ---------- nav ---------- */
.nav{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);
border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;gap:22px;height:60px}
.logo{display:flex;align-items:center;gap:9px;font-weight:800;letter-spacing:.16em;font-size:14.5px;color:var(--navy)}
.logo .mark{width:28px;height:28px;border-radius:7px;background:var(--navy);color:var(--gold2);
display:grid;place-items:center;font-size:15px;letter-spacing:0}
.navlinks{display:flex;gap:20px;margin-left:auto}
.navlinks a{font-size:13.5px;font-weight:600;color:var(--muted)}
.navlinks a:hover{color:var(--navy)}
.langs{display:flex;gap:2px;background:var(--soft);border:1px solid var(--line);border-radius:8px;padding:3px}
.langs a{font-size:11.5px;font-weight:700;padding:3px 8px;border-radius:6px;color:var(--muted);letter-spacing:.04em}
.langs a.on{background:var(--navy);color:#fff}
.langs a:hover:not(.on){color:var(--navy)}
.btn{display:inline-flex;align-items:center;gap:8px;font-weight:700;border-radius:9px;cursor:pointer;
transition:.18s;border:1px solid transparent}
.btn-navy{background:var(--navy);color:#fff;padding:9px 16px;font-size:13.5px}
.btn-navy:hover{background:var(--navy2)}
.btn-gold{background:var(--gold);color:#fff;padding:13px 24px;font-size:15px}
.btn-gold:hover{background:var(--gold2)}
.btn-ghost{border-color:rgba(255,255,255,.35);color:#fff;padding:13px 24px;font-size:15px}
.btn-ghost:hover{border-color:var(--gold2);color:var(--gold2)}
.btn-line{border-color:var(--line);color:var(--navy);padding:13px 24px;font-size:15px;background:#fff}
.btn-line:hover{border-color:var(--navy)}
.burger{display:none;margin-left:auto;background:none;border:0;font-size:22px;color:var(--navy);cursor:pointer}
/* ---------- hero ---------- */
.hero{background:radial-gradient(900px 420px at 78% -10%,rgba(201,149,60,.22),transparent 60%),
radial-gradient(700px 380px at 8% 108%,rgba(44,66,112,.55),transparent 60%),linear-gradient(160deg,var(--navyD),var(--navy));
color:#fff;padding:88px 0 66px}
.badge{display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(212,168,67,.5);color:var(--gold2);
font-size:12.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:7px 14px;border-radius:99px;background:rgba(201,149,60,.1)}
.badge .dot{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 0 3px rgba(26,127,76,.25)}
.hero .sub{color:rgba(255,255,255,.82);font-size:18px;max-width:730px;margin-top:20px}
.hero .ctas{display:flex;gap:14px;margin-top:30px;flex-wrap:wrap}
.hero .note{margin-top:22px;color:rgba(255,255,255,.55);font-size:13px;letter-spacing:.02em}
.hstats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:46px;
border-top:1px solid rgba(255,255,255,.14);padding-top:28px}
.hstat .n{font-size:clamp(24px,3vw,34px);font-weight:800;color:var(--gold2);letter-spacing:-.01em}
.hstat .l{color:rgba(255,255,255,.66);font-size:12.5px;margin-top:3px}
/* ---------- cards & grids ---------- */
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:24px;box-shadow:0 1px 2px rgba(15,26,51,.04)}
.card p{color:var(--muted);font-size:14.5px;margin-top:8px}
.num{font-size:13px;font-weight:800;color:var(--gold);letter-spacing:.1em}
.ic{width:42px;height:42px;border-radius:10px;background:var(--goldsoft);color:var(--navy);
display:grid;place-items:center;font-size:19px;margin-bottom:14px}
.tag{display:inline-block;font-size:10.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
color:var(--navy);background:var(--goldsoft);border:1px solid rgba(201,149,60,.35);border-radius:6px;padding:3px 8px}
/* two-col platform lists */
.twocol .card ul{list-style:none;margin-top:12px}
.twocol li{padding:9px 0 9px 26px;position:relative;color:var(--ink);font-size:14.5px;border-top:1px dashed var(--line)}
.twocol li:first-child{border-top:0}
.twocol li::before{content:"✓";position:absolute;left:2px;color:var(--gold);font-weight:800}
/* score */
.scoregrid{display:grid;grid-template-columns:1fr 1.15fr;gap:22px;align-items:start}
.bignum{font-size:clamp(52px,6vw,76px);font-weight:800;letter-spacing:-.03em;
background:linear-gradient(100deg,var(--navy),var(--gold));-webkit-background-clip:text;background-clip:text;color:transparent}
.scorebar{height:10px;border-radius:99px;background:linear-gradient(90deg,#E8EBF1 0%,var(--gold) 60%,var(--green) 100%);margin:16px 0 6px;position:relative;overflow:hidden}
.scorebar::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 46px,rgba(255,255,255,.55) 46px 48px)}
.dim{display:flex;gap:12px;padding:10px 0;border-top:1px dashed var(--line)}
.dim:first-of-type{border-top:0}
.dim .ck{color:var(--green);font-weight:800}
.dim b{color:var(--navy)}
.dim span.d{color:var(--muted);font-size:14px}
.steps{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.step{display:flex;gap:11px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 13px;align-items:flex-start}
.step .i{min-width:24px;height:24px;border-radius:7px;background:var(--navy);color:var(--gold2);font-size:12px;font-weight:800;display:grid;place-items:center}
.step p{font-size:13.5px;color:var(--ink)}
.ribbon{margin-top:26px;background:linear-gradient(120deg,var(--navyD),var(--navy2));color:#fff;border-radius:14px;
padding:20px 24px;display:flex;gap:14px;align-items:center;font-weight:600}
.ribbon .r{font-size:22px;color:var(--gold2)}
/* pipeline chips */
.chips{display:flex;flex-wrap:wrap;gap:9px;align-items:center;margin-top:16px}
.chip{background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 14px;font-size:13.5px;font-weight:700;color:var(--navy)}
.ar{color:var(--gold);font-weight:800}
.cascade{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}
.casc .card{padding:18px}
.casc .cn{font-size:12px;font-weight:800;color:var(--gold);letter-spacing:.1em}
.softstrip{margin-top:20px;border:1px dashed rgba(201,149,60,.55);background:var(--goldsoft);
border-radius:12px;padding:15px 20px;font-size:14.5px;color:var(--ink)}
/* modules */
.mods{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}
.mod{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px}
.mod .mg{font-size:19px;color:var(--navy);background:var(--goldsoft);width:36px;height:36px;border-radius:9px;display:grid;place-items:center}
.mod b{display:block;color:var(--navy);margin-top:10px;font-size:14px}
.mod p{color:var(--muted);font-size:12.5px;margin-top:3px;line-height:1.5}
/* metrics */
.mstats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.mstat{background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px;text-align:left}
.mstat .n{font-size:clamp(30px,3.4vw,40px);font-weight:800;color:var(--navy);letter-spacing:-.02em}
.mstat .l{color:var(--muted);font-size:13.5px;margin-top:4px}
.casecard{margin-top:22px;background:linear-gradient(120deg,var(--navyD),var(--navy));border-radius:16px;color:#fff;padding:28px;display:grid;grid-template-columns:1.05fr 1fr;gap:26px}
.casecard h3{color:#fff;font-size:18px}
.casecard .ct{color:var(--gold2);font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
.casecard .rows{display:grid;gap:8px}
.crow{display:flex;justify-content:space-between;gap:14px;border-bottom:1px dashed rgba(255,255,255,.18);padding-bottom:8px;font-size:14px}
.crow b{color:var(--gold2);font-weight:700;white-space:nowrap;text-align:right}
.crow span{color:rgba(255,255,255,.85)}
.qlist{display:grid;grid-template-columns:1fr 1fr;gap:8px 22px;margin-top:14px}
.qlist div{padding-left:24px;position:relative;color:var(--muted);font-size:14px}
.qlist div::before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:800}
/* compare */
.cmp .card{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.cmp .grp b{color:var(--navy);font-size:16px}
.cmp .who{color:var(--muted);font-size:13.5px;margin-top:5px}
.cmp .lim{color:var(--red);font-size:13.5px;margin-top:8px;display:flex;gap:8px}
.cmp .win{color:var(--ink);font-size:14.5px;display:flex;gap:10px}
.cmp .win::before{content:"✓";color:var(--green);font-weight:800}
.cmp .win b{color:var(--navy)}
.cmp .card + .card{margin-top:14px}
/* pricing */
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch}
.tier{background:#fff;border:1px solid var(--line);border-radius:16px;padding:26px;display:flex;flex-direction:column;position:relative}
.tier.hot{background:linear-gradient(160deg,var(--navyD),var(--navy2));color:#fff;border-color:var(--navy)}
.tier .tn{font-size:18px;font-weight:800;color:var(--navy)}
.tier.hot .tn{color:#fff}
.tier .tf{color:var(--muted);font-size:13.5px;margin-top:3px}
.tier.hot .tf{color:rgba(255,255,255,.72)}
.tier ul{list-style:none;margin:16px 0 22px;flex:1}
.tier li{padding:7px 0 7px 24px;position:relative;font-size:14px;border-top:1px dashed var(--line)}
.tier.hot li{border-top-color:rgba(255,255,255,.15)}
.tier li::before{content:"✓";position:absolute;left:2px;color:var(--gold);font-weight:800}
.tier .btn{justify-content:center}
.pop{position:absolute;top:-11px;right:18px;background:var(--gold);color:#fff;font-size:10.5px;font-weight:800;
letter-spacing:.09em;text-transform:uppercase;border-radius:99px;padding:5px 12px}
.tier .btn-navy{width:100%;justify-content:center}
.tier.hot .btn-gold{width:100%}
.pnote{text-align:center;color:var(--muted);font-size:13.5px;margin-top:20px}
/* market */
.mcards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.mcard .mn{font-size:21px;font-weight:800;color:var(--navy);letter-spacing:-.01em}
.mcard .mt{color:var(--gold);font-weight:800;font-size:11.5px;letter-spacing:.12em;text-transform:uppercase}
/* roadmap */
.timeline{position:relative;margin-top:8px;padding-left:26px}
.timeline::before{content:"";position:absolute;left:7px;top:8px;bottom:8px;width:2px;background:linear-gradient(var(--gold),var(--line))}
.tl{position:relative;padding:0 0 26px 18px}
.tl:last-child{padding-bottom:0}
.tl::before{content:"";position:absolute;left:-26px;top:5px;width:16px;height:16px;border-radius:50%;
background:#fff;border:3px solid var(--gold)}
.tl .yr{display:inline-block;background:var(--navy);color:var(--gold2);font-size:11.5px;font-weight:800;letter-spacing:.08em;
border-radius:6px;padding:3px 10px;margin-bottom:6px}
.tl b{color:var(--navy);display:block}
.tl span{color:var(--muted);font-size:14px}
/* cta */
.ctaband{background:radial-gradient(700px 300px at 85% 0%,rgba(201,149,60,.28),transparent 60%),linear-gradient(140deg,var(--navyD),var(--navy));
border-radius:20px;color:#fff;padding:56px 40px;text-align:center}
.ctaband .ctas{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:26px}
/* footer */
footer{background:var(--navyD);color:rgba(255,255,255,.72);padding:52px 0 30px;font-size:13.5px}
.fgrid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:34px}
footer h4{color:#fff;font-size:13px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:14px}
footer .fl{display:grid;gap:9px}
footer a{overflow-wrap:anywhere}
footer a:hover{color:var(--gold2)}
.flogo{display:flex;align-items:center;gap:9px;color:#fff;font-weight:800;letter-spacing:.16em}
.flogo .mark{width:28px;height:28px;border-radius:7px;background:rgba(212,168,67,.15);color:var(--gold2);display:grid;place-items:center;font-size:15px}
.fbottom{border-top:1px solid rgba(255,255,255,.12);margin-top:36px;padding-top:20px;display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;color:rgba(255,255,255,.45);font-size:12.5px}
/* reveal */
.js .reveal{opacity:0;transform:translateY(14px);transition:opacity .55s ease,transform .55s ease}
.js .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.js .reveal{opacity:1;transform:none;transition:none}}
/* responsive */
@media(max-width:1020px){
 .grid3,.mcards,.mstats{grid-template-columns:1fr 1fr}
 .mods{grid-template-columns:1fr 1fr 1fr}
 .cascade{grid-template-columns:1fr 1fr}
 .scoregrid,.casecard{grid-template-columns:1fr}
 .cmp .card{grid-template-columns:1fr}
 .grid4{grid-template-columns:1fr 1fr!important}
}
@media(max-width:1080px){
 .navlinks{display:none;position:absolute;top:60px;left:0;right:0;background:#fff;border-bottom:1px solid var(--line);
 flex-direction:column;padding:16px 24px;gap:14px}
 .navlinks.open{display:flex}
 .langs{margin-left:auto}
 .burger{display:block;margin-left:0}
}
@media(max-width:720px){
 .nav .wrap{gap:10px}
 .logo{font-size:12.5px;letter-spacing:.09em;gap:7px}
 .langs{margin-left:auto;padding:2px}
 .langs a{padding:3px 6px;font-size:10.5px}
 .nav .btn-navy{display:none}
 .fgrid{grid-template-columns:1fr;gap:26px}
 .crow{flex-direction:column;gap:2px}
 .crow b{white-space:normal;text-align:left}
 .grid3,.grid2,.mstats,.mcards,.tiers,.steps,.qlist,.cascade{grid-template-columns:1fr}
 .mods{grid-template-columns:1fr 1fr}
 .grid4{grid-template-columns:1fr!important}
 .twocol .card+.card{margin-top:14px}
 .hstats{grid-template-columns:1fr 1fr;gap:20px}
 .ctaband{padding:40px 22px}
 .casecard{padding:22px}
 section{padding:56px 0}
}
@media(max-width:400px){
 .h1,h1{font-size:27px}
}
"""


def head(c, path_prefix):
    """<head> with hreflang alternates, canonical, meta — per language."""
    l = c["lang"]
    canonical = HOST + ("/" if not path_prefix else "/" + path_prefix)
    alts = "".join(
        f'\n  <link rel="alternate" hreflang="{code}" href="{HOST}/{("" if code == "en" else code + "/")}">'
        for code in ORDER
    )
    alts += f'\n  <link rel="alternate" hreflang="x-default" href="{HOST}/">'
    og_locale = {"en": "en_US", "uk": "uk_UA", "ru": "ru_RU", "es": "es_ES", "fr": "fr_FR", "hi": "hi_IN"}[l]
    og_image = (f'\n  <meta property="og:image" content="{OG_IMAGE}">'
                f'\n  <meta property="og:image:width" content="1200">'
                f'\n  <meta property="og:image:height" content="630">'
                f'\n  <meta name="twitter:image" content="{OG_IMAGE}">')
    return f"""<!DOCTYPE html>
<html lang="{l}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{c['meta_title']}</title>
<meta name="description" content="{c['meta_desc']}">
<meta property="og:title" content="{c['meta_title']}">
<meta property="og:description" content="{c['meta_desc']}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{og_locale}">
<meta name="twitter:card" content="summary_large_image">{og_image}{alts}
<link rel="canonical" href="{canonical}"><style>{CSS}</style>
<script>document.documentElement.classList.add('js');</script>
</head>"""


def nav(c, path_prefix):
    n = c["nav"]
    links = "".join(
        f'<a href="#{a}">{n[a]}</a>' for a in ["platform", "score", "security", "product", "metrics", "pricing"]
    )
    depth = 0 if not path_prefix else 1  # root page vs language subpage

    def lang_href(code):
        if code == c["lang"]:
            return "./"
        base = "" if depth == 0 else "../"
        return base if code == "en" else base + code + "/"

    langs = "".join(
        f'<a href="{lang_href(code)}" class="{"on" if code == c["lang"] else ""}">{code.upper()}</a>'
        for code in ORDER
    )
    return f"""
<nav class="nav"><div class="wrap">
  <a class="logo" href="#"><span class="mark">⚿</span>PARSELEX</a>
  <div class="navlinks" id="navlinks">{links}<a href="{DOCS}" target="_blank" rel="noopener">{n['docs']}</a></div>
  <div class="langs">{langs}</div>
  <a class="btn btn-navy" href="{LOGIN}">{n['cta']}</a>
  <button class="burger" id="burger" aria-label="Menu">☰</button>
</div></nav>"""


def sec_head(kicker, title, lead=""):
    x = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="head reveal"><p class="kicker">{kicker}</p><h2>{title}</h2>{x}</div>'


def render(c, path_prefix):
    h = c["hero"]
    p = c["problem"]
    pl = c["platform"]
    sc = c["sectors"]
    s = c["score"]
    se = c["security"]
    ar = c["arch"]
    mo = c["modules"]
    me = c["metrics"]
    cm = c["compare"]
    pr = c["pricing"]
    mk = c["market"]
    rm = c["roadmap"]
    ct = c["cta"]
    f = c["footer"]

    hstats = "".join(f'<div class="hstat"><div class="n">{n}</div><div class="l">{t}</div></div>' for n, t in h["stats"])
    hero = f"""
<header class="hero"><div class="wrap">
  <span class="badge"><span class="dot"></span>{h['badge']}</span>
  <h1 style="margin-top:22px">{h['h1']}</h1>
  <p class="sub">{h['sub']}</p>
  <div class="ctas"><a class="btn btn-gold" href="{LOGIN}">{h['cta1']}</a>
  <a class="btn btn-ghost" href="{DOCS}" target="_blank" rel="noopener">{h['cta2']}</a></div>
  <p class="note">{h['note']}</p>
  <div class="hstats">{hstats}</div>
</div></header>"""

    pcards = "".join(
        f'<div class="card"><div class="num">{x["num"]}</div><h3 style="margin-top:8px">{x["t"]}</h3><p>{x["d"]}</p></div>'
        for x in p["cards"]
    )
    why = "".join(
        f'<div class="card"><div class="ic">{x["icon"]}</div><h3>{x["t"]}</h3><p>{x["d"]}</p></div>' for x in p["why"]
    )
    problem = f"""
<section id="problem"><div class="wrap">
  {sec_head(p['kicker'], p['title'], p['lead'])}
  <div class="grid3">{pcards}</div>
  <h3 style="margin:44px 0 18px;font-size:20px" class="reveal">{p['why_title']}</h3>
  <div class="grid3 reveal">{why}</div>
</div></section>"""

    def ul(items):
        return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

    platform = f"""
<section id="platform" class="alt"><div class="wrap">
  {sec_head(pl['kicker'], pl['title'], pl['lead'])}
  <div class="grid2 twocol reveal">
    <div class="card"><h3>{pl['c1t']}</h3>{ul(pl['c1'])}</div>
    <div class="card"><h3>{pl['c2t']}</h3>{ul(pl['c2'])}</div>
  </div>
</div></section>"""

    scards = "".join(
        f'<div class="card"><div class="ic">{x["icon"]}</div><span class="tag">{x["tag"]}</span>'
        f'<h3 style="margin-top:10px">{x["t"]}</h3><p>{x["d"]}</p></div>' for x in sc["cards"]
    )
    sectors = f"""
<section id="sectors"><div class="wrap">
  {sec_head(sc['kicker'], sc['title'], sc['lead'])}
  <div class="grid4 reveal" style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px">{scards}</div>
  <p class="softstrip reveal">{sc['strip']}</p>
</div></section>"""

    dims = "".join(
        f'<div class="dim"><span class="ck">✓</span><div><b>{x["t"]}</b> — <span class="d">{x["d"]}</span></div></div>'
        for x in s["dims"]
    )
    steps = "".join(
        f'<div class="step"><span class="i">{i}</span><p>{t}</p></div>' for i, t in enumerate(s["steps"], 1)
    )
    score = f"""
<section id="score" class="alt"><div class="wrap">
  {sec_head(s['kicker'], s['title'], s['lead'])}
  <div class="scoregrid">
    <div class="card reveal">
      <div class="bignum">{s['big']}</div>
      <p style="color:var(--muted)">{s['big_label']}</p>
      <div class="scorebar"></div>
      {dims}
    </div>
    <div class="reveal">
      <h3 style="font-size:18px">{s['steps_title']}</h3>
      <div class="steps">{steps}</div>
    </div>
  </div>
  <div class="ribbon reveal"><span class="r">⚖</span><p>{s['ribbon']}</p></div>
</div></section>"""

    secards = "".join(
        f'<div class="card"><div class="ic">{x["icon"]}</div><h3>{x["t"]}</h3><p>{x["d"]}</p></div>' for x in se["cards"]
    )
    security = f"""
<section id="security"><div class="wrap">
  {sec_head(se['kicker'], se['title'], se['lead'])}
  <div class="grid2 reveal">{secards}</div>
  <p class="softstrip reveal" style="margin-top:22px">{se['pilot']}</p>
</div></section>"""

    chips = '<span class="ar">→</span>'.join(f'<span class="chip">{x}</span>' for x in ar["pipeline"])
    casc = "".join(
        f'<div class="card"><div class="cn">{x["n"]}</div><h3 style="margin-top:6px;font-size:15px">{x["t"]}</h3><p style="font-size:13.5px">{x["d"]}</p></div>'
        for x in ar["cascade"]
    )
    arch = f"""
<section id="architecture" class="alt"><div class="wrap">
  {sec_head(ar['kicker'], ar['title'], ar['lead'])}
  <h3 class="reveal" style="font-size:17px">{ar['pipeline_title']}</h3>
  <div class="chips reveal">{chips}</div>
  <h3 class="reveal" style="font-size:17px;margin-top:34px">{ar['cascade_title']}</h3>
  <div class="casc cascade reveal">{casc}</div>
  <p class="softstrip reveal">{ar['strip']}</p>
</div></section>"""

    tiles = "".join(
        f'<div class="mod"><div class="mg">{x["icon"]}</div><b>{x["t"]}</b><p>{x["d"]}</p></div>' for x in mo["tiles"]
    )
    modules = f"""
<section id="product"><div class="wrap">
  {sec_head(mo['kicker'], mo['title'], mo['lead'])}
  <div class="mods reveal">{tiles}</div>
</div></section>"""

    mstats = "".join(
        f'<div class="mstat reveal"><div class="n">{n}</div><div class="l">{t}</div></div>' for n, t in me["stats"]
    )
    case_rows = "".join(f'<div class="crow"><span>{k}</span><b>{v}</b></div>' for k, v in me["case"]["rows"])
    quality = "".join(f"<div>{q}</div>" for q in me["quality"])
    metrics = f"""
<section id="metrics" class="alt"><div class="wrap">
  {sec_head(me['kicker'], me['title'], me['lead'])}
  <div class="mstats">{mstats}</div>
  <div class="casecard reveal">
    <div><p class="ct">{me['case']['tag']}</p><h3 style="margin-top:8px">{me['case']['title']}</h3>
    <p style="color:rgba(255,255,255,.75);font-size:14px;margin-top:12px">{me['case']['desc']}</p></div>
    <div class="rows">{case_rows}</div>
  </div>
  <h3 class="reveal" style="margin-top:30px;font-size:17px">{me['quality_title']}</h3>
  <div class="qlist reveal">{quality}</div>
</div></section>"""

    rows = "".join(
        f'<div class="card reveal"><div class="grp"><b>{x["grp"]}</b><p class="who">{x["who"]}</p>'
        f'<p class="lim"><span>⊗</span>{x["lim"]}</p></div><p class="win"><span><b>{x["win_t"]}</b> {x["win_d"]}</span></p></div>'
        for x in cm["rows"]
    )
    compare = f"""
<section id="compare"><div class="wrap">
  {sec_head(cm['kicker'], cm['title'], cm['lead'])}
  <div class="cmp">{rows}</div>
  <div class="ribbon reveal"><span class="r">✓</span><p>{cm['ribbon']}</p></div>
</div></section>"""

    tiers = ""
    for t in pr["tiers"]:
        feats = "".join(f"<li>{x}</li>" for x in t["features"])
        pop = '<span class="pop">' + t["pop"] + "</span>" if t.get("pop") else ""
        btn_cls = "btn-gold" if t.get("hot") else "btn-navy"
        btn = f'<a class="btn {btn_cls}" href="{LOGIN}">{t["cta"]}</a>'
        tiers += f'<div class="tier{" hot" if t.get("hot") else ""} reveal">{pop}<div class="tn">{t["name"]}</div><div class="tf">{t["for"]}</div><ul>{feats}</ul>{btn}</div>'
    pricing = f"""
<section id="pricing" class="alt"><div class="wrap">
  {sec_head(pr['kicker'], pr['title'], pr['lead'])}
  <div class="tiers">{tiers}</div>
  <p class="pnote">{pr['note']}</p>
</div></section>"""

    mcards = "".join(
        f'<div class="card mcard reveal"><p class="mt">{x["t"]}</p><div class="mn" style="margin-top:6px">{x["n"]}</div><p style="margin-top:8px">{x["d"]}</p></div>'
        for x in mk["cards"]
    )
    market = f"""
<section id="market"><div class="wrap">
  {sec_head(mk['kicker'], mk['title'], mk['lead'])}
  <div class="mcards">{mcards}</div>
</div></section>"""

    tl = "".join(f'<div class="tl"><span class="yr">{x["yr"]}</span><b>{x["t"]}</b><span>{x["d"]}</span></div>' for x in rm["items"])
    roadmap = f"""
<section id="roadmap" class="alt"><div class="wrap">
  {sec_head(rm['kicker'], rm['title'], rm['lead'])}
  <div class="timeline reveal" style="max-width:640px">{tl}</div>
</div></section>"""

    ab = ABOUT[c["lang"]]
    about = f"""
<section id="about"><div class="wrap">
  <div class="head reveal"><p class="kicker">{ab['kicker']}</p><h2>{ab['title']}</h2>
    <p style="margin-top:14px"><span class="tag">{ab['tag']}</span></p></div>
  <div class="grid2 reveal">
    <div class="card"><p style="margin-top:0;font-size:15px">{ab['p1']}</p></div>
    <div class="card"><p style="margin-top:0;font-size:15px">{ab['p2']}</p></div>
  </div>
  <div style="margin-top:22px" class="reveal"><a class="btn btn-line" href="{LINKEDIN}" target="_blank" rel="noopener">in&nbsp;·&nbsp;{ab['cta']}</a></div>
</div></section>"""

    cta = f"""
<section id="get-started"><div class="wrap">
  <div class="ctaband reveal">
    <h2 style="color:#fff">{ct['title']}</h2>
    <p style="color:rgba(255,255,255,.8);font-size:16.5px;max-width:620px;margin:14px auto 0">{ct['sub']}</p>
    <div class="ctas"><a class="btn btn-gold" href="{LOGIN}">{ct['primary']}</a>
    <a class="btn btn-ghost" href="{DOCS}" target="_blank" rel="noopener">{ct['secondary']}</a></div>
  </div>
</div></section>"""

    def legal_links():
        base = DOCS + (f"/{c['lang']}" if c["lang"] != "en" else "")
        items = [
            ("privacy", f["legal"]["privacy"]),
            ("personal-data", f["legal"]["personal_data"]),
            ("cookies", f["legal"]["cookies"]),
            ("terms", f["legal"]["terms"]),
            ("payments", f["legal"]["payments"]),
            ("disclaimer", f["legal"]["disclaimer"]),
        ]
        return "".join(f'<a href="{base}/legal/{slug}/">{name}</a>' for slug, name in items)

    flinks = (
        f'<a href="{LOGIN}">{f["col_platform"][0]}</a>'
        f'<a href="{DOCS}" target="_blank" rel="noopener">{f["col_platform"][1]}</a>'
        f'<a href="{DOCS}/security/">{f["col_platform"][2]}</a>'
        f'<a href="{DOCS}/benchmark/">{f["col_platform"][3]}</a>'
        f'<a href="{CHANGELOG}">Changelog</a>'
        f'<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>'
    )
    footer = f"""
<footer><div class="wrap">
  <div class="fgrid">
    <div>
      <a class="flogo" href="#"><span class="mark">⚿</span>PARSELEX</a>
      <p style="margin-top:14px;max-width:320px">{f['tagline']}</p>
      <p style="margin-top:10px">{f['docs_note']} <a href="{DOCS}" target="_blank" rel="noopener" style="color:var(--gold2);font-weight:600">docs.parselex.app</a></p>
    </div>
    <div><h4>{f['col_platform_title']}</h4><div class="fl">{flinks}</div></div>
    <div><h4>{f['col_legal_title']}</h4><div class="fl">{legal_links()}</div></div>
  </div>
  <div class="fbottom"><span>{f['contact']}&nbsp;·&nbsp;parselex_support@googlegroups.com</span><span>{f['copyright']}</span></div>
</div></footer>"""

    js = """
<script>
var b=document.getElementById('burger'),n=document.getElementById('navlinks');
if(b){b.addEventListener('click',function(){n.classList.toggle('open')});
n.addEventListener('click',function(){n.classList.remove('open')})}
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){
es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},
{threshold:.08});
document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)})}
else{document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in')})}
</script>"""

    return (
        nav(c, path_prefix) + hero + problem + platform + sectors + score + security
        + arch + modules + metrics + compare + pricing + market + roadmap + about + cta
        + footer + js + "</body>\n</html>"
    )


_WL_SCRIPT = """<script>
(function(){
  var f=document.getElementById('wlform'),m=document.getElementById('wlmsg'),b=document.getElementById('wlbtn');
  if(!f||!m||!b){return}
  f.addEventListener('submit',function(e){
    e.preventDefault();
    b.disabled=true;b.textContent='Subscribing\u2026';
    fetch('https://formsubmit.co/ajax/parselex_support@googlegroups.com',{
      method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body:JSON.stringify({
        email:(f.elements.email.value||'').trim(),
        _subject:'Parselex waiting list \u2014 new subscriber',
        _template:'table',
        _captcha:'false',
        _honey:f.elements._honey.value
      })
    }).then(function(r){return r.json()}).then(function(j){
      if(j&&(j.success===true||j.success==='true')){
        m.textContent="You're on the list \u2014 thank you! We'll email you the moment access opens.";
        m.className='wlmsg ok';b.textContent='Subscribed';
      }else{throw new Error('rejected')}
    }).catch(function(){
      m.textContent='Something went wrong \u2014 please try again in a minute.';
      m.className='wlmsg err';b.disabled=false;b.textContent='Join the waiting list';
    });
    m.hidden=false;
  });
})();
</script>"""


def render_login():
    """Standalone sign-in hub page at /login/ — lists all fleet services.

    While the applications are in final development every card links to the
    on-page waiting list (#waitlist) instead of the service entry points.
    """
    cards = (
        ("Studio", "Main application",
         "The main Parselex application (user space): your documents, cases and workflows."),
        ("Admin Workspace", "Administration",
         "Sysadmin dashboard &#8212; fleet administration &amp; operational status."),
        ("MCP Hub", "Developers",
         "Developer hub &amp; service status."),
    )
    items = "".join(
        f'<a class="lcard{" lcard-primary" if i == 0 else ""}" href="#waitlist">'
        f'<span class="lcard-kicker">{kick}</span>'
        f'<span class="lcard-name">{name}</span>'
        f'<span class="lcard-desc">{desc}</span>'
        f'<span class="lcard-go">Coming soon &#8212; subscribe for updates &#8594;</span></a>'
        for i, (name, kick, desc) in enumerate(cards)
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Sign in &#8212; Parselex</title>
<meta name="description" content="Sign in to Parselex: Studio (main application), Admin Workspace and MCP Hub are in final development &#8212; join the waiting list and get launch updates.">
<link rel="canonical" href="https://parselex.app/login/">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='13' font-size='13'>&#9878;</text></svg>">
<style>
:root{{--navy:#1B2A4A;--navy2:#2C4270;--gold:#C9953C;--gold2:#D4A843;
--goldsoft:rgba(201,149,60,.14);--ink:#1F2937;--muted:#5B6B7F;--line:#E4E8EF;
--bg:#FFFFFF;--soft:#F6F8FB;--radius:14px}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:Inter,system-ui,-apple-system,'Segoe UI',sans-serif;background:var(--soft);color:var(--ink);min-height:100vh;display:flex;flex-direction:column}}
.lnav{{background:var(--navy);padding:18px 24px}}
.lnav .wrap{{max-width:960px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}}
.logo{{color:#fff;text-decoration:none;font-weight:800;letter-spacing:.14em;font-size:15px}}
.logo .mark{{color:var(--gold2)}}
.lback{{color:rgba(255,255,255,.75);text-decoration:none;font-size:13px}}
.lback:hover{{color:#fff}}
main{{flex:1;max-width:960px;width:100%;margin:0 auto;padding:64px 24px}}
h1{{font-size:clamp(28px,4vw,38px);color:var(--navy);letter-spacing:-.02em}}
.sub{{color:var(--muted);margin:12px 0 40px;font-size:15.5px;line-height:1.6;max-width:56ch}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}}
.lcard{{display:flex;flex-direction:column;gap:8px;background:var(--bg);border:1px solid var(--line);
border-radius:var(--radius);padding:26px 24px;text-decoration:none;color:inherit;
transition:transform .18s,box-shadow .18s,border-color .18s}}
.lcard:hover{{transform:translateY(-3px);box-shadow:0 14px 34px rgba(27,42,74,.10);border-color:var(--gold)}}
.lcard-primary{{border-color:var(--gold);background:linear-gradient(180deg,var(--goldsoft),var(--bg) 60%)}}
.lcard-kicker{{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold)}}
.lcard-name{{font-size:19px;font-weight:750;color:var(--navy)}}
.lcard-desc{{font-size:13.5px;color:var(--muted);line-height:1.55;flex:1}}
.lcard-go{{font-size:13px;font-weight:700;color:var(--navy2);margin-top:6px}}
.lcard:hover .lcard-go{{color:var(--gold)}}
.lfoot{{max-width:960px;width:100%;margin:0 auto;padding:24px;border-top:1px solid var(--line);
display:flex;gap:20px;justify-content:space-between;flex-wrap:wrap;font-size:12.5px;color:var(--muted)}}
.lfoot a{{color:var(--navy2);text-decoration:none}}
.lfoot a:hover{{color:var(--gold)}}
html{{scroll-behavior:smooth}}
.wl{{margin-top:44px;background:linear-gradient(180deg,var(--goldsoft),var(--bg) 70%);border:1px solid var(--line);border-radius:var(--radius);padding:30px 28px}}
.wl h2{{font-size:21px;color:var(--navy);letter-spacing:-.01em}}
.wl p{{color:var(--muted);font-size:14px;line-height:1.6;margin-top:8px;max-width:62ch}}
.wlrow{{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap}}
.wlrow input[type=email]{{flex:1;min-width:220px;height:46px;border:1px solid var(--line);border-radius:10px;padding:0 14px;font:inherit;font-size:14.5px;color:var(--ink);background:var(--bg);outline:none;transition:border-color .15s,box-shadow .15s}}
.wlrow input[type=email]:focus{{border-color:var(--gold);box-shadow:0 0 0 3px var(--goldsoft)}}
.wlrow button{{height:46px;padding:0 22px;border:0;border-radius:10px;background:var(--navy);color:#fff;font:inherit;font-size:14px;font-weight:700;cursor:pointer;transition:background .15s}}
.wlrow button:hover{{background:var(--navy2)}}
.wlrow button:disabled{{opacity:.65;cursor:default}}
.hp{{position:absolute;left:-9999px;opacity:0;width:0;height:0}}
.wlmsg{{margin-top:12px;font-size:13.5px;font-weight:600}}
.wlmsg.ok{{color:#1A7F37}}
.wlmsg.err{{color:#B42318}}
.wlsmall{{font-size:12px;color:var(--muted);margin-top:12px}}
.wlsmall a{{color:var(--navy2);text-decoration:underline}}
.wlsocial{{display:flex;gap:10px;align-items:center;margin-top:16px;flex-wrap:wrap}}
.wlsep{{font-size:12.5px;color:var(--muted)}}
.wlsbtn{{display:inline-flex;align-items:center;gap:7px;height:38px;padding:0 15px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--navy);font:inherit;font-size:13px;font-weight:700;text-decoration:none;transition:border-color .15s,color .15s}}
.wlsbtn:hover{{border-color:var(--gold);color:var(--gold)}}
.wlsbtn svg{{width:15px;height:15px;flex:none;fill:currentColor}}
</style>
</head>
<body>
<nav class="lnav"><div class="wrap">
  <a class="logo" href="/"><span class="mark">&#9878;</span> PARSELEX</a>
  <a class="lback" href="/">&#8592; Back to parselex.app</a>
</div></nav>
<main>
  <h1>Sign in to Parselex</h1>
  <p class="sub">All Parselex applications are in final development. Explore what&#8217;s
  launching below and subscribe to be notified the moment your sign-in goes live &#8212;
  every application will use your Parselex account through LexZTNA, our Zero-Trust secure client.</p>
  <div class="grid">{items}</div>
  <section class="wl" id="waitlist">
    <h2>Be the first to know</h2>
    <p>Studio, Admin Workspace and MCP Hub are in final development. Leave your email
    and we&#8217;ll notify you the moment access opens &#8212; launch news only, no spam.</p>
    <form class="wlrow" id="wlform">
      <input type="email" name="email" required placeholder="you@company.com" aria-label="Email address">
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button type="submit" id="wlbtn">Join the waiting list</button>
    </form>
    <p class="wlmsg" id="wlmsg" hidden></p>
    <div class="wlsocial"><span class="wlsep">or follow the news:</span><a class="wlsbtn" href="https://t.me/parselex" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>Telegram channel</a><a class="wlsbtn" href="https://whatsapp.com/channel/0029VbE5KT165yD2C4j5yW0V" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>WhatsApp channel</a><a class="wlsbtn" href="https://groups.google.com/g/parselex_support" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>Mailing list</a></div>
    <p class="wlsmall">By joining you agree to receive launch updates from Parselex.
    Prefer email? Write to <a href="mailto:parselex_support@googlegroups.com">parselex_support@googlegroups.com</a>
    and we&#8217;ll add you manually.</p>
  </section>
</main>
<footer class="lfoot">
  <span>&#9878; Parselex &#8212; Legal Document Intelligence Platform</span>
  <span><a href="https://docs.parselex.app" rel="noopener">Documentation</a></span>
</footer>
{_WL_SCRIPT}
</body>
</html>"""


def render_changelog():
    """Public changelog at /changelog/ — product-facing 'alive signal' (EN)."""
    entries = [
        ("2026-10", "Mailing list and news channels",
         "Platform news now reach you three ways &#8212; the Telegram channel, the WhatsApp "
         "channel and the official mailing list parselex_support@googlegroups.com. All three are "
         "linked from the sign-in hub."),
        ("2026-10", "Waiting list opens",
         "Studio (the main application), Admin Workspace and MCP Hub are in final development. "
         "The sign-in hub now carries a waiting list &#8212; subscribe and get notified the "
         "moment access opens."),
        ("2026-10", "Ukrainian language",
         "The landing is now available in Ukrainian — the sixth language of the site "
         "(EN · ES · FR · HI · RU · UK)."),
        ("2026-10", "Unified sign-in hub",
         "parselex.app/login/ becomes the single entry point for all Parselex services: "
         "LexRegister, the application Dashboard and the MCP Hub."),
        ("2026-09", "Google OAuth sign-in",
         "LexRegister went live with Google OAuth alongside provider-based sign-in; "
         "per-user document isolation is enforced across the workspace."),
        ("2026-09", "Multi-agent hub v5.3",
         "The orchestration hub reached version 5.3 — 40 tools, four agent roles, live health "
         "monitoring in the MCP Hub console."),
        ("2026-08", "Automated case backups",
         "Per-case document backups are now fully automated and independently verifiable, "
         "branch-per-case."),
        ("2026-07", "Public security deep dive",
         "Security architecture documentation and the RAG benchmark went public on "
         "docs.parselex.app."),
    ]
    rows = "".join(
        f'<div class="centry reveal"><span class="cdate">{d}</span><div><h3>{t}</h3><p>{x}</p></div></div>'
        for d, t, x in entries
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Changelog &#8212; Parselex</title>
<meta name="description" content="What's new in Parselex: releases, capabilities and platform milestones.">
<link rel="canonical" href="https://parselex.app/changelog/">
<meta property="og:title" content="Changelog &#8212; Parselex">
<meta property="og:image" content="{OG_IMAGE}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='13' font-size='13'>&#9878;</text></svg>">
<style>
:root{{--navy:#1B2A4A;--navy2:#2C4270;--gold:#C9953C;--gold2:#D4A843;--goldsoft:rgba(201,149,60,.14);
--ink:#1F2937;--muted:#5B6B7F;--line:#E4E8EF;--bg:#FFFFFF;--soft:#F6F8FB}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:Inter,system-ui,-apple-system,'Segoe UI',sans-serif;background:var(--soft);color:var(--ink);
min-height:100vh;display:flex;flex-direction:column}}
.cnav{{background:var(--navy);padding:18px 24px}}
.cnav .wrap{{max-width:860px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}}
.logo{{color:#fff;text-decoration:none;font-weight:800;letter-spacing:.14em;font-size:15px}}
.logo .mark{{color:var(--gold2)}}
.cback{{color:rgba(255,255,255,.75);text-decoration:none;font-size:13px}}
.cback:hover{{color:#fff}}
main{{flex:1;max-width:860px;width:100%;margin:0 auto;padding:56px 24px}}
h1{{font-size:clamp(28px,4vw,38px);color:var(--navy);letter-spacing:-.02em}}
.sub{{color:var(--muted);margin:12px 0 40px;font-size:15.5px;line-height:1.6}}
.centry{{display:flex;gap:22px;background:var(--bg);border:1px solid var(--line);border-radius:14px;
padding:22px 24px;margin-bottom:14px}}
.centry h3{{font-size:16.5px;color:var(--navy)}}
.centry p{{color:var(--muted);font-size:14px;margin-top:6px;line-height:1.55}}
.cdate{{min-width:78px;font-weight:800;color:var(--gold);font-size:13px;padding-top:3px}}
.cfoot{{max-width:860px;width:100%;margin:0 auto;padding:24px;border-top:1px solid var(--line);
font-size:12.5px;color:var(--muted)}}
.cfoot a{{color:var(--navy2)}}
@media(max-width:560px){{.centry{{flex-direction:column;gap:8px}}}}
</style>
</head>
<body>
<nav class="cnav"><div class="wrap">
  <a class="logo" href="/"><span class="mark">&#9878;</span> PARSELEX</a>
  <a class="cback" href="/">&#8592; parselex.app</a>
</div></nav>
<main>
  <h1>Changelog</h1>
  <p class="sub">What's new across the Parselex platform — releases, capabilities and milestones.</p>
  {rows}
</main>
<footer class="cfoot">&#9878; Parselex &#8212; <a href="/">parselex.app</a> &#183; <a href="https://docs.parselex.app">docs.parselex.app</a></footer>
</body>
</html>"""


def write_robots(out):
    txt = ("User-agent: *\nAllow: /\nDisallow: /login/\n\n"
           f"Sitemap: {HOST}/sitemap.xml\n")
    with open(os.path.join(out, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(txt)
    print(f"written {os.path.join(out, 'robots.txt')}")


def write_sitemap(out):
    """6 locale pages (with xhtml alternates) + changelog. /login/ is noindex — excluded."""
    urls = []
    pages = ["/"] + [f"/{code}/" for code in ORDER if code != "en"]
    for p in pages:
        loc = HOST + p
        alts = "".join(
            f'<xhtml:link rel="alternate" hreflang="{c}" href="{HOST}/{("" if c == "en" else c + "/")}"/>'
            for c in ORDER)
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{HOST}/"/>'
        urls.append(f"<url><loc>{loc}</loc>{alts}</url>")
    urls.append(f"<url><loc>{CHANGELOG}</loc></url>")
    body = "".join(urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "\n</urlset>\n")
    with open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)
    print(f"written {os.path.join(out, 'sitemap.xml')}")


def main():
    # Optional --out override:  python build_landing.py --out /path/to/dir
    out = DEFAULT_OUT
    if "--out" in sys.argv:
        i = sys.argv.index("--out")
        if i + 1 < len(sys.argv):
            out = os.path.abspath(sys.argv[i + 1])
    for code, (c, prefix) in LANGS.items():
        d = out if code == "en" else os.path.join(out, code)
        os.makedirs(d, exist_ok=True)
        html = head(c, prefix) + "<body>" + render(c, prefix)
        path = os.path.join(d, "index.html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"written {path}  ({len(html)//1024} KB, lang={code})")
    ld = os.path.join(out, "login")
    os.makedirs(ld, exist_ok=True)
    lhtml = render_login()
    with open(os.path.join(ld, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(lhtml)
    print(f"written {os.path.join(ld, 'index.html')}  ({len(lhtml)//1024} KB)")
    cd = os.path.join(out, "changelog")
    os.makedirs(cd, exist_ok=True)
    chtml = render_changelog()
    with open(os.path.join(cd, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(chtml)
    print(f"written {os.path.join(cd, 'index.html')}  ({len(chtml)//1024} KB)")
    write_robots(out)
    write_sitemap(out)
    # og.png social preview: committed at repo root, copied into the artifact
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    og_src = os.path.join(repo_root, "og.png")
    og_dst = os.path.join(out, "og.png")
    if os.path.isfile(og_src) and os.path.abspath(og_src) != os.path.abspath(og_dst):
        with open(og_src, "rb") as s, open(og_dst, "wb") as d:
            d.write(s.read())
        print(f"written {og_dst}  (copied from repo root)")
    elif os.path.abspath(og_src) == os.path.abspath(og_dst):
        # --out points at the repo root itself: copying onto itself would truncate
        # the committed PNG to 0 bytes (open(...,'wb') truncates before read).
        print(f"kept {og_dst}  (output dir is repo root, no self-copy)")
    if not (os.path.isfile(og_dst) and os.path.getsize(og_dst) > 0):
        raise SystemExit("og.png missing or empty — regenerate it with scripts/gen_og.py")


if __name__ == "__main__":
    main()
