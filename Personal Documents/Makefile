.PHONY: CV Resume Coverletter clean

CC = xelatex
SOURCE_DIR = Sources
OUTPUT_DIR = Generated

all: CV Resume Coverletter clean

CV: $(SOURCE_DIR)/CV.tex
	$(CC) -output-directory=$(OUTPUT_DIR) -include-directory=$(SOURCE_DIR)/ $<

Resume: $(SOURCE_DIR)/Resume.tex
	$(CC) -output-directory=$(OUTPUT_DIR) -include-directory=$(SOURCE_DIR)/ $<

Coverletter: $(SOURCE_DIR)/Coverletter.tex
	$(CC) -output-directory=$(OUTPUT_DIR) -include-directory=$(SOURCE_DIR)/ $<

clean:
	del /Q $(OUTPUT_DIR)\*.aux
	del /Q $(OUTPUT_DIR)\*.lof
	del /Q $(OUTPUT_DIR)\*.log
	del /Q $(OUTPUT_DIR)\*.lot
	del /Q $(OUTPUT_DIR)\*.out
	del /Q $(OUTPUT_DIR)\*.toc
