# How to cook the perfect egg 
import math 
import numpy as np 

import matplotlib as mpl 
import matplotlib.pyplot as plt

def celsius_to_kelvin(T):
    return T + 273.15

def cooking_time(M,c,rho,K,T0,Tw,Ty):
    T0 = celsius_to_kelvin(T0)
    Tw = celsius_to_kelvin(Tw)   
    Ty = celsius_to_kelvin(Ty)
    f1 = (math.pow(M,2./3)*c*math.pow(rho,1./3))/(K*(math.pi**2)*math.pow((4*math.pi)/3,2./3));
    f2 = math.log(0.76 * ((T0-Tw)/(Ty-Tw)));
    t = f1*f2;
    return t 
    # print('The time needed for the center of the yolk to reach the temperature T_y = %g C is t = %g s' %(Ty-273.15,t))

M_small = 47;   # grams 
M_large = 67;   # grams 
c = 3.7;        # J g-1 K-1 - specific heat capacity 
rho = 1.038;    # g cm-3 - density of the egg 
K = 5.4*0.001;  # W cm-1 K-1 - thermal conductivity 

# T_0_fridge = 4; # Celsius - temperature of an egg taken from the fridge
# T_0_room = 20;  # Celsius - temperature of an egg in a room 

T_w = 100;      # Celsius - temperature of boiling water
T_y = 70;       # Celsius - requested temperature 

init_temp = []
cooking_time_large_egg = []
cooking_time_small_egg = []

kk = 2; 
while kk <= 25:
    init_temp.append(round(kk,2));
    cooking_time_large_egg.append(cooking_time(M_large,c,rho,K,kk,T_w,T_y))
    cooking_time_small_egg.append(cooking_time(M_small,c,rho,K,kk,T_w,T_y))
    kk += 0.05; 

np_init_temp = np.array(init_temp)
np_cooking_time_large_egg = np.array(cooking_time_large_egg)
np_cooking_time_small_egg = np.array(cooking_time_small_egg)

plt.plot(np_init_temp, np_cooking_time_large_egg, color = 'blue', linewidth=3)
plt.plot(np_init_temp, np_cooking_time_small_egg, color = 'red', linewidth=3)
plt.title('Time for the yolk to reach 70°C')
plt.xlabel('T_0 [°C]')
plt.ylabel('Time Needed [s]')
plt.grid()

plt.xlim([0, 27])
plt.savefig('Yolk.png', dpi=300)

plt.show()