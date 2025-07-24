import cv2

# Read an image
image_path = '/home/pszaa1/test.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Could not open or find the image at {image_path}")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Grayscale Image', blurred_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
