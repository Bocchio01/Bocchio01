.PHONY: generate clean

CC = xelatex
SRC_DIR = Sources
OUT_DIR = Generated
CV_DIR = Sources/cv
CV_SRCS = $(shell find $(CV_DIR) -name '*.tex')

# examples: $(foreach x, coverletter cv resume, $x.pdf)
generate: $(foreach x, cv, $(OUT_DIR)/$x.pdf)

$(OUT_DIR)/cv.pdf: $(SRC_DIR)/cv.tex $(CV_SRCS)
	$(CC) -output-directory=$(SRC_DIR) $<

clean:
	-rm -f $(SRC_DIR)/*.{aux,dvi,log,bbl,blg,brf,fls,toc,thm,out,fdb_latexmk}
