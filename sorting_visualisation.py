import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Bubble sort generator for visualization
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data[:]  # return a copy of the list for each step

# Generate random dataset
size = 100
data = [random.randint(1, 50) for _ in range(size)]

# Create the figure and initial bar chart
fig, ax = plt.subplots()
bars = ax.bar(range(len(data)), data, color="skyblue")
ax.set_title("Bubble Sort Visualization")

def update(frame):
    for bar, val in zip(bars, frame):
        bar.set_height(val)

# Run animation
ani = animation.FuncAnimation(
    fig, update, frames=bubble_sort(data), interval=1, repeat=False
)

plt.show()
