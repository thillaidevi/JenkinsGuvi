from selenium import webdriver


def test_login_with_valid_cred():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    print(driver.title)

def test_login_with_invalid_cred():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    print(driver.title)

def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    print(driver.title)