import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Load and preprocess the image
image_path = "../output_videos/cropped_img.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Focus on central top region to avoid background (jersey only)
h, w = image.shape[:2]
jersey_crop = image[int(0.05*h):int(0.35*h), int(0.25*w):int(0.75*w)]

# Reshape to 2D array for clustering
image_2d = jersey_crop.reshape(-1, 3)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(image_2d)

# Reconstruct clustered image
labels = kmeans.labels_
clustered_image = labels.reshape(jersey_crop.shape[:2])

# Decide which cluster is background based on corner pixels
corners = [clustered_image[0,0], clustered_image[0,-1], clustered_image[-1,0], clustered_image[-1,-1]]
non_player_cluster = max(set(corners), key=corners.count)
player_cluster = 1 - non_player_cluster

# Get the RGB color of the player's jersey
player_color = kmeans.cluster_centers_[player_cluster]
print("Player team color (RGB):", player_color.astype(int))

# Optional: Visualize clustered result
colored_output = np.zeros_like(jersey_crop)
for i in range(2):
    colored_output[clustered_image == i] = kmeans.cluster_centers_[i]

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.title("Original Jersey Crop")
plt.imshow(jersey_crop)

plt.subplot(1, 2, 2)
plt.title("Clustered Colors")
plt.imshow(colored_output)
plt.show()
