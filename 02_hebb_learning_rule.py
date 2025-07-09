"""
Practical 2: Hebb's Learning Rule
---------------------------------

Aim:
To write a program to implement Hebb’s Rule.

Concept:
- Hebb’s rule is a learning algorithm used to update the weights of a neuron.
- It states: "When an input and output neuron activate together, the connection between them is strengthened."
- Weight update formula: w_new = w_old + x * y
  where:
    x = input vector
    y = target output
    w = weight vector

"""

import numpy as np

# Step 1: Define two input vectors (binary patterns)
x1 = np.array([1, 1, 1, -1, 1, -1, 1, 1, 1])
x2 = np.array([1, 1, 1, 1, -1, 1, 1, 1, 1])

# Step 2: Define target outputs for both inputs
y = np.array([1, -1])  # y[0] for x1, y[1] for x2

# Step 3: Initialize weight and bias
wt_old = np.zeros((9,))  # weights initialized to zero
wt_new = np.zeros((9,))  # second array to store updated weights
b = 0  # bias initialized to 0

# ---------------------------------------------
# First input update
# ---------------------------------------------
print("First input with target = 1")
for i in range(9):
    # Apply Hebb's rule: w_new = w_old + x * y
    wt_old[i] = wt_old[i] + x1[i] * y[0]

# Update the new weights and bias
wt_new = wt_old.copy()
b = b + y[0]

# Display updated values
print("Old weight =", wt_old.astype(int))
print("Bias value =", b)
print("\n")

# ---------------------------------------------
# Second input update
# ---------------------------------------------
print("Second input with target = -1")
for i in range(9):
    # Apply Hebb's rule again using x2 and y[1]
    wt_new[i] = wt_old[i] + x2[i] * y[1]

b = b + y[1]

# Display updated weight and bias
print("New weight =", wt_new.astype(int))
print("Bias value =", b)
