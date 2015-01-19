all: resume.html resume.pdf

MARGIN=0.8in

resume.pdf: resume.html
	wkhtmltopdf --encoding utf-8 --grayscale --page-size Letter --margin-top $(MARGIN) --margin-bottom $(MARGIN) --margin-left $(MARGIN) --margin-right $(MARGIN) resume.html resume.pdf

resume.html: resume.md style.css
	pandoc  --standalone -H style.css resume.md -o resume.html
#	pandoc  --standalone --css=style.css resume.md -o resume.html

clean:
	rm -f resume.html
	rm -f resume.pdf

