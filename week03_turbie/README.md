# SPP Week 3: CodeCamp and Turbie

TA office hours: Mondays and Wednesdays from 13:00 to 14:30.

Slides from lecture:  
 * In this subfolder.


## Welcome to Turbie

This week, you will work through part of the CodeCamp material
and learn basic applied skills such as loading data from text
files, plotting, and working with numeric arrays.

There are a lot of tasks this week, so please remember to reach out
to your classmates, our lovely TAs or visit us during office hours if you need support.


## Sign up for team by deadline or get EM grade

Each student is responsible for finding a team.

All students must join a CodeCamp team and the associated GitHub assignment
(instructions in Part 1) by February 24 at 23:59. Any student whose name is
left in the unassigned column in the signup sheet OR who has not joined
the GitHub assignment by that deadline will automatically fail the codecamp
project. This means you will not be qualified to participate in the final
project, and thus you will receive an "EM" (no-show) grade in the course.


## Homework due next week

It is possible to parallelize these tasks within the team. Part 1
should be done in collaboration, but Parts 2, 3, 4 (and 5, if you
choose to do it) can be split among different people.

Note that Part 2 is more time-intensive for new programmers.
Furthermore, Part 3 requires a function from Part 2 to be merged to main
before it can be completed.

If you split up the work in your team, watch out for merge
conflicts and, when you're done with the tasks, have a team meeting
to review each other's code.


### PART I: Form and join CodeCamp teams (with team, in class)

You should complete this with your new CodeCamp team in class.  

1. Talk with your peers and form groups of 2 to 3 people.  
1. Decide on a team name.  
1. Sign up all members of your team:  
   * Learn / Content / Administration / Programming teams, tab "codecamp-teams".  
   * **!!! DELETE !!!** All team members in left columns.  
   * Write your team name and the **FULL** names of your team members in
     one of the team boxes on the right side of the sheet.  
1. ONE person from your group:  
   * Under Learn / Content / Administration, click the link for the GitHub Assignment
     for CodeCamp.  
   * When prompted, create a new team. Name your team what you wrote in the sign-up
     sheet.  
   * If you get a 503 error, we have reached max. invitation limit for today.
     You will have to try again tomorrow. :(  
1. Other group members should now click the same link on Learn for the GitHub
   assignment BUT join the existing team.  
   * If you get a 503 error, we have reached max. invitation limit for today.
     You will have to try again tomorrow. :(  
1. DO NOT FORK YOUR TEAM REPO. Everyone should work off the repo with
   "DTUWindEducation" in the URL.  
1. Everyone clones the new CodeCamp team repo locally to their computer.  
1. Discuss with your team:  
   * How will you tackle the homework?  
   * Branches off main? Who reviews pull requests?
   * Will you meet physically or virtually? 
   * How do you communicate? Team chat on Slack?  
1. Make and push `Collaboration.md` with the results from your discussion.
   Don't forget to pull afterwards if you didn't push!  

### PART II: Loading data from a text file (indiv. or collab.)

Part 2 is a more intensive task for new programmers. Please leave
adequate time for this and ask for help from TAs/instructors.


1. Run the tests for this week, which should all fail.  
    * Open an Anaconda Prompt.  
    * Change directory to your local copy of your team's repo.  
    * Run pytest on this week's test: `pytest test_week3.py`.  
    * There should be some white and red text and notes about failures. 
1. Navigate to the
   [CodeCamp Day 1 (Part 1) video](https://panopto.dtu.dk/Panopto/Pages/Viewer.aspx?id=33445122-c93b-491e-9db3-afa000fc777c)
   and watch the "Introduction to Turbie" and "Loading data from a 
   text file" chapters.
1. Read the [Definition](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/turbie/1-definition.html)
   page on the CodeCamp website.
1. In a text editor of your choice, open the results file `resp_12_ms_TI_0.1.txt`.
   You can find the file in the `data` folder on your CodeCamp Team
   repo. How many columns are there? What does each column represent?
      4 columns, Time, Vel, Blade deflection and Tower deflection.
1. Scroll through the results file and find out what the wind speed
   is at $t=60$ s. What are the responses at $t = 345$ s?
   V = 11.665; /// xb = 0.853; xt = 0.55.
1. In `codecamp/__init__.py` on your team repo, make a function called `load_resp()` that:  
    * Loads the Turbie response saved in a text file in the same
      format as `resp_12_ms_TI_0.1.txt`, to a set of NumPy arrays.  
         * **TIP!** Don't reinvent the wheel here. There are existing functions
           you can/should re-use.    
    * The input to the function is `path_resp`, which is the path to
      the file and is a string or a `pathlib.Path` object.  
    * The function also has an optional argument ("keyword argument")
      `t_start` that allows a user to specify a start time for the
      data returned by the function. For example, if the data in the
      file starts at 0 seconds and ends at 660 but a user specifies
      `t_start=60`, then the function would only return the data from
      60 to 660 seconds. The default value for `t_start` should be 0.
      If you aren't familiar with keyword/default arguments, [this
      is a nice tutorial](https://www.educative.io/answers/what-are-keyword-arguments-in-python).
    * The function returns 4 1-dimensional NumPy arrays: `t`, `u`,
      `xb`, and `xt`.
1. Add code to `code_week3.py` that uses your new `load_resp()`
   function on the response file located in the `data/` folder.  
   * Note that we have already imported the `codecamp` local package for you!
     Since your `load_resp()` function is in `codecamp/__init__.py`, you can
     simply call `codecamp.load_resp()`. Check the existing example
     in `code_week3.py`.    
   * We will learn more about why this works later, in packaging. But if you are
     curioius, [here is a tutorial about importing](https://diveintopython.org/learn/functions/import-functions).  
1. Re-run the weekly tests. A few should now be passing. If they are all still
   failing, check your `load_resp()` function and the related tests.  
1. Make a similar function called `load_wind()` and place it in
   `codecamp/__init__.py`. The `load_wind()` function should:  
    * Loads the Turbie wind time series saved in a text file to a set
      of NumPy arrays. An example file is `wind_12_ms_TI_0.1.txt`, which
      you can find in the `data/` folder on your team repo.  
    * The input to `load_wind()` is `path_wind`, which is the path to
      the wind data file and can be a string or a `pathlib.Path` object.  
    * The function also has an optional argument ("keyword argument")
      `t_start` that allows a user to specify a start time for the
      data returned by the function. For example, if the data in the
      file starts at 0 seconds and ends at 660 but a user specifies
      `t_start=60`, then the function would only return the data from
      60 to 660 seconds. The default value for `t_start` should be 0.
    * The function returns 2 1-dimensional NumPy arrays: `t_wind`, `u_wind`.  
1. Modify `code_week3.py` so the code calls `load_wind()` on the example
   wind file in the `data/` folder.  
1. Re-run your tests. Everything related to `load_wind()` and `load_resp()`
   should now be passing.  

### PART III:  Plotting data using matplotlib (indiv. or collab.)

You must have a `load_resp()` function from Part 2 merged to main before you
can start this task.

1. Read the first part of [this matplotlib tutorial](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)
   to see how you can make a figure with multiple subplots.  
    * Recommendation: use the keyword argument `figsize` to control the
      aspect ratio of the plot. E.g.:  
```fig, axs = plt.subplots(2, 1, figsize=(9, 4))```
1. Append code to `code_week3.py` that makes a plot of the time series.
   The figure should:  
    * Have two subplots, the top showing the wind speed and the
      bottom showing the blade and tower deflections (two lines on
      the same plot).  
    * Have x-limits going from 60 to 660.  
    * Have the axes/subplots labelled as you see fit.  
   **TIP**: Be sure to add `fig.tight_layout()` and `plt.show()` at
   the very end of your plotting code. This improves the format and
   shows the plot, respectively.
1. Move your plotting code to a function called `plot_resp()` that:  
    * Is placed in `codecamp/__init__.py`.  
    * Takes as input the 4 arrays returned from `load_resp()`.  
    * Has a keyword argument `xlim`, which is a tuple indicating the
      start and stop times. The default should be `(60, 660)`.
    * Returns the figure and axes handles, `fig` and `axs`,
      respectively.  
1. Rerun the tests. Does the test related to `plot_resp()` pass?  
1. Rewrite `code_week3.py` so it does not have plotting code but just
   calls `plot_resp()` to create the plot.  

### PART IV: Construct Turbie matrices (indiv. or collab.)

1. Read the [Definition](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/turbie/1-definition.html)
   page on the CodeCamp website, if you haven't already.
1. Open the `data/turbie_parameters.txt` file in VS code and
   inspect it. What are the different variable values stored in the
   file?
1. Write a function `load_turbie_parameters()` that:  
    * Takes as input the path to the parameters text file (type is
    string or `pathlib.Path` object).
    * Reads the values in the text file.  
    * Returns a dictionary with every value in the text file listed as a key
      in the dictionary.  
   * **NOTE**: Writing code to flexibly load the keys and values of a parameter file in
           this format is quite challenging. For a simpler option, we are okay with you hard-coding
           the dictionary keys in your function, then loading the values with `np.loadtxt()`, 
           utilizing the function's keyword argument `comments`.  
1. Place `load_turbie_parameters()` in `codecamp/__init__.py`. Update
   `code_week3.py` such that it calls `load_turbie_parameters()` to load the parameters.  
1. Watch the
   [CodeCamp Day 1 (Part 2) video](https://panopto.dtu.dk/Panopto/Pages/Viewer.aspx?id=cc28450d-9335-40a6-8ed6-b10d00d31085).  
1. Create a function `get_turbie_system_matrices()` that:  
    * Takes as input the path to the parameters text file (type is
    string or `pathlib.Path` object).  
    * Loads the variables in the text file using your
    `load_turbie_parameters()` function and then assembles Turbie's
      mass, stiffness, and damping matrices.  
    * Returns `M`, `C`, and `K`.  
1. Update `code_week3.py` such that it imports/calls
   `get_turbie_system_matrices()` and defines variables `M`, `C`, and
   `K` in the script.  
1. Rerun the tests. Do they all pass? If yes, you're done! Whoo!      


### PART V: Extra credit (indiv. or collab.)

As noted in earlier weeks, parts marked "extra credit" have no bearing on
your grade. This is extra material for students who want more practice or
exposure to more advanced topics.

1. Look at all the test functions in `test_week3.py` and make sure you
   understand them. Especially the one testing `plot_resp()`, how does it work?  
1. Watch any other chapters in the [CodeCamp Day 1 videos](https://panopto.dtu.dk/Panopto/Pages/Sessions/List.aspx?folderID=ce2dc79a-9a96-41a1-a048-af9b00bd02dc)
   that seem interesting.
1. Watch the "Eigenanalysis" chapter in [CodeCamp Day 2](https://panopto.dtu.dk/Panopto/Pages/Viewer.aspx?id=82d3d6fd-f3ad-420f-abfd-afa000fd43d9)
   and complete the exercise "Calculate Turbie's natural frequency".
1. Read the [Power spectral density](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/turbie/3-psd.html)
   page and complete the "Exercises for the reader".
1. Compare what you see in your PSD plot with the natural
   frequencies from the eigenanalysis. Does anything match?
