import sys
import json

def toHTML(data):
	return (
		'<table>\n'
			'<tbody>\n'
				'<tr>\n'
					'<td align="left">{}</td>\n'
					'<td align="center"></td>\n'
					'<td align="right">{}</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td align="left">{}</td>\n'
					'<td align="center"><span class="name">{}</span></td>\n'
					'<td align="right">{}</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td align="left">{}</td>\n'
					'<td align="center"></td>\n'
					'<td align="right">{}</td>\n'
				'</tr>\n'
			'</tbody>\n'
		'</table>\n'
		'<hr>\n'
		'<table>\n'
			'<tbody>\n'
				'<tr>\n'
					'<td><p>EDUCATION</p></td>\n'
					'<td>\n{}\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><p>SKILLS</p></td>\n'
					'<td>\n{}\n<br>\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><p>EXPERIENCE</p></td>\n'
					'<td>\n{}\n<br>\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><p>ACTIVITIES</p></td>\n'
					'<td>\n{}\n<br>\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><p>ACHIEVEMENTS</p></td>\n'
					'<td>\n{}\n<br>\n</td>\n'
				'</tr>\n'
				'<tr>\n'
					'<td><p>PROJECTS</p></td>\n'
					'<td>\n{}\n</td>\n'
				'</tr>\n'
			'</tbody>\n'
		'</table>\n'
	).format(
		data['address'],
		data['phone'],
		data['city'],
		data['name'],
		data['email'],
		data['linkedin'],
		data['github'],
		'\n'.join([
			"<strong>{}</strong> <right>{}</right> <br>\n".format(
				school['school'],
				school['time'],
			) +
			(
				"{}\n".format('<br>\n'.join(school['description'][:-1]))
				if 'description' in school else ''
			) +
			'<br>' +
			(
				"Coursework: {}<br>\n".format(', '.join(school['coursework'][:-1]))
				if 'coursework' in school else ''
			) +
			'<br>' +
			''
			for school in data['education'] if 'school' in school
		]),
		"Proficient in {}<br><hr>\nFamiliar with {}<br><hr>\nLanguages: {}<br>\n".format(
			', '.join(data['skills']['proficient'][:-1]),
			', '.join(data['skills']['familiar'][:-1]),
			', '.join(data['skills']['libraries'][:-1]),
		),
		'<br>\n'.join([
			"<strong>{}</strong> <right>{}</right> <br>\n <em>{}, {}</em> <br>\n".format(
				job['role'],
				job['time'],
				job['group'],
				job['city'],
			) +
			'<hr>' +
			(
				'<br><hr>\n'.join([
					' '.join(statement[:-1]) + '.'
					for statement in job['description'] if len(statement) > 0
				])
				if 'description' in job else ''
			) +
			'<br>\n' +
			''
			for job in data['experience'] if len(job) > 0
		]),
		'\n'.join([
			"<strong>{} ({})</strong> <right>{}</right> <br>\n".format(
				group['group'],
				group['role'],
				group['time'],
			) +
			'<hr>' +
			(
				'<br><hr>\n'.join([
					' '.join(statement[:-1]) + '.'
					for statement in group['description'] if len(statement) > 0
				])
				if 'description' in group else ''
			) +
			'<br><hr>\n' +
			''
			for group in data['activities'] if len(group) > 0
		]),
		'<br><hr>\n'.join([
			' '.join(achievement[:-1])
			for achievement in data['achievements']
		]),
		'<br><hr>\n'.join([
			(
				"({}) ".format(project['language'])
				if 'language' in project else ''
			) +
			' '.join(project['description'][:-1])
			for project in data['projects'] if 'description' in project
		]),
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

