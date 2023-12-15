# CDC-Project


## Background

### Many infectious diseases like Covid-19 can be modeled using an SIR (susceptible, infected, recovered) model or one of its variants. The models in this project are typically a set of 3 or 4 ODEs that must be solved numerically.

## Goal

### Create a front-end GUI where users can interact with parameter values for the chosen SIR model. The ODE will be solved numerically on the back-end from these paramter values. From the solution, a graph is output for the user to gain knowledge from regarding the disease.


## Methodology

### First, I have been exploring the creation of a GUI with tkinter. I will explore a few other packages including pygame (based off Harrison's recommendation). Tkinter will require integration with numpy to solve the ODEs as well as MatPlotLib to create the graphical output.

### From tkinter, I have been able to create a window with sliders that can be moved for three variables, a calculate button that leads to a separate window, and a quit option. Ideally, I would like an entry box that is linked to the slider so someone coudl choose which to use since sliders can be difficult to operate at times. If using this package for the entire goal, I would need to store the slider values, solve the ODEs based off the values, and output a graph from the solutions. Finally, I could make the UI more appealing to the user. I believe the idea of linking the slider and the entry box is beyond the capabilities of this package or perhaps just beyond my knowledge at the moment. I would like to build something nice from tkinter to compare to another GUI. I believe I will have enough time to compare.

### From some exploration, PyQTGraph or PyQT may be the way to go with another framework to create the GUI.

### I have also seen plenty of publications that use 4th order Runge Kutta method.

### My idea as of 7/5/23 is to create this for basic SIR model then, if time allows, extend to SEIR/SIRS/with deaths model as this seems a logical way to tackle this with the given time. 

## Questions

### Who specifically within the term "healthcare professionals" will be utilizing this? When would they turn to this product? What exactly would they hope to gain from this product? Where would they gain access to this product? 

## Next Steps

* ~~Lit review on SIR/SEIR/SIRS for flu/Covid-19 modeling.~~
* Investigate tkinter further 
* ~~Once I've decided on SIR/SEIR/SIRS find best numerical method to solve to reduce error~~
* ~~Compile a list of pubs that use Runge Kutta method/any other method to solve SIR model~~
* ~~Write a small script to solve simple SIR model with given parameters with 4th order Runge Kutta method~~
* Find a baseline example to check Runge-Kutta code
* Explore PyQTGraph
