import math

def area_calculator():
    while True:
        print("=" * 18)
        print("Area Calculator 📐")
        print("=" * 18)
        print("\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n")

        choice = input("Which shape: ")

        if choice == "1":
            base = float(input("\nBase: "))
            height = float(input("Height: "))
            area = 0.5 * base * height
            print(f"\nThe area is {area}\n")

        elif choice == "2":
            length = float(input("\nLength: "))
            width = float(input("Width: "))
            area = length * width
            print(f"\nThe area is {area}\n")

        elif choice == "3":
            side = float(input("\nSide: "))
            area = side * side
            print(f"\nThe area is {area}\n")

        elif choice == "4":
            radius = float(input("\nRadius: "))
            area = math.pi * radius ** 2
            print(f"\nThe area is {area:.2f}\n")

        elif choice == "5":
            print("\nGoodbye! 👋")
            break

        else:
            print("\nInvalid choice, try again!\n")



