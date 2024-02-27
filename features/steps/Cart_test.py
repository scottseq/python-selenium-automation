from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open Target main page')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')

@when('Open Cart icon')
def open_cart_icon(context):
    context.driver.find_element(By. CSS_SELECTOR,"[data-test='@web/CartLink']").click()
    sleep(5)
@then('Target cart')
def target_cart(context):
    actual_cart = context.driver.find_element(By. CSS_SELECTOR, "[class*='StyledHeading']").text
    assert 'Your cart is empty' ==actual_cart, f"Expected {'Your cart is empty'} but got {actual_text}"

#question3
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By. CSS_SELECTOR, "[data-test='@web/AccountLinkMobile")
    context.driver.find_element(By. CSS_SELECTOR, "[data-test='@web/accountNav-signIn").click()

@then('Verify Sign In Open')
def verify_sign_in(context):
    actual_cart = context.driver.find_element(By. CSS_SELECTOR, "#username")
