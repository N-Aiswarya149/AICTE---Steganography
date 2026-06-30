# AICTE – Image Steganography

## Overview

This project is an **Image Steganography System** developed as part of the AICTE internship. It allows users to securely hide confidential text messages inside digital images and later retrieve them using the correct decryption key.

Steganography enhances data security by concealing the existence of secret information within an image, making it difficult for unauthorized users to detect.

##  Features

* Hide secret messages inside images
* Extract hidden messages from encoded images
* Password-protected message retrieval
* Simple and easy-to-use Python implementation
* Maintains the visual quality of the original image

##  Technologies Used

* Python
* OpenCV
* NumPy

##  Project Structure

```
AICTE-Steganography/
│── stego.py
│── inputimage.png
│── encoded.jpg
│── encryptedImage.jpg
│── README.md
```

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/N-Aiswarya149/AICTE---Stenograpy.git
```

### 2. Navigate to the project folder

```bash
cd AICTE---Stenograpy
```

### 3. Install the required packages

```bash
pip install opencv-python numpy
```

### 4. Run the program

```bash
python stego.py
```

##  Sample Workflow

1. Select an input image.
2. Enter the secret message.
3. Enter an encryption/decryption key.
4. Generate the encoded image.
5. Decode the message using the correct key.

##  Applications

* Secure communication
* Confidential data sharing
* Digital watermarking
* Information protection
* Cybersecurity education

##  Learning Outcomes

* Understanding image steganography concepts
* Working with image processing in Python
* Implementing secure message hiding techniques
* Exploring basic cybersecurity concepts

##  Author

**Aiswarya N**

* GitHub: https://github.com/N-Aiswarya149

##  License

This project is intended for educational and learning purposes.
