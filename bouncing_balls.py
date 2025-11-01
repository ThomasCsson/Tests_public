import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots()
ax.set_xlim(0, 10)  
ax.set_ylim(0, 10)  

ball_radius = 0.25
ball, = ax.plot([], [], 'o', markersize=ball_radius * 40)
ball2_radius = 0.25
ball2, = ax.plot([], [], 'o', markersize=ball2_radius * 40)

x_pos = 5 
x_vel = 5
y_pos = 10  
y_vel = -5  

x2_pos = 1  
x2_vel = 3
y2_pos = 15 
y2_vel = 0 

gravity = -9.81  
time_step = 0.05  
elasticity = 1  

def init():
    ball.set_data([], [])
    ball2.set_data([], [])
    return ball, ball2

def update(frame):
    global y_pos, y_vel, x_pos, x_vel, y2_pos, y2_vel, x2_pos, x2_vel
    randomness = 0.001 * random.randint(900,1100)
    
    y_vel += gravity * time_step
    y_pos += y_vel * time_step
    x_pos += x_vel * time_step
    
    y2_vel += gravity * time_step
    y2_pos += y2_vel * time_step
    x2_pos += x2_vel * time_step

    if y_pos  < 0:
        y_pos = ball_radius 
        y_vel = -y_vel * elasticity * randomness  
    if y_pos > 10:
        y_pos = 10-ball_radius
        y_vel = -y_vel * elasticity

    if x_pos > 10:
        x_pos = 10 - ball_radius
        x_vel = -x_vel* elasticity
    if x_pos < 0:
        x_pos = ball_radius
        x_vel = -x_vel * elasticity



    if y2_pos  < 0:
        y2_pos = ball2_radius 
        y2_vel = -y2_vel * elasticity * randomness  
    if y2_pos > 10:
        y2_pos = 10-ball2_radius
        y2_vel = -y2_vel * elasticity

    if x2_pos > 10:
        x2_pos = 10 - ball2_radius
        x2_vel = -x2_vel* elasticity
    if x2_pos < 0:
        x2_pos = ball2_radius
        x2_vel = -x2_vel * elasticity

    ball.set_data(x_pos, y_pos)
    ball2.set_data(x2_pos, y2_pos)

    return ball, ball2

ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True, interval=20)

plt.show()