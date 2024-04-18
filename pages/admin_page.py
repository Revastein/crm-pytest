from base.base_class import BaseClass
from base.base_page import BasePage
from config.links import Links


class AdminPage(BasePage, BaseClass):
    page_url = Links.ADMIN_PAGE
