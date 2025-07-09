"""
05_bam_network.py
------------------

Aim:
Write a program for implementing BAM (Bidirectional Associative Memory) network.

Concept:
- BAM is a recurrent neural network designed to store and recall associations between two sets of binary patterns.
- Bidirectional: can recall A from B or B from A.
- Weights are learned using Hebbian learning: w_ij += x_i * y_j
- Recall works by matrix multiplication and sign activation function.

"""

import numpy as np

# Step 1: Define BAM class
class BAM:
    def __init__(self):
        self.weights = None

    def train(self, patterns_A, patterns_B):
        """
        Train weights using Hebbian learning rule.
        """
        num_features_A = patterns_A.shape[1]
        num_features_B = patterns_B.shape[1]
        self.weights = np.zeros((num_features_A, num_features_B))

        for a, b in zip(patterns_A, patterns_B):
            # Outer product and accumulate
            self.weights += np.outer(a, b)

    def recall_A(self, pattern_B):
        """
        Recall pattern A from B: A = sign(B . Wᵗ)
        """
        result = np.dot(pattern_B, self.weights.T)
        return np.sign(result)

    def recall_B(self, pattern_A):
        """
        Recall pattern B from A: B = sign(A . W)
        """
        result = np.dot(pattern_A, self.weights)
        return np.sign(result)

# ----------------------------------------
# Example usage
# ----------------------------------------
if __name__ == "__main__":
    # Step 2: Define the training patterns
    patterns_A = np.array([[1, -1, -1], [-1, 1, 1], [-1, -1, -1]])
    patterns_B = np.array([[1, -1], [-1, 1], [1, 1]])

    # Step 3: Initialize and train the BAM
    bam = BAM()
    bam.train(patterns_A, patterns_B)

    # Step 4: Test recall A from B
    test_pattern_B = np.array([1, -1])
    recalled_A = bam.recall_A(test_pattern_B)
    print("Recalled Pattern A for test pattern B", test_pattern_B, "is:", recalled_A)

    # Step 5: Test recall B from A
    test_pattern_A = np.array([1, -1, -1])
    recalled_B = bam.recall_B(test_pattern_A)
    print("Recalled Pattern B for test pattern A", test_pattern_A, "is:", recalled_B)
