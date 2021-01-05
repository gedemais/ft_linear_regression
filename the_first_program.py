from sys import stderr, stdout
import os

keep = True

while keep:
    keep = False
    try:
        s = input("Enter a mileage (or q to quit)-> ")

        if s == "q":
            print("Goodbye !")
            exit(0)

        mileage = int(s)

    except ValueError:

        print("This is not a correct mileage !", file=stderr)
        keep = True

theta_0 = os.getenv("THETA_ZERO")
theta_1 = os.getenv("THETA_ONE")

which = "THETA_ZERO" if not theta_0 else "THETA_ONE"

if not theta_0 or not theta_1:
    print(which + " environnement variable not found !", file=stderr)
    exit(1)

try:
    t0 = float(theta_0)
    t1 = float(theta_1)
except:
    print("THETA_ZERO/THETA_ONE environnement variables content is not valid !", file=stderr)
    exit(1)

result = t0 + (t1 * mileage)

print(str(result) + '€')
