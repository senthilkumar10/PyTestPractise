
import json
import pytest
from selenium import webdriver
from pathlib import Path

@pytest.fixture
def config(scope='session'):

  # Read the file
  with open('../config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config


@pytest.fixture()
def setup(config):
    
    # Initialize the WebDriver instance
    if config['browser'] == 'Chrome':
        driver = webdriver.Chrome(Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"))
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = webdriver.Chrome(executable_path = Path.joinpath(Path.cwd().parent, "drivers", "chromedriver"),options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')


    #Maximize the browser
    driver.maximize_window()    

   # Make its calls wait for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    #Return the webdriver instance for the setup
    yield driver

    #Quit the webdriver instance
    driver.quit()