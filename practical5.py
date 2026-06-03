import math
# Input values
a = int(input("Enter value of a: "))
p = int(input("Enter a prime number p: "))
# Check gcd condition
if math.gcd(a, p) != 1:
    print("Fermat's Little Theorem is not applicable as gcd(a, p) ≠ 1")
else:
    result = pow(a, p - 1, p)
    print(f"{a}^({p-1}) mod {p} = {result}")
    
    if result == 1:
        print("Fermat's Little Theorem is verified")
    else:
        print("Fermat's Little Theorem is not verified")