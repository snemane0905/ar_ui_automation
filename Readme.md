# Selenium Automation Script for Airalo eSIM Packages

This script uses Selenium WebDriver to automate the process of verifying eSIM package details on the Airalo website. It performs various actions such as navigating to the website, accepting cookies, searching for eSIM packages, and verifying the package details against expected values.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Code Overview](#code-overview)

---


## Installation

### Prerequisites

- Python 3.x
- Selenium
- ChromeDriver

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/snemane0905/ar_ui_automation.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd ar_ui_automation
    ```

3. **Install Required Python Packages:**

    Ensure you have `selenium` installed. If not, install it using:

    ```bash
     pip install -r requirements.txt
    ```

4. **Download ChromeDriver:**

    Download the appropriate version of ChromeDriver for your version of Chrome from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/). Place the `chromedriver` executable in a directory accessible from your PATH or specify its path in the `config.ini` file.

## Configuration

Before running the script, you need to configure the portal URL and chrome driver path in a `config.ini` file. Place this file in the root directory of your project.

### `config.ini` Format:

```ini
[airalo]
portal_url = https://www.airalo.com
chrome_driver_path = /path/to/chromedriver
```
Make sure to update the values of chrome_driver_path

## Usage

### Run the tests:

1. **Once you have configured the `config.ini` file, you can run the main script:**

```bash
python verify_esim_package_details.py
```
2. **Check the output:**
The script will print the results of the verification process in the console, including the number of passed and failed assertions.

## Code Overview

### Functions

- **`assert_response(expected_response, actual_response)`**: 
  Compares the actual response with the expected response and updates the count of passed and failed assertions.

- **`read_config(config=None)`**: 
  Reads configuration settings from the `config.ini` file.

- **`accept_cookie(driver)`**: 
  Accepts cookies shown in the popup.

- **`allow_notification(driver)`**: 
  Allows notifications by clicking the 'ALLOW' button (You can click on Don't Allow too).

### Script Flow

1. **Initialization**: 
   Reads configuration settings and sets up the WebDriver.

2. **Navigate to Website**: 
   Opens the Airalo website and performs actions like accepting cookies and allowing notifications.

3. **Search and Select eSIM Package**: 
   Searches for "Japan", selects the first eSIM package, and extracts its details.

4. **Verify Package Details**: 
   Compares the extracted details with the expected values.

5. **Print Results**: 
   Outputs the number of total, passed, and failed assertions.
