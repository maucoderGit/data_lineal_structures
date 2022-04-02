from arrays import Array

def run():
    menu = Array(int(input("De qué tamaño será el array: ")))
    
    lower = int(input("Elige el mínimo valor de un número en el array: "))
    upper = int(input("Elige el máximo valor de un número en el array: "))

    menu.__randreplace__(lower, upper)
    print(menu)
    print(menu.__sumelements__())

if __name__ == "__main__":
    run()