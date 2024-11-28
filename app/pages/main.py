import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main import LocatorsMainPage


class MainPage:
    def __init__(self, app):
        self.app = app

    @allure.step("Get row result")
    def get_row_result(self, row: WebElement) -> dict:
        name = row.find_element(*LocatorsMainPage.grid_row_name_rel).text
        count = row.find_element(*LocatorsMainPage.grid_row_count_rel).text
        return {"name": name, "count": int(count)}

    @allure.step("Get grid results")
    def get_grid_results(self) -> list[dict]:
        wd = self.app.wd
        try:
            rows = WebDriverWait(wd, 5).until((EC.visibility_of_all_elements_located(LocatorsMainPage.grid_rows)))
            result = []
            for row in rows:
                result.append(self.get_row_result(row))
            return result
        except TimeoutException:
            return []

    @allure.step("Get row result by name: {name}")
    def get_row_result_by_name(self, name: str) -> dict:
        wd = self.app.wd
        row = WebDriverWait(wd, 5).until(EC.visibility_of_element_located(LocatorsMainPage.get_grid_row_by_name(name)))
        return self.get_row_result(row)