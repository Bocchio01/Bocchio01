.PHONY: Maths Physics clean

CC = xelatex
SOURCE_DIR_MATH = maths
SOURCE_DIR_PHYSICS = physics
OUTPUT_DIR =

all: Maths Physics clean

Maths: $(SOURCE_DIR_MATH)/Maths.tex
	cd $(SOURCE_DIR_MATH)
	$(CC) -output-directory=$(OUTPUT_DIR) -include-directory=$(SOURCE_DIR_MATH)/ $<

Physics: $(SOURCE_DIR_PHYSICS)/Physics.tex
	cd $(SOURCE_DIR_PHYSICS)
	$(CC) -output-directory=$(OUTPUT_DIR) -include-directory=$(SOURCE_DIR_PHYSICS)/ $<

clean:
	del /Q $(OUTPUT_DIR)*.aux
	del /Q $(OUTPUT_DIR)*.lof
	del /Q $(OUTPUT_DIR)*.log
	del /Q $(OUTPUT_DIR)*.lot
	del /Q $(OUTPUT_DIR)*.out
	del /Q $(OUTPUT_DIR)*.toc
	del /Q $(OUTPUT_DIR)*.fls
	del /Q $(OUTPUT_DIR)*.fdb_latexmk
	del /Q $(OUTPUT_DIR)*.synctex.gz