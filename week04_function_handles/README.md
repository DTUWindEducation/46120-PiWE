# PiWE Week 4: Turbie Part 2

Office hours, slides, recordings:  
 * Office hours: Monday and Wednesday 13.00 - 14.30 on Zoom.
 * Slides: In this subfolder  
 * Recording: on Learn

## Welcome to Turbie Part 2: Windy Boogaloo

This week, you will continue the journey in our Turbie project. You will write 
functions to simulate homogeneous and forced repsonse of the turbine under a given wind condition. This will be achieved by solving 
an initial value problem (IVP) for a system of ODEs (ordinary differential 
equations), for which the `scipy.integrate.solve_ivp` function will be used.


## Homework due next week

Part 1 should be 
done by everyone individually, but Parts 2 onwards can be parallelized.

### PART 0: Plan of attack (in class with team)

Read through this page and make a plan of attack
for who does which parts. Branches with PRs? Team deadlines?

### PART I: Understand the problem formulation
1. Read the [Definition](hhttps://python-at-risoe.pages.windenergy.dtu.dk/codecamp/turbie/1-definition.html)
   page on the CodeCamp website.
1. Read the [Homogeneous response](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/turbie/5-homogeneous-response.html)
   page on the CodeCamp website, ignore the Excercise part for now.
1. Read the [Forced response and save to file](https://python-at-risoe.pages.windenergy.dtu.dk/codecamp/turbie/6-forced-response.html)
   page on the CodeCamp website, ignore the Excercise part for now.
1. Understand the state-space equation of the dynamic system, and note that the
   mass, damping and stiffness matrices (`M`, `C`, and `K`) are given by the 
   function `get_turbie_system_matrices()` that you have written in the Week 2 
   homework.


### PART II: Caculate Ct

1. Run the Week 4 tests using `pytest`. Everything should fail.  
1. Examine the Ct file  `CT.txt`, which is in the `data/` folder
   in your team repo.
1. Make a function in `codecamp/__init__.py` called
   `calculate_ct(u_wind, path_ct)`:  
    * `u_wind` is a numpy array of wind time series, `path_ct` is a
      string or `pathlib.Path` object.  
    * The function calculates the mean of `u`, then interpolates
      the Ct curve and returns a float `ct`.  
    * The interpolation can be done by using `numpy.interp`. Consult the 
      [documentation](https://numpy.org/doc/stable/reference/generated/numpy.interp.html) 
      to learn its usage.   
1. Add code to `code_week4.py` that calls `calculate_ct()` for the wind
   speeds stored in `wind_12_ms_TI_0.1.txt`. (Hint: you might need to call
   `load_wind()` before you call `calculate_ct()`.)  
1. Re-run this week's tests. Does anything pass now?  


### PART III: Write a dydt function for homogenous and forced responses
In this part, you will write a function called `calculate_dydt`
that is of the form `dydt = f(t, y, ...)`. This calculates dy/dt
for the Turbie dynamical system. It should calculate homogenous
or forced response depending on inputs.

1. Run the Week 4 tests using `pytest` and see what is failing.  
1. Recall the state-space equations for the homogenous and forced response, as
   you have gone through in PART I.
1. Make a function called `calculate_dydt` in `codecamp/__init__.py` that
   calculate the RHS (right hand side) of the equation:
   * The required arguments shall be: 
      * `t`: time (float/int)
      * `y`: state vector (1D numpy array or list).
      * `M`: mass matrix (2D numpy array)  
      * `C`: damping matrix (2D numpy array)  
      * `K`: stiffness matrix  (2D numpy array)  
   * The keyword arguments shall be:  
      * `rho`: airdensity [kg/m3], default value: None (float/int)
      * `ct`: thrust coefficient [-], default value: None (float/int)
      * `rotor_area`: rotor area [m2], default value: None (float/int)
      * `t_wind`: time for the wind speed time series [s], default value: None 
         (1D numpy array)
      * `u_wind`: stream wise wind speed for the wind speed time series  [m/s], 
         default value: None (1D numpy array)  
   * It shall return:  
      * A 1D (!!!) numpy array of shape (4,). If your function returns an
        array of shape (4, 1), your output will be wrong size due to something
        called "broadcasting".    
   * When `u_wind` takes the default `None` value, calculate the homogenous
     response (i.e., forcing is zero).
   * When `u_wind` is not `None`, assume other required inputs (`rho`,
     `rotor_area`, `Ct`, `t_wind`) are also provided and calculate the forced
     response.
   * NOTES:  
      * Matrix multipication in the state-space equations should be matrix
        product (`numpy.matmul` with `@` operator as a shorthand).
      * Note that the specific wind speed at time `t` needs to be computed by
        interpolation using the given wind speed time series, defined by `t_wind`
        and `u_wind`.  
5. Add code to `code_week4.py` that calls `calculate_dydt()`
   function for both the homogenous response case and the forced response case.  
    * Use `t = 1` and `y = [1, 2, 3, 4]`.  
1. Re-run this week's tests. Do any more tests pass?  

### PART IV: Simulate homogenous and foced responses by solving an IVP

1. Run the Week 4 tests using `pytest` and see what is failing.  
1. Read the [documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) 
   and go through the examples for `scipy.integrate.solve_ivp`.
1. In `codecamp/__init__.py`, make a function called `simulate_turbie()` that:  
   * Takes as input:
      * `path_wind`: the path to the wind data file and is a string or a 
        `pathlib.Path` object. 
      * `path_parameters`: the path to the turbine parameters file and is a 
        string or a `pathlib.Path` object. 
      * `path_Ct`: the path to the turbine parameters file and is a 
        string or a `pathlib.Path` object.  
   * The function should return:
      * `t`: time of the simulated response [s], same as in the wind speed
         time series.
      * `u_wind`: stream wise wind speed [m/s].
      * `x_b`: displacment of the blade [m].
      * `x_t`: displacment of the tower [m].
   * Pass `calculate_dydt` into `scipy.integrate.solve_ivp` to solve the
     time-marching solution. Assume initial condition `(0, 0, 0, 0).`  
1. Update `code_week4.py` so it calls `simulate_turbie()` on
   `wind_12_ms_TI_0.1.txt`.  
1. Re-run this week's tests. Do any more tests pass?  

### PART V: Save response to file

1. Run the Week 4 tests using `pytest` and see what is failing.  
1. In `codecamp/__init__.py`, make a function called `save_resp` that:  
    * Takes as inputs `t`, `u`, `xb` and `xt` (each 1D numpy arrays)
      and `path_save` (string/pathlib.Path).  
    * Saves the simulation results to txt file.
   * `numpy.savetxt` can be used with `delimiter='\t'` and 
     `fmt='%.3f'` to get a nice file. You should also pass in a header string 
      that explains the columns.
1. Add code to `code_week4.py` that saves your simulated results to a
file in a new subfolder called `resp/` with a filename `test_resp.txt`.   
    * Side quest: If you call `git status`, does it "see" the file? 
    Why/why not? (Hint: look at the `.gitignore`.)
    If you want the file to be added to your repo, check out the
    "force" option for `git add`.  
1. Compare the file you just simulated to `resp_12_ms_TI_0.1.txt`. Do they
   match?  
1. Re-run this week's tests. Do any more tests pass?  

### PART VI: (Extra credit) Plan of attack for codecamp submission

1. Read the project description and rubric for CodeCamp in Week 6 subfolder.  
1. DO NOT WRITE ANY CODE THIS WEEK.  
    * E.g., meet with no laptops at a whiteboard.  
1. Design with your team an outline for the code you want to write.  
    * E.g., make a sketch, a list of steps, description of new functions and
    in which files they will be placed, etc.  
    * Be sure to consider the project constraints!  

### PART VII: (Extra credit) Go through CodeCamp lecture videos
If you want to know more behind the methods, if you have problems understand
the previous parts, or if you can find time, please go through the relevant
parts of the Day 3 lectures (there are different chapters you can navigate):
* [CodeCamp Aug 2022 Day 3 (Part A)](https://panopto.dtu.dk/Panopto/Pages/Viewer.aspx?id=8f0f69e4-c584-4314-a4e3-b10f00e67a1e) 
* [CodeCamp Aug 2022 Day 3 (Part B)](https://panopto.dtu.dk/Panopto/Pages/Viewer.aspx?id=4af05508-7fb4-49bd-b4f8-b10f00e67a19)
* [CodeCamp Aug 2022 Day 3 (Part C)](https://panopto.dtu.dk/Panopto/Pages/Viewer.aspx?id=84b1aa75-f9ec-4d05-aeb7-b10f00e67a1e)
   

### Additional materials

1. McConnell, Steve. "[Why you should use routines... routinely.](https://gitlab.windenergy.dtu.dk/spp/spp-course-material/-/blob/main/week3_turbie_part2/%5BJ%5D%201998%20Why%20you%20should%20use%20routines...%20routinely.pdf?ref_type=heads)" IEEE Software 15.4 (1998): 96-95.  
    * In this subfolder!  
1. Tobin A. Driscoll and Richard J. Braun. "[Basics of IVPs](https://fncbook.github.io/fnc/ivp/basics.html)" in: *Fundamentals of Numerical Computation*. 

