import pytest
import allure

from testdata.data_main_page import data_verify_results


@allure.suite("Main page")
@allure.label("owner", "Sergei Borzakovskii")
class TestSuiteMainPage:

    @allure.id(1)
    @allure.title("Verify results displayed on the main page")
    @allure.description(
        "This test case verifies that the results are displayed on the main page"
    )
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("xray", "DEV-1000")
    @allure.label("jira", "DEV-1000")
    @allure.label("layer", "ui_tests")
    @allure.issue("DEV-2000")
    @allure.tag("grid", "main")
    @pytest.mark.parametrize("result", data_verify_results)
    def test_verify_results(self, app, result):
        app.common.open_page("/login")
        app.page.login.enter_username()
        app.page.login.enter_username()
        app.page.login.click_submit_btn()
        app.common.open_page("/main")
        results = app.page.main.get_grid_results()
        app.assertion.list_of_dicts_has_dict(
            results,
            result["expected_result"],
            "Verify expected result displayed on the main page"
        )