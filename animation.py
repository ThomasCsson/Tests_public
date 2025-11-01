import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort(arr, bars, ax):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            bars[j].set_color('red')
            bars[j + 1].set_color('red')

            yield arr  
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            bars[j].set_color('blue')
            bars[j + 1].set_color('blue')

def update_plot(arr, bars):
    for bar, val in zip(bars, arr):
        bar.set_height(val)

def visualize_sorting(arr):
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")

    bars = ax.bar(range(len(arr)), arr, color='blue')

    ani = animation.FuncAnimation(
        fig, update_plot, fargs=(bars,),
        frames=bubble_sort(arr, bars, ax),
        repeat=False, blit=False, interval=50
    )

    plt.show()

if __name__ == "__main__":
    arr = random.sample(range(1, 50), 10)
    visualize_sorting(arr)
