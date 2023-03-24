from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Login_App:

    def __init__(self):
        self.login_form="//input[@id='email']"
        self.submit_button="//input[@name='submit']"
        self.account="//a[@class='listBox']//span[contains(text(),'BapanTestaccount2.adobelearningmanager.com')]"
        self.password_form="//input[@id='PasswordPage-PasswordField']"
        self.continue_button="//span[@class='spectrum-Button-label']"
        self.proceed_button="//input[@id='submitAction']"

    def login_prime(self,url,driver,email,password):
        driver.implicitly_wait(4)
        driver.get(url)
        login_form=driver.find_element(By.XPATH,self.login_form)
        login_form.send_keys(email)
        submit_button=driver.find_element(By.XPATH,self.submit_button)
        submit_button.click()
        account=driver.find_element(By.XPATH,self.account)
        account.click()
        sleep(20)
        password_form=driver.find_element(By.XPATH,self.password_form)
        password_form.send_keys(password)
        continue_button=driver.find_element(By.XPATH,self.continue_button)
        continue_button.click()
        sleep(20)
        proceed_button=driver.find_element(By.XPATH,self.proceed_button)
        proceed_button.click()
        sleep(20)
        driver.close()

    def login_app_activity(self,url,driver,email,password):
        driver.implicitly_wait(4)
        driver.get(url)
        login_form=driver.find_element(By.XPATH,self.login_form)
        login_form.send_keys(email)
        submit_button=driver.find_element(By.XPATH,self.submit_button)
        submit_button.click()
        account=driver.find_element(By.XPATH,self.account)
        account.click()
        sleep(15)
        password_form=driver.find_element(By.XPATH,self.password_form)
        password_form.send_keys(password)
        continue_button=driver.find_element(By.XPATH,self.continue_button)
        continue_button.click()
        sleep(15)
        proceed_button=driver.find_element(By.XPATH,self.proceed_button)
        proceed_button.click()
        sleep(15)
        return driver
    

class LearnerAPP:
    def __init__(self):
        self.mylearning="//span[@id='navigation.text.myLearning']"
        self.catalog="//a[@id='ember2028']//span[@class='small icon no float']//*[name()='svg']//*[name()='path'][9]"
        self.social="//a[@title='Social Learning']//span[@class='small icon no float']//*[name()='svg']"
        self.skills="//a[@id='ember2030']"
        self.toggle_0="//span[@class='large icon no float']//*[name()='svg']"
        self.toggle_1="//span[@class='large close icon no float']//*[name()='svg']//*[name()='path' and contains(@d,'M76.72 199')]"
        self.searchbox="//input[@id='globalSearchBox']"
        self.search_filter="//button[@id='searchScope']//*[name()='svg']//*[name()='circle'][2]"
        self.search_notes="//div[@name='searchIn'][normalize-space()='Notes']"
        self.search_course="//div[@name='searchIn'][normalize-space()='Course Metadata']"
        self.search_skills="//div[@name='searchIn'][normalize-space()='Badges']"
        self.all_boards='//*[@id="all"]'



    def click_apps_in_learnerapp(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(2)
        mylearning=driver.find_element(By.XPATH,self.mylearning)
        mylearning.click()
        sleep(10)
        catalog=driver.find_element(By.XPATH,self.catalog)
        catalog.click()
        sleep(10)
        social=driver.find_element(By.XPATH,self.social)
        social.click()
        sleep(10)
        skills=driver.find_element(By.XPATH,self.skills)
        skills.click()
        sleep(10)
        driver.close()


    def refresh_social_app(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(5)
        social=driver.find_element(By.XPATH,self.social)
        social.click()
        sleep(10)
        driver.get(driver.current_url)
        sleep(10)
        driver.maximize_window()
        driver.close()

    def toggle_panel(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(5)
        social=driver.find_element(By.XPATH,self.social)
        social.click()
        sleep(10)
        driver.get(driver.current_url)
        sleep(10)
        driver.maximize_window()
        toggle0=driver.find_element(By.XPATH,self.toggle_0)
        toggle0.click()
        sleep(3)
        toggle1=driver.find_element(By.XPATH,self.toggle_1)
        toggle1.click()
        sleep(3)
        driver.close()

    def scroll_social_page(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(5)
        social=driver.find_element(By.XPATH,self.social)
        social.click()
        sleep(10)
        driver.get(driver.current_url)
        sleep(10)
        driver.maximize_window()
        sleep(5)
        driver.execute_script('window.scrollBy(0,3000)')
        sleep(20)
        driver.minimize_window()
        driver.close()
    
    def explore_serachbox(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(5)
        search_box=driver.find_element(By.XPATH,self.searchbox)
        search_box.send_keys("Course hello")
        sleep(4)
        search_filter=driver.find_element(By.XPATH,self.search_filter)
        search_filter.click()
        sleep(10)
        driver.close()

    def uncheck_dropdown_checkboxes(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(5)
        search_box=driver.find_element(By.XPATH,self.searchbox)
        search_box.send_keys("Course hello")
        sleep(4)
        search_filter=driver.find_element(By.XPATH,self.search_filter)
        search_filter.click()
        select_course=driver.find_element(By.XPATH,self.search_course)
        if select_course.is_selected():
           select_course.click()
           sleep(1)
        select_course.click()
        sleep(1)
        select_notes=driver.find_element(By.XPATH,self.search_notes)
        if select_notes.is_selected():
           select_notes.click()
           sleep(1)
        select_notes.click()
        sleep(1)
        select_skills=driver.find_element(By.XPATH,self.search_skills)
        if select_skills.is_selected():
           select_skills.click()
           sleep(1)
        select_skills.click()
        sleep(5)
        driver.get(driver.current_url)
        sleep(5)
        driver.close()

    def loop_uncheck_dropdown_checkboxes(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(5)
        search_box=driver.find_element(By.XPATH,self.searchbox)
        search_box.send_keys("Course hello")
        sleep(4)
        search_filter=driver.find_element(By.XPATH,self.search_filter)
        search_filter.click()
        objs=driver.find_elements(By.NAME,"searchIn")
        for element in objs:
            element.click()
            sleep(2)
            element.click()
            sleep(2)
        driver.get(driver.current_url)
        sleep(2)
        driver.close()

    def explore_boards(self,url,driver,email,password):
        app=Login_App()
        driver=app.login_app_activity(url,driver,email,password)
        sleep(5)
        social=driver.find_element(By.XPATH,self.social)
        social.click()
        sleep(10)
        driver.get(driver.current_url)
        sleep(2)
        driver.switch_to.frame("socialIframe")
        driver.find_element(By.ID,"all").click()
        sleep(10)
        driver.find_element(By.ID,"my").click()
        sleep(10)
        driver.close()


        
        









