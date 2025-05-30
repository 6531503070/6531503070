# generate_readme.py

with open('skills.txt', 'r') as f:
    skills = f.read().strip()

badge_url_light = f"https://go-skill-icons.vercel.app/api/icons?i={skills}&perline=20&theme=light"
badge_url_dark = f"https://go-skill-icons.vercel.app/api/icons?i={skills}&perline=20&theme=dark"

badge_html = f'''<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{badge_url_dark}" />
  <source media="(prefers-color-scheme: light)" srcset="{badge_url_light}" />
  <img alt="My Skills" src="{badge_url_light}" />
</picture>'''

with open('README.template.md', 'r') as f:
    template = f.read()

readme = template.replace("{{SKILLS_BADGE}}", badge_html)

with open('README.md', 'w') as f:
    f.write(readme) 