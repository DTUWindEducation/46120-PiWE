# PiWE Week 9: Classes, inheritance and OOP

Office hours, slides, recordings:  
 * Office hours: Monday 13.00 - 14.30 and Tuesday 15.30 - 17.00 on Zoom.
 * Slides: In this subfolder  
 * Recording: on Learn

## Overview

Object Oriented Programming (OOP) is a programming paradigm that organizes code
using classes/objects to bundle data (attributes) and behaviors (methods) into 
self-contained units, promoting modular, reusable, and maintainable code.

Classes are blueprints for creating objects. They define:

* **Attributes** (e.g., a `Car` class might have color and speed).

* **Methods** (e.g., `drive()` or `break()`).

A class acts as a template, while objects are specific instances.

OOP is based on the principles of abstraction, encapsulation, inheritance, and 
polymorphism:

* **Abstraction** allows us to focus on essential features of an object and 
hide irrelevant details.

* **Encapsulation** helps in keeping the data and methods together and secure 
from unauthorized access by external code.

* **Inheritance** allows creating new classes based on existing ones, 
inheriting their properties and methods.

* **Polymorphism** means that objects of different classes can be treated as if
they are of the same class, making the code more flexible and reusable.


## Reminder

Check Week 8 for details, and rememeber the following deadline:
* **Due time of the final project**: 23:59 on Sunday, May 4th, 2025.
* **Due time of Custom Project approval**: 23:59 on Wednesday, April 9th, 2025.

## Homework due next week

### Homework 0: Write wind turbine classes
Write a `GeneralWindTurbine` class and a `WindTurbine` class that inherits the 
`GeneralWindTurbine` class. They should encapsulate data that describes the 
turbine characteristics and provide function to predict power output of the 
turbine under a given wind speed.

The following tasks need to be done:
1. Write a `GeneralWindTurbine` class that can be initialized by:
    * rotor_diameter [m]
    * hub_height [m]
    * rated_power [kW]
    * v_in [m/s]
    * v_rated [m/s] 
    * v_out [m/s]
    * name, optional (default set as `None`) 
    
    where v_in < v_rated < v_out are the cut_in, rated and cut_out wind speed, 
    and has the function `get_power()` that return power output P at wind speed 
    v using following rules:
    * if v < v_in or v > v_out, P = 0
    * if v_in <= v < v_rated,  P = rated_power*(v/v_rated)**3
    * if v_rated <= v <= v_out, P = rated_power


2. Write a `WindTurbine` class inherits from `GeneralWindTurbine` class, which
should have an extra attribute: `power_curve_data` which is assumed to be an 
n by 2 `numpy` array defines the power curve, i.e., first column defines wind
speed [m/s] and second column defines power [kW].

    Overide the `get_power(v)` function using the power curve data based on interpolation (e.g., using `numpy.interp`).

3. Initialize two objects of the two classes using the data of LEANWIND_8MW_164_RWT, which can be access at:
https://nrel.github.io/turbine-models/LEANWIND_8MW_164_RWT.html 

    Its power curve data can be obtained at:
https://github.com/NREL/turbine-models/blob/main/turbine_models/data/Offshore/LEANWIND_Reference_8MW_164.csv

4. Plot out and compare the power curves of these wind turbine objects and see 
how different they are.

5. (Optional): vectorize the `get_power` function in both classes, make sure 
they can take numpy array of any shape.

Note: if you need some background knowledge on wind turbine power curve, you 
may check: https://theroundup.org/wind-turbine-power-curve/ 


### Homework 1: 
1. Design a class for your final project that has at least:
    * one attribute that relates to the input data (those inside `inputs` if you 
 are working on one of the pre-defined final projects).
    * one method that is useful for your final project.
2. Write your code (the code for the class in `inputs` and script that create
an object of the class and run the method in `examples`) and push to GitHub. 
Remember to use branch and PR.
3. Add proper docstring and comments for all the code. If you can, also write
the related tests.
4. Think about how you may design multiple classes and how they should interact
with each other for your final project. 

### Homework Optional: 
#### Restructure Codecamp with OOP
The code you have written in the Codecamp project is current organized in 
module, i.e., different functions are separate from each other and may lie in 
different files.

Considering the OOP (object-oriented programming) principle you have learned
this week, it may seem like a better idea to encapsulate the relevant data
and function for a Turbie in a class.

The `Turbie` class you write should be able to initialize a given turbine 
that has a given set of parameters (like rotor diameter, `M`, `C`, `K`, etc.). 
Then the intialized object should provide esstential functions like 
`simulate_turbie` that can simulate the homogenous/forced response for a given
time series of wind speed. Note that in this case, when the `simulate_turbie`
function is called from the Turbie object, it should only needs input that 
defines the wind speed time series.

When turning your Turbie code into a class, you may like to think about the 
following:

* What parameters should be included as attributes of the `Turbie` class?
* What parameters should be provided as inputs when calling the associated
functions?
* What functions should be included in the `Turbie` class? How should they be
adapted?
* Previously, a mean wind speed is used to find a single value of `Ct` and used
in the response simulation. Consider how to use a varying `Ct`, i.e., different
values corresponding to different wind speeds, in the simulation. Note that 
a `get_Ct` function can be defined for the `Turbie` class, like the 
`get_power` function we wrote in Homework I.

After this process, you can reflect on: what are the differences between class
based `Turbie` and module/functions based `Turbie`, what advantages (and/or 
disadvantages) OOP has provided?

#### Design a base class `DynamicalSystem`
Considering that the 2 DOF model of Turbie we have developed in Codecamp is a 
special case of a multiple DOF dynamical system characterized by the `M`, `C`,
 `K` matrices, we can define a general `DynamicalSystem` that holds the `M`, 
 `C`, `K` matrices and providing functions to solve the homogeneous response 
 for a given list of time steps and solve the forced response under a given 
 timeseries of forces, by solving the associated IVP (initial value problem).

 Your task will be:
 * Write a base class `DynamicalSystem` that can simulated the homogeneous 
 response and forced response.
 * Adapt your `Turbie` class to inherit from the base class.
 * Think about another class that can inherit the base class that define 
 another dynamical system, like [pendulum](https://en.wikipedia.org/wiki/Pendulum_(mechanics)).


 ### Note about homework
 You should complete Homework 0 individually, you may peer-review each other's
 code in your final project group.

 You should complete Homework 1 collaboratively with your final project group.
 
 Homework optional can be done individually, in your original Codecamp group, 
 or in your final project group.
