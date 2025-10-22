#!/usr/bin/env python3
import yaml
import textwrap

LINE_WIDTH = 100

def wrap_text(text, width=LINE_WIDTH, indent="    "):
    """Wrap text to specified width with proper indentation for continuation lines."""
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent="",
        subsequent_indent=indent,
        break_long_words=False,
        break_on_hyphens=False
    )
    return wrapper.fill(text)

def main():
    with open("resume.yaml", "r") as f:
        data = yaml.safe_load(f)

    pi, edu = data['personal_info'], data['education']
    lines = []

    # Header
    lines.append(pi['name'].upper())
    lines.append(f"{pi['email']}  |  {pi['website']}")
    lines.append("")
    lines.append("=" * LINE_WIDTH)
    lines.append("")

    # Experience
    lines.append("EXPERIENCE")
    lines.append("-" * LINE_WIDTH)
    lines.append("")
    for job in data['experience']:
        lines.append(f"{job['company']} | {job['title']}")
        lines.append(f"{job['date']}")
        for item in job['description']:
            wrapped = wrap_text(f"  - {item}", width=LINE_WIDTH, indent="    ")
            lines.append(wrapped)
        lines.append("")

    # Education & Research
    lines.append("EDUCATION & RESEARCH PUBLICATIONS")
    lines.append("-" * LINE_WIDTH)
    lines.append("")
    lines.append(f"{edu['institution']} | {edu['lab']}")
    lines.append(f"{edu['date']}")
    for degree in edu['degrees']:
        gpa_str = f"GPA {degree['gpa']} (out of {degree['gpa_scale']})"
        if 'notes' in degree:
            gpa_str += f", {degree['notes']}"
        concentration = f" ({degree['concentration']})" if 'concentration' in degree else ""
        degree_text = f"  {degree['type']} {degree['field']}{concentration}, {gpa_str}"
        wrapped = wrap_text(degree_text, width=LINE_WIDTH, indent="    ")
        lines.append(wrapped)
    lines.append("")
    for pub in edu['publications']:
        pub_text = f'  {pub["authors"]}, \"{pub["title"]}\", {pub["venue"]}'
        wrapped = wrap_text(pub_text, width=LINE_WIDTH, indent="    ")
        lines.append(wrapped)
    lines.append(f"  {edu['publications_note']}")
    lines.append("")

    # Skills
    lines.append("SKILLS")
    lines.append("-" * LINE_WIDTH)
    lines.append("")
    lines.append(f"Languages: {', '.join(data['skills']['languages'])}")
    lines.append(f"ML/AI: {', '.join(data['skills']['ml_ai'])}")
    lines.append(f"Tools: {', '.join(data['skills']['tools'])}")
    lines.append("")

    # Page break
    lines.append("=" * LINE_WIDTH)
    lines.append("")

    # Activities
    lines.append("ACTIVITIES")
    lines.append("-" * LINE_WIDTH)
    lines.append("")
    for activity in data['activities']:
        lines.append(f"{activity['title']} | {activity['organization']} | {activity['date']}")
        desc_wrapped = wrap_text(f"  {activity['description']}", width=LINE_WIDTH, indent="  ")
        lines.append(desc_wrapped)
        lines.append("")

    # Awards
    lines.append("AWARDS")
    lines.append("-" * LINE_WIDTH)
    lines.append("")
    lines.append(" | ".join(data['awards']))
    lines.append("")

    # Projects
    lines.append("PROJECTS")
    lines.append("-" * LINE_WIDTH)
    lines.append("")
    for project in data['projects']:
        proj_text = f"{project['language']}: {project['description']}"
        wrapped = wrap_text(proj_text, width=LINE_WIDTH, indent="    ")
        lines.append(wrapped)
    lines.append("")

    text = "\n".join(lines)

    with open("resume.txt", "w") as f:
        f.write(text)
    print("✓ Generated resume.txt")

if __name__ == "__main__":
    main()
