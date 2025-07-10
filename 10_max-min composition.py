# Aim:
# Implement a program to perform max-min composition on any two fuzzy relations.

# Concept:
# In fuzzy set theory, the max-min composition is used to combine two fuzzy relations.
# Let R be a fuzzy relation from set A to B, and S be a fuzzy relation from set B to C.
# Then the max-min composition T of R and S is defined as:
#     T(x, z) = max(min(R(x, y), S(y, z))) for all y in B
# This finds the strongest (maximum) level of agreement via intermediary element y.


# Step 1: Create a fuzzy relation using Cartesian product
def cartesian_product_fuzzy_relation(A, B):
    """
    Create a fuzzy relation by Cartesian product of fuzzy sets A and B.
    Each pair (x, y) is assigned a membership value = min(A[x], B[y]).
    """
    relation = {}  # Dictionary to store the relation

    # Loop over all elements x in fuzzy set A
    for x in A:
        # Loop over all elements y in fuzzy set B
        for y in B:
            # Set the membership of (x, y) as the min of A[x] and B[y]
            relation[(x, y)] = min(A[x], B[y])

    return relation


# Step 2: Perform max-min composition of two fuzzy relations R and S
def max_min_composition(R, S):
    """
    Perform max-min composition of fuzzy relations R and S.
    Returns a new relation T such that:
    T(x, z) = max over y [min(R(x, y), S(y, z))]
    """
    T = {}  # Dictionary to store the result of composition

    # Extract all unique elements from R and S
    x_elements = set(x for x, y in R)  # Elements from first set
    y_elements = set(y for x, y in R)  # Intermediate elements
    z_elements = set(z for y, z in S)  # Elements from last set

    # Loop over all (x, z) combinations to compute T(x, z)
    for x in x_elements:
        for z in z_elements:
            min_values = []

            # Loop over y to compute min(R(x, y), S(y, z))
            for y in y_elements:
                if (x, y) in R and (y, z) in S:
                    min_val = min(R[(x, y)], S[(y, z)])
                    min_values.append(min_val)

            # Set the max of all min values as T(x, z)
            if min_values:
                T[(x, z)] = max(min_values)

    return T


# Step 3: Define fuzzy sets A, B, and C
A = {"x1": 0.7, "x2": 0.4, "x3": 0.9}  # Fuzzy Set A
B = {"y1": 0.6, "y2": 0.8, "y3": 0.5}  # Fuzzy Set B
C = {"z1": 0.5, "z2": 0.9, "z3": 0.3}  # Fuzzy Set C

# Step 4: Compute fuzzy relations R (A × B) and S (B × C)
R = cartesian_product_fuzzy_relation(A, B)
S = cartesian_product_fuzzy_relation(B, C)

# Step 5: Compute max-min composition of R and S
T = max_min_composition(R, S)

# Step 6: Print all fuzzy sets and their relations
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Fuzzy Set C:", C)

print("\nFuzzy Relation R (A × B):")
for (x, y), value in R.items():
    print(f"({x}, {y}): {value}")

print("\nFuzzy Relation S (B × C):")
for (y, z), value in S.items():
    print(f"({y}, {z}): {value}")

print("\nMax–Min Composition T (R ∘ S):")
for (x, z), value in T.items():
    print(f"({x}, {z}): {value}")
# Aim:
# Implement a program to perform max-min composition on any two fuzzy relations.

# Concept:
# In fuzzy set theory, the max-min composition is used to combine two fuzzy relations.
# Let R be a fuzzy relation from set A to B, and S be a fuzzy relation from set B to C.
# Then the max-min composition T of R and S is defined as:
#     T(x, z) = max(min(R(x, y), S(y, z))) for all y in B
# This finds the strongest (maximum) level of agreement via intermediary element y.


# Step 1: Create a fuzzy relation using Cartesian product
def cartesian_product_fuzzy_relation(A, B):
    """
    Create a fuzzy relation by Cartesian product of fuzzy sets A and B.
    Each pair (x, y) is assigned a membership value = min(A[x], B[y]).
    """
    relation = {}  # Dictionary to store the relation

    # Loop over all elements x in fuzzy set A
    for x in A:
        # Loop over all elements y in fuzzy set B
        for y in B:
            # Set the membership of (x, y) as the min of A[x] and B[y]
            relation[(x, y)] = min(A[x], B[y])

    return relation


# Step 2: Perform max-min composition of two fuzzy relations R and S
def max_min_composition(R, S):
    """
    Perform max-min composition of fuzzy relations R and S.
    Returns a new relation T such that:
    T(x, z) = max over y [min(R(x, y), S(y, z))]
    """
    T = {}  # Dictionary to store the result of composition

    # Extract all unique elements from R and S
    x_elements = set(x for x, y in R)  # Elements from first set
    y_elements = set(y for x, y in R)  # Intermediate elements
    z_elements = set(z for y, z in S)  # Elements from last set

    # Loop over all (x, z) combinations to compute T(x, z)
    for x in x_elements:
        for z in z_elements:
            min_values = []

            # Loop over y to compute min(R(x, y), S(y, z))
            for y in y_elements:
                if (x, y) in R and (y, z) in S:
                    min_val = min(R[(x, y)], S[(y, z)])
                    min_values.append(min_val)

            # Set the max of all min values as T(x, z)
            if min_values:
                T[(x, z)] = max(min_values)

    return T


# Step 3: Define fuzzy sets A, B, and C
A = {"x1": 0.7, "x2": 0.4, "x3": 0.9}  # Fuzzy Set A
B = {"y1": 0.6, "y2": 0.8, "y3": 0.5}  # Fuzzy Set B
C = {"z1": 0.5, "z2": 0.9, "z3": 0.3}  # Fuzzy Set C

# Step 4: Compute fuzzy relations R (A × B) and S (B × C)
R = cartesian_product_fuzzy_relation(A, B)
S = cartesian_product_fuzzy_relation(B, C)

# Step 5: Compute max-min composition of R and S
T = max_min_composition(R, S)

# Step 6: Print all fuzzy sets and their relations
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Fuzzy Set C:", C)

print("\nFuzzy Relation R (A × B):")
for (x, y), value in R.items():
    print(f"({x}, {y}): {value}")

print("\nFuzzy Relation S (B × C):")
for (y, z), value in S.items():
    print(f"({y}, {z}): {value}")

print("\nMax–Min Composition T (R ∘ S):")
for (x, z), value in T.items():
    print(f"({x}, {z}): {value}")
# Aim:
# Implement a program to perform max-min composition on any two fuzzy relations.

# Concept:
# In fuzzy set theory, the max-min composition is used to combine two fuzzy relations.
# Let R be a fuzzy relation from set A to B, and S be a fuzzy relation from set B to C.
# Then the max-min composition T of R and S is defined as:
#     T(x, z) = max(min(R(x, y), S(y, z))) for all y in B
# This finds the strongest (maximum) level of agreement via intermediary element y.


# Step 1: Create a fuzzy relation using Cartesian product
def cartesian_product_fuzzy_relation(A, B):
    """
    Create a fuzzy relation by Cartesian product of fuzzy sets A and B.
    Each pair (x, y) is assigned a membership value = min(A[x], B[y]).
    """
    relation = {}  # Dictionary to store the relation

    # Loop over all elements x in fuzzy set A
    for x in A:
        # Loop over all elements y in fuzzy set B
        for y in B:
            # Set the membership of (x, y) as the min of A[x] and B[y]
            relation[(x, y)] = min(A[x], B[y])

    return relation


# Step 2: Perform max-min composition of two fuzzy relations R and S
def max_min_composition(R, S):
    """
    Perform max-min composition of fuzzy relations R and S.
    Returns a new relation T such that:
    T(x, z) = max over y [min(R(x, y), S(y, z))]
    """
    T = {}  # Dictionary to store the result of composition

    # Extract all unique elements from R and S
    x_elements = set(x for x, y in R)  # Elements from first set
    y_elements = set(y for x, y in R)  # Intermediate elements
    z_elements = set(z for y, z in S)  # Elements from last set

    # Loop over all (x, z) combinations to compute T(x, z)
    for x in x_elements:
        for z in z_elements:
            min_values = []

            # Loop over y to compute min(R(x, y), S(y, z))
            for y in y_elements:
                if (x, y) in R and (y, z) in S:
                    min_val = min(R[(x, y)], S[(y, z)])
                    min_values.append(min_val)

            # Set the max of all min values as T(x, z)
            if min_values:
                T[(x, z)] = max(min_values)

    return T


# Step 3: Define fuzzy sets A, B, and C
A = {"x1": 0.7, "x2": 0.4, "x3": 0.9}  # Fuzzy Set A
B = {"y1": 0.6, "y2": 0.8, "y3": 0.5}  # Fuzzy Set B
C = {"z1": 0.5, "z2": 0.9, "z3": 0.3}  # Fuzzy Set C

# Step 4: Compute fuzzy relations R (A × B) and S (B × C)
R = cartesian_product_fuzzy_relation(A, B)
S = cartesian_product_fuzzy_relation(B, C)

# Step 5: Compute max-min composition of R and S
T = max_min_composition(R, S)

# Step 6: Print all fuzzy sets and their relations
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Fuzzy Set C:", C)

print("\nFuzzy Relation R (A × B):")
for (x, y), value in R.items():
    print(f"({x}, {y}): {value}")

print("\nFuzzy Relation S (B × C):")
for (y, z), value in S.items():
    print(f"({y}, {z}): {value}")

print("\nMax–Min Composition T (R ∘ S):")
for (x, z), value in T.items():
    print(f"({x}, {z}): {value}")
