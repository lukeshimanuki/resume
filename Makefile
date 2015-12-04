all: resume.html resume.pdf

resume.pdf: resume.html
	wkhtmltopdf --encoding utf-8 --grayscale --page-size Letter --margin-top 0.5in --margin-bottom 0.5in --margin-left 1.0in --margin-right 1.0in resume.html resume.pdf

resume.html: resume.md style.css
	pandoc  --standalone -H style.css resume.md -o resume.html
#	pandoc  --standalone --css=style.css resume.md -o resume.html

clean:
	rm -f resume.html
	rm -f resume.pdf

