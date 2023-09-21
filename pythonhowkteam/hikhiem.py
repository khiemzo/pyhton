

from decimal  import Decimal, getcontext
from fractions import Fraction
getcontext().prec = 35
print(Decimal(11)/ Decimal(3))
