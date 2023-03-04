import math
import decimal

infinity = int(input("What number should be substituted for infinity? : "));
decimal.getcontext().prec = 1+(int(input("How many digits would you like to compute for each calculation : ")));

e = ((1+(1/decimal.Decimal(infinity)))**infinity);

print(e);