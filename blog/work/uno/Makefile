all: unknown_nuclear_opponent

unknown_nuclear_opponent: unknown_nuclear_opponent.lyx
	lyx --export xetex unknown_nuclear_opponent.lyx
	xelatex unknown_nuclear_opponent
	bibtex unknown_nuclear_opponent
	xelatex unknown_nuclear_opponent
	xelatex unknown_nuclear_opponent
	rm -f *.aux *.bbl *.blg *.log *.nlo *.tex *.ilg *.nls
	evince unknown_nuclear_opponent.pdf
