#NOTE: ref to man page: https://selenium-python.readthedocs.io/navigating.html#moving-between-windows-and-frames

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

# set up driver for Safari
driver = webdriver.Safari()

# navigate to a Apple Store
driver.get("https://www.apple.com/shop")

# -------
# wait to avoid dynamic animation
time.sleep(2)
# -------

# wait for search icon and then click
search_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "globalnav-menubutton-link-search"))
)
search_icon.click()

# Wait 10 seconds for the search input box to appear and then input the search term
input_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "globalnav-searchfield-input"))
)

input_box.send_keys("iPhone 15 Pro") # enter in iPhone model
time.sleep(2)
input_box.send_keys(Keys.RETURN) # press enter

time.sleep(5) # wait for search results to load

# img_element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//img[@src='https://www.apple.com/autopush/ww/search/modules/iphone15proandiphone15promax/image__btmvnyfmx16q_large_2x.jpg?']"))
# )
# img_element.click()






# close browser after 5 second wait
driver.implicitly_wait(5)
driver.quit()
