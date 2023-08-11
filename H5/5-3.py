num1=float(input("Geef getal 1 in: "))
num2=float(input("Geef getal 2 in: "))
num3=float(input("Geef getal 3 in: "))

print("De grootste is {:.2f}".format(max(num1, num2, num3)))
print("De kleinste is {:.2f}".format(min(num1, num2, num3)))
print("Het gemiddelde is {:.2f}".format((num1 + num2 + num3)/3))
