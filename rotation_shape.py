import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from math import sqrt

# Show coordinate system
def drawPoints(points, color = "red"):
    for point in points:
        plt.scatter(point[0], point[1], color=color)



def calculate_new_point(points, rotate_angle):
    new_points = []

    for point in points:
        new_x = point[0]*np.cos(np.deg2rad(rotate_angle)) - point[1]*np.sin(np.deg2rad(rotate_angle))
        new_y = point[0]*np.sin(np.deg2rad(rotate_angle)) + point[1]*np.cos(np.deg2rad(rotate_angle))
        new_points.append([new_x, new_y])

    return new_points


# Points
"""
points =[
    [-3, 2],
    [0, 5],
    [3, 2],
    [3, -2],
    [-3, -2]
]"""

points = [
    [2,5],
    [4,0],
    [2,-5],
    [-2,-5],
    [-4,0],
    [-2,5]
]


# Create window and axis points
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)


# graphic enlargement
plt.xlim(-10, 10) 
plt.ylim(-10, 10)

# Origin
ox = np.mean([point[0] for point in points])
oy = np.mean([point[1] for point in points])

drawPoints([[ox, oy]])


line_list = []
for i in range(len(points)):
    
    if i != len(points)-1:
        point, = plt.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]], 'b-')
        line_list.append(point)
    else:
        point, = plt.plot([points[i][0], points[0][0]], [points[i][1], points[0][1]], 'g-')
        line_list.append(point)



# Create Slider
ax_slider_x = plt.axes([0.25, 0.1, 0.65, 0.03])
rotate_slider = Slider(ax_slider_x, 'Rotate Angle', 0, 360)

# Update Slider
def update(rotate_angle):
    
    new_points = calculate_new_point(points, rotate_angle)

    for i in range(len(line_list)):
        if i != len(line_list)-1:
            line_list[i].set_xdata([new_points[i][0], new_points[i+1][0]])
            line_list[i].set_ydata([new_points[i][1], new_points[i+1][1]])
        else:
            line_list[i].set_xdata([new_points[i][0], new_points[0][0]])
            line_list[i].set_ydata([new_points[i][1], new_points[0][1]])

    fig.canvas.draw_idle()


# Link slider changes
rotate_slider.on_changed(update)

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Rotating')

plt.show()