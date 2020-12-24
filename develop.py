import os, zipfile
import time

from selenium import webdriver

# Configure filepaths
chrome_exe = './drivers/chromedriver.exe'
ext_dir = 'extension'
ext_file = './UBExtension.crx'

# Create zipped extension
# Read in your extension files

# Save files to zipped archive
with zipfile.ZipFile('sp.zip', mode='w') as myzip:
    myzip.write(ext_file)


# Add extension
#  chrome_options = webdriver.ChromeOptions()
# chrome_options.add_extension('sp.zip')

# Start driver
driver = webdriver.Chrome(executable_path=chrome_exe)
driver.get('chrome://extensions/')
time.sleep(2000)
driver.quit()
