
from teste import senha
from selenium import webdriver
import time
import pyperclip
import pyautogui
import smtplib
import email.message

def sendEmail(num):
    body = f'''
    Chegou no valor definido {num}
    '''

    msg = email.message.Message()
    msg['Subject'] = "Binance dollar"
    msg['From'] = '*****@********.com'
    msg['To'] = "*****@********.com"
    password = senha
    msg.add_header('Content-Type','text/html')
    msg.set_payload(body)

    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(msg['From'], password)
    smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("email enviado")

driver = webdriver.Edge(executable_path=r'./msedgedriver.exe')
driver.get('https://www.binance.com/pt-BR/my/wallet/account/main')
time.sleep(30)

catch = driver.find_element_by_class_name('css-6u02o9')
text = catch.text
pyperclip.copy(text)
value = pyperclip.paste()
list_1 = list(value)
list_1.remove(list_1[0])
list_1.remove(list_1[0])
list_1.remove(list_1[0])

string = ''.join(map(str, list_1))
number = float(string)

print(number)
time.sleep(10)

if (number <= 14.50):
    while (number <= 14.50):
        driver.get('https://www.binance.com/pt-BR/my/wallet/account/main')
        time.sleep(15)
        catch = driver.find_element_by_class_name('css-16rmdce')
        text = catch.text
        pyperclip.copy(text)
        value = pyperclip.paste()
        list_1 = list(value)
        list_1.remove(list_1[0])
        list_1.remove(list_1[0])
        list_1.remove(list_1[0])

        string = ''.join(map(str, list_1))
        number = float(string)

        print(number)
        time.sleep(15)

    sendEmail(number)

else:
    sendEmail(number)
 

      

