from selenium import webdriver
from Primeapp.login_app import Login_App,LearnerAPP
from time import sleep
import pytest

def test_prime_login():
        app=Login_App()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.login_prime(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()
        
def test_learner_mylearning_skills_catalog_social():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.click_apps_in_learnerapp(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()
        

def test_refresh_social_app():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.refresh_social_app(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()


def test_click_all_board():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.toggle_panel(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()



def test_scroll_social_page():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.scroll_social_page(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()


def test_search_course():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.explore_serachbox(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()

def test_checkbox_dropdown():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.uncheck_dropdown_checkboxes(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()



def test_loop_checkbox_dropdown():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.loop_uncheck_dropdown_checkboxes(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()


def test_explore_all_boards():
        app=LearnerAPP()
        url="https://learningmanagerqe.adobe.com/acapindex.html"
        driver=webdriver.Chrome(executable_path="chromedriver")
        app.explore_boards(url,driver,"bapan1690814@gmail.com","Learner#12")
        driver.close()




    

    











