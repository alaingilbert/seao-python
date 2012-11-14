from bs4 import BeautifulSoup
from seao.errors import NotLoggedError, InvalidUsernamePasswordError

import requests


class Seao:
    url_index = 'https://seao.ca/index.aspx'
    url_monseao = 'http://seao.ca/SEAO/monseao.aspx'
    url_viewfile = 'https://seao.ca/GenericComponents/CUG10/viewFile.aspx?itemid=%s'


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()
        self.login()


    def login(self):
        res = self.session.get(self.url_index).text
        soup = BeautifulSoup(res)
        data = {'Login1:loginButton': 'Enter',
                'Login1:passwordTextBox': self.password,
                'Login1:usernameTextBox': self.username,
                'UCFooterMenu1:WiseScroll1': '',
                'UCOpportunitySearch1:txtSearchInput': '',
                '__EVENTARGUMENT': '',
                '__EVENTTARGET': '',
                '__EVENTVALIDATION': soup.find(id='__EVENTVALIDATION').get('value'),
                '__VIEWSTATE': '',
                '__VIEWSTATE_SERSIDE': 1}
        res = self.session.post(self.url_index, data).text
        if res.find('window.location.replace') == -1:
            raise InvalidUsernamePasswordError()


    def logout(self):
        res = self.session.get(self.url_monseao).text
        soup = BeautifulSoup(res)
        data = {'UCFooterMenu1:WiseScroll1': '',
                'UCOpportunitySearch1:txtSearchInput': '',
                '__EVENTARGUMENT': 'Quit',
                '__EVENTTARGET': 'UCSessionBasketMenu1$ASPnetMenu1',
                '__EVENTVALIDATION': soup.find(id='__EVENTVALIDATION').get('value'),
                '__VIEWSTATE': '',
                '__VIEWSTATE_SERSIDE': 2}
        res = self.session.post(self.url_monseao, data).text
        soup = BeautifulSoup(res)
        data = {'UCFooterMenu1:WiseScroll1': '',
                'UCMessageBox1:buttonYes': 'Oui',
                '__EVENTARGUMENT': '',
                '__EVENTTARGET': '',
                '__EVENTVALIDATION': soup.find(id='__EVENTVALIDATION').get('value'),
                '__VIEWSTATE': '',
                '__VIEWSTATE_SERSIDE': 3}
        self.session.post(self.url_monseao, data)
        self.session = requests.session()


    def get_file(self, item_id):
        res = self.session.get(self.url_viewfile % item_id).content
        if res.find('window.location.replace') != -1:
            raise NotLoggedError()
        else:
            return res
