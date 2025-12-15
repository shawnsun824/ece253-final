# Image Enhancement and Shadow Removal Project

This repository contains three image enhancement pipelines:
- Traditional image processing methods
- ML-based shadow removal using ShadowFormer
- Low-light image enhancement using Zero-DCE

Each method can be run independently as described below.

---

## 1. Traditional Methods

This part implements traditional image processing techniques (e.g., gamma correction).

 Steps
```bash
cd traditional

Add your own test image to the traditional directory.
Open hello.py and modify the image path:
image_bgr = cv2.imread("02.jpeg", cv2.IMREAD_COLOR)
Run the script:
python hello.py

The processed image will be displayed and/or saved according to the script settings.

## 2. Traditional Methods

ML-based Shadow Removal (ShadowFormer)
This part evaluates shadow removal performance using a pre-trained ShadowFormer model.

cd ShadowFormer
Prepare your test dataset following the ISTD format, including:
Shadow images
Shadow masks
Shadow-free ground truth images
Open test1.py and modify the dataset path:
parser.add_argument(
    '--input_dir',
    default='/home/has038/teams/project-team-7/pics',
    type=str,
    help='Directory of validation images'
)
Run the evaluation:
python test1.py
Optional flags:
--save_images to save output images
--cal_metrics to compute PSNR / SSIM / RMSE
3. Low-light Image Enhancement (Zero-DCE)
This part applies Zero-DCE for low-light image enhancement.
cd Zero-DCE
cd Zero-DCE_code
python lowlight_test.py
Structure:
project-team-7/
├── traditional/
├── ShadowFormer/
├── Zero-DCE/
├── data/
├── results/
└── README.md
Acknowledgements
This project uses open-source implementations of ShadowFormer and Zero-DCE for research and educational purposes.
