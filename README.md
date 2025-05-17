# QR Code Generator for Biox Systems

This Python application generates a QR code for the official Biox Systems website: [https://www.bioxsystems.com](https://www.bioxsystems.com).

## Features

- Generates a QR code using Python and the `qrcode` library
- Saves the QR code image as `biox_qr_code.png`
- Opens the QR code image in the default viewer after creation

## Requirements

- Python 3.x
- `qrcode` library with Pillow support

## Installation

1. Clone or download this repository.
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install 'qrcode[pil]'
   ```

## Usage

Run the script from your terminal:

```bash
python qr_code_generator.py
```

This will:
- Generate a QR code image pointing to the Biox Systems website
- Save it as `biox_qr_code.png`
- Display the image in your default viewer

## Example Output

![QR Code Example](biox_qr_code.png)

> Scan this with any QR code reader to visit [https://www.bioxsystems.com](https://www.bioxsystems.com)

## Files Included

- `qr_code_generator.py` – Python script to generate the QR code
- `requirements.txt` – List of dependencies
- `README.md` – Project documentation

## Author

Prafulla – MSCS-633 Hands-On Assignment 2
