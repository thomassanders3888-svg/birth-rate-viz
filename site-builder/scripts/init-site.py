#!/usr/bin/env python3
"""
Initialize a new website project from template.
Usage: python3 init-site.py <site-name> --template <landing-page|blog|dashboard|portfolio>
"""

import argparse
import shutil
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Initialize website project')
    parser.add_argument('name', help='Site folder name')
    parser.add_argument('--template', default='landing-page', 
                       choices=['landing-page', 'blog', 'dashboard', 'portfolio'],
                       help='Template to use')
    args = parser.parse_args()
    
    skill_dir = Path(__file__).parent.parent
    template_dir = skill_dir / 'assets' / 'templates' / args.template
    output_dir = Path.home() / '.openclaw' / 'workspace' / 'sites' / args.name
    
    if not template_dir.exists():
        print(f"Template not found: {template_dir}")
        sys.exit(1)
    
    if output_dir.exists():
        print(f"Site already exists: {output_dir}")
        sys.exit(1)
    
    # Copy template
    shutil.copytree(template_dir, output_dir)
    
    # Create deployment README
    readme = output_dir / 'README.md'
    readme.write_text(f"""# {args.name}

## Local Preview
```bash
cd {output_dir}
python3 -m http.server 8080
# Open http://localhost:8080
```

## Deployment Options

### Vercel (Recommended)
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel --prod`

### Netlify
1. Drag `sites/{args.name}/` folder to https://app.netlify.com/drop

### Cloudflare Pages
1. Connect Git repo or upload via CLI
2. Build command: none (static)
3. Output: `/`

## Domain Registration
- Cloudflare Registrar (cost + privacy protection)
- Namecheap (cheap, good support)
- Porkbun (modern, simple)

## Next Steps
1. [ ] Customize content in index.html
2. [ ] Update styles in styles.css
3. [ ] Add any images to assets/images/
4. [ ] Deploy to hosting
5. [ ] Point custom domain (optional)
""")
    
    print(f"✓ Created site: {output_dir}")
    print(f"  Template: {args.template}")
    print(f"  Preview: cd {output_dir} && python3 -m http.server 8080")

if __name__ == '__main__':
    main()
