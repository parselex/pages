#!/usr/bin/env python3
"""Generate og.png (1200x630 social preview) for parselex.app — brand navy/gold."""
from playwright.sync_api import sync_playwright

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;height:630px;overflow:hidden;
font-family:'Inter',-apple-system,'Segoe UI',system-ui,sans-serif;
background:radial-gradient(900px 420px at 78% -10%,rgba(201,149,60,.25),transparent 60%),
radial-gradient(700px 380px at 8% 108%,rgba(44,66,112,.55),transparent 60%),
linear-gradient(160deg,#0F1A33,#1B2A4A);
color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 84px;position:relative}
.logo{display:flex;align-items:center;gap:14px;font-weight:800;letter-spacing:.16em;font-size:26px}
.logo .mark{width:52px;height:52px;border-radius:13px;background:rgba(212,168,67,.15);
color:#D4A843;display:grid;place-items:center;font-size:28px}
h1{font-size:64px;line-height:1.12;letter-spacing:-.02em;font-weight:800;margin-top:38px;max-width:900px}
h1 .accent{color:#D4A843}
.sub{color:rgba(255,255,255,.78);font-size:24px;margin-top:22px;max-width:820px;line-height:1.5}
.stats{display:flex;gap:46px;margin-top:44px;border-top:1px solid rgba(255,255,255,.16);padding-top:28px}
.stat .n{font-size:34px;font-weight:800;color:#D4A843}
.stat .l{color:rgba(255,255,255,.62);font-size:14px;margin-top:2px}
.pill{position:absolute;top:44px;right:84px;border:1px solid rgba(212,168,67,.5);color:#D4A843;
font-size:14px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:8px 16px;
border-radius:99px;background:rgba(201,149,60,.12)}
</style></head><body>
<div class="pill">Built for Legal Practice</div>
<div class="logo"><span class="mark">&#9878;</span>PARSELEX</div>
<h1>Legal Document <span class="accent">Intelligence</span> Platform</h1>
<p class="sub">From any source to an objective Case Readiness Score (0&#8211;100) &#8212; working product, Zero-Trust by architecture.</p>
<div class="stats">
  <div class="stat"><div class="n">99.6%</div><div class="l">processing success</div></div>
  <div class="stat"><div class="n">7</div><div class="l">intelligence categories</div></div>
  <div class="stat"><div class="n">2,500+</div><div class="l">documents in production</div></div>
</div>
</body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    pg.set_content(HTML, wait_until="networkidle")
    pg.screenshot(path="/home/z/my-project/landing-repo/og.png")
    b.close()
print("og.png written (1200x630)")
