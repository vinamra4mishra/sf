"""
06_maxnet.py
------------

Aim:
Implement a program to find the winning neuron using MaxNet.

Concept:
- MaxNet is a competitive neural network used to find the neuron with the highest activation.
- It uses lateral inhibition to suppress weaker activations iteratively.
- At each step, neurons inhibit each other slightly, and the weakest ones are driven to zero.
- The process continues until only one neuron has a non-zero activation (the winner).

"""

import numpy as np

def maxnet(input_vector, epsilon=0.1, max_iterations=100):
    """
    MaxNet algorithm to find the winning neuron.

    Parameters:
    input_vector (np.array): Initial activations of neurons.
    epsilon (float): Inhibition factor (small positive number).
    max_iterations (int): Maximum number of iterations to run.

    Returns:
    int: Index of the winning neuron.
    """
    # Step 1: Copy input to activations
    activations = np.copy(input_vector)
    num_neurons = len(input_vector)

    for _ in range(max_iterations):
        # Step 2: Compute total inhibition for each neuron
        inhibition = epsilon * (np.sum(activations) - activations)

        # Step 3: Subtract inhibition
        new_activations = activations - inhibition

        # Step 4: Clamp negative values to 0
        new_activations[new_activations < 0] = 0

        # Step 5: If only one neuron is left active, break loop
        if np.count_nonzero(new_activations) == 1:
            break

        # Step 6: Update activations for next round
        activations = new_activations

    # Step 7: Return the index of the neuron with max activation
    return np.argmax(activations)

# ----------------------------------------
# Example usage
# ----------------------------------------
if __name__ == "__main__":
    # Input activations
    input_vector = np.array([0.2, 0.5, 0.1, 0.7, 0.4])

    # Run MaxNet
    winning_neuron = maxnet(input_vector)

    # Display the result
    print(f"The winning neuron is at index {winning_neuron} with activation {input_vector[winning_neuron]}")
