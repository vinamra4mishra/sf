"""
04_hamming_network.py
----------------------

Aim:
Solve the Hamming Network, given the exemplar vectors.

Concept:
- The Hamming network is used to match a given input vector to the closest pattern (exemplar) from a set.
- It uses the Hamming distance, which is the number of differing bits between two binary vectors.
- The input is compared with each exemplar, and the one with the smallest distance is chosen.

"""

import numpy as np

# Step 1: Define exemplar vectors (pre-stored patterns to compare with)
exemplar_vectors = np.array(
    [[1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0]]
)

# Step 2: Define the input vector
input_vector = np.array([1, 0, 1, 1, 0, 1, 0, 1])


# Step 3: Define a function to compute Hamming distance between two binary vectors
def hamming_distance(v1, v2):
    """
    Compute the Hamming distance by counting differing positions.
    """
    return np.sum(v1 != v2)


# Step 4: Function to find the closest exemplar using Hamming distance
def hamming_network(input_vector, exemplar_vectors):
    """
    Compare input vector with all exemplars and return the index of closest match.
    """
    distances = np.array(
        [hamming_distance(input_vector, ev) for ev in exemplar_vectors]
    )
    min_distance_index = np.argmin(distances)  # index of the smallest distance
    return min_distance_index, distances[min_distance_index]


# Step 5: Run the Hamming Network
index, distance = hamming_network(input_vector, exemplar_vectors)

# Step 6: Output the result
print(
    f"The input vector is closest to exemplar vector at index {index} with a Hamming distance of {distance}."
)
