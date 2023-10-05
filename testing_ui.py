import pytest

from test_page import OperationHelper
import yaml

with open('testdata.yaml') as fy:
    testdata = yaml.safe_load(fy)


def test_authorize_invalid(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_botton()

    assert testpage.get_error_text() == '401'


@pytest.mark.contact
def test_authorize_valid(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_botton()

    assert testpage.get_success_text() == f'Hello, {testdata["username"]}', 'not enty'


def test_add_new_post(browser):
    testpage = OperationHelper(browser)
    testpage.click_new_post_botton()
    testpage.enter_title_new_post(testdata['title'])
    testpage.enter_description_new_post(testdata['description'])
    testpage.enter_content_new_post(testdata['content'])
    testpage.click_save_new_post()