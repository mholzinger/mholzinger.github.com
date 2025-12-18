# Mike Holzinger's Blog

Personal blog powered by [Pelican](https://getpelican.com/) static site generator.

## Repository Structure

This repository uses two branches:

- **`main`** - Published HTML output (GitHub Pages serves from this branch)
- **`pelican`** - Pelican source files for creating new articles

## Writing a New Article

### 1. Switch to the pelican branch

```bash
git checkout pelican
```

### 2. Create a new markdown file in `content/`

```bash
# Example: content/my-new-article.md
```

### 3. Add article metadata and content

Every article needs frontmatter with metadata:

```markdown
Title: Your Article Title
Date: 2025-12-17 10:30
Category: Gitlab CI
Author: Mike Holzinger

Your article content goes here in Markdown format...
```

**Available Categories:**
- Gitlab CI
- Security
- (or create a new category)

### 4. Add images (if needed)

Place images in `content/images/` and reference them in your article:

```markdown
![Alt text](/images/your-image.jpg)
```

### 5. Build and preview locally

```bash
# Install Pelican if needed
uv pip install --system pelican markdown

# Build the site
pelican content -s publishconf.py

# Preview in output/ directory
```

### 6. Commit your article source

```bash
git add content/your-article.md
git commit -m "Add article: Your Article Title"
git push origin pelican
```

### 7. Publish to main branch

```bash
# Build with publish settings
pelican content -s publishconf.py

# Switch to main branch
git checkout main

# Copy generated files from output/
cp -r output/* .

# Commit and push to publish
git add .
git commit -m "Publish: Your Article Title"
git push origin main
```

Your article is now live at https://cipherpop.com/

## Site Configuration

- **`pelicanconf.py`** - Main configuration (for development)
- **`publishconf.py`** - Publishing configuration (for production builds)
- **`Makefile`** / **`tasks.py`** - Build automation tools

## Pelican Commands

```bash
# Build site
pelican content

# Build with publish settings
pelican content -s publishconf.py

# Serve locally (if using development server)
pelican --listen
```

## Notes

- The `output/` directory is gitignored and regenerated on each build
- Published articles remain in `main` branch as HTML
- Source markdown files live only in `pelican` branch
- The `pelican` branch contains both source files AND published HTML for reference
