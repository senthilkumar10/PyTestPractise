from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

  # URL

  URL = 'https://www.duckduckgo.com'

  # Locators

  SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

  # Initializer

  def __init__(self, driver):
    self.driver = driver

  # Interaction Methods

  def load(self):
    self.driver.get(self.URL)

  def search(self, phrase):
    self.driver.find_element(*self.SEARCH_INPUT).send_keys(phrase + Keys.RETURN)