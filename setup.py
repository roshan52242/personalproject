from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from jarvis import Jarvis_Base_Operations
import warnings
import logging


ScriptDir = pathlib.Path().absolute()
logging.basicConfig(level=logging.WARNING)
warnings.simplefilter("ignore")

url = ""
with open('passkey.txt','r') as f:
    url = f.read()
    


chrome_option = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_option.add_argument("user-agent={user_agent}")
chrome_option.add_argument("--profile-directory=Default")
name = input("Enter the user name : ")
chrome_option.add_argument(f"user-data-dir={ScriptDir}\\DataBase\\{name}")

chrome_option.headless=True
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option )
driver.get(url)
driver.maximize_window()
sleep(10000)