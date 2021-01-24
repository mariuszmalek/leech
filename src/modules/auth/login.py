import getpass
from time import sleep
from ....src.system import get_config, show_in_console

def auth_login():

        username = 'mariuszmalek'
        password = 'malek4ever'

        #base_warnings = self.BASE_TRANSLATE(metod=self.authLogin, warnings=True)
        #base_inputs = self.BASE_TRANSLATE(metod=self.authLogin, inputs=True)
        #base_sleep = self.BASE_SLEEP(metod=self.authLogin)

        try:
            print(get_config(base_warnings+"warning5"))
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            usernameInput = self.driver.find_elements_by_css_selector('form input')[0]
            passwordInput = self.driver.find_elements_by_css_selector('form input')[1]
            usernameInput.send_keys(username.strip())
            passwordInput.send_keys(password.strip())
            passwordInput.send_keys(Keys.ENTER)
            sleep(get_config("{base}sleep2".format(base=base_sleep)))
            self.girisKontrol()
            if self.authStatus:
                self.aktifKullaniciGetir()
                self.bildirimThreadOlustur()
                self.menu()
            else:
                self.inputTemizle(usernameInput)
                self.inputTemizle(passwordInput)
                self.authLogin()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning6")).format(hata=str(error)), 2)