from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators1.contact_locators import ContactLocators

class Contactpage:


      def __init__(self, driver):
          self.driver = driver

      def click_contact_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ContactLocators.contact_btn))).click()

      def set_email(self, email):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ContactLocators.email))).send_keys(email)

      def set_name(self, name):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ContactLocators.name))).send_keys(name)

      def set_message(self, message):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ContactLocators.message))).send_keys(message)
          return message

      def click_send_message(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ContactLocators.send_message_btn))).click()
          WebDriverWait(self.driver, 5)

      def click_close_btn(self):
          WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, ContactLocators.close_btn))).click()
