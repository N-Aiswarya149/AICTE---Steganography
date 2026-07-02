# AICTE – Image Steganography

## Overview

This project is an **Image Steganography System** developed as part of the AICTE Internship. It allows users to securely hide confidential text messages inside digital images and retrieve them later using the correct decryption key.

Steganography enhances data security by concealing the existence of secret information within an image, making it difficult for unauthorized users to detect.

## Features

- Hide secret messages inside images
- Extract hidden messages from encoded images
- Password-protected message retrieval
- Simple and user-friendly Python implementation
- Preserves the visual quality of the original image

## Technologies Used

- Python
- OpenCV (cv2)
- NumPy

## Project Structure

```
AICTE---Steganography/
│── stego.py
│── inputimage.png
│── encoded.jpg
│── encryptedImage.jpg
│── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/N-Aiswarya149/AICTE---Steganography.git
```

### 2. Navigate to the project directory

```bash
cd AICTE---Steganography
```

### 3. Install the required dependencies

```bash
pip install opencv-python numpy
```

> **Note:** If you encounter a `ModuleNotFoundError: No module named 'cv2'`, install OpenCV using:

```bash
pip install opencv-python
```

### 4. Run the application

```bash
python stego.py
```

## How It Works

1. Select an input image.
2. Enter the secret message to hide.
3. Provide an encryption/decryption key.
4. Generate the encoded image.
5. Decode the hidden message using the correct key.

## Applications

- Secure communication
- Confidential data sharing
- Digital watermarking
- Information protection
- Cybersecurity education

## Learning Outcomes

- Understanding image steganography concepts
- Working with image processing using Python
- Implementing secure message hiding techniques
- Exploring practical cybersecurity concepts

## Author

**Aiswarya N**

GitHub: https://github.com/N-Aiswarya149

## License

This project is created for educational and learning purposes.
