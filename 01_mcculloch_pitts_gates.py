"""
Practical 1: McCulloch-Pitts Neuron – Logic Gates (AND, OR, NOT)
----------------------------------------------------------------

Aim:
To implement AND, OR, and NOT gates using the McCulloch-Pitts neuron model.

Concept:
- The McCulloch-Pitts neuron is a binary threshold unit.
- It computes a weighted sum of binary inputs.
- If the sum is greater than or equal to a threshold (t), the neuron fires (output = 1).
- Otherwise, it does not fire (output = 0).
- Used to simulate basic logic gates by setting proper weights and thresholds.

"""

# ------------------------------------------------------------
# AND, OR, and NOT gates using McCulloch-Pitts model in one script
# ------------------------------------------------------------

# ----------------------------
# AND Gate
# ----------------------------

# Step 1: Define input combinations for 2-input logic gates
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

# Step 2: Define weights for both inputs (same in all cases)
w1 = [1, 1, 1, 1]
w2 = [1, 1, 1, 1]

# Step 3: Set threshold value for AND gate (sum must be ≥ 2)
threshold_and = 2

print("AND Gate Truth Table")
print("x1 x2 w1 w2 sum output")
for i in range(len(x1)):
    # Weighted sum = x1*w1 + x2*w2
    total = x1[i] * w1[i] + x2[i] * w2[i]

    # Output is 1 if total >= threshold, else 0
    output = 1 if total >= threshold_and else 0

    print(x1[i], x2[i], w1[i], w2[i], total, output)

print("\n")

# ----------------------------
# OR Gate
# ----------------------------

# Step 4: Set threshold for OR gate (only one input is enough to fire neuron)
threshold_or = 1

print("OR Gate Truth Table")
print("x1 x2 w1 w2 sum output")
for i in range(len(x1)):
    total = x1[i] * w1[i] + x2[i] * w2[i]
    output = 1 if total >= threshold_or else 0
    print(x1[i], x2[i], w1[i], w2[i], total, output)

print("\n")

# ----------------------------
# NOT Gate
# ----------------------------

# Step 5: Define single input for NOT gate
x = [0, 1]

# Step 6: Use negative weights to invert output
w = [-1, -1]

# Step 7: Set threshold = 0
threshold_not = 0

print("NOT Gate Truth Table")
print("x w sum output")
for i in range(len(x)):
    total = x[i] * w[i]
    output = 1 if total >= threshold_not else 0
    print(x[i], w[i], total, output)

# ----------------------------
# End of Practical 1
# ----------------------------
