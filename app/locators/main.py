from selenium.webdriver.common.by import By

class LocatorsMainPage:
    grid_rows = (By.XPATH, "//table//div[@class='grid-row']")
    grid_row_name_rel = (By.XPATH, ".//td[@id='name']")
    grid_row_count_rel = (By.XPATH, ".//td[@id='count']")

    @staticmethod
    def get_grid_row_by_name(name: str):
        return By.XPATH, f"//table//td[@id='name' and text()='{name}']//ancestor::div[@class='grid-row']"

    title_input = (By.XPATH, "//input[@id='title']")