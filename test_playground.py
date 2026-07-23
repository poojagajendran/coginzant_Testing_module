import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("message",["Hello","Selenium Automation","12345"])
def test_simple_form_submission(driver,base_url,message):
    driver.get(base_url+"simple-form-demo")
    box=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"user-message")))
    box.clear(); box.send_keys(message)
    driver.find_element(By.ID,"showInput").click()
    out=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"message")))
    assert out.text==message

def test_checkbox_demo(driver,base_url):
    driver.get(base_url+"checkbox-demo")
    cb=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='checkbox']")))
    cb.click(); assert cb.is_selected()
    cb.click(); assert not cb.is_selected()

def test_dropdown_selection(driver,base_url):
    driver.get(base_url+"select-dropdown-demo")
    sel=Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"select-demo"))))
    sel.select_by_visible_text("Wednesday")
    assert sel.first_selected_option.text=="Wednesday"
