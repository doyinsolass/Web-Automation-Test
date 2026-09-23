# Selenium Blog Signup Automation 📰

This project is a basic web automation test for signing up on the Selenium Blog website using Python and Selenium WebDriver. The test script automates the process of filling out the signup form, entering an email and verifying the success message.  
   
## Prerequisites

Before you start, make sure that you have the following apps on your machine:

- Python 3.x
- Selenium WebDriver
- Firefox browser
- Geckodriver (for Firefox)

## Installation

1. **Clone the repo:**

    ```sh
    git clone https://github.com/yourusername/selenium-blog-signup.git
    cd selenium-blog-signup
    ```

2. **Install the required Python packages:**

    ```sh
    pip install selenium
    ```

3. **Download and install Geckodriver:**

    - Download Geckodriver from the [official website](https://github.com/mozilla/geckodriver/releases).
    - Extract the downloaded file and add the path to your system's PATH environment variable.

## Running the Test

1. **Navigate to the project directory:**

    ```sh
    cd selenium-blog-signup
    ```

2. **Run the test script:**

    ```sh
    python test.py
    ```

## Learning Python with this Project

If you are learning Python, this repository is a good beginner example of:

- writing a `unittest.TestCase` class
- using variables and formatted strings (`f"user{timestamp}"`)
- calling functions from imported modules (`time.time()`, Selenium methods)
- making assertions with `self.assertEqual(...)`

Try changing one value at a time (for example the username prefix) and re-running the script to observe how Python code behaves.

## Test Script Overview

The test script `test.py` performs the following actions:

1. Opens the Firefox browser and navigates to the Selenium Blog signup page.
2. Fills out the signup form with a unique username and email address.
3. Submits the form.
4. Verifies that the success message is displayed.
