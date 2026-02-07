---
name: site-builder
description: Rapid website creation from concept to deployment-ready code. Use when the user wants to build a website, landing page, web app, or online presence. Triggers on phrases like "build a site", "create a website", "landing page", "web app", or when discussing domains, hosting, and online projects.
---

# Site Builder

Rapidly prototype and build websites from scratch to deployment-ready state.

## Quick Start

For any website request:

1. **Clarify purpose** - What does the site do? Who is it for?
2. **Select template** - Choose from `assets/templates/`
3. **Customize** - Edit content, colors, branding
4. **Generate** - Output to workspace `sites/<project-name>/`
5. **Stage** - Use `canvas` to preview or serve locally
6. **Document** - Provide next steps for domain/hosting

## Templates Available

| Template | Use Case | Location |
|----------|----------|----------|
| `landing-page/` | Product/service landing | `assets/templates/landing-page/` |
| `blog/` | Content/blog site | `assets/templates/blog/` |
| `dashboard/` | Admin dashboard | `assets/templates/dashboard/` |
| `portfolio/` | Personal portfolio | `assets/templates/portfolio/` |

## Workflow

### 1. Init Site
```bash
python3 site-builder/scripts/init-site.py <site-name> --template <template-name>
```

### 2. Customize
Edit files in `sites/<site-name>/`:
- `index.html` - Structure and content
- `styles.css` - Design system
- `script.js` - Interactivity

### 3. Preview
Use canvas or serve locally:
```bash
cd sites/<site-name> && python3 -m http.server 8080
```

## Domain & Hosting Guide

See `references/hosting-guide.md` for:
- Domain registrars (Namecheap, Cloudflare, etc.)
- Static hosting (Vercel, Netlify, Cloudflare Pages, GitHub Pages)
- Deployment steps

## Output Structure

```
sites/<project-name>/
├── index.html
├── styles.css
├── script.js
├── assets/
│   ├── images/
│   └── fonts/
└── README.md (deployment instructions)
```
