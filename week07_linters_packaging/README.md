# PiWE Week 7: Misc., Linters and Packaging

Office hours, slides, recordings:  
 * Office hours: Monday and Wednesday 13.00 - 14.30 on Zoom.
 * Slides: In this subfolder  
 * Recording: on Learn

## Overview

Linters and style guides ensure that code written by other people "looks"
the same, making it easier to review. Packaging allows you to bundle functions/classes
together and install them, making them accessible anywhere on your computer.


## Homework due next week

### PART 0: Plan of attack (in class)

Determine who will work on which parts. Note high chance for merge
conflicts. Recommend that Part 1 PR is merged before Part 2 PR.

### PART 1: Make codecamp a package

1. Next `codecamp/` into a `src/` folder and create a `pyproject.toml` for your project.  
1. Editably install your package in your standard environment. Run `pytest` on `test_week3.py`.
   Do the tests successfully discover the newly installed `codecamp` package?  
1. Make a new folder called `tests/` and move your tests there. Call pytest from the main-repo
   level: `pytest tests/`. Do all tests run?
1. Move `code_week*.py` and `main.py` to a new subolder, `examples/`. **!!! NOTE !!!** you'll probably
   need to change paths in `main.py`.  
1. Make/activate a new environment called test. Install your codecamp package editably. 
   Run your tests. Run main.py. Do they work?  
1. Create a new environment with Python 3.11 per the instructions shared earlier in the class.
   Install your package editably and re-run tests. Does it work?  
1. Make a PR with your changes. Have another team member review/approve/merge.  

### PART 2: Clean up code style

1. Enable the pylint and flake8 extensions in VS Code.  
1. Install pylint if you don't have it. In Anaconda Prompt, `pip install pylint`.  
1. Run pylint on codecamp: `pylint codecamp/` or `pylint src/`. What is your score?  
1. Make changes to your code so your score is above 7 (ideally higher).
1. Make a PR with your changes. Have another team member review/approve/merge.  

## Extra credit

* Name your package `<team>-codecamp` and try to upload it to PyPI per the instructions
  in the slide deck. Can you successfully install it from PyPI without having to
  clone first?