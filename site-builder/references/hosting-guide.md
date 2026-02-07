# Domain & Hosting Guide

## Domain Registrars

| Provider | Price Range | Notes |
|----------|-------------|-------|
| Cloudflare | Wholesale (~$10/yr) | No markup, great DNS |
| Namecheap | $5-15/yr | Good support, free privacy |
| Porkbun | $5-12/yr | Modern UI, free WHOIS privacy |
| Google Domains | Migrated to Squarespace | Not recommended |

## Static Hosting (Free Tier)

### Vercel
- **Pros**: Git integration, previews, edge network
- **Free tier**: Unlimited deploys, 100GB bandwidth
- **Deploy**: `vercel --prod` or Git push

### Netlify
- **Pros**: Drag-drop deploy, forms, functions
- **Free tier**: 100GB bandwidth, 300 build minutes
- **Deploy**: Drag folder or `netlify deploy --prod`

### Cloudflare Pages
- **Pros**: Fastest CDN, generous limits
- **Free tier**: Unlimited requests, 500 builds/month
- **Deploy**: Git integration or Wrangler CLI

### GitHub Pages
- **Pros**: Free, integrated with repos
- **Limitations**: Public repos only, no server-side

## Quick Deploy Commands

```bash
# Vercel
npm i -g vercel
vercel --prod

# Netlify
npm i -g netlify-cli
netlify deploy --prod --dir=.

# Cloudflare (install Wrangler first)
npx wrangler pages deploy .
```
