from PIL import Image, ImageEnhance
import cv2

# Load image using OpenCV
img = cv2.imread(r'C:\Users\Harish Raj\Downloads\Pl 300 certificate_page-0001.jpg')

# Resize image (e.g., double the size)
img_resized = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Save resized image temporarily
cv2.imwrite('resized_photo.jpg', img_resized)

# Enhance sharpness using Pillow
pil_img = Image.open('resized_photo.jpg')
enhancer = ImageEnhance.Sharpness(pil_img)
sharper_img = enhancer.enhance(2.0)  # Increase sharpness

# Save the final enhanced image
sharper_img.save('enhanced_photo.jpg')
print("Enhanced photo saved as enhanced_photo.jpg")