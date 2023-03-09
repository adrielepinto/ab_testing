import time
import numpy as np

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#path_webdriver = '/Users/adriele/Documents/repos/ab_testing/notebooks/bayesian_test/chromedriver1'
#driver = webdriver.Chrome( path_webdriver )

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get( 'http://127.0.0.1:5001/home' )

clicks = 10000

for click in range( clicks ):
    if np.random.random() < 0.3:
        driver.find_element( 'name', 'yescheckbox' ).click()
        driver.find_element( 'id', 'yesbtn' ).click()
        time.sleep(0.5)
        
    else:
        driver.find_element( 'name', 'nocheckbox' ).click()
        driver.find_element( 'id', 'nobtn' ).click()
        time.sleep(0.5)
