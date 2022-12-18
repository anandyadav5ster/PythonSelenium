from selenium import webdriver
import pytest

def test_openBrowser():
    global driver
    driver = webdriver.Chrome("/Users/anandyadav/Desktop/Softwares/chromedriver.exe")

def test_openURL():
    driver.get("https://www.amazon.com")

def test_closeDriver():
    driver.close()


