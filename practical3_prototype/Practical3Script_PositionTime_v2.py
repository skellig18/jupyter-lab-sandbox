#### -------------- IMPORT BLOCK ------------------ ####
# In this section we import important Python packages. #

import numpy as np # NumPy, a numerical Python package, is used for representing numerical data
import matplotlib.pyplot as plt # Matplotlib, a Python plotting package, is used for plotting data. 

### -------(!!!) INPUT DATA (!!!) ----------- ###
### You may change these variables as needed. ###

# The input data section takes two forms: position or acceleration,
# depending on your experimental design. Your TA should have let you
# know which file to be using.

# POSITION_FILENAME:
#
# The name of the file containing your position-time data.
# 
# Your file should be a comma-separated value file
# with time in the first column and position in the second. 
#
# The units of position should be meters. 
POSITION_FILENAME="time-position.csv"  

#### ------------- DATA LOAD BLOCK ------------------- ####
# In this section we import CSV files from your Practical #
# and load them into NumPy arrays.                        #

# Use NumPy to load the position data from the CSV file
position_data = np.loadtxt(POSITION_FILENAME, delimiter=',', comments='#')

# Separate the data into position and time 
time=  position_data[:,0] # time in (s)
position = position_data[:,1] # position in m

# Calculate the velocity based on position

velocity = np.gradient(position, time)

# Calculate the acceleration based on position 

acceleration = np.gradient(velocity, time)


#### ------------- FITTING BLOCK ------------------- ####
# In this section we average the data to get a constant #
# fit to the data.                                      #

# Calculate the average velocity. 
avg_velocity = np.mean(velocity)
fit_velocity = np.ones(np.shape(velocity))*avg_velocity

# Calculate the spread in this average velocity. 
uncertainty_velocity = np.std(velocity)/np.abs(avg_velocity)

# Calculate the average acceleration.
avg_acceleration= np.mean(acceleration)
fit_acceleration = np.ones(np.shape(acceleration))*avg_acceleration

# Calculate the spread in the average acceleration. 
uncertainty_acceleration= np.std(acceleration)/np.abs(avg_acceleration)

#### ---------- VELOCITY PLOTTING BLOCK ------------- ####
# In this section we plot the data from your experiment. #
# Here we are plotting force/mass next to acceleration.  #

plt.plot(time, velocity, 'b.', label="Velocity (m/s)")
plt.plot(time, fit_velocity, 'r-', label= "Average Velocity (m/s)")
plt.title("Practical 3 Velocity Data")
plt.legend()
plt.savefig("Velocity_Data_Practical3.png")
plt.show()
plt.clf()

#### ---------- ACCELERATION PLOTTING BLOCK ------------- ####
# In this section we plot the data from your experiment. #
# Here we are plotting force/mass next to acceleration.  #

plt.plot(time, acceleration, 'b.', label="Acceleration (m/s**2)")
plt.plot(time, fit_acceleration, 'r-', label= "Average Acceleration (m/s**2)")
plt.title("Practical 3 Acceleration Data")
plt.legend()
plt.savefig("Acceleration_Data_Practical3.png")
plt.show()
plt.clf()

#### ------------- ACCELERATION RESIDUALS BLOCK -------------------- ####
# In this section we compare the data from your experiment #
# to determine more precisely if the hypothesis is true.   #

plt.plot(time, acceleration - fit_acceleration, 'r.', label="Residuals (m/s**2)")
plt.text(0,0, "Percent Uncertainty in fit: {:.2f}".format(uncertainty_acceleration*100))
plt.title("Practical 3 Acceleration Residuals")
plt.legend()
plt.savefig("Practical3_AccelerationResiduals")
plt.show()

#### ------------- VELOCITY RESIDUALS BLOCK -------------------- ####
# In this section we compare the data from your experiment #
# to determine more precisely if the hypothesis is true.   #

plt.plot(time, velocity - fit_velocity, 'r.', label="Residuals (m/s**2)")
plt.text(0,0, "Percent Uncertainty in fit: {:.2f}".format(uncertainty_velocity*100))
plt.title("Practical 3 Velocity Residuals")
plt.legend()
plt.savefig("Practical3_VelocityResiduals")
plt.show()
