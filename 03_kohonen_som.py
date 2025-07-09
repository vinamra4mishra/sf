"""
03_kohonen_som.py
-----------------

Aim:
To implement Kohonen Self-Organizing Maps (SOM).

Concept:
- SOM is an unsupervised learning algorithm used for clustering and dimensionality reduction.
- It maps high-dimensional data onto a low-dimensional (usually 2D) grid.
- Each node on the grid has a weight vector.
- During training, the node whose weight is closest to the input becomes the Best Matching Unit (BMU).
- The BMU and its neighbors update their weights to resemble the input vector.

"""

import numpy as np
import matplotlib.pyplot as plt

class KohonenSOM:
    def __init__(self, x, y, input_len, learning_rate=0.5, radius=None, radius_decay=0.99, learning_rate_decay=0.99):
        # Grid size
        self.x = x
        self.y = y
        self.input_len = input_len

        # Initial learning rate and radius
        self.learning_rate = learning_rate
        self.radius = radius if radius is not None else max(x, y) / 2

        # Decay rates
        self.radius_decay = radius_decay
        self.learning_rate_decay = learning_rate_decay

        # Initialize weights randomly for each node in grid
        self.weights = np.random.rand(x, y, input_len)

    def train(self, data, num_iterations):
        # Train the SOM with the given data
        for i in range(num_iterations):
            # Randomly pick one input sample
            sample = data[np.random.randint(len(data))]

            # Step 1: Find the BMU (Best Matching Unit)
            bmu_index = self.find_bmu(sample)

            # Step 2: Update weights of BMU and its neighbors
            self.update_weights(sample, bmu_index, i, num_iterations)

            # Step 3: Decay the learning rate and radius
            self.learning_rate *= self.learning_rate_decay
            self.radius *= self.radius_decay

    def find_bmu(self, sample):
        # Compute Euclidean distance from sample to all weights
        distances = np.linalg.norm(self.weights - sample, axis=-1)
        # Index of minimum distance (BMU)
        bmu_index = np.unravel_index(np.argmin(distances), (self.x, self.y))
        return bmu_index

    def update_weights(self, sample, bmu_index, iteration, num_iterations):
        for i in range(self.x):
            for j in range(self.y):
                # Distance of (i,j) node from BMU
                distance_to_bmu = np.linalg.norm(np.array([i, j]) - np.array(bmu_index))

                # If within radius, update weight
                if distance_to_bmu <= self.radius:
                    influence = np.exp(-distance_to_bmu**2 / (2 * (self.radius**2)))
                    self.weights[i, j, :] += influence * self.learning_rate * (sample - self.weights[i, j, :])

    def visualize(self):
        # Reshape weights to 2D for visualization
        plt.imshow(self.weights.reshape(self.x * self.y, self.input_len), cmap='viridis')
        plt.colorbar()
        plt.title("SOM Weight Map")
        plt.show()

# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    # Generate random data (100 samples, 3 features each)
    data = np.random.rand(100, 3)

    # Create SOM with 10x10 grid
    som = KohonenSOM(x=10, y=10, input_len=3, learning_rate=0.5)

    # Train the SOM
    som.train(data, num_iterations=1000)

    # Visualize the result
    som.visualize()
