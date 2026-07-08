import math

def calculate_gravitational_force(m1, m2, r):
    """Calculates the gravitational force between two objects."""
    G = 6.67430e-11  # Universal gravitational constant (N·m²/kg²)
    force = G * (m1 * m2) / (r ** 2)
    return force


def main():
    print("Gravitational Force Calculator")

    try:
        mass1 = float(input("Enter the mass of the first object (kg): "))
        mass2 = float(input("Enter the mass of the second object (kg): "))
        distance = float(input("Enter the distance between the objects (m): "))

        if mass1 <= 0 or mass2 <= 0 or distance <= 0:
            print("Masses and distance must be positive values.")
            return

        force = calculate_gravitational_force(mass1, mass2, distance)
        print(f"The gravitational force between the objects is {force:.2e} N.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()