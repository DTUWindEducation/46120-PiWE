# SPP Week 0: Pre-course preparation

SPP is a student-driven course, so most of your time learning is outside the classroom. This includes
preparation, which is essential. Take assigned preparation seriously so you aren't lost during lecture.

The final Python exercises are designed to give you a foundation in the basics of Python. We assign
this as preparation instead of teaching it explicitly because (1) many students often already know
them and (2) it is easy to learn these skills from online tutorials.  

This means **the prep time for Week 1 may be significantly higher for people who have less
experience with Python**. Please take this into account when planning your time. This
skewed preparation time across students will reduce substantially in a few weeks.  

We begin Week 1 with peer-to-peer presentations of `week00_prep_answers.py` (see end of page). So
be sure to have it ready to discuss with your colleagues.

You are ready for Week 1 of PiWE when you have:  
1.	Installed Python and VS code.  
2.	Installed scientific Python packages.  
3.	Installed git.  
4. Created a GitHub account.  
5.	Forked and cloned this repository.  
6. Completed the Python exercises (potentially including extra prep).  

## Working in pairs

Steps 1 through 5 need to be completed on your individual laptop/computer. For the Python exercises (Step 6),
you are welcome--nay, encouraged!--to work in pairs. Engineering is collaborative problem solving. When
you have finished `week00_prep_answers.py`, add a comment to the top with your names and make sure you
both have a copy locally before coming to class in Week 1.

## 1. Install/verify VS Code and Python

* If you already have a Python IDE/distribution (e.g., Anaconda/Spyder, PyCharm, etc.):  
   * If you are comfortable with your IDE and Python distribution (e.g., know how to install/uninstall
     Python packages from the terminal and run the debugger):
      * You may keep your current setup at your own risk. If Python compatibility issues arise during the
        semester, you may need to revert to the recommended set-up.  
   * If you do not know how to install packages from the terminal and/or run the debugger:  
      * Please unintall Python/Anaconda/PyCharm and any other related applications, then follow
        installation instructions in the next bullet.  
* If you need a Python IDE/distribution:  
   * Follow the instructions for "automated installation" [here at DTU Python support](https://pythonsupport.dtu.dk/install/python.html).  
   * Verify the installation per the instructions at the link.  
   * If there are issues, read the installation page thoroughly, but then contact DTU Python support
     if it still won't behave.  


## 2. Install scientific Python packages

If you already have the packages below installed in a Python distribution/environment, you may skip this step.

Search for and open an Anaconda Prompt (application). In the resulting terminal, enter the following
command:  

   ```python -m pip install numpy matplotlib scipy pandas pytest pytest-cov pylint```  

This will install these packages to your base Python environment.
We will learn more about what they do during the course.


## 3. Install git

If you already have a git program, skip this step.

Install the git program from [this website](https://git-scm.com/).


## 4. Make a GitHub account

Go to [GitHub.com](https://github.com/) and create an account. Noice.

## 5. Fork and clone this repository

A "repository" is often called "repo", 'cause life is short.  

### a. Fork the repo

1. Open this repository on GitHub: [https://github.com/DTUWindEducation/46120-PiWE](https://github.com/DTUWindEducation/46120-PiWE).  
2. In the upper-right corner, click the box that says "Fork".  
3. Keep the default settings and click "Create fork".  
4. After a few seconds, the page should refresh. HOWEVER the URL should now be different:
   instead of having "DTUWindEducation" in the name, it should have your GitHub username instead.  
      * This new webpage is a copy (fork) of the `46120-PiWE` repo, but under your user namespace.
        This means that you can push/pull changes to the copy (fork) without affecting the original
        repo.  
5. Click the green "Code" button in the upper-right corner, and copy the HTTPS link.  

### b. Clone the repo

1. Create a folder on your computer where you want your PiWE materials to be saved.  
2. Open a git bash terminal in this folder. On Windows:  
   a. Right-click in the folder.  
   b. Select "More options".  
   c. Select "Open Git Bash here".  
3. In the git terminal, enter the following command:  
   ```git clone <HTTPS link you copied in part a>```
4. This should create a subfolder called `46120-PiWE`, which should contain the repo material.  


## 6. Complete Python exercises (and prep)

All PiWE students, regardless of level, should review the section on refresher material. Complete
parts of the refresher material depending on what makes sense for you.

The final exercise to complete before class, `week00_prep_answers.py`, is explained in the final
subsection.

### Refresher material

It is **highly recommended** that you, regardless of Python level, at least complete the module-end exercises in
the `welcome_to_python.ipynb` Jupyter notebook. This will verify you have a solid foundation.

If you are inexperienced with VS Code and/or Python, you should go through more of the refresher material.  

Everything labelled "DPS Tutorial" is a video tutorial from [DTU Python Support](https://pythonsupport.dtu.dk/videos/index.html).
Each tutorial is about 5 minutes long.  

If you need to learn (or need a refresher) with...  
* VS Code  
   * DPS Tutorial: Getting started with VS Code  
   * DPS Tutorial: Workspaces and files in VS Code  
   * DPS Tutorial: Jupyter notebooks  
      * Even if you're familiar with notebooks, VS Code has a few differences you should know about  
   * DPS Tutorial: Keybindings in VS Code  
   * DPS Tutorial: Integrated terminal in VS Code  
   * DPS Tutorial: Extensions in VS Code  
* Basic Python and/or Jupyter Notebooks  
   * Jupyter notebook `welcome_to_python.ipynb` (**RECOMMENDED FOR ALL!**)
   * DPS Tutorial: Debugging tool in VS Code  
   * DPS Tutorial: Importing packages  
   * DPS Tutorial: Module not found error in conda  
* Using the terminal  
   * DPS Tutorial: Using the terminal


### Finish week00_prep_answers.py

Once you have finished the refresher material, it's time to complete the "final" preparation exercise.

Create a file called `week00_prep_answers.py` in your `46120-PiWE/week00_prep/` folder on your computer.
In this file, write code that completes Required Exercises 1 through 5 on [this page](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/preparation.html#Required-exercises). 

If you're still thirstin' for knowledge, you can complete the "Optional Python exercises" on the same
page.

Once you're finished `week00_prep_answers.py`, you're freeeeeeeeee!
