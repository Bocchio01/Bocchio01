.PHONY: PingPong clean

CC = pdflatex

all: PingPong clean

PingPong: PingPong_problem.tex
	$(CC) $<

clean:
	del /Q *.aux *.lof *.log *.lot *.out *.toc *.fls *.fdb_latexmk
