"""
07_de_morgans_law.py
---------------------

Aim:
Implement a program to verify De-Morgan’s Laws.

Concept:
De-Morgan's Laws in Boolean logic state:
1. ~(A ∨ B) = ~A ∧ ~B
2. ~(A ∧ B) = ~A ∨ ~B

These laws show how negation interacts with AND/OR operations and are fundamental in logic design and simplification.

"""

# Law 1: ~(A ∨ B) = ~A ∧ ~B
def de_morgans_law_1(A, B):
    not_A_or_B = not (A or B)
    not_A_and_not_B = (not A) and (not B)
    return not_A_or_B, not_A_and_not_B

# Law 2: ~(A ∧ B) = ~A ∨ ~B
def de_morgans_law_2(A, B):
    not_A_and_B = not (A and B)
    not_A_or_not_B = (not A) or (not B)
    return not_A_and_B, not_A_or_not_B

# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    # Take Boolean inputs from user
    A = bool(input("Enter A (True/False): "))
    B = bool(input("Enter B (True/False): "))

    # Test Law 1
    result_1 = de_morgans_law_1(A, B)
    print("\nDeMorgan's Law 1: ~(A ∨ B) = ~A ∧ ~B")
    print(f"~({A} ∨ {B}) = {result_1[0]}")
    print(f"~{A} ∧ ~{B} = {result_1[1]}")
    print(f"Law holds: {result_1[0] == result_1[1]}\n")

    # Test Law 2
    result_2 = de_morgans_law_2(A, B)
    print("DeMorgan's Law 2: ~(A ∧ B) = ~A ∨ ~B")
    print(f"~({A} ∧ {B}) = {result_2[0]}")
    print(f"~{A} ∨ ~{B} = {result_2[1]}")
    print(f"Law holds: {result_2[0] == result_2[1]}")
