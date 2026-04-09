# store-automation-ocr
OCR-based automation tool for restaurant sales reporting. Extracts data from receipts and inputs into Excel.
# Store Automation OCR

## Overview
This project is an OCR-based automation tool designed to improve daily sales management in restaurants.

It extracts key information such as sales, number of customers, and payment data from receipt images and automatically inputs them into an existing Excel format.

The focus of this project is not only technical implementation but also real-world usability in an operational environment.

---

## Background
In a restaurant where I worked part-time, daily sales were manually transcribed from paper reports into Excel.

This caused:
- Time-consuming work
- Human errors
- Complex management of multiple payment methods

To solve this problem, I developed an OCR-based automation system.

---

## Key Features

### 1. Designed for Real-World Use
Instead of introducing a new system, this tool integrates with existing Excel workflows.

→ No need to change current operations

---

### 2. Robust OCR Handling
OCR results are inherently unstable, so the system includes:

- Image preprocessing (contrast adjustment)
- Pattern-based data extraction (regex)
- Noise filtering

→ Designed with OCR limitations in mind

---

### 3. Data Extraction
Extracts:
- Sales (tax excluded)
- Number of customers
- Number of groups
- Payment breakdown (cash, card, etc.)

---

## Tech Stack
- Python
- Tesseract OCR
- Pillow
- Excel processing

---

## System Flow
1. Input receipt image  
2. Apply image preprocessing  
3. Perform OCR  
4. Extract required data  
5. Write to Excel  

---

## Notes
- This repository contains a **simplified version for demonstration purposes**
- Some implementation details are intentionally omitted

---

## Future Work
- Improve OCR accuracy  
- Implement LINE-based interface  
- Cloud support for multiple stores  
- Data visualization  
