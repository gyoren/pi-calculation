from decimal import Decimal, getcontext
from time import process_time
from math import factorial
import argparse

argument_parser = argparse.ArgumentParser(description="Calculate Pi using the Chudnovsky algorithm.")
argument_parser.add_argument("precision", metavar="precision", type=int)
argument_parser.add_argument("iterations", metavar="iterations", type=int)

getcontext().prec = argument_parser.parse_args().precision

s = process_time()

print(Decimal(-1)
      /Decimal(sum(Decimal(factorial(6*k)*(545140134*k+13591409))
        /Decimal(factorial(3*k)*(factorial(k)**3)*(-262537412640768000**k))
            for k in range(argument_parser.parse_args().iterations))
      /Decimal(426880*Decimal(10005).sqrt())))

e = process_time()
print("\a", end="")
print(f"Process time: {round(e-s, 4)} secs")