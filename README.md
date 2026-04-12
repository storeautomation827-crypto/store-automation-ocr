# Store Automation OCR

## Overview
Store Automation OCR is a practical automation system designed to streamline daily sales reporting operations in restaurants.

The system uses OCR (Optical Character Recognition) to extract key information from receipt or report images and automatically transfers the data into an existing Excel-based workflow.

This project focuses not only on technical implementation, but also on real-world usability, aiming to reduce manual workload and improve operational efficiency.

---

## Background

In my part-time job at a restaurant, daily sales data was manually transcribed from paper reports into Excel sheets.

This process led to several operational challenges:

- Significant time consumption (approximately 15 minutes per day)  
- Frequent human errors during manual input  
- Increased complexity due to multiple payment methods (cash, credit card, electronic payment, etc.)

To solve these issues, I developed an OCR-based automation system that integrates seamlessly with existing workflows.

---

## Features

- OCR-based extraction of numerical and textual data from images  
- Image preprocessing using OpenCV to improve recognition accuracy  
- Rule-based parsing to handle noisy and inconsistent OCR outputs  
- Automatic Excel integration without modifying existing formats  
- Messaging interface via LINE API for intuitive operation  
- User confirmation flow to ensure data accuracy before saving  

---

## System Architecture

The system follows a simple pipeline:

Image → Preprocessing → OCR → Data Parsing → Excel Output

This modular structure allows each component to be improved independently.

---

## User Interaction Flow

1. User sends an image via LINE  
2. OCR processes the image and extracts data  
3. Extracted data is displayed for confirmation  
4. User approves or cancels the input  
5. Approved data is written into Excel  

This design ensures both usability and reliability in real-world environments.

---

## Tech Stack

- Python  
- Flask (Web API / Backend)  
- Requests (API communication)  
- Tesseract OCR  
- OpenCV (Image preprocessing)  
- Pillow (Image handling)  
- openpyxl (Excel integration)  
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


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd store_automation
2. Create a virtual environment
python -m venv .venv

This command creates a folder named .venv that contains an isolated Python environment.

3. Activate the virtual environment
Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
Windows (Command Prompt)
.venv\Scripts\activate
macOS / Linux
source .venv/bin/activate

Once activated, you should see (.venv) at the beginning of your terminal prompt.

4. Upgrade pip (recommended)
python -m pip install --upgrade pip
5. Install required packages
python -m pip install -r requirements.txt

If some packages are missing, install them manually:

python -m pip install requests
python -m pip install opencv-python
6. Deactivate the virtual environment
deactivate
