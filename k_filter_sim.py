import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter

# init the vars

ball_init_distance = 20 #starting distance (in meters)
ball_final_distance = 0 #ending distance (in meters)
ball_init_vel = 0
ball_state = np.array([ball_init_distance,ball_init_vel])

#data to be plotted
true_pos = np.array([])
home_made_pos=np.array([])
kalman_pos =np.array([])

g = -9.81 #m/s^2
mass = 1.0 #mass of ball in kg
timeElapsed =0

f = KalmanFilter (dim_x=2, dim_z=1)
f.x = ball_state
#sim the stuff twin
while(pos > ball_final_distance):
    noise = np.random.normal(loc=0.0, scale=1.0, size=1000)
    vel =  vel + g*timeElapsed
    pos = pos + vel*timeElapsed

    f.predict()
    f.update(pos)
    timeElapsed = timeElapsed+.01
# postion vs time graph

plt.plot(true_pos, marker = 'o')
plt.plot(home_made_pos, marker = 'o')
plt.plot(kalman_pos, marker = 'o')

plt.show()
# def home_made_kalmanFilter():
    