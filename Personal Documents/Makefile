.PHONY: CV Resume Coverletter clean

CC = xelatex
SRC_DIR = Sources
OUT_DIR = Generated

CV: $(SRC_DIR)/CV.tex
	$(CC) -output-directory=$(SRC_DIR) $<

Resume: $(SRC_DIR)/Resume.tex
	$(CC) -output-directory=$(SRC_DIR) $<

Coverletter: $(SRC_DIR)/Coverletter.tex
	$(CC) -output-directory=$(SRC_DIR) $<

clean:
	rm $(SRC_DIR)/*.{aux,dvi,log,bbl,blg,brf,fls,toc,thm,out,fdb_latexmk}
