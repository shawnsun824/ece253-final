import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load image in grayscale
image = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)
# Utility function to display images

def display_images(titles, images, save_path):
    fig, axs = plt.subplots(1, len(images), figsize=(15, 5))
    for ax, title, img in zip(axs, titles, images):
        ax.imshow(img, cmap='gray')
        ax.set_title(title)
        ax.axis('off')
        plt.show()
        plt.savefig(save_path)

def gamma_correction(image, gamma):
    # Normalize the image to range [0, 1]
    normalized_img = image / 255.0
    gamma_corrected_img = np.power(normalized_img, gamma)
    # Scale back to [0, 255]
    return np.uint8(gamma_corrected_img * 255)
# Example gamma correction
gamma_0_5 = gamma_correction(image, 0.5) # Brightening
gamma_2 = gamma_correction(image, 2.0) # Darkening
display_images(
    ["Original Image", "Gamma Correction (0.5)", "Gamma Correction (2.0)"],
    [image, gamma_0_5, gamma_2],
    save_path="gamma_results.png"
)
