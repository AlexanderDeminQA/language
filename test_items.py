from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

class TestingOne():
    def test_stop(self, browser):
        browser.get(link)
