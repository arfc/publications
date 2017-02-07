NAME=Moltres
AUX=$(NAME).aux
INTERMEDIATES=$(NAME).bbl $(NAME).blg $(NAME).log $(NAME).out

all: $(NAME).pdf

$(NAME).pdf : $(NAME).tex
	pdflatex -shell-escape $(NAME)
	# bibtex $(NAME)
	makeglossaries $(NAME)
	pdflatex -shell-escape $(NAME)
	pdflatex -shell-escape $(NAME)

clean :
	rm $(AUX) $(INTERMEDIATES)

clobber :
	rm $(NAME).pdf
