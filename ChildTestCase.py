import time

from selenium.webdriver.common.by import By
from BaseTestClass import BaseTestCase


class ChildTestCase(BaseTestCase):
    def test_registration(self):
        self.driver.get(self.url)
        # Find the "Sign Up" button by its XPath (you can use other methods like ID or class as well)
        sign_up_button = self.driver.find_element(By.XPATH, "This element is inside Shadow DOM and for such elements XPath won't support.")
        # Click on the "Sign Up" button
        sign_up_button.click()
        # Wait for a few seconds to ensure the page loads
        time.sleep(5)
        expected_register_url = "https://www.abcmouse.com/abt/register"
        current_registration_url = self.driver.current_url
        self.assertEqual(expected_register_url, current_registration_url, "Expected URL does not match current URL")
        # Find the email input field by its ID (you can use other locators)
        email_input = self.driver.find_element(By.ID, "user_email")
        email_input.send_keys(self.email_address)

        # Find the email input field by its XPath (you can use other methods like ID or name as well)
        email_input = self.driver.find_element_by_xpath("//input[@id='user_email']")
        # Enter the email address
        email_address = "example@example.com"  # Replace with the email address you want to enter
        email_input.send_keys(email_address)
        # Find the "Submit" button by its XPath (you can use other methods like ID or name as well)
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        # Click the "Submit" button
        submit_button.click()
        # Wait for a few seconds sp page can load
        time.sleep(5)
        # Verify that the current URL is the subscription page URL
        expected_url = "https://www.abcmouse.com/abt/subscription"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, "Expected URL does not match current URL")
        membership_text_element = self.driver.find_element_by_xpath("//*[contains(text(), 'Try it FREE for 30 days!')]")
        # Check if the element is visible on the page
        is_visible = membership_text_element.is_displayed()
        self.assertTrue(is_visible, "The 'Become a Member!' text is not visible on the page")


x = ChildTestCase()
x.test_registration()
