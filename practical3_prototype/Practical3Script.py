#### -------------- IMPORT BLOCK ------------------ ####
# In this section we import important Python packages. #

import numpy as np # NumPy, a numerical Python package, is used for representing numerical data
import qexpy       # QExPy, an experimental Physics package for labs like you, was developed at 
                   # Queen's University. 

import qexpy.plotting as plt # Plotting module for QExPy


### -------(!!!) INPUT DATA (!!!) ----------- ###
### You may change these variables as needed. ###

# MASS:
#
# The mass of the object in your experiment. 
# 
# The units of the mass should be kg. 
MASS= 2.0 # kg

# FORCE_FILENAME:
#
# The name of the file containing your force data
# 
# Your file should be a comma-separated value file
# with time in the first column and force in the second. 
#
# The units of the force should be N (kg*m/s**2)
FORCE_FILENAME="time-force.csv"  


# ACCELERATION_FILENAME:
#
# The name of the file containing your acceleration data
# 
# Your file should be a comma-separated value file
# with time in the first column and acceleration in the second. 
#
# The units of the acceleration should be (m/s**2)
ACCELERATION_FILENAME="time-acceleration.csv"  


#### ------------- DATA LOAD BLOCK ------------------- ####
# In this section we import CSV files from your Practical #
# and pass them into QExpy's unit-labelled quantities.    #

# Use NumPy to load the force data from the CSV file
force_data = np.loadtxt(FORCE_FILENAME, delimiter=',', comments='#')

# Convert the data into QExpy Measurement Arrays
force_time=  qexpy.MeasurementArray(force_data[:,0], unit="s", name="Time (Force)")
force = qexpy.MeasurementArray(force_data[:,1], unit="N", name="Force")

# Use NumPy to load the force data from the CSV file
acceleration_data = np.loadtxt(ACCELERATION_FILENAME, delimiter=',', comments='#')

# Convert the data into QExpy Measurement Arrays
acceleration_time=  qexpy.MeasurementArray(acceleration_data[:,0], unit="s", name="Time (Acceleration)")
acceleration = qexpy.MeasurementArray(acceleration_data[:,1], unit="N", name="Acceleration")

# Convert the mass into a QExpy Measurement
mass = qexpy.Measurement(MASS, unit="kg", name="Mass")

#### ------------- PLOTTING BLOCK ------------------- ####
# In this section we plot the data from your experiment. #
# Here we are plotting force/mass next to acceleration.  #

force_div_mass = force/mass

figure= plt.plot(acceleration_time, acceleration, label="Acceleration (m/s**2)")
figure.plot(force_time, force_div_mass, label= "Force/mass (m/s**2)")

figure.title= "Practical 3 Data"
figure.legend()
figure.show()


#### ------------- RESIDUALS BLOCK -------------------- ####
# In this section we compare the data from your experiment #
# to determine more precisely if the hypothesis is true.   #

force_div_mass = force/mass

figure= plt.plot(acceleration_time, acceleration - force_div_mass, label="Residuals (m/s**2)")
figure.title= "Practical 3 Residuals"
figure.legend()
figure.show()
