import numpy as np
import cv2

def add_noise(image_path, mean=0, std_dev=1):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Generate Gaussian noise
    gauss = np.random.normal(mean, std_dev, image.shape)

    # Add the Gaussian noise to the image
    noisy_image = image + gauss

    # Ensure the noisy image has valid pixel values
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    # Save the noisy image
    output_path = 'noisy_image.jpg'
    cv2.imwrite(output_path, noisy_image)
    print(f"Noisy image saved as {output_path}")

# Usage:
noisy_image = add_noise('images/testimg1.jpg')
cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
