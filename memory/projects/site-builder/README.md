# Site-Builder Skill

**Status**: Ready for use
**Created**: 2026-02-07

## What It Does
Rapid website creation from concept to deployment-ready code. Supports landing pages, portfolios, blogs, dashboards.

## Templates
- landing-page/ - Modern dark-themed landing
- portfolio/ - Personal portfolio
- blog/ - Content site (WIP)
- dashboard/ - Admin panel (WIP)

## Usage
```bash
python3 site-builder/scripts/init-site.py <site-name> --template landing-page
```

## Generated Output
```
sites/<site-name>/
├── index.html      # Content (replace {{VARIABLES}})
├── styles.css      # Dark modern design
├── script.js       # Smooth scroll + animations
└── README.md       # Deployment guide
```

## Hosting
See `site-builder/references/hosting-guide.md` for Vercel/Netlify/CF Pages deploy options.

## Next Steps
- [ ] Complete remaining templates
- [ ] Add image/brand asset variables
- [ ] Test with actual site request
