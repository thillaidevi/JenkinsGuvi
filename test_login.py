from selenium import webdriver

def test_login_with_valid_credential():
    driver=webdriver.Chrome()
    driver.get("https://facebook.com")
    print(driver.title)