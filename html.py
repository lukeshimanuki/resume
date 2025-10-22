#!/usr/bin/env python3
import yaml

def bold_shimanuki(text):
    return text.replace('L. Shimanuki', '<strong>L. Shimanuki</strong>')

def main():
    with open("resume.yaml", "r") as f:
        data = yaml.safe_load(f)

    pi, edu = data['personal_info'], data['education']

    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Luke Shimanuki - Resume</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"><style>body{{font-family:Arial,Helvetica,sans-serif;font-size:11pt;line-height:1.3;color:#333;background:white;max-width:8.5in;margin:0 auto;padding:0.4in}}@media print{{body{{margin:0;padding:0.4in;background:white;-webkit-print-color-adjust:exact}}.page-break{{page-break-before:always}}@page{{margin:0.4in;size:letter}}}}.header{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.1in;padding-bottom:0}}.header h1{{font-size:14pt;font-weight:bold;letter-spacing:1px;text-transform:uppercase;margin:0}}.header-left,.header-right{{font-size:10pt;padding-top:2px}}.header a{{color:#333;text-decoration:none}}.header a:hover{{text-decoration:underline}}.section{{margin-bottom:0.15in}}.section-page2{{margin-bottom:0.25in}}.section-title{{font-size:11pt;font-weight:bold;text-transform:uppercase;letter-spacing:1px;border-bottom:1px solid #666;padding-bottom:2px;margin-bottom:0.1in}}.skills-box{{font-size:11pt;padding:0.06in 0.12in;margin-bottom:0.15in;border:1px solid #666;display:flex;align-items:baseline;gap:20px;transition:background-color 0.2s}}.skills-box:hover{{background-color:#f5f5f5}}.skills-box .skills-label{{font-weight:bold;text-transform:uppercase;letter-spacing:0.5px;white-space:nowrap}}.skills-box .skills-content{{flex:1;display:flex;justify-content:space-between}}.skills-box .skill-label{{font-weight:bold;margin-right:0.3em}}.job,.education-item,.activities-item,.project-item{{margin-bottom:0.08in}}.experience-table,.activities-table,.projects-table{{width:100%;margin-bottom:0}}.experience-table td,.activities-table td,.projects-table td{{padding:0;vertical-align:top;border:none;transition:background-color 0.2s}}.experience-table td:hover,.activities-table td:hover,.projects-table td:hover{{background-color:#f5f5f5}}.experience-table .company-cell{{font-weight:bold;font-size:11pt;width:44%;min-width:200px}}.experience-table .title-cell{{font-size:10pt;width:41%;padding-left:8px}}.experience-table .date-cell{{font-size:10pt;color:#666;text-align:right;white-space:nowrap;width:15%}}.activities-table .activity-title-cell{{font-weight:bold;width:35%;white-space:nowrap}}.activities-table .activity-org-cell{{font-style:italic;width:45%;padding-left:8px}}.activities-table .activity-date-cell{{color:#666;text-align:right;white-space:nowrap;width:20%}}.projects-table .project-lang-cell{{font-weight:bold;width:10%}}.projects-table .project-desc-cell{{width:90%;padding-left:8px}}.job-description{{list-style-type:disc;margin-left:0.2in;padding-left:0;margin-bottom:0;margin-top:0.02in}}.job-description li{{margin-bottom:0.03in;transition:background-color 0.2s;padding:0.02in 0}}.job-description li:hover{{background-color:#f5f5f5}}.education-degrees{{margin-bottom:0.08in}}.education-degrees div{{margin-bottom:0.02in;transition:background-color 0.2s;padding:0.02in 0}}.education-degrees div:hover{{background-color:#f5f5f5}}.publications-note{{font-style:italic;font-size:9pt;margin-top:0.03in}}.publications-table{{width:100%;margin-top:0.05in;margin-bottom:0.03in;border-collapse:collapse}}.publications-table td{{padding:0.02in 0;vertical-align:top;border:none;font-size:10pt;line-height:1.3}}.publications-table .pub-content-cell{{width:88%}}.publications-table .pub-venue-cell{{width:12%;text-align:right;padding-left:0.15in;white-space:nowrap}}.publications-table tr{{transition:background-color 0.2s}}.publications-table tr:hover{{background-color:#f5f5f5}}.publications-table a{{color:#333;text-decoration:none;display:block}}.publications-table tr:hover a{{color:#0066cc}}.degree{{font-weight:bold;font-size:11pt}}.dates{{font-size:10pt;color:#666}}.education-header{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:0.03in}}.education-header>div{{transition:background-color 0.2s;padding:0.02in 0}}.education-header>div:hover{{background-color:#f5f5f5}}.awards-list{{display:flex;justify-content:space-between;flex-wrap:wrap;gap:0 10px}}.award{{font-weight:bold;flex:0 0 auto;transition:background-color 0.2s;padding:0.02in 0.05in}}.award:hover{{background-color:#f5f5f5}}.activity-desc{{margin-top:0.03in;transition:background-color 0.2s;padding:0.02in 0}}.activity-desc:hover{{background-color:#f5f5f5}}.page-break{{page-break-before:always;padding-top:0.5in}}@media (max-width:768px){{body{{padding:0.2in}}.header{{flex-direction:column;align-items:center;text-align:center}}.header-left,.header-right{{margin-top:5px}}.experience-table,.activities-table,.projects-table{{display:block;width:100%}}.experience-table tbody,.activities-table tbody,.projects-table tbody{{display:block}}.experience-table tr,.activities-table tr,.projects-table tr{{display:flex;flex-direction:column;margin-bottom:0.1in}}.experience-table td,.activities-table td,.projects-table td{{display:block;width:100%!important;padding-left:0!important;white-space:normal!important;text-align:left!important}}.skills-box{{flex-direction:column;gap:5px}}.skills-box .skills-content{{flex-direction:column}}.publications-table{{display:block}}.publications-table tbody{{display:block}}.publications-table tr{{display:flex;flex-direction:column}}.publications-table td{{display:block;width:100%!important;padding-left:0!important;white-space:normal!important;text-align:left!important}}}}</style></head><body><div class="header"><div class="header-left"><a href="mailto:{pi['email']}">{pi['email']}</a></div><h1>{pi['name']}</h1><div class="header-right"><a href="{pi['website']}">{pi['website']}</a></div></div><div class="section"><div class="section-title">Experience</div>'''

    for job in data['experience']:
        html += f'<div class="job"><table class="experience-table"><tbody><tr><td class="company-cell">{job["company"]}</td><td class="title-cell">{job["title"]}</td><td class="date-cell">{job["date"]}</td></tr></tbody></table><ul class="job-description">'
        for item in job['description']:
            html += f'<li>{item}</li>'
        html += '</ul></div>'

    html += f'''</div><div class="section"><div class="section-title">Education & Research Publications</div><div class="education-item"><div class="education-header"><div><div class="degree">{edu['institution']} | {edu['lab']}</div></div><div class="dates">{edu['date']}</div></div><div class="education-degrees">'''

    for d in edu['degrees']:
        gpa = f"GPA {d['gpa']} (out of {d['gpa_scale']})"
        if 'notes' in d: gpa += f", {d['notes']}"
        c = f" ({d['concentration']})" if 'concentration' in d else ""
        html += f'<div><strong>{d["type"]}</strong> {d["field"]}{c}, {gpa}</div>'

    html += '</div><table class="publications-table"><tbody>'
    for p in edu['publications']:
        a = bold_shimanuki(p['authors'])
        html += f'<tr><td class="pub-content-cell"><a href="{p["url"]}" target="_blank">{a}, "{p["title"]}"</a></td><td class="pub-venue-cell"><a href="{p["url"]}" target="_blank">{p["venue"]}</a></td></tr>'

    html += f'</tbody></table><div class="publications-note">{edu["publications_note"]}</div></div></div><div class="skills-box"><div class="skills-label">Skills</div><div class="skills-content">'
    html += '<span><span class="skill-label">Languages:</span>' + ', '.join(data['skills']['languages']) + '</span>'
    html += '<span><span class="skill-label">ML/AI:</span>' + ', '.join(data['skills']['ml_ai']) + '</span>'
    html += '<span><span class="skill-label">Tools:</span>' + ', '.join(data['skills']['tools']) + '</span>'
    html += '</div></div><div class="page-break"></div><div class="section section-page2"><div class="section-title">Activities</div>'

    for a in data['activities']:
        html += f'<div class="activities-item"><table class="activities-table"><tbody><tr><td class="activity-title-cell">{a["title"]}</td><td class="activity-org-cell">{a["organization"]}</td><td class="activity-date-cell">{a["date"]}</td></tr></tbody></table><div class="activity-desc">{a["description"]}</div></div>'

    html += '</div><div class="section section-page2"><div class="section-title">Awards</div><div class="awards-list">'
    for award in data['awards']:
        html += f'<span class="award">{award}</span>'

    html += '</div></div><div class="section section-page2"><div class="section-title">Projects</div>'
    for p in data['projects']:
        html += f'<div class="project-item"><table class="projects-table"><tbody><tr><td class="project-lang-cell">{p["language"]}</td><td class="project-desc-cell">{p["description"]}</td></tr></tbody></table></div>'

    html += '</div><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script></body></html>'

    with open("resume.html", "w") as f:
        f.write(html)
    print("✓ Generated resume.html")

if __name__ == "__main__":
    main()
