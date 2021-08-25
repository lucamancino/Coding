# Trajectory of a ball using the parametric form of the equation of motion 
import math 

g = 9.81;     # m/s^2 
v0 = 15;      # km/h 
theta = 60;   # degrees
x = 0.5;      # m
y0 = 1;       # m 

v0 = v0*1000/3600;            # Conversion from km/h to m/s 
theta = math.radians(theta);  # Conversion from degrees to radians

y_at_x = y0 + x*math.tan(theta) - (g/(2*v0**2))*(x**2/math.cos(theta)**2)
print('The height of the ball is %.1f m' %y_at_x)