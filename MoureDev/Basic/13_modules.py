import modules

modules.my_sum(5, 5, 5)
modules.printName("Rojas", "Valladares", "Pedro", "Alberto")

from modules import my_sum, printName

my_sum(23, 16, 16)
printName("RV", "PA")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as pi_value
print(pi_value)