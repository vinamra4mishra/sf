"""
08_fuzzy_set_operations.py
---------------------------

Aim:
Implement Union, Intersection, Complement, and Difference operations on fuzzy sets.

Concept:
- Fuzzy sets allow partial membership with values in [0, 1].
- Union (A ∪ B): max(A(x), B(x))
- Intersection (A ∩ B): min(A(x), B(x))
- Complement (A'): 1 - A(x)
- Difference (A - B): min(A(x), 1 - B(x))
"""

# Union operation: max(A(x), B(x))
def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A).union(B)}

# Intersection operation: min(A(x), B(x))
def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A).intersection(B)}

# Complement operation: 1 - A(x)
def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

# Difference operation: min(A(x), 1 - B(x))
def fuzzy_difference(A, B):
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in set(A).union(B)}

# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    # Define fuzzy sets A and B
    A = {'x1': 0.1, 'x2': 0.4, 'x3': 0.7}
    B = {'x2': 0.5, 'x3': 0.2, 'x4': 0.8}

    # Perform all fuzzy set operations
    union_result = fuzzy_union(A, B)
    intersection_result = fuzzy_intersection(A, B)
    complement_result_A = fuzzy_complement(A)
    difference_result = fuzzy_difference(A, B)

    # Display results
    print("Fuzzy Set A:", A)
    print("Fuzzy Set B:", B)
    print("\nResults of the operations performed on the fuzzy sets:")
    print("Union (A ∪ B):", union_result)
    print("Intersection (A ∩ B):", intersection_result)
    print("Complement (A'):", complement_result_A)
    print("Difference (A - B):", difference_result)
