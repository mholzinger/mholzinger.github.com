# cipherpop.com — Pelican blog (Claude context)

Personal site for Mike Holzinger. Static HTML served by GitHub Pages at `cipherpop.com` (CNAME). Source is Pelican (markdown → HTML).

## Branch layout

- **`pelican`** — source: `content/`, `theme/`, `pelicanconf.py`, `publishconf.py`. **This is where all editing happens.**
- **`main`** — published HTML, served by GitHub Pages. Touched only during the manual publish step.

## Manual publish workflow (intentional — do NOT automate)

The publish flow is `pelican content -s publishconf.py` → manually `cp` selected files from `output/` into `main` → commit → push. **Never** use `make github`, `ghp-import`, GitHub Actions, or anything that wholesale-replaces `main` with `output/`.

**Why:** Two articles deployed on cipherpop.com (`breaking-out-of-docker.html`, `security-scanning-with-sast-in-gitlab-ci.html`) have **no source markdown** anywhere — the `.md` files are lost. Any `ghp-import`-style flow rebuilds only what's in `content/` and wipes the rest. Manual cherry-pick preserves them.

The `pages/archive.html` page links to those two legacy posts so they remain reachable from nav even though they're not regenerated.

## Editing rules

- **Never delete published articles.** If retiring, add to the Archive page; don't `rm` HTML on `main` and don't remove sources for posts that were ever live.
- **Unpublished drafts** (in `content/` but never deployed) CAN be deleted if the user explicitly says so. (Example: in May 2026 we deleted four Nov-2023 GitLab CI drafts at user request.)
- **Don't push or deploy without explicit OK.** Show the file list / diff and wait for sign-off.

## Resume — direct-link convention

`https://cipherpop.com/Resume.pdf` is a workflow-critical URL the user shares directly. Never relocate or rename.

- Source: `content/images/Resume.pdf`
- `pelicanconf.py` has `EXTRA_PATH_METADATA = {'images/Resume.pdf': {'path': 'Resume.pdf'}}` — publishes it to output root.
- The Bio page (`content/pages/bio.md`) embeds it via `<iframe src="/Resume.pdf">`.
- On publish, copy `output/Resume.pdf` → `main/Resume.pdf` (and legacy paths `main/pdf/Resume.pdf`, `main/pdf/Resume - Mike Holzinger (Brooklyn, NY).pdf` if those URLs have ever been shared).

## Top-nav

Pinned order via `MENUITEMS` in `pelicanconf.py`: **Development | Bio | Game Design | Archive**. Categories and auto-page menus are disabled to keep this exact order.

## Theme

Custom theme at `theme/` — fork of pelican's `notmyidea`. `THEME` is set in `pelicanconf.py` via `os.path.join(...)` to an absolute path (relative `'theme'` would collide with built-in theme name resolution).

Local mods vs upstream `notmyidea`:
- `static/css/main.css` — added a `.social a[href*='gitlab.com']` rule so the GitLab social link gets a favicon
- `static/images/icons/gitlab.png` — the icon for the above rule (32×32 PNG)
- `templates/base.html` — removed the "Proudly powered by Pelican / theme by Smashing Magazine" footer block

## Plugin warning

`pelican_fontawesome` is listed in `PLUGINS` but isn't installed. The build prints `Cannot import plugin 'pelican_fontawesome'` — **harmless**. Nothing in the current content uses it.

## Build / preview

```bash
# Dev build (relative URLs — works in local browser)
pelican content -s pelicanconf.py

# Prod build (absolute URLs to cipherpop.com — for what actually goes to main)
pelican content -s publishconf.py

# Preview
cd output && python3 -m http.server 8000
# open http://localhost:8000
```

The PDF iframe in `/pages/bio.html` only resolves when served from a real HTTP origin — `file://` opens won't load it.

### ⚠️ Preview-vs-publish trap

**Always preview with the dev build (`pelicanconf.py`), not the prod build (`publishconf.py`).**

The prod build sets `SITEURL=http://cipherpop.com` and `RELATIVE_URLS=False`, so the generated HTML loads CSS, JS, images, and the resume PDF from `cipherpop.com` — not from your localhost server. You end up with a hybrid: HTML from local, assets from production. Theme/CSS changes you just made won't appear because the browser is fetching the OLD deployed CSS, even though your local server has the new one.

If you've already built with publishconf and want to preview, rebuild with pelicanconf before opening the local server.

## Slash commands

- **`/new-article "Title"`** — scaffold a new post in `content/` with frontmatter, draft body interactively, preview locally, and walk through the manual publish step.
