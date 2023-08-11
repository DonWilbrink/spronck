from math import sqrt

print("De stelling van pythagoras: c*c = a*a + b*b")
a=float(input("Geef a in: "))
b=float(input("Geef b in: "))

c=sqrt(a*a+b*b)

print("De schuine zijde c is {:.2f} lang.".format(c))
