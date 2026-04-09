# Store Automation OCR

## Overview
This project is an OCR-based automation tool designed to improve daily sales management in restaurants.

It extracts key information such as sales, number of customers, and payment data from receipt images and automatically inputs them into an existing Excel format.

The system is designed not only for technical implementation, but also for real-world usability in an operational environment.

---

## Background
In a restaurant where I worked part-time, daily sales were manually transcribed from paper reports into Excel.

This caused:
- Time-consuming work
- Human errors
- Complex management of multiple payment methods

To address these issues, I developed an OCR-based automation system.

---

## Key Features

- OCR-based data extraction from receipt images  
- Image preprocessing for improved recognition accuracy  
- Rule-based parsing to handle unstable OCR output  
- Automatic Excel integration without changing existing workflows  
- Messaging-based interface using LINE API  

---

## System Flow
Image → OCR → Data Extraction → Excel Output

---

## User Interaction Design

The system includes a simple interaction flow that allows users to:

- Review extracted OCR results  
- Confirm or cancel data before saving  
- Ensure data accuracy before updating records  

This design improves reliability and reduces input errors in real-world operations.

---

## Tech Stack
- Python
- Flask
- Requests
- Tesseract OCR
- Pillow
- OpenCV
- openpyxl
- LINE Messaging API

---

## Project Structure

The project is organized as follows:

- README.md  
  Project overview and documentation

- requirements.txt  
  List of required Python libraries

- src/ocr.py  
  Handles image preprocessing and OCR execution

- src/parser.py  
  Extracts structured data from OCR results

- src/excel_writer.py  
  Writes processed data into Excel format

- src/line_bot_app.py  
  Provides a messaging interface for command handling and image-based OCR processing through LINE

- examples/simple_ocr_demo.py  
  Standalone demo script that runs independently of the full system

---

## Example Usage

### Standalone OCR Demo

Run the standalone demo:

```bash
python examples/simple_ocr_demo.py
