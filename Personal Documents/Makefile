.PHONY: Sources

CC = xelatex
SRC_DIR = Sources
RESUME_DIR = Sources/resume
CV_DIR = Sources/cv
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
CV_SRCS = $(shell find $(CV_DIR) -name '*.tex')

# examples: $(foreach x, coverletter cv resume, $x.pdf)
examples: $(foreach x, cv, $x.pdf)

resume.pdf: $(SRC_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(SRC_DIR) $<

cv.pdf: $(SRC_DIR)/cv.tex $(CV_SRCS)
	$(CC) -output-directory=$(SRC_DIR) $<

coverletter.pdf: $(SRC_DIR)/coverletter.tex
	$(CC) -output-directory=$(SRC_DIR) $<

clean:
	rm -rf $(SRC_DIR)/*.pdf

