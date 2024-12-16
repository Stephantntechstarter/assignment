def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y !=0:
        return x / y
    else
        return "Division durch null ist nicht erlaubt"

def calculator():
    operation = input("Willst du addieren, subtrahieren, multiplizieren oder dividieren?").lower()

try:
    x = float(input("Erste Zahl bitte: "))
    y = float(input("Zeite Zahl bitte: "))
except ValueError:
    print("Bitte gültige Zahlen verwenden.")
    return

if operation == "addieren":
    result = add(x, y)
elif operation == "subtrahieren":
    result = subtract(x, y)
elif operation == "multiplizieren":
    result = mult(x, y)
elif operation == "dividieren":
    result = div(x, y)
else:
    print("Passt was nicht. Schreibe addieren, subtrahieren, multiplizieren oder dividieren")
    return

print(f"Das Ergebnis des {operation} von {x} und {y} ist: {result}")

calculator()