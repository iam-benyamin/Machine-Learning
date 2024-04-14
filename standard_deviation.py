import numpy

# Standard Deviation
speed = [86, 87, 88, 86, 87, 85, 86]
print(numpy.std(speed))

speed = [32, 111, 138, 28, 59, 77, 97]
print(numpy.std(speed))


# Variance
# To calculate the variance you have to do as follows:
var = numpy.var(speed)
print(var)
