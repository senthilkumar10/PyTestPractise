"""
These tests cover DuckDuckGo searches.

To Run it in Parallel mode - Make sure to install pytest-xdist 

Command ==> pytest test_search.py -n 3 ==> This will open three browsers and run it in parallel

install allure-pytest

command ==> pytest -v -s test_search.py --alluredir=/home/senthil/Documents/MyProjects/PyTestPractise/reports

"""

import pytest
import allure
import sys
sys.path.append('../')

from pages.results import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@allure.description("Validation of Search Results")
@allure.severity(severity_level = "NORMAL")
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(setup, phrase):
  search_page = DuckDuckGoSearchPage(setup)
  result_page = DuckDuckGoResultPage(setup)
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for the phrase
  search_page.search(phrase)

  # Then the search result query is the phrase
  assert phrase == result_page.search_input_value()
  
  
  # And the search result links pertain to the phrase
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

  # And the search result title contains the phrase
  # (Putting this assertion last guarantees that the page title will be ready)
  assert phrase in result_page.title()
