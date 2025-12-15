# Image Enhancement and Shadow Removal Project
This project we aim to improve the image quality for further calorie estimation, in this repository we mainly focus on illumination and shadow removal.

This repository contains three image enhancement pipelines:

- Traditional image processing methods
- ML-based shadow removal using ShadowFormer
- Low-light image enhancement using Zero-DCE

Each method can be run independently as described below.

---

## 1. Traditional Image Processing Methods

This part implements traditional image processing techniques such as gamma correction.

### Requirements
   ```bash
   cd ShadowFormer
   pip install requirements.txt
   ```
### Steps

1. Enter the directory:
   ```bash
   cd traditional
   ```

2. Add your test image to the `traditional` directory.

3. Modify the image path in `hello.py`:
   ```python
   image_bgr = cv2.imread("02.jpeg", cv2.IMREAD_COLOR)
   ```

4. Run the script:
   ```bash
   python hello.py
   ```

The processed image will be displayed and/or saved according to the script settings.

---

## 2. ML-based Shadow Removal (ShadowFormer)

This part evaluates shadow removal performance using a pre-trained ShadowFormer model.

### Steps

1. Enter the directory:
   ```bash
   cd ShadowFormer
   ```

2. Prepare your test dataset following the ISTD format, including:
   - Shadow images
   - Shadow masks
   - Shadow-free ground truth images

3. Modify the dataset path in `test1.py`:
   ```python
   parser.add_argument(
       '--input_dir',
       default='/home/has038/teams/project-team-7/pics',
       type=str,
       help='Directory of validation images'
   )
   ```

4. Run the evaluation:
   ```bash
   python test1.py
   ```

Optional flags:
- `--save_images` : save output images
- `--cal_metrics` : compute PSNR / SSIM / RMSE

---

## 3. Low-light Image Enhancement (Zero-DCE)

This part applies Zero-DCE for low-light image enhancement.

### Steps

```bash
cd Zero-DCE
cd Zero-DCE_code
python lowlight_test.py
```

---

## Project Structure

```text
project-team-7/
├── traditional/
├── ShadowFormer/
├── Zero-DCE/
├── data/
├── results/
└── README.md
```

---

## Acknowledgements

This project uses open-source implementations of ShadowFormer and Zero-DCE for research and educational purposes.

