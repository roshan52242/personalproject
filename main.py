from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import logging
from brian import Speak2
from speech import listening_function
import pywhatkit as pw
from datetime import datetime
from face_checker import main
from Fileopener import openfile
import time


ScriptDir = pathlib.Path().absolute()
logging.basicConfig(level=logging.WARNING)
warnings.simplefilter("ignore")

url = ""
with open('passkey.txt','r') as f:
    url = f.read()
    


text_area = r"/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea"
submit_button = r"/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button"
reply_element = r"/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]"

def entry_animations():
    try:
        sleep(2)
        driver.find_element(by=By.XPATH,value=r"/html/body/div/main/div/div/button").click()
        sleep(2)
        driver.find_element(by=By.XPATH,value=r"/html/body/div/main/div/div/button").click()
        sleep(2)
        driver.find_element(by=By.XPATH,value=r"/html/body/div/main/div/div/div[1]/div[1]/div[2]/button[1]").click()
    except:
        pass
    finally:

        print(f"Jarvis : {chat_with_py('Hello Jarvis')}")
        # reply = chat_with_py("Hello Jarvis")
        # Speak2(reply)
        # Enable Audio
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button"))).click()


def response_taker():
    text_element_locator = (By.XPATH, reply_element)

    response_element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(text_element_locator)
    )


    response_text = response_element.text
    return response_text
        
def find_enabled():
    while True:
        driver.find_element(by=By.XPATH,value=text_area).send_keys("h")
        submit_enabled = driver.find_element(by=By.XPATH,value=submit_button).is_enabled()
        if submit_enabled:
            driver.find_element(by=By.XPATH,value=text_area).clear()
            break
        else:
            pass
def chat_with_py(text):
    input_element =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,text_area)))
    input_element.send_keys(text)
    input_element.clear()

    
    button_element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,submit_button)))
    button_element.click()
    find_enabled()
    response_text  = response_taker()


    return response_text

def find_audio():
    is_audio_playing = driver.execute_script("""
    var audioElements = document.querySelectorAll('audio');
    var isPlaying = false;
    for (var i = 0; i < audioElements.length; i++) {
        if (!audioElements[i].paused) {
            isPlaying = true;
            break;
        }
    }
    return isPlaying;
""")
    return is_audio_playing

def wait_for_audio():
    while find_audio():
        time.sleep(1) 




user_name = main()

user_name = "Roshan" if user_name == None else user_name 

chrome_option = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_option.add_argument("user-agent={user_agent}")
chrome_option.add_argument("--profile-directory=Default")
chrome_option.add_argument(f"user-data-dir={ScriptDir}\\DataBase\\{user_name}")
chrome_option.headless=True
chrome_option.add_argument("--headless=new")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option )
driver.get(url)
driver.maximize_window()
entry_animations()

while True:
    wait_for_audio()
    prompt = input("Enter your query : ")
    # prompt = listening_function()
    prompt = str(prompt).lower()

    if prompt !="":

        if "youtube" in prompt and "play" in prompt:
            prompt = prompt
            prompt = prompt.replace("youtube","")
            prompt = prompt.replace("jarvis","")
            prompt = prompt.replace("play","")
            prompt = prompt.replace("can","")
            prompt = prompt.replace("you","")
            prompt = prompt.replace("for","")
            prompt = prompt.replace("me","")
            Speak2("Playing {prompt} on Youtube") 
            pw.playonyt(prompt)

        elif "what" in prompt and "time" in prompt:
            time_now = datetime.now().strftime("%I:%M:%p")
         
            Speak2(f"The time is {time_now}")
        
        elif "open" in prompt:
            prompt = prompt.replace("open","")
            prompt = prompt.replace("jarvis","")
            prompt = prompt.replace("please","")
            prompt = prompt.replace("can","")
            prompt = prompt.replace("you","")
            prompt = prompt.replace("for","")
            prompt = prompt.replace("me","")
            Speak2(f"Opening {prompt}")

            openfile(prompt)


             

        else:
            wait_for_audio()
            print(f"Joel ==> {prompt}")
            reply = chat_with_py(prompt)
            # Speak2(reply)

        
            print("")
            print(f"Jarvis : {reply}")
            print("")
            

