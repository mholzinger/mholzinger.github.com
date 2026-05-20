---
description: Scaffold, draft, preview, and walk through publishing a new cipherpop article
argument-hint: "Article title in quotes (e.g. /new-article \"Why I Switched to Pelican\")"
---

You are helping Mike write a new article for cipherpop.com. Follow the workflow below. **Read `CLAUDE.md` first** for the full project context (branch layout, manual publish rules, archive policy, theme structure) — do not skip this.

The user's article title is: **$ARGUMENTS**

If no title was passed, ask for one before continuing.

## Step 1 — Scaffold

Derive a slug from the title: lowercase, spaces → hyphens, drop punctuation. Confirm the slug with the user before writing.

Create `content/<slug>.md` with this frontmatter (use today's date):

```markdown
Title: <Title from $ARGUMENTS>
Date: <YYYY-MM-DD HH:MM>
Category: <ask the user — common: "Development", "Game Design", "Notes">
Tags: <ask the user — comma-separated, optional>
Slug: <slug>
Summary: <ask the user for a 1-2 sentence summary; this shows on the homepage>

# <Title>

<placeholder body — replace in next step>
```

## Step 2 — Draft

Ask the user how they want to draft:
- (a) They'll write the body themselves in the file; you wait and offer edits.
- (b) They give you bullet points / notes; you draft from those for their review.
- (c) They paste an existing draft and you polish.

Whatever path: keep the user's voice. Don't over-formalize. No emojis unless they ask.

For images: drop them in `content/images/` and reference as `![alt](/images/filename.ext)`. Confirm with the user before grabbing or generating any image.

## Step 3 — Local preview

Build with the **dev** config (relative URLs work locally):

```bash
pelican content -s pelicanconf.py
cd output && python3 -m http.server 8000
```

Give the user these URLs to spot check:
- `http://localhost:8000/` — homepage; new article should appear in the list
- `http://localhost:8000/<slug>.html` — the article itself
- `http://localhost:8000/archives.html`, `categories.html`, `tags.html` — verify the new piece is indexed correctly

Wait for the user's spot-check sign-off before moving on.

## Step 4 — Production build

```bash
pelican content -s publishconf.py
```

This rebuilds with `SITEURL=http://cipherpop.com`. Output lands in `output/`.

## Step 5 — Manual cherry-pick publish (NEVER auto-publish)

**Re-read the manual-publish section of `CLAUDE.md` before this step.** The defensive cherry-pick is what protects the two source-less legacy articles on `main` from being wiped.

List for the user exactly which files in `output/` should be copied to `main`. For a typical new article, that's:
- `output/<slug>.html` — the new article (NEW file on main)
- `output/index.html` — homepage (OVERWRITES — verify it still references the legacy posts in some form; if not, that's expected, the Archive page is the safety net)
- `output/archives.html`, `categories.html`, `tags.html` — index pages (OVERWRITES)
- `output/feeds/*.atom.xml` — feeds (OVERWRITES)
- `output/category/<new-category>.html` if it's a new category
- `output/author/mike-holzinger.html` — likely overwrite
- `output/theme/**` — only if theme changed since last publish (usually skip)
- `output/Resume.pdf` — only if resume updated since last publish (skip otherwise)

Generate the exact `cp` commands and show them to the user. Do NOT run them. The user runs them, inspects `git status` / `git diff` on `main`, commits, and pushes manually.

## Step 6 — Commit & push (USER ONLY)

Suggest a commit message: `Publish: <Title>`. Do NOT run `git commit` or `git push` yourself — the user does this after they've eyeballed everything.

After they push, give them the public URL: `https://cipherpop.com/<slug>.html` and the homepage to refresh.

## Notes

- If the article is part of a new category, ensure the category appears wherever the user wants it (likely doesn't need to be in nav — categories aren't in the current `MENUITEMS`).
- If anything about the resume, bio, theme, or legacy archive changes during the article work, mention it explicitly — those have special rules in CLAUDE.md.
- The `pelican_fontawesome` plugin warning during build is harmless; ignore it.
