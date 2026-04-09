# Store Automation OCR

## Overview
This project is an OCR-based automation tool designed to improve daily sales management in restaurants.

It extracts key information such as sales, number of customers, and payment data from receipt images and automatically inputs them into an existing Excel format.

---

## Background
In a restaurant where I worked part-time, daily sales were manually transcribed from paper reports into Excel.

This caused:
- Time-consuming work
- Human errors
- Complex management of multiple payment methods

---

## System Flow
Image → OCR → Data Extraction → Excel Output

---

## Tech Stack
- Python
- Tesseract OCR
- Pillow
- openpyxl

---

## Project Structure

store-automation-ocr/
├── README.md
├── requirements.txt
├── src/
│   ├── ocr.py
│   ├── parser.py
│   └── excel_writer.py

---

## Notes
This is a simplified version for demonstration purposes.
Some details are intentionally omitted.
