# PiWE Week 2: Functions and Tests

TA office hours: Mondays and Wednesdays from 13:00 to 14:30.

Slides: here in this subfolder.

## Overview

Functions are a way to bundle code that is meant to be executed multiple
times, but with different values. A test is a kind of function that uses an
assert statement to check whether the behaviour of a part of code matches
what is expected.

This week, you will reorganize your pre-class assignment
code into functions and a main script, and you will update the Week 2 tests
to check whether your functions work as expected. You will finish off by
doing some tutorials on scientific Python packages as preparation for next
week.

## Homework due next week

Parts 2A and 2B are decoupled from each other and can be done in
parallel. We recommend you split into subteams, each subteam works on
their part in branches, then merge the solutions when finished.
We expect you will need to merge the Part 2A branch into Part 2B
partway through the Part 2B assignment.

### Notes on "Extra credit"

Homework in this class will often have sections marked as "Extra credit".
This content has no impact on your grade. It is for you if you have
extra bandwidth and want a deeper or more advanced understanding
of topics. You are welcome to complete, or not complete, parts marked
"extra credit" at your leisure.

### PART 1: As a team, in class

1. Individually, fill out the [46120 Pre-evaluation](https://evaluering.dtu.dk/) (3 minutes).  
1. Individually, read through this homework description.  
1. Take a team meeting and:  
    * Create a file in your team repo called `Collaboration.md`.  
    * Discuss: Will you split into subteams? In your subteams, will you pair-program?
      Meet physically or virtually?    
    * Discuss: What is your branch structure? One per person? One per subteam?  
    * Write your decisions in `Collaboration.md` and push it.  
    * Other team members, pull `Collaboration.md`
1. Run the Week 2 tests, which should FAIL at this point:  
    * Open an Anaconda Prompt.  
    * Change directory to your local copy of your team's repo.  
    * Run pytest on the week2 test: `pytest test_week2.py`.  
    * There should be some white and red text and notes about failures.  
1. Extra credit:   
    * Read the output text from pytest. What error(s) are causing
      the tests to fail? (Do NOT try to fix the error yet! Just try
      to diagnose.)

### PART 2A: Restructure/diagram your pre-class code

1. Create and checkout into a new branch, you choose the name.  
1. Restructure the code in `preclass_assignment` in your team's repo such that:  
    * There are two files, called `functions.py` and `main.py`.
    * The only code in `functions.py` is the [five functions](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/preparation.html#Required-exercises)
      that you made for the pre-class assignment.  
    * The code in `main.py` should import/demonstrate/execute the functions, similar to
      what is seen on [the description page](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/preparation.html#Required-exercises).
      There should be no functions defined in `main.py`.
1. Run `main.py` and make sure it properly imports and executes the
   functions.  
1. In VS Code, install the [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
   extension by Henning Dieterichs.  
1. In your team repo, create a file called `FunctionDiagram.drawio`:  
    * Open the file in VS Code. You should have a nice view of an
      empty drawing canvas.  
    * Create black-box diagrams of the five functions in `functions.py`.
      Remember to include types of inputs and outputs!
    * Note that if a function does not explicitly return an output, then
      the return value is `None`. 
1. Push your branch.  

### PART 2B: Analyse/update tests

1. Create and checkout into a new branch, you choose the name.  
1. Open `test_week2.py` in VS Code.  
1. Read through the functions and docstrings (triple-quote text below
   the function definition).  
    * How many functions are there? What is each function's purpose?
1. Read through the `test_square_list()` function. Do you understand
   how it works?  
1. Write the test for `test_fibonacci_stop()`:  
    * Use a similar function structure to `test_square_list()`.  
    * Use the same input and expected output as the values in
      [the description page](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/preparation.html#4.-While-loops).  
    * Update the assert statement, again using `test_square_list()`
      as inspiration.  
1. If Part 2A is complete, merge in the branch from Part 2A.  
    * If you were able to merge, run `pytest` again. Take time and read
      the output from pytest carefully. How many tests are passing now?
      Which ones are still failing?  
1. Write the test for `test_clean_pitch()`:  
    * Use `test_fibonacci_stop()` and `test_square_list()` as
      inspiration, though make changes as needed.  
1. If you have merged in the branch from Part 2A, re-run `pytest` and
   examine the test output. Are your test functions passing?  
1. Write the test in `test_goldilocks()` for one value:  
    * Choose a single test input and expected print from 
      [the description page](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/preparation.html#2.-If/else-statements).
    * Use the code in `test_greet()` as an example, and update
      `test_goldilocks()` so it tests the `goldilocks()`
      function for your test input.  
    * NOTES:  
        - Because `greet()` and `goldilocks()` do not return a string but rather
          print text to screen, the test function needs to be set up differently
          than what we saw in the other tests.
          Specifically, we need to use a special `pytest` functionality that captures
          and saves text that would normally be printed to screen. We then assert
          that the "standard output" of what we captured (i.e., `captured.out`),
          is equal to our expected text. Tricky, eh?  
        - `test_greet()` is not perfect! We should have defined an
          `exp_print` variable in `# given` for the expected print output,
          `Hello, world!\n`. Oops!  
1. If you have merged in the branch from Part 2A, re-run `pytest` and
   examine the test output. Are all your test functions passing?  
1. Extra credit: update `test_goldilocks()` to check the other test cases. See
   details in "Extra credit" below.  
1. If all your test functions are passing, push your branch.  

### PART 3: Individually

1. In the [PiWE GitHub repo](https://github.com/DTUWindEducation/46120-PiWE),
   there is a subfolder called `tutorials_scientific_python`.  
1. Go through:  
    * (If you need instructions on Jupyter notebooks) `1-introduction_to_jupyter_notebooks.ipynb`  
    * `2a-tutorial_numpy_array_basics.ipynb`  
    * `3a-tutorial_matplotlib_basics.ipynb`
1. Highly recommended if you have time:  
    * `2b-exercise_numpy.ipynb`  
    * `3b-exercise_matplotlib.ipynb`  
1. Once you have finished these tutorials, you're done for this week!  

### Extra credit

1. Update `test_goldilocks()` to test all edge cases shown in
   [the description page](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/preparation.html#2.-If/else-statements).
   You could do this in a few different ways:  
    * (Not great) Copy/pasting the function contents and updating the input/expected
      output accordingly. Gets the job done, but messy code.  
    * (Okay) Implementing a for loop in your test function. Ask a TA/instructor if you
      need help iterating over two lists at once, or google the `zip()` function.  
    * (Most elegant) Read up on and implement a [pytest parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html).  
1. Open and read through `test_week1.py`.  
    * What did each function do? How did they work? You might need to read up on 
      [`pathlib.path`](https://docs.python.org/3/library/pathlib.html),
      e.g., [this introduction to it](https://www.datacamp.com/tutorial/comprehensive-tutorial-on-using-pathlib-in-python-for-file-system-manipulation).  
1. Read through some of the extra material below, depending on what interests you.  

## Videos, tutorials, and other resources

* [PiWE tutorials (Jupyter notebooks) on numpy, matplotlib, pands](https://github.com/DTUWindEducation/46120-PiWE/tree/main/tutorials_scientific_python)  
* [Tutorial on assert statements](https://www.w3schools.com/python/ref_keyword_assert.asp)  
* [Introduction to Python functions, including return values and keyword arguments](https://openstax.org/books/introduction-python-programming/pages/6-introduction)  
* [Short overview on Given, When, Then and connection to other testing concepts](https://martinfowler.com/bliki/GivenWhenThen.html)  
* [A gentle introduction to testing with pytest](https://bas.codes/posts/python-pytest-introduction)  
