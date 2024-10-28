import cv2

# Read the image file
img = cv2.imread("nasa.jpg")
# Resize the image to 400x400 pixels
resized_img = cv2.resize(img, (400, 400))

# Initialize edge detection flag
edge_bool = False
# Convert image to grayscale
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
# Apply Canny edge detection
edges = cv2.Canny(gray_img, 100, 200)

# Display the original image
cv2.imshow("showing", resized_img)
# Wait for keyboard input
key = cv2.waitKey(0)

# If 'q' is pressed, close all windows
if key == ord("q"):
    cv2.destroyAllWindows()
# If 'b' is pressed, show edge detection
elif key == ord("b"):
    cv2.destroyAllWindows()
    cv2.imshow("edges", edges)
    key = cv2.waitKey(0)
    if key == ord("q"): cv2.destroyAllWindows()
    edge_bool = not edge_bool

# Close all windows at the end
cv2.destroyAllWindows()