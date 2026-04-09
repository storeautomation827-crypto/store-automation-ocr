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

## System Flow
Image → OCR → Data Extraction → Excel Output

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
  Provides a messaging interface for text commands and image-based OCR processing
---

## Notes
This repository contains a simplified version for demonstration purposes.  
Some implementation details are intentionally omitted.

---

## Implementation Notes
For public sharing, this repository includes a simplified version of the OCR, parsing, and Excel export workflow.  
Production-specific logic and sensitive configurations have been excluded.

---

## Project Value
This project focuses not only on technical implementation, but also on solving real-world operational problems.

Instead of replacing existing systems, it integrates with current workflows, making it practical for real use.

Through this project, I learned the importance of designing systems that are both technically effective and operationally practical.
