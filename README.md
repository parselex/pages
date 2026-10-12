# parselex.app — main landing site

Static landing page for **parselex.app** — the public marketing site for the
Parselex legal-intelligence platform. Built from the v15 investor presentation,
using the same international terminology as [docs.parselex.app](https://docs.parselex.app)
(LexZTNA, Ethics Firewall, Case Readiness Score, 7 intelligence categories).

Five locales, EN canonical at the root:

| Locale | URL |
|--------|-----|
| EN (canonical) | https://parselex.app/ |
| RU | https://parselex.app/ru/ |
| ES | https://parselex.app/es/ |
| FR | https://parselex.app/fr/ |
| HI | https://parselex.app/hi/ |

The pages are fully self-contained: inline CSS/JS, zero external resources,
zero images. Detailed product documentation lives at docs.parselex.app.

## Repository layout

```
├── index.html              # EN landing (built artifact, committed)
├── ru/ es/ fr/ hi/         # localized landings (built artifacts, committed)
├── CNAME                   # parselex.app — GitHub Pages custom domain
├── scripts/
│   ├── build_landing.py    # generator: template + CSS + i18n links
│   └── content_{en,ru,es,fr,hi}.py   # per-locale content dictionaries
└── .github/workflows/deploy.yml      # CI: rebuild → verify → deploy
```

## Editing content

Content lives in `scripts/content_*.py` — one Python dictionary per locale
(keys: `meta_title`, `nav`, `hero`, `problem`, `platform`, `sectors`, `score`,
`security`, `arch`, `modules`, `metrics`, `compare`, `pricing`, `market`,
`roadmap`, `cta`, `footer`). After editing:

```bash
python scripts/build_landing.py --out .   # rebuild into this repo
git add -A && git commit -m "content: ..." && git push
```

CI rebuilds the site from the content modules on every push, so even if you
push only `scripts/` changes the deployed pages stay in sync.

## CI/CD (GitHub Actions)

`.github/workflows/deploy.yml` on every push to `main`:

1. Rebuilds all 5 pages from `scripts/content_*.py` into `site/`.
2. Verifies artifact integrity: 5 non-empty pages, EN canonical
   `https://parselex.app/`, full hreflang set (5 locales + `x-default`),
   no external `<img|script|iframe>` sources, `CNAME` = parselex.app.
3. Deploys the artifact with the official `actions/deploy-pages@v4`.

The workflow can also be triggered manually via **workflow_dispatch**.

## One-time GitHub setup

1. Create repo under the `parselex` organization (`pages`)
   and push this project to `main`.
2. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
3. **Settings → Pages → Custom domain:** enter `parselex.app` and save
   (the `CNAME` file keeps it stable across deploys). Wait until the
   certificate is provisioned (DNS must point at GitHub first — see below).
4. Enable **Enforce HTTPS** once GitHub shows the certificate as active.
5. Check the first run of the **Deploy Landing Pages** workflow
   (Actions tab) — it deploys automatically after the first push.

## Cloudflare setup (implemented, live)

parselex.app is **proxied through Cloudflare** to GitHub Pages (zone
`parselex.app`, account-owned API token):

| Type  | Name | Content                 | Proxy |
|-------|------|-------------------------|-------|
| A     | `@`  | `185.199.108.153`       | Proxied |
| AAAA  | `@`  | `2606:50c0:8000::153`   | Proxied |
| CNAME | `www`| `parselex.github.io`    | Proxied |

- Zone SSL mode is **Full** (non-strict): Cloudflare terminates TLS with its
  Universal SSL cert and accepts GitHub's `*.github.io` origin certificate —
  no dependency on GitHub's own custom-domain cert issuance.
- **Redirect Rule** (zone `http_request_dynamic_redirect`):
  `/auth-gate*` and `/signup*` → 302 `https://docs.parselex.app$uri`
  (the app entry points live on the docs site).
- The old origin server (13.140.143.252) is fully out of the loop; MX/TXT
  (Email Routing) and mcp-*/dashboard/lexregister/tracing subdomains untouched.
- `scripts/cf_proxy_mode.py --revert` (needs CF token) flips back to the
  DNS-only record set (4×A + 4×AAAA) once GitHub's own custom-domain
  certificate is active — that mirrors docs.parselex.app exactly.

### Verify

```bash
dig +short parselex.app A                      # → Cloudflare edge IPs
curl -sI https://parselex.app/ | head -3       # → HTTP/2 200, server: cloudflare
curl -s  https://parselex.app/ru/ | grep '<html lang="ru"'
curl -sI https://parselex.app/auth-gate        # → 302 docs.parselex.app
```
