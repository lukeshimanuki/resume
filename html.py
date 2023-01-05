import sys
import json

def toHTML(data):
	return (
		'<table>\n'
			'<tbody>\n'
				'<tr>\n'
					'<td align="left" class="highlight">{address}<br>{city}</td>\n'
					'<td align="center"><span class="name highlight">{name}</span><br><span class="highlight"><a href="mailto:{email}" target="_blank" rel="noopener noreferrer">{email}</a></span></td>\n'
					'<td align="right"><span class="highlight"><a href="tel:+{phone}" target="_blank" rel="noopener noreferrer">{phone}</a></span><span class="highlight"><a href="{website}" target="_blank" rel="noopener noreferrer">{website}</a></span></td>\n'
				'</tr>\n'
			'</tbody>\n'
		'</table>\n'
		'<table>\n'
			'<tbody>\n'
				'<tr>\n'
					'<td class="highlight padright">EXPERIENCE</td>\n'
					'<td>\n{experience}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td class="highlight padright">RESEARCH</td>\n'
					'<td>\n{research}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td class="highlight padright">EDUCATION</td>\n'
					'<td>\n{education}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td class="highlight padright">ACTIVITIES</td>\n'
					'<td>\n{activities}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td class="highlight padright">SKILLS</td>\n'
					'<td>\n{skills}\n\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td class="highlight padright">AWARDS</td>\n'
					'<td>\n{awards}\n\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td class="highlight padright">PROJECTS</td>\n'
					'<td>\n{projects}\n</td>\n'
				'</tr>\n'
			'</tbody>\n'
		'</table>\n'
	).format(
		education='<table class="highlight">\n' +
		'\n'.join([
			'<tr><td colspan=5>\n' +
			'<table>\n<tr>\n' +
			"<td><strong>{}</strong></td>".format(school['school']) +
			(
				"<td>{}</td>".format(school['field'])
				if 'field' in school else ''
			) +
			"<td><right>{}</right></td>\n".format(school['time']) +
			'</tr></table>\n' +
			(
				"{}<br>\n".format('<br>\n'.join(school['description'][:-1]))
				if 'description' in school else ''
			) +
			'</td></tr>\n' +
			(
				'\n'.join([
					'<tr>\n' +
					'\n'.join([
						'<td>{}</td>\n'.format(course)
						for course in school['coursework'][i:i+4]
					]) +
					'</tr>\n'
					for i in range(0, len(school['coursework']) - 1, 4)
				])
				if 'coursework' in school else ''
			) +
			'<tr><td></td></tr>\n' +
			''
			for school in data['education'] if 'school' in school
		]) +
		'</table>\n',
		skills = (
			'<table>\n'
				'<tr class="highlight">\n'
					'<td>Proficient in:</td>\n'
					'<td>{}</td>\n'
				'</tr>\n'
				'<tr class="highlight">\n'
					'<td>Familiar with:</td>\n'
					'<td>{}</td>\n'
				'</tr>\n'
				'<tr class="highlight">\n'
					'<td>Libraries:</td>\n'
					'<td colspan=1>{}</td>\n'
				'</tr>\n'
			'</table>\n'
		).format(
			'</td><td>'.join(data['skills']['proficient'][:-1]),
			'</td><td>'.join(data['skills']['familiar'][:-1]),
			'</td><td colspan=1>'.join(data['skills']['libraries'][:-1]),
		),
		experience = '<table><tbody class="highlight">\n' +
		'</tbody><tbody class="highlight">\n'.join([
			(
				'<tr>\n'
					'<td>\n'
						"<strong>{}</strong>"
					'</td>\n'
					'<td>\n'
						"<em>{}</em>"
					'</td>\n'
					'<td>\n'
						"<right>{}</right> <br>\n"
					'</td>\n'
				'</tr>\n'
			).format(
				job['role'],
				job['group'],
				job['time'],
			) +
			'<tr><td colspan=3>\n' +
			(
				'<br>\n'.join([
					' '.join(statement[:-1])
					for statement in job['description'] if len(statement) > 0
				])
				if 'description' in job else ''
			) +
			'</td></tr>\n' +
			''
			for job in data['experience'] if len(job) > 0
		]) +
		'</tbody></table>\n',
		research = '<table>\n' +
		'\n'.join([
			(
				'<tr>\n'
					'<td colspan=2><table class="highlight"><tr>'
						"<td><strong>{}</strong></td>"
						"<td><right>{}</right></td>"
					"</tr></table></td>"
				'</tr>\n'
			).format(
				position['group'],
				position['time'],
			) +
			'\n'.join(
				("<tr class='highlight'>"
					"<td>{link_begin}<span class='padright'>{published}</span>{link_end}</td>"
					"<td>{link_begin}<span class='padright'>{description}</span>{link_end}</td>"
				"</tr>").format(**project, link_begin="<a href='{url}' target='_blank' rel='noopener noreferrer'>".format(**project) if len(project['url']) > 0 else '', link_end='</a>' if len(project['url']) > 0 else '')
				for project in position['projects'] if len(project) > 0
			)
			for position in data['research'] if len(position) > 0
		]) +
		'</table>\n',
		activities = '<table><tbody class="highlight">\n' +
		'</tbody><tbody class="highlight">\n'.join([
			(
				'<tr>\n'
					'<td>\n'
						"<strong>{}</strong>"
					'</td>\n'
					'<td>\n'
						"<em>{}</em>"
					'</td>\n'
					'<td>\n'
						"<right>{}</right> <br>\n"
					'</td>\n'
				'</tr>\n'
			).format(
				group['role'],
				group['group'],
				group['time'],
			) +
			'<tr><td colspan=3>\n' +
			(
				'<br>\n'.join([
					' '.join(statement[:-1])
					for statement in group['description'] if len(statement) > 0
				])
				if 'description' in group else ''
			) +
			'</td></tr>\n' +
			''
			for group in data['activities'] if len(group) > 0
		]) +
		'</tbody></table>\n',
		awards = '<table><tr>' + '</tr><tr>'.join([
			"<td class='highlight'>{}</td><td class='highlight'>{}</td>".format(' '.join(data['achievements'][i]), ' '.join(data['achievements'][i + 1]))
			for i in range(0, len(data['achievements']) - 1, 2)
		]) + '</tr></table>',
		projects = '<table>\n<tr class="highlight">\n' +
		'</tr><tr class="highlight">\n'.join([
			(
				"<td class='padright'><strong>{}</strong></td> ".format(project['language'])
				if 'language' in project else ''
			) +
			'<td>\n' +
			' '.join(project['description'][:-1]) +
			'</td>\n'
			for project in data['projects'] if 'description' in project
		]) +
		'</tr>\n</table>\n',
		**{
			key: value
			for key, value in data.items()
			if key in (
				'address',
				'name',
				'phone',
				'city',
				'email',
				'website',
			)
		}
	)

def genHTML(body, style):
	return (
		'<!DOCTYPE html>'
		'<html>\n'
			'<head>\n'
				"{}\n"
			'</head>\n'
			'<body>\n'
			"{}\n"
			'</body>\n'
		'</html>\n'
	).format(style, body)

def main():
	sys.stdout.write(genHTML(toHTML(json.loads(open('resume.json').read())), open('style.html').read()))

if __name__ == "__main__":
	main()

