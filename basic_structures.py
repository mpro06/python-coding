#
# Copyright Marco Profenno 2023
#
# BSD License
#

import sys
import math
import numpy as np

# print(sys.argv[1])
# print(sys.argv[2])

opt = sys.argv[1]
person = sys.argv[2]


# Greeting Function
def greeting(greetingType):
    i = 0
    while i < 10:
        i = i + 1
        print(greetingType + ", " + person + "! (" + str(i) + ")")


# Main Code
if opt == '-h':
    greeting('Hello')
elif opt == '-g':
    greeting('Goodbye')

print("Math Time")
theNumber = 8.23324234
print(math.ceil(theNumber))
print(math.pi)

a = np.array([1, 2, 3, 4])
print(np.std(a))
