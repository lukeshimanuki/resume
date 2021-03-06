import sys
import json

def toHTML(data):
	return (
		'<table>\n'
			'<tbody>\n'
				'<tr>\n'
					'<td align="left">{}</td>\n'
					'<td align="center"><span class="name">{}</span></td>\n'
					'<td align="right">{}</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td align="left">{}</td>\n'
					'<td align="center">{}</td>\n'
					'<td align="right">{}</td>\n'
				'</tr>\n'
			'</tbody>\n'
		'</table>\n'
		'<table>\n'
			'<tbody>\n'
				'<tr>\n'
					'<td><table><tr><td>EDUCATION</td></tr></table></td>\n'
					'<td>\n{}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><table><tr><td>SKILLS</td></tr></table></td>\n'
					'<td>\n{}\n\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><table><tr><td>EXPERIENCE</td></tr></table></td>\n'
					'<td>\n{}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><table><tr><td>RESEARCH</td></tr></table></td>\n'
					'<td>\n{}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><table><tr><td>ACTIVITIES</td></tr></table></td>\n'
					'<td>\n{}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><p>AWARDS</p></td>\n'
					'<td>\n{}\n\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><table><tr><td>PROJECTS</td></tr></table></td>\n'
					'<td>\n{}\n</td>\n'
				'</tr>\n'
			'</tbody>\n'
		'</table>\n'
	).format(
		data['address'],
		data['name'],
		data['phone'],
		data['city'],
		data['email'],
		data['github'],
		'<table>\n' +
		'\n'.join([
			'<tr><td colspan=3>\n' +
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
						for course in school['coursework'][i:i+2]
					]) +
					'</tr>\n'
					for i in range(0, len(school['coursework']) - 1, 2)
				])
				if 'coursework' in school else ''
			) +
			'<tr><td></td></tr>\n' +
			''
			for school in data['education'] if 'school' in school
		]) +
		'</table>\n',
		(
			'<table>\n'
				'<tr>\n'
					'<td>Proficient in:</td>\n'
					'<td>{}</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td>Familiar with:</td>\n'
					'<td>{}</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td>Libraries:</td>\n'
					'<td colspan=1>{}</td>\n'
				'</tr>\n'
			'</table>\n'
		).format(
			'</td><td>'.join(data['skills']['proficient'][:-1]),
			'</td><td>'.join(data['skills']['familiar'][:-1]),
			'</td><td colspan=1>'.join(data['skills']['libraries'][:-1]),
		),
		'<table>\n' +
		'\n'.join([
			(
				'<tr>\n'
					'<td>\n'
						"<strong>{}</strong>"
					'</td>\n'
					'<td>\n'
						"<ex>{}</em>"
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
		'</table>\n',
		'<table>\n' +
		'\n'.join([
			(
				'<tr>\n'
					'<td>\n'
						"<strong>{}</strong>"
					'</td>\n'
					'<td>\n'
						"<right>{}</right> <br>\n"
					'</td>\n'
				'</tr>\n'
			).format(
				position['group'],
				position['time'],
			) +
			'<tr><td colspan=3>\n' +
			(
				'<br>\n'.join([
					' '.join(statement[:-1])
					for statement in position['description'] if len(statement) > 0
				])
				if 'description' in position else ''
			) +
			'</td></tr>\n' +
			''
			for position in data['research'] if len(position) > 0
		]) +
		'</table>\n',
		'<table>\n' +
		'\n'.join([
			(
				'<tr>\n'
					'<td>\n'
						"<strong>{}</strong>"
					'</td>\n'
					'<td>\n'
						"<ex>{}</em>"
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
		'</table>\n',
		'<table><tr>' + '</tr><tr>'.join([
			"<td>{}</td><td>{}</td>".format(' '.join(data['achievements'][i]), ' '.join(data['achievements'][i + 1]))
			for i in range(0, len(data['achievements']) - 1, 2)
		]) + '</tr></table>',
		'<table>\n<tr>\n' +
		'</tr><tr>\n'.join([
			(
				"<td><strong>{}</strong></td> ".format(project['language'])
				if 'language' in project else ''
			) +
			'<td>\n' +
			' '.join(project['description'][:-1]) +
			'</td>\n'
			for project in data['projects'] if 'description' in project
		]) +
		'</tr>\n</table>\n'
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
	sys.stdout.write(genHTML(toHTML(json.loads(open('resume.json').read())), open('style.css').read()))

if __name__ == "__main__":
	main()

