import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_locators.locators import test_locators
from Test_Excel_functions.excel_functions import all_excel_functions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class Test_zenclass:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        excel_file = 'C:\\Users\\Admin\\Desktop\\TASK_27\\ZenClass\\Test_Datas\\test_data.xlsx'
        sheet_name = 'Sheet1'
        self.s = all_excel_functions(excel_file, sheet_name)
        self.rows = self.s.row_count()
        yield
        self.driver.close()
    
    def test_login(self, boot):
        self.driver.get(test_locators.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 8)
        start_row = 2
        end_row = 6

        for row_no in range(start_row, end_row + 1):
            username = self.s.read_data(row_no, 5)
            password = self.s.read_data(row_no, 6)
            print(username)
            print(password)
            
            username_element = wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Email)))
            username_element.send_keys(username)
            
            password_element = wait.until(EC.visibility_of_element_located((By.NAME, test_locators().Password)))
            password_element.send_keys(password)
            
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, test_locators().Login_button)))
            login_button.click()

            try:
                wait.until(EC.url_matches('https://www.zenclass.in/class'))
                self.s.write_data(row_no, 7, "TEST PASS")
                print("SUCCESS : Logged in with Username {a} & {b}".format(a = username, b = password))


                profile_image = wait.until(EC.presence_of_element_located((By.XPATH, test_locators().Profile_image)))
                profile_image.click()
                logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, test_locators().Logout_button)))
                logout_button.click()

                wait.until(EC.url_matches("https://www.zenclass.in/login"))
                
            except TimeoutException:
                self.s.write_data(row_no, 7, "TEST FAIL")

                assert self.driver.current_url == 'https://www.zenclass.in/login'
                print("FAIL : Login failed with Username {a} & {b}".format(a = username, b = password))

                self.driver.refresh()
                
