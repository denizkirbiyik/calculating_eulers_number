import math
import decimal

iter = int(input("How many iterations of the convergent series do you want to compute? : "));
decimal.getcontext().prec = 1+(int(input("How many digits would you like to compute for each calculation : ")));
i = 0; e = 0;

while (i<iter):
    e = e + 1/decimal.Decimal(math.factorial(i));
    i = i + 1;

print(e);