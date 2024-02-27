from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Search for coffee')
def search_for_coffee(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.XPATH, '//button[@data-test="@web/Search/SearchButton"]').click()
    sleep(3)

@then('Search results for coffee are shown')
def search_results_for_coffee(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'coffee' in actual_text, f'Expected word coffee not in actual text: {actual_text}'
