import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_view_products(self):
        # login first
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # view products
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        response_data = driver.find_element(By.CLASS_NAME, "title").text
        self.assertIn('YOUR CART', response_data)

    def test_add_to_cart(self):
        # login first
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # add product to cart
        driver.find_element(By.CLASS_NAME, "btn_primary").click()
        time.sleep(1)
        response_data = driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge").text
        self.assertIn('1', response_data)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
