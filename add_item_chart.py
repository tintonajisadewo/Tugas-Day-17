import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_add_to_cart(self):
        # Login
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Add to cart
        driver.find_element(
            By.XPATH, "//div[@class='inventory_item'][1]//button[text()='Add to cart']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='inventory_item'][2]//button[text()='Add to cart']")\
            .click()
        time.sleep(2)

        # Go to cart
        driver.find_element(By.XPATH, "//a[text()='Open Menu']").click()
        driver.find_element(By.XPATH, "//a[text()='Cart']").click()
        time.sleep(2)

        # Verify added items
        added_items = driver.find_elements(
            By.XPATH, "//div[@class='cart_item']")
        self.assertEqual(2, len(added_items))
        item_names = [item.find_element(By.XPATH, ".//div[@class='inventory_item_name']")
                      .text for item in added_items]
        self.assertIn("Sauce Labs Backpack", item_names)
        self.assertIn("Sauce Labs Bolt T-Shirt", item_names)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
