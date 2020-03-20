from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


print("─────█─▄▀█──█▀▄─█─────")
print("────▐▌──────────▐▌────")
print("────█▌▀▄──▄▄──▄▀▐█────")
print("───▐██──▀▀──▀▀──██▌───")
print("──▄████▄──▐▌──▄████▄──")
print("\n")
print(">>WHATSAPP MESSAGE BOMBER VERSION 1.0 :")
print(">>Created By [github/Khansaad1275] :")

print(">>>Keep Looking On The Terminal For All The Instruction ")
print("\n")



target = input("Enter The name of the person In Your Contact (Case sensitive) : ")
message = input("Enter Your Message : ")
amount = int(input("How Manny Times You Wanna Send Your Message : "))
delay = int(input("How Manny Sec Of Dealy between Every Message (please enter numbers only) : "))
print("🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥🖥")


driver = webdriver.Chrome()
print(">Opening Browser Window :")
driver.get("https://web.whatsapp.com/")
print(">>>Please Scan The QR Code : ")
wait = WebDriverWait(driver, 20)

try:
    x_arg = "//span[@title= '{}' ]".format(target)
    contact_name = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    contact_name.click()
    print(">Login successful : ")
except Exception as e:
    print(e)
    driver.close()


print("> " + target + "Selected : ")


try:
    text_box = wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))

    i = 1
    print(">>Started Sending Message : ")
    while i <= amount:
        time.sleep(delay)
        text_box.send_keys(message + Keys.ENTER)
        print(">>>Number of Message send : " + str(i))
        i += 1
    print(">>Sending Complete : ")
except:
    print("Please Type the Name properly we are unable to find contact name : " + target)
    driver.quit()
    input("PLEASE CLOSE THE TERMINAL AND RUN AGAIN!!")