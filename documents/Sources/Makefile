# Makefile for compiling LaTeX documents
.PHONY: all cv resume clean cleanall help

# Configuration
LATEX = xelatex -interaction=nonstopmode -quiet
OUTPUT_DIR = ../Generated
BASENAME = Tommaso_Bocchietti

# Input files
CV_SOURCE = CV.tex
RESUME_SOURCE = Resume.tex

# Output files
CV_PDF = $(OUTPUT_DIR)/CV_$(BASENAME).pdf
RESUME_PDF = $(OUTPUT_DIR)/Resume_$(BASENAME).pdf
.PHONY: $(CV_PDF) $(RESUME_PDF)

# Default target: build all versions
all: $(CV_PDF) $(RESUME_PDF)
	@echo "All documents compiled successfully."

# Create output directory if it doesn't exist
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

$(CV_PDF): $(CV_SOURCE) | $(OUTPUT_DIR)
	@echo "Compiling Curriculum Vitae..."
	$(LATEX) -jobname=temp_cv $(CV_SOURCE)
	@mv temp_cv.pdf $(CV_PDF)
	@rm -f temp_cv.aux temp_cv.log temp_cv.out

$(RESUME_PDF): $(RESUME_SOURCE) | $(OUTPUT_DIR)
	@echo "Compiling Resume..."
	$(LATEX) -jobname=temp_resume $(RESUME_SOURCE)
	@mv temp_resume.pdf $(RESUME_PDF)
	@rm -f temp_resume.aux temp_resume.log temp_resume.out

# Individual targets
cv: $(CV_PDF)
resume: $(RESUME_PDF)

# Clean generated files
clean:
	@echo "Cleaning temporary files..."
	@rm -f *.aux *.log *.out temp_*.pdf
	@rm -f $(OUTPUT_DIR)/*.aux $(OUTPUT_DIR)/*.log $(OUTPUT_DIR)/*.out

# Clean everything including PDFs
cleanall: clean
	@echo "Removing all generated PDFs..."
	@rm -f $(OUTPUT_DIR)/*.pdf

# Help target
help:
	@echo "Available targets:"
	@echo "  make all        - Compile all resume versions (default)"
	@echo "  make cv         - Compile only Curriculum Vitae"
	@echo "  make resume     - Compile only Resume"
	@echo "  make clean      - Remove temporary files"
	@echo "  make cleanall   - Remove all generated files including PDFs"
	@echo "  make help       - Show this help message"