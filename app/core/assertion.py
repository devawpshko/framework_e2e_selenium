import allure


class CustomAssertions:

    @staticmethod
    @allure.step("{message}")
    def list_of_dicts_has_dict(list_of_dicts: list[dict], dict_to_find: dict, message: str):
        for i_dict in list_of_dicts:
            found = False
            for key, value in dict_to_find.items():
                if i_dict[key] == value:
                    found = True
                else:
                    found = False
                    break
            if found is True:
                break
        raise AssertionError(f"{message} \n\n {dict_to_find} \n\n not found in \n\n {list_of_dicts}")
