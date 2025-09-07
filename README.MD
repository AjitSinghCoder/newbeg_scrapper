# Newegg Product Scraper

This project extracts product data from Newegg and stores it in a SQLite database.

## Requirements

- Python 3.10.12
- `requirements.txt` (contains all necessary Python packages)
- SQLite database (`newegg_products.db` will be created in the main folder)

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment (Linux/macOS)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate

### 2. Install dependencies 

pip install -r requirements.txt

### 3. Run script 
python main.py

The script will:
Extract product data from Newegg
Store the data in a SQLite database newegg_products.db located in the main folder

### 4. View the database
    You can view the stored data using any SQLite viewer
    
### 5. Proxy instructions (if required)
    If the terminal shows output like this:

    Url -> <some_url>
    Status code -> <some_status_code>
    Please use proxy to access the website

    It means the website is blocking direct access.
    Please configure and use a proxy to fetch the data successfully.
