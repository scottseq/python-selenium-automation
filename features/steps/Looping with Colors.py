from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


COLOR_OPTIONS = (By. CSS_SELECTOR, "[class*='ButtonWrapper'] ing")
SELECTED_COLOR = (By. CSS_SELECTOR,"[class*='styles__ButtonWrapper]")



@given('Open target product A-88357757 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/A-88357757')
    sleep(6)



@then('verify user can click through colors')
def click_and_verify_colors(context):
    expected_color = ['Black',  'Brown',  'Magenta', 'Olive Green']
    actual_color = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()







        # @given('Open Target page')
        # def open_target_page(context):
        #  context.driver.get('https://www.target.com/')

        # @when('Search for tea')
        # def search_product(context):
        #  context.driver.find_element(By.ID, 'search').send_keys('tea')
        #    context.driver.find_element(By. XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
        #   sleep(5)

        # @then('Search results for tea are shown')
        # def verify_search_results_correct(context):
        #   actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
        #   assert'tea' in actual_text, f'Expected tea not found in {actual_text}'
        #  print('Test case passed')