import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean
mean = sum(speed) / len(speed)

mean2 = numpy.mean(speed)

# print(mean, mean2)


# Median

speed.sort()
median = speed[(round(len(speed) / 2))]

median2 = numpy.median(speed)

print(median, median2)

# mode
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = stats.mode(speed)

print(x)
