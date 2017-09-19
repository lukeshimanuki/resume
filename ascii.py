import sys
import json

def toASCII(data):
	return (
		"{}\n\n\n"
		"{}\n"
		"{}\n\n"
		"{}\n"
		"{}\n\n"
		"{}\n"
		"{}\n\n\n"
		"EDUCATION\n\n{}\n\n"
		"SKILLS\n\n{}\n\n"
		"EXPERIENCE\n\n{}\n\n"
		"RESEARCH\n\n{}\n\n"
		"ACTIVITIES\n\n{}\n\n"
		"ACHIEVEMENTS\n\n{}\n\n"
		"PROJECTS\n\n{}\n\n"
	).format(
		data['name'],
		data['address'],
		data['city'],
		data['email'],
		data['phone'],
		data['github'],
		data['linkedin'],
		'\n'.join([
			"{} ({})\n".format(
				school['school'],
				school['time'],
			) +
			(
				"{}\n".format(school['field'])
				if 'field' in school else ''
			) +
			(
				"{}\n".format('\n'.join(school['description'][:-1]))
				if 'description' in school else ''
			) +
			(
				"Coursework: {}\n".format(', '.join(school['coursework'][:-1]))
				if 'coursework' in school else ''
			) +
			''
			for school in data['education'] if 'school' in school
		]),
		"Proficient in {}\nFamiliar with {}\nLanguages: {}\n".format(
			', '.join(data['skills']['proficient'][:-1]),
			', '.join(data['skills']['familiar'][:-1]),
			', '.join(data['skills']['libraries'][:-1]),
		),
		'\n'.join([
			"{} ({})\n{}, {}\n".format(
				job['role'],
				job['time'],
				job['group'],
				job['city'],
			) +
			(
				'\n'.join([
					' '.join(statement[:-1]) + '.'
					for statement in job['description'] if len(statement) > 0
				])
				if 'description' in job else ''
			) +
			'\n' +
			''
			for job in data['experience'] if len(job) > 0
		]),
		'\n'.join([
			"{} ({})\n".format(
				position['group'],
				position['time'],
			) +
			(
				'\n'.join([
					' '.join(statement[:-1]) + '.'
					for statement in position['description'] if len(statement) > 0
				])
				if 'description' in position else ''
			) +
			'\n' +
			''
			for position in data['research'] if len(position) > 0
		]),
		'\n'.join([
			"{} ({})\n{}\n".format(
				group['role'],
				group['time'],
				group['group'],
			) +
			(
				'\n'.join([
					' '.join(statement[:-1]) + '.'
					for statement in group['description'] if len(statement) > 0
				])
				if 'description' in group else ''
			) +
			'\n' +
			''
			for group in data['activities'] if len(group) > 0
		]),
		'\n'.join([
			' '.join(achievement[:-1])
			for achievement in data['achievements']
		]),
		'\n'.join([
			(
				"({}) ".format(project['language'])
				if 'language' in project else ''
			) +
			' '.join(project['description'][:-1])
			for project in data['projects'] if 'description' in project
		]),
	)

def main():
	sys.stdout.write(toASCII(json.loads(open('resume.json').read())))

if __name__ == "__main__":
	main()

