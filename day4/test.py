from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_saucedemo:


    def test_empty_usernameAndPassword(self):

        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginButton.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(1)
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu: {testResult}")


    def test_emptyPassword(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        input_username = driver.find_element(By.ID, "user-name")
        sleep(1)
        input_username.send_keys("1")
        sleep(1)
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(1)
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu: {testResult}")



    def test_locked_out_user(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        input_username = driver.find_element(By.ID, "user-name")
        sleep(1)
        input_password = driver.find_element(By.ID,"password")
        sleep(1)
        input_username.send_keys("locked_out_user")
        input_password.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Test sonucu: {testResult}")


    def test_redXButtons(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginButton.click()
        sleep(2)        


        firstRedX = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")
        sleep(1)
        secondRedX= driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")
        sleep(1)

        if firstRedX.is_displayed():
            if secondRedX.is_displayed():
                print("Test Basarili, kirmizi X ler mevcut.")
        sleep(1)






        closeWarningButton = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(1)
        closeWarningButton.click()
        sleep(2)

        isRedButtonsStillExists = len(driver.find_elements(By.CLASS_NAME,"error_icon"))>0

        if isRedButtonsStillExists:
            print("Butonlar kapatilmamis.")
        else:
            print("Butonlar kapatilmis, test basarili.")

        # try: driver.find_elements(By.CLASS_NAME,"error_icon")
        # except:
        #     print("Butonlar kapatilmamis")




    def test_standart_user(self):
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        input_username = driver.find_element(By.ID, "user-name")
        sleep(1)
        input_password = driver.find_element(By.ID,"password")
        sleep(1)
        input_username.send_keys("standard_user")
        input_password.send_keys("secret_sauce")
        sleep(5)

        loginButton = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginButton.click()
        sleep(2)


        currentUrl =driver.current_url

        if currentUrl == "https://www.saucedemo.com/inventory.html" : 
            print("Test succeed, signed in.")
        else:
            print("Test failed.")

        urunListesi = driver.find_elements(By.CLASS_NAME,"inventory_item")

        if len(urunListesi) == 6:
            print("Test succeed, 6 product listed.")
        else:
            print("Test failed.")










testSauce =  Test_saucedemo()
testSauce.test_empty_usernameAndPassword()
testSauce.test_emptyPassword()
testSauce.test_locked_out_user()
testSauce.test_redXButtons()
testSauce.test_standart_user()