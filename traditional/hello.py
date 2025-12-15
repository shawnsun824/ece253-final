import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read color image then convert to RGB for consistent display + processing
image_bgr = cv2.imread("02.jpeg", cv2.IMREAD_COLOR)
image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)   # <-- changed

def gamma_correction(image, gamma):
    normalized_img = image.astype(np.float32) / 255.0
    gamma_corrected_img = np.power(normalized_img, gamma)
    return np.uint8(gamma_corrected_img * 255)

def apply_gamma_on_luminance_rgb(rgb_img, gamma):
    # RGB -> YCrCb
    ycrcb = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2YCrCb)  # <-- changed

    # gamma only on Y channel
    ycrcb[:, :, 0] = gamma_correction(ycrcb[:, :, 0], gamma)

    # back to RGB
    return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)     # <-- changed

def display_images(titles, images, save_path):
    fig, axs = plt.subplots(1, len(images), figsize=(15, 5))
    if len(images) == 1:
        axs = [axs]

    for ax, title, img in zip(axs, titles, images):
        if img.ndim == 2:
            ax.imshow(img, cmap='gray')
        else:
            ax.imshow(img)  # already RGB
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

gamma_0_5 = apply_gamma_on_luminance_rgb(image, 0.5)
gamma_2   = apply_gamma_on_luminance_rgb(image, 2.0)

display_images(
    ["Original Image", "Gamma on Y (0.5)", "Gamma on Y (2.0)"],
    [image, gamma_0_5, gamma_2],
    save_path="gamma_results.png"
)
