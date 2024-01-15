from statistics import mean
def better_than_average(class_points, your_points):
    return mean(class_points) < your_points
