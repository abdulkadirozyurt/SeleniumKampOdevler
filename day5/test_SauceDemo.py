from time import sleep
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date




class Test_saucedemoClass:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    
    def test_emptyUsernameAndPassword(self):

        self.waitForElementVisible((By.ID,"login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")        
        loginButton.click()
        
        # errorMessageLocator=[(By.ID,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")]
        self.waitForElementVisible((By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test_emptyUsernameAndPassword.png")

        assert errorMessage.text == "Epic sadface: Username is required"
       

    @pytest.mark.parametrize("username",["admin1","admin2","admin3"])
    def test_emptyPassword(self,username):
        
        self.waitForElementVisible((By.ID,"user-name"))
        self.waitForElementVisible((By.ID,"login-button"))

        input_username = self.driver.find_element(By.ID, "user-name")        
        input_username.send_keys(username)       

        loginButton = self.driver.find_element(By.ID, "login-button")        
        loginButton.click()

        self.waitForElementVisible((By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test_emptyPassword-{username}.png")

        assert errorMessage.text == "Epic sadface: Password is required"
        


    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_out_user(self,username,password):
        
        self.waitForElementVisible((By.ID,"user-name"))
        self.waitForElementVisible((By.ID,"password"))
        self.waitForElementVisible((By.ID,"login-button"))

        input_username = self.driver.find_element(By.ID, "user-name")        
        input_password = self.driver.find_element(By.ID,"password")        
        input_username.send_keys("locked_out_user")
        input_password.send_keys("secret_sauce")
        
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test_locked_out_user.png")

        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        

    
    def test_redXButtons(self):
        
        self.waitForElementVisible((By.ID, "login-button"))
        loginButton = self.driver.find_element(By.ID, "login-button")        
        loginButton.click()

        self.waitForElementVisible((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg"))     
        self.waitForElementVisible((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg"))        

        firstRedX = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")        
        secondRedX= self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")
        
        

        if firstRedX.is_displayed():
            if secondRedX.is_displayed():
                assert True
        else: False

        self.waitForElementVisible((By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3/button"))
        closeWarningButton = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3/button")        
        closeWarningButton.click()        

        isRedButtonsStillExists = len(self.driver.find_elements(By.CLASS_NAME,"error_icon"))>0

        if isRedButtonsStillExists:
            assert False
        else:
            assert True

        self.driver.save_screenshot(f"{self.folderPath}/test_redXButtons.png")
        
        # try: driver.find_elements(By.CLASS_NAME,"error_icon")
        # except:
        #     print("Butonlar kapatilmamis")
            
        

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_standart_user(self,username,password):
        
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID,"password"))
        self.waitForElementVisible((By.ID, "login-button"))

        input_username = self.driver.find_element(By.ID, "user-name")        
        input_password = self.driver.find_element(By.ID,"password")
        
        input_username.send_keys("standard_user")
        input_password.send_keys("secret_sauce")        
        
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        


        currentUrl =self.driver.current_url

        if currentUrl == "https://www.saucedemo.com/inventory.html" : 
            assert True
        else:
            assert False

        urunListesi = self.driver.find_elements(By.CLASS_NAME,"inventory_item")

        if len(urunListesi) == 6:
            assert True
        else:
            assert False
        
        self.driver.save_screenshot(f"{self.folderPath}/test_standart_user.png")

    
    def test_acceptedUsernamesAre(self):

        self.waitForElementVisible((By.ID,"login_credentials"))
        acceptedUsernamesBox = self.driver.find_element(By.ID,"login_credentials")

        if acceptedUsernamesBox.is_displayed():
            assert True
        else:
            assert False
        
        self.driver.save_screenshot(f"{self.folderPath}/test_acceptedUsernamesAre.png")
            


    def test_AddToCartButtons(self):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID,"password"))
        self.waitForElementVisible((By.ID, "login-button"))

        input_username = self.driver.find_element(By.ID, "user-name")        
        input_password = self.driver.find_element(By.ID,"password")
        
        input_username.send_keys("standard_user")
        input_password.send_keys("secret_sauce")        
        
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        
        self.waitForElementVisible((By.CLASS_NAME,"btn_small"))
        addToCartButtons = self.driver.find_elements(By.CLASS_NAME,"btn_small")        
        butonSayisi = len(addToCartButtons)
        
        self.driver.save_screenshot(f"{self.folderPath}/test_AddToCartButtons.png")
        assert butonSayisi==6

    def test_sortContainer(self):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID,"password"))
        self.waitForElementVisible((By.ID, "login-button"))

        input_username = self.driver.find_element(By.ID, "user-name")        
        input_password = self.driver.find_element(By.ID,"password")
        
        input_username.send_keys("standard_user")
        input_password.send_keys("secret_sauce")        
        
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

        self.waitForElementVisible((By.CLASS_NAME,"product_sort_container"))
        sortContainer = self.driver.find_element(By.CLASS_NAME,"product_sort_container")
        
        self.driver.save_screenshot(f"{self.folderPath}/test_sortContainer.png")
        assert sortContainer.is_displayed()
            
        

        
        

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
        
    
















        






    


