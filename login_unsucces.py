import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_b_unsuccess_login(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("locked_out_user")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//*[@data-test='error']")
        self.assertIn('Epic sadface', response_data.text)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
