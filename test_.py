import time

from selenium import webdriver
def test_simple():
    # path = 'C:\\Users\\AMALYGIN\\Downloads\\GitHUb\\jenkins\\Driver\\chromedriver.exe'
    # driver = webdriver.Chrome(executable_path = path)
    driver = webdriver.Firefox()
    driver.get("http://www.pt.energypluscompany.com/myinbound/login.php")
    driver.find_element_by_name("email").send_keys("aleksandr.malygin@nrg.com")
    driver.find_element_by_name("password").send_keys("energy")
    driver.find_element_by_id("button").click()
    time.sleep(1)
    assert 1 == 1
    driver.quit()
