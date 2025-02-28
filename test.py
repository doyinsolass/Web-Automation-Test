import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumBlogSignup(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://selenium-blog.herokuapp.com/signup")


    def test_signup(self):
        driver = self.driver
        timestamp = int(time.time())

        # Find the username field and enter a unique username
        username_field = driver.find_element(By.ID, "user_username")
        username_field.send_keys(f"user{timestamp}")

        # Find the email field and enter a unique email
        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys(f"user{timestamp}@test.com")

        # Find the password field and enter a password
        password_field = driver.find_element(By.ID, "user_password")
        password_field.send_keys("password")

        # Find the submit button and click it
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Find the success banner and get its text
        banner = driver.find_element(By.ID, "flash_success")
        banner_text = banner.text

        # Assert that the banner text is as expected
        self.assertEqual(banner_text, "Welcome to the alpha blog user")

        time.sleep(10)

if __name__ == "__main__":
    unittest.main()