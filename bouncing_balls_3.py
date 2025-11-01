import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ball_radius = 0.5
ball1, = ax.plot([], [], 'o', markersize=ball_radius * 20, color='b')
ball2, = ax.plot([], [], 'o', markersize=ball_radius * 20, color='r')


x_pos1 = 3
y_pos1 = 9
y_vel1 = 0

x_pos2 = 7
y_pos2 = 7
y_vel2 = 0

gravity = -9.8
time_step = 0.05
elasticity = 0.8

def init():
    ball1.set_data([], [])
    ball2.set_data([], [])
    return ball1, ball2

def update(frame):
    global y_pos1, y_vel1, y_pos2, y_vel2

    y_vel1 += gravity * time_step
    y_pos1 += y_vel1 * time_step

    if y_pos1 - ball_radius < 0:
        y_pos1 = ball_radius
        y_vel1 = -y_vel1 * elasticity

    y_vel2 += gravity * time_step
    y_pos2 += y_vel2 * time_step

    if y_pos2 - ball_radius < 0:
        y_pos2 = ball_radius
        y_vel2 = -y_vel2 * elasticity

    ball1.set_data(x_pos1, y_pos1)
    ball2.set_data(x_pos2, y_pos2)

    return ball1, ball2

# Animation function
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True, interval=20)

# Show animation
plt.show()