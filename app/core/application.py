import json
import os

from core.assertion import CustomAssertions
from core.base import CommonActions
from pages import Pages


class Application:

    def __init__(self, *args, **kwargs):
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(BASE_PATH, "../config.json")) as f:
            self.cfg = json.load(f)
        self.test_env = kwargs.get("test_env")
        self.worker_id = kwargs.get("worker_id")
        self.APP_URL = os.environ.get("APP_URL", self.cfg[self.test_env]["app_url"])
        self.API_URL = os.environ.get("API_URL", self.cfg[self.test_env]["api_url"])
        self.wd = kwargs.get("wd")

        self.user_email = self.cfg[self.test_env]["users"][self.worker_id]
        self.user_password = os.environ.get("USER_PASSWORD")

        # links
        self.common = CommonActions(self)
        self.assertion = CustomAssertions()
        self.page = Pages(self)