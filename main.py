import random

def run():
    random_number = random.randint(1, 10)
    while True:
        try:
            chosen_number = int(input("Elige un número del 1 al 10: "))
            if chosen_number < 1 or chosen_number > 10:
                print("El número debe estar entre 1 y 10. Intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Ingresa un número válido.")
    
    while chosen_number != random_number:
        if chosen_number < random_number:
            print("Busca un número más grande.")
        else:
            print("Busca un número más pequeño.")
        chosen_number = int(input("Elige otro número: "))
    
    print("¡Ganaste!")

if __name__ == "__main__":
    run()