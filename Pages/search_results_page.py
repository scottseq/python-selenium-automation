from selenium.webdriver.common.by import By

from Pages.base_page import Page

class SearchResultsPage(Page):


    SEARCH_RESULTS_HEARDER = (By.CSS_SELECTOR, "")
    

    def verify_search_results_correct(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert 'coffee' in actual_text, f'Expected word coffee not in {actual_text} '


    def verfiy_search_results_page_url(self):
        url = self.driver.current_url
        assert expected_part_url in url, f'Expected {expected_part_url} not in {url}'
