from selenium.webdriver.common.by import By
from behave import given, when, then

BOX_ICON = (By.CSS_SELECTOR,   "[class*='styles__BenefitTextContainer']")

@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')

@then('Search the benefit boxes')
def search_benefit_boxes(context, benefit_boxes):
    context.driver.find_elements(*BOX_ICON)

@then('Verify header has {expected_count} boxes')
def verify_header_has_expected_boxes(context, expected_count):
    verify_benefit_boxes = context.driver.find_elements(*BOX_ICON)
    assert len(verify_benefit_boxes) == expected_count, f'Expected {expected_count} boxes, but got {len(verify_benefit_boxes)}'
