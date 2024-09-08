PYTHON = python3

# The main script
MAIN = main.py

# Default target
all: run

# Run the game
run:
	$(PYTHON) $(MAIN)

# Clean up any generated files (not really necessary for Python, but included for completeness)
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.PHONY: all run clean