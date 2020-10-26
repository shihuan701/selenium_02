from myselenium.page.main_page import MainPage


class TestWx():

    def setup(self):
        self.main = MainPage()


    def test_wx(self):
        username = 'sw039'
        acctid = '17777777739'
        phone = '17777777739'
        # addmember = self.main.goto_addmember_index()
        addmember = self.main.goto_addmember_nav()
        addmember().add_member(username,acctid,phone)
        assert username in addmember().get_member(username)
