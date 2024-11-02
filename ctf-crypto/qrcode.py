# Let's take a look at the contents of the CSV file to understand its structure and data.
import pandas as pd

# Load the CSV file
file_path = '/mnt/data/STEG05.csv'
csv_data = pd.read_csv(file_path)

# Display the first few rows to inspect the data
csv_data.head()


import numpy as np
import matplotlib.pyplot as plt

# Convert the DataFrame to a NumPy array
pixel_data = csv_data.to_numpy()

# Plot the pixel data as an image (grayscale)
plt.imshow(pixel_data, cmap='gray', interpolation='nearest')
plt.axis('off')  # Hide axes for better visualization
plt.show()
