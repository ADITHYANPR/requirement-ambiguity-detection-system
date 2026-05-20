import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_name = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
file_path = f"C:/Users/HP/Desktop/requirement_ambiguity_system/uploads/{file_name}"

from selenium import webdriver

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("http://127.0.0.1:5000")

upload = wait.until(EC.presence_of_element_located((By.NAME, "srs_file")))
upload.send_keys(file_path)

upload.submit()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard")))
wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

assert "Overall SRS Quality" in driver.page_source
assert "Severity" in driver.page_source
assert "Explanation" in driver.page_source

print("TEST PASSED: Advanced verification successful")

time.sleep(15)
driver.quit()
