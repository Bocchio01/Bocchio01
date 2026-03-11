# Makefile for compiling LaTeX documents
.PHONY: all cv resume letter clean cleanall help

# Configuration
SRC_DIR = src
OUT_DIR = build
LATEX = xelatex -interaction=nonstopmode -quiet

# Input files
SRC_CV = curriculum-vitae.tex
SRC_RESUME = resume.tex
SRC_LETTER = cover-letter.tex

# Output files
OUT_CV = Tommaso_Bocchietti_CV.pdf
OUT_RESUME = Tommaso_Bocchietti_Resume.pdf
OUT_LETTER = Tommaso_Bocchietti_CoverLetter.pdf

# Default target: build all versions
all: cv resume letter
	@echo "All documents compiled successfully."

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

cv: $(SRC_DIR)/$(SRC_CV) | $(OUT_DIR)
	@printf "Compiling Curriculum Vitae..."
	@cd $(SRC_DIR) && $(LATEX) -jobname=temp_cv $(SRC_CV)
	@mv $(SRC_DIR)/temp_cv.pdf $(OUT_DIR)/$(OUT_CV)
	@rm -f $(SRC_DIR)/temp_cv.*
	@echo " done"

resume: $(SRC_DIR)/$(SRC_RESUME) | $(OUT_DIR)
	@printf "Compiling Resume..."
	@cd $(SRC_DIR) && $(LATEX) -jobname=temp_resume $(SRC_RESUME)
	@mv $(SRC_DIR)/temp_resume.pdf $(OUT_DIR)/$(OUT_RESUME)
	@rm -f $(SRC_DIR)/temp_resume.*
	@echo " done"

letter: $(SRC_DIR)/$(SRC_LETTER) | $(OUT_DIR)
	@printf "Compiling Cover Letter..."
	@cd $(SRC_DIR) && $(LATEX) -jobname=temp_letter $(SRC_LETTER)
	@mv $(SRC_DIR)/temp_letter.pdf $(OUT_DIR)/$(OUT_LETTER)
	@rm -f $(SRC_DIR)/temp_letter.*
	@echo " done"

clean:
	@printf "Cleaning temporary files..."
	@rm -f $(SRC_DIR)/*.aux $(SRC_DIR)/*.log $(SRC_DIR)/*.out $(SRC_DIR)/temp_*.pdf
	@rm -f $(OUT_DIR)/*.aux $(OUT_DIR)/*.log $(OUT_DIR)/*.out
	@echo " done"

cleanall: clean
	@printf "Removing all generated PDFs..."
	@rm -f $(OUT_DIR)/*.pdf
	@echo " done"

help:
	@echo "Available targets:"
	@echo "  make all        - Compile all resume versions (default)"
	@echo "  make cv         - Compile only Curriculum Vitae"
	@echo "  make resume     - Compile only Resume"
	@echo "  make letter     - Compile only Cover Letter"
	@echo "  make clean      - Remove temporary files"
	@echo "  make cleanall   - Remove all generated files including PDFs"
	@echo "  make help       - Show this help message"