#!/usr/bin/env python3
import yaml
from html_common import generate_html

def main():
    with open("resume.yaml", "r") as f:
        data = yaml.safe_load(f)

    html = generate_html(data, split_experience=True)

    with open("resume_split_experience.html", "w") as f:
        f.write(html)
    print("✓ Generated resume_split_experience.html")

if __name__ == "__main__":
    main()
