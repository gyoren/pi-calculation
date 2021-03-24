from decimal import Decimal, getcontext
from time import process_time
import argparse

argument_parser = argparse.ArgumentParser(description="Calculate Pi using BBP.")
argument_parser.add_argument("precision", metavar="precision", type=int)
argument_parser.add_argument("iterations", metavar="iterations", type=int)

getcontext().prec = argument_parser.parse_args().precision

s = process_time()

print(sum(1/Decimal(16)**k * 
          (Decimal(4)/(8*k+1) - 
           Decimal(2)/(8*k+4) - 
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(argument_parser.parse_args().iterations)))

e = process_time()
print("\a", end="")
print(f"Process time: {round(e-s, 4)} secs")