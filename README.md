# Day-50-Gravitational-Force

Day 50/100 - Python Program to Find Gravitational Force Between the Two Object

# Calculate Gravitational Force

A program to calculate the physical force of gravity between two masses at a given distance using Newton's law of universal gravitation.

## 📝 Description

This program explores classical mechanics by calculating the gravitational force between two distinct objects. It utilizes Newton's famous formula:


$$F = G \frac{m_1 m_2}{r^2}$$


where $F$ is the force, $m_1$ and $m_2$ are the masses of the objects, $r$ is the distance between their centers, and $G$ is the gravitational constant ($6.67430 \times 10^{-11} \text{ N}\cdot\text{m}^2/\text{kg}^2$).

The script features a dedicated function `calculate_gravitational_force` to handle the core mathematics. It implements strict validation to ensure that masses and distances are strictly positive values, as negative mass or distance doesn't apply in this context. Finally, it uses Python's `try-except` structure to gracefully catch any non-numerical inputs, and utilizes scientific notation formatting (`:.2e`) in the print statement to clearly display extremely large or extremely small force values.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A floating-point number representing the mass of the first object (`mass1`) in kilograms.
* **Input 2:** A floating-point number representing the mass of the second object (`mass2`) in kilograms.
* **Input 3:** A floating-point number representing the distance between the objects (`distance`) in meters.

### Output:

* If valid: A formatted string stating: "The gravitational force between the objects is [force] N." using scientific notation.
* If invalid (zero or negative): "Masses and distance must be positive values."
* If invalid (non-numeric): "Invalid input. Please enter numeric values."

### Rules:

1. The program must accept three numerical inputs from the user.
2. Ensure inputs are successfully cast to `float` within a `try-except` block to catch `ValueError`.
3. Check if any of the three values are `<= 0`. If true, print the error message and terminate.
4. Calculate the force using the provided gravitational constant $G$ and the mathematical formula.
5. Print the resulting force formatted to two decimal places in scientific notation (`.2e`).

---

## 💡 Examples

### Example 1 (Standard Everyday Objects)

**Input:**

```
70
80
2

```

**Output:**

```
Gravitational Force Calculator
The gravitational force between the objects is 9.34e-08 N.

```

**Explanation:** Two average humans standing 2 meters apart exert a very tiny gravitational pull on each other ($9.34 \times 10^{-8}$ Newtons).

### Example 2 (Planetary Scale - Earth and Moon)

**Input:**

```
5.972e24
7.348e22
3.844e8

```

**Output:**

```
Gravitational Force Calculator
The gravitational force between the objects is 1.98e+20 N.

```

**Explanation:** The massive scale of celestial bodies results in an immense gravitational force holding them in orbit. Python naturally accepts scientific notation inputs (e.g., `5.972e24`) when casting to a float.

### Example 3 (Negative Value Handling)

**Input:**

```
100
100
-5

```

**Output:**

```
Gravitational Force Calculator
Masses and distance must be positive values.

```

**Explanation:** Distance cannot be negative in this formula. The initial conditional check safely intercepts this and halts the calculation.

### Example 4 (String Error Handling)

**Input:**

```
ten

```

**Output:**

```
Gravitational Force Calculator
Invalid input. Please enter numeric values.

```

**Explanation:** The word "ten" cannot be cast to a float, triggering a `ValueError` which is cleanly caught and handled by the program.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-50-Gravitational-Force.git
cd gravitational-force

```

2. **Run the program**:

```bash
python main.py

```

Enter the two masses (in kg) and the distance between them (in m) when prompted to discover the exact gravitational pull they exert on one another.

---

To help visualize how altering the mass or distance impacts the resulting gravitational force, I've generated an interactive simulator for you to explore below!
