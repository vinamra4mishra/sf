"""
09_fuzzy_cartesian_relation.py
-------------------------------

Aim:
Create Fuzzy relation by Cartesian product of any two fuzzy sets.

Concept:
- Cartesian product of fuzzy sets A and B generates a fuzzy relation R.
- Each pair (x, y) has a membership value defined as:
    R(x, y) = min(A(x), B(y))
"""

# Function to generate Cartesian product fuzzy relation
def cartesian_product_fuzzy_relation(A, B):
    relation = {}
    for x in A:
        for y in B:
            relation[(x, y)] = min(A[x], B[y])
    return relation

# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    # Define fuzzy sets A and B
    A = {'x1': 0.7, 'x2': 0.4, 'x3': 0.9}
    B = {'y1': 0.6, 'y2': 0.8, 'y3': 0.5}

    # Generate fuzzy relation
    relation = cartesian_product_fuzzy_relation(A, B)

    # Print sets and relation
    print("Fuzzy Set A:", A)
    print("Fuzzy Set B:", B)
    print("\nCartesian Product Fuzzy Relation:")
    for (x, y), value in relation.items():
        print(f"({x}, {y}): {value}")
