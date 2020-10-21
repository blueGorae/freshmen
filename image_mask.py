# import numpy and cv2 module
import numpy as np
import cv2


# Define image path
IMAGE_PATH = "sample.png"

# Read an input image
image = cv2.imread(IMAGE_PATH, flags=cv2.IMREAD_UNCHANGED)

# Print the image shape
print(image.shape)

# Define a full mask
mask = np.ones_like(image, dtype=np.bool)
# Define a mask position
h = 300
delta_h = 250
w = 500
delta_w = 250

mask[h:(h+delta_h), w: (w+delta_w)] = False

# Apply the mask to the image
image = mask * image

# Show the image
cv2.imshow("Input Image", image)
cv2.waitKey()
