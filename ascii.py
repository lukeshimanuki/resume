import sys
import json

def toASCII(data):
	return (
		"{name}\n\n\n"
		"{address}\n"
		"{city}\n\n"
		"{email}\n"
		"{phone}\n\n"
		"{website}\n\n\n"
		"EXPERIENCE\n\n{experience}\n\n"
		"RESEARCH\n\n{research}\n\n"
		"EDUCATION\n\n{education}\n\n"
		"ACTIVITIES\n\n{activities}\n\n"
		"SKILLS\n\n{skills}\n\n"
		"AWARDS\n\n{awards}\n\n"
		"PROJECTS\n\n{projects}\n\n"
	).format(
		education = '\n'.join([
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
		skills = "Proficient in {}\nFamiliar with {}\nLibraries: {}\n".format(
			', '.join(data['skills']['proficient'][:-1]),
			', '.join(data['skills']['familiar'][:-1]),
			', '.join(data['skills']['libraries'][:-1]),
		),
		experience = '\n'.join([
			"{} ({})\n{}, {}\n".format(
				job['role'],
				job['time'],
				job['group'],
				job['city'],
			) +
			(
				'\n'.join([
					' '.join(statement[:-1])
					for statement in job['description'] if len(statement) > 0
				])
				if 'description' in job else ''
			) +
			'\n' +
			''
			for job in data['experience'] if len(job) > 0
		]),
		research = '\n'.join([
			"{} ({})\n".format(
				position['group'],
				position['time'],
			) +
			(
				'\n'.join("{description} -- {published}".format(**project)
					for project in position['projects']
					if len(project) > 0
				)
			) +
			'\n' +
			''
			for position in data['research'] if len(position) > 0
		]),
		activities = '\n'.join([
			"{} ({})\n{}\n".format(
				group['role'],
				group['time'],
				group['group'],
			) +
			(
				'\n'.join([
					' '.join(statement[:-1])
					for statement in group['description'] if len(statement) > 0
				])
				if 'description' in group else ''
			) +
			'\n' +
			''
			for group in data['activities'] if len(group) > 0
		]),
		awards = '\n'.join([
			' '.join(achievement[:-1])
			for achievement in data['achievements']
		]),
		projects = '\n'.join([
			(
				"({}) ".format(project['language'])
				if 'language' in project else ''
			) +
			' '.join(project['description'][:-1])
			for project in data['projects'] if 'description' in project
		]),
		**{
			key: value
			for key, value in data.items()
			if key in (
				'name',
				'address',
				'city',
				'email',
				'phone',
				'website',
			)
		},
	)

def main():
	sys.stdout.write(toASCII(json.loads(open('resume.json').read())))

if __name__ == "__main__":
	main()

