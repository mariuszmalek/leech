def girisYap(self, username=False, password=False):
        base_warnings = self.BASE_UYARI(metod=self.girisYap, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.girisYap, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.girisYap)

        try:
            if not username and not password:
                print(" ")
                print(" ")
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 1)
                username = input(self.configGetir(base_inputs+"input1"))
                password = getpass.getpass(prompt=self.configGetir(base_inputs+"input2"))
            elif not username:
                username = input(self.configGetir(base_inputs+"input1"))
            elif not password:
                password = getpass.getpass(prompt=self.configGetir(base_inputs+"input2"))

            if not username and not password:
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
                self.girisYap()
            elif not username:
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
                self.girisYap(False, password)
            elif not password:
                self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 2)
                self.girisYap(username, False)

            print(self.configGetir(base_warnings+"warning5"))
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            usernameInput = self.driver.find_elements_by_css_selector('form input')[0]
            passwordInput = self.driver.find_elements_by_css_selector('form input')[1]
            usernameInput.send_keys(username.strip())
            passwordInput.send_keys(password.strip())
            passwordInput.send_keys(Keys.ENTER)
            sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
            self.girisKontrol()
            if self.girisYapildimi:
                self.aktifKullaniciGetir()
                self.bildirimThreadOlustur()
                self.menu()
            else:
                self.inputTemizle(usernameInput)
                self.inputTemizle(passwordInput)
                self.girisYap()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(hata=str(error)), 2)