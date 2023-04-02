from project.SHClass67.pom.common import GetDriver


class PageLogin:
    username = ('id', 'username')
    password = ('id', 'password')
    checkcode = ('id', 'verifycode')
    login_button = ('xpath', '//button[contains(text(),"登录")]')

    def __init__(self):
        self.dr = GetDriver.get_driver()

    def login(self, username='admin', password='123456', checkcode='0000'):
        self.dr.get('http://192.168.18.128:8080/woniusales/')
        self.dr.find_element(*self.username).clear()
        self.dr.find_element(*self.username).send_keys(username)
        self.dr.find_element(*self.password).send_keys(password)
        self.dr.find_element(*self.checkcode).send_keys(checkcode)
        self.dr.find_element(*self.login_button).click()
