from builtins import print

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime
import os
import urllib.request
import requests
import getpass
from colorama import init
import threading
from random import randint
import json
from src.modules.auth import auth_login
from src.system import configFile, get_config, dosyaMevcutMu, show_in_console

class Instagram():
    def __init__(self):
        init(convert=True)
        self.dil = None
        configFile()
        self.getLanguage()
        self.script()
        self.tarayiciThreadOlustur()
        self.authStatus = False
        self.aktifKullanici = ""
        self.index = 1
        self.BASE_URL = "https://www.instagram.com/"

    def script(self):
        print("")
        show_in_console("# ==============================================================================", 1)
        show_in_console("# author       : Mariusz Malek", 1)
        show_in_console("# linkedin     : https://www.linkedin.com/in/mariuszmalek", 1)
        show_in_console("# github       : https://github.com/mariuszmalek", 1)
        show_in_console("# email        : contact < at > mariuszmalek[.]com", 1)
        show_in_console("# date         : 23.01.2021", 1)
        show_in_console("# version      : 1.0", 1)
        show_in_console("# ==============================================================================", 1)
        print("")

    def menu(self):
        menu = get_config("languages.{dil}.menu".format(dil=self.dil))
        for secenek in menu:
            show_in_console(secenek, 3)
        self.islemSec()

    def islemSec(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.islemSec, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.islemSec, inputs=True)
        secim = input(get_config(base_inputs + "input1")).strip()
        if secim:
            try:
                secim = int(secim)
                if 0 < secim < 27:
                    self.secilenIslemiGoster(secim)
                    if secim in [1, 2, 3, 9, 12, 20, 21, 22, 23]:
                        self.profilSec(secim)
                    elif secim == 4:
                        self.topluTakiptenCik()
                    elif secim == 5:
                        self.topluYorumYapma()
                    elif secim == 6:
                        self.takipEtmeyenleriTakiptenCik()
                    elif secim == 7:
                        self.topluMesajSilme()
                    elif secim == 8:
                        self.oneCikanHikayeIndir()
                    elif secim in [10, 11]:
                        self.gonderiIndir()
                    elif secim == 13:
                        self.kullaniciListesiTakipEt(secim=secim)
                    elif secim == 14:
                        self.gonderiBegenenleriTakipEt()
                    elif secim == 15:
                        self.followUsersByTag()
                    elif secim == 16:
                        self.likingPostsByTag()
                    elif secim == 17:
                        self.gonderiBegen()
                    elif secim == 18:
                        self.gonderiBegen(False)
                    elif secim == 19:
                        self.commentingPost()
                    elif secim == 24:
                        self.ayarlar()
                    elif secim == 25:
                        self.oturumKapat()
                    elif secim == 26:
                        self.quit()
                    elif secim == 27:
                        self.commentPostsByTag()
                else:
                    show_in_console(get_config(base_warnings + "warning1"), 2)
                    self.islemSec()
            except Exception:
                show_in_console(get_config(base_warnings + "warning2"), 2)
                self.islemSec()
        else:
            self.islemSec()

    def secilenIslemiGoster(self, secim):
        base_warnings = self.BASE_TRANSLATE(metod=self.secilenIslemiGoster, warnings=True)
        secimler = get_config("languages.{dil}.warnings.secilenIslemiGoster.secimler".format(dil=self.dil))
        print("")
        show_in_console(secimler.get(str(secim), get_config(base_warnings + "warning1")), 1)
        if secim < 24:
            show_in_console(get_config(base_warnings + "warning2"), 3)
        print("")

    def profilSec(self, secim):
        base_warnings = self.BASE_TRANSLATE(metod=self.profilSec, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.profilSec, inputs=True)

        kullanici = input(get_config(base_inputs + "input1")).strip()

        if not kullanici:
            self.profilSec(secim)

        self.anaMenuyeDonsunMu(kullanici)

        if self.kullaniciKontrol(kullanici):
            print(str(get_config(base_warnings + "warning1")).format(kullanici=kullanici))
            if secim == 1:
                self.gonderileriIndir(kullanici, secim)
            elif secim == 2:
                self.gonderileriBegen(kullanici, secim)
            elif secim == 3:
                self.gonderileriBegen(kullanici, secim, False)
            elif secim == 9:
                self.hikayeIndir(kullanici, secim)
            elif secim == 12:
                self.kullaniciTakipcileriniTakipEt(kullanici, secim)
            elif secim == 20:
                self.kullaniciTakipEt(kullanici, secim)
            elif secim == 21:
                self.kullaniciTakipEt(kullanici, secim, False)
            elif secim == 22:
                self.kullaniciEngelle(kullanici, secim)
            elif secim == 23:
                self.kullaniciEngelle(kullanici, secim, False)
        else:
            show_in_console(str(get_config(base_warnings + "warning2")).format(kullanici=kullanici), 2)
            self.profilSec(secim)

    def ilkGonderiTikla(self):
        ilkGonderi = self.driver.find_elements_by_css_selector("article div.v1Nh3")[0]
        ilkGonderi.click()

    def gonderileriIndir(self, kullanici, secim):
        base_warnings = self.BASE_TRANSLATE(metod=self.gonderileriIndir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.gonderileriIndir)

        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print(str(get_config(base_warnings+"warning1")).format(
                    kullanici=kullanici))
                gonderiSayisi = self.gonderiSayisi()
                gonderiSayisi=int(self.metindenKarakterSil(gonderiSayisi,','))
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)
                self.ilkGonderiTikla()
                sleep(get_config("{base}sleep1".format(base=base_sleep)))
                self.klasorOlustur(kullanici)
                self.indexOne()
                for index in range(gonderiSayisi):
                    if self.gonderiAlbumMu():
                        self.klasorOlustur(str(self.index) + "_album")
                        tempIndex = self.index
                        self.indexOne()
                        self.getAlbumUrl()
                        self.klasorDegistir("../")
                        self.index = tempIndex + 1
                    else:
                        [url, veriTuru] = self.gonderiUrlGetir()
                        if url is not None:
                            self.dosyaIndir(url, veriTuru)
                        else:
                            continue
                    self.gonderiIlerlet()
                    sleep(get_config("{base}sleep2".format(base=base_sleep)))
                self.klasorDegistir("../")
                print(str(get_config(base_warnings+"warning2")).format(
                    kullanici=kullanici))
            else:
                show_in_console(str(get_config(base_warnings+"warning3")).format(
                    kullanici=kullanici), 2)

            self.profilSec(secim)
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning4")).format(kullanici=kullanici, hata=error), 2)
            self.profilSec(secim)

    def gonderileriBegen(self, kullanici, secim, durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.gonderileriBegen, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.gonderileriBegen)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print(str(get_config(base_warnings+"warning1")).format(
                    kullanici=kullanici))
                gonderiSayisi = self.gonderiSayisi()
                gonderiSayisi = int(self.metindenKarakterSil(gonderiSayisi, ','))
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)
                self.ilkGonderiTikla()
                sleep(get_config("{base}sleep1".format(base=base_sleep)))
                self.indexOne()
                for index in range(gonderiSayisi):
                    btn_begen = self.begenButon()
                    begeniDurum = self.begenButonuDurumGetir(btn_begen)
                    if durum:
                        if begeniDurum == "like":
                            show_in_console(str(get_config(base_warnings+"warning2")).format(index=str(self.index),
                                                                                                     url=self.driver.current_url), 1)
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            print(str(get_config(base_warnings+"warning3")).format(url=self.driver.current_url))
                            self.gonderiIlerlet()
                            sleep(get_config("{base}sleep2".format(base=base_sleep)))
                    else:
                        if begeniDurum == "unlike":
                            show_in_console(str(get_config(base_warnings+"warning4")).format(index=str(self.index),
                                                                                                     url=self.driver.current_url),
                                              1)
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            print(str(get_config(base_warnings+"warning5")).format(url=self.driver.current_url))
                            self.gonderiIlerlet()
                            sleep(get_config("{base}sleep3".format(base=base_sleep)))
                print(str(get_config(base_warnings+"warning6")).format(
                    kullanici=kullanici))
                self.profilSec(secim)
            else:
                if durum:
                    show_in_console(str(get_config(base_warnings+"warning7")).format(
                        kullanici=kullanici), 2)
                else:
                    show_in_console(str(get_config(base_warnings+"warning8")).format(
                        kullanici=kullanici), 2)
                self.profilSec(secim)
        except Exception as error:
            if durum:
                show_in_console(str(get_config(base_warnings+"warning9")).format(
                    kullanici=kullanici, hata=error), 2)
            else:
                show_in_console(str(get_config(base_warnings+"warning10")).format(
                    kullanici=kullanici, hata=error), 2)
            self.profilSec(secim)

    def topluTakiptenCik(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.topluTakiptenCik, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.topluTakiptenCik)
        try:
            print(get_config(base_warnings+"warning1"))
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            btn_takipEdilenler = self.takipEdilenlerButon()
            takipEdilenSayisi = btn_takipEdilenler.find_element_by_css_selector("span.g47SY").text
            takipEdilenSayisi = int(self.metindenKarakterSil(takipEdilenSayisi, ','))
            btn_takipEdilenler.click()
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            self.indexOne()
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = self.takipEdilenKullaniciAdiGetir(element=takip)
                    btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                    if btn_takip.text == "Following":
                        btn_takip.click()
                        sleep(get_config("{base}sleep2".format(base=base_sleep)))
                        try:
                            btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                            btn_onay.click()
                        except Exception as error:
                            show_in_console(str(get_config(base_warnings+"warning2")).format(
                                kullanici=takipEdilenKullanıcıAdi, hata=str(error)), 2)
                            continue
                        show_in_console(str(get_config(base_warnings+"warning3")).format(
                            index=self.index, kullanici=takipEdilenKullanıcıAdi), 1)
                        self.indexUp()
                        if (self.index - 1) >= takipEdilenSayisi:
                            devamEtsinMi = False
                            break
                        sleep3=get_config("{base}sleep3".format(base=base_sleep))
                        sleep(self.beklemeSuresiGetir(sleep3[0],sleep3[1]))
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        show_in_console(str(get_config(base_warnings+"warning4")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(get_config("{base}sleep4".format(base=base_sleep)))
            print(get_config(base_warnings + "warning5"))
            self.menu()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning6")).format(hata=str(error)), 2)
            self.menu()

    def topluYorumYapma(self, url=None, yorumSayisi=None, secilenIslem=None):
        base_warnings = self.BASE_TRANSLATE(metod=self.topluYorumYapma, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.topluYorumYapma, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.topluYorumYapma)
        sleep1 = get_config(base_sleep + "sleep1")
        try:
            if url is None:
                url = input(get_config(base_inputs + "input1")).strip()
                self.anaMenuyeDonsunMu(url)

                self.urlGirildiMi(url=url, metod=self.topluYorumYapma)
                self.urlGecerliMi(url=url, metod=self.topluYorumYapma)

                print(str(get_config(base_warnings + "warning1")).format(url=url))
                self.urlYonlendir(url)

                if not self.sayfaMevcutMu():
                    show_in_console(str(get_config(base_warnings + "warning2")).format(url=url), 2)
                    self.topluYorumYapma()

                if self.hesapGizliMi():
                    show_in_console(
                        str(get_config(base_warnings + "warning3")).format(
                            url=url), 2)
                    self.topluYorumYapma()

            if not yorumSayisi:
                yorumSayisi = input(get_config(base_inputs + "input2")).strip()
                self.anaMenuyeDonsunMu(yorumSayisi)
                if yorumSayisi.isnumeric() and int(yorumSayisi) > 0:
                    yorumSayisi = int(yorumSayisi)
                    if self.yorumLimitiAsildiMi(yorumSayisi):
                        yorumSayisi = 50
                        print(get_config(base_warnings + "warning4"))
                else:
                    show_in_console(get_config(base_warnings + "warning5"), 2)
                    self.topluYorumYapma(url=url, yorumSayisi=None, secilenIslem=None)

            if not secilenIslem:
                for secenek in get_config(base_warnings + "warning6"):
                    show_in_console(secenek, 3)
                secilenIslem = str(input(get_config(base_inputs + "input3")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                show_in_console(get_config(base_warnings + "warning7"), 1)
                print(str(get_config(base_warnings + "warning8")).format(url=url))
                for i in range(yorumSayisi):
                    yorum = self.rastgeleYorumGetir()
                    yorum = self.yorumUzunlukBelirle(yorum)
                    self.yorumYap(yorum)
                    show_in_console(str(get_config(base_warnings + "warning9")).format(index=i + 1), 1)

                    sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
            elif secilenIslem == "2":
                show_in_console(get_config(base_warnings + "warning10"), 1)
                dosya = self.dosyaSec()
                yorumlar = self.dosyaİceriginiAl(dosya)
                if self.dosyaİcerigiAlindiMi(yorumlar):
                    print(str(get_config(base_warnings + "warning11")).format(url=url))
                    for index, yorum in enumerate(yorumlar):
                        yorum = self.yorumUzunlukBelirle(yorum)
                        self.yorumYap(yorum)
                        show_in_console(str(get_config(base_warnings + "warning12")).format(index=index + 1), 1)
                        if (index + 1) == yorumSayisi:
                            break
                        sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
                else:
                    self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=secilenIslem)
            else:
                show_in_console(get_config(base_warnings + "warning13"), 2)
                print("")
                self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=None)

            print(str(get_config(base_warnings + "warning14")).format(url=url))
            self.topluYorumYapma()
        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning15")).format(url=url, hata=str(error)), 2)
            self.topluYorumYapma()

    def takipEtmeyenleriTakiptenCik(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.takipEtmeyenleriTakiptenCik, warnings=True)
        try:
            print(get_config(base_warnings + "warning1"))
            takipciler = self.takipcileriGetir()
            print(get_config(base_warnings + "warning2"))
            print(get_config(base_warnings + "warning3"))
            self.takipEdilenleriGetir(takipciler=takipciler)
            print(get_config(base_warnings + "warning4"))
            self.menu()
        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning5")).format(
                hata=str(error)), 2)
            self.menu()

    def topluMesajSilme(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.topluMesajSilme, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.topluMesajSilme)
        try:

            print(get_config(base_warnings+"warning1"))
            self.kullaniciProfilineYonlendir('direct/inbox/')
            devamEtsinMi = True
            silinenMesajlar = set()
            self.indexOne()
            while devamEtsinMi:
                mesajListesi = self.driver.find_elements_by_css_selector("div.N9abW  a.rOtsg")
                if len(mesajListesi) == 0:
                    print(get_config(base_warnings+"warning2"))
                    break
                for mesaj in mesajListesi:
                    if mesaj not in silinenMesajlar:
                        silinenMesajlar.add(mesaj)
                        kullaniciAdi = mesaj.find_element_by_css_selector("._7UhW9.xLCgt.MMzan.KV-D4.fDxYl").text
                        print(str(get_config(base_warnings+"warning3")).format(index=self.index,kullanici=kullaniciAdi))
                        self.mesajSil(mesaj)
                        show_in_console(str(get_config(base_warnings+"warning4")).format(index=self.index, kullanici=kullaniciAdi), 1)
                        self.indexUp()
                        sleep1 = get_config(base_sleep + "sleep1")
                        sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
                    break

            print(get_config(base_warnings+"warning5"))
            self.menu()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning6")).format(hata=str(error)),2)
            self.menu()

    def oneCikanHikayeIndir(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.oneCikanHikayeIndir, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.oneCikanHikayeIndir, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.oneCikanHikayeIndir)

        try:
            url = input(get_config(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url=url,metod=self.oneCikanHikayeIndir)
            self.urlGecerliMi(url=url,metod=self.oneCikanHikayeIndir)

            print(str(get_config(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)

            if not self.sayfaMevcutMu():
                show_in_console(get_config(base_warnings+"warning2"), 2)
                self.oneCikanHikayeIndir()

            print(str(get_config(base_warnings+"warning3")).format(url=url))
            btn_oynat = self.driver.find_element_by_css_selector("button._42FBe")
            btn_oynat.click()
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            kullanici = self.driver.find_element_by_css_selector("a.FPmhX").get_attribute("title")
            self.klasorOlustur(kullanici)
            self.indexOne()
            self.hikayeleriGetir()
            self.klasorDegistir("../")
            print(str(get_config(base_warnings+"warning4")).format(url=url))
            self.oneCikanHikayeIndir()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.oneCikanHikayeIndir()

    def hikayeIndir(self, kullanici, secim):
        base_warnings = self.BASE_TRANSLATE(metod=self.hikayeIndir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.hikayeIndir)

        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                if self.hikayeVarMi():
                    self.driver.find_element_by_css_selector("div.RR-M-").click()
                    sleep(get_config("{base}sleep1".format(base=base_sleep)))
                    print(str(get_config(base_warnings + "warning1")).format(
                        kullanici=kullanici))
                    self.klasorOlustur(kullanici)
                    self.indexOne()
                    self.hikayeleriGetir()
                    self.klasorDegistir("../")
                    print(str(get_config(base_warnings + "warning2")).format(
                        kullanici=kullanici))
                else:
                    show_in_console(get_config(base_warnings + "warning3"), 2)
            else:
                show_in_console(str(get_config(base_warnings + "warning4")).format(
                    kullanici=kullanici), 2)
            self.profilSec(secim)
        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning5")).format(hata=str(error)), 2)
            self.profilSec(secim)

    def gonderiKullaniciAdi(self):
        return self.driver.find_element_by_css_selector("a.sqdOP").text

    def gonderiIndir(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.gonderiIndir, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.gonderiIndir, inputs=True)
        try:
            url = input(get_config(base_inputs + "input1")).strip()
            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url=url, metod=self.gonderiIndir)
            self.urlGecerliMi(url=url, metod=self.gonderiIndir)

            print(str(get_config(base_warnings + "warning1")).format(url=url))
            self.urlYonlendir(url)
            if not self.hesapGizliMi():
                print(str(get_config(base_warnings + "warning2")).format(url=url))
                kullanici = self.gonderiKullaniciAdi()
                self.klasorOlustur(kullanici)
                if self.gonderiAlbumMu():
                    self.indexOne()
                    self.klasorOlustur(str(self.index) + "_album")
                    self.getAlbumUrl()
                    self.klasorDegistir("../")
                else:
                    [url, veriTuru] = self.gonderiUrlGetir()
                    if url is not None:
                        self.dosyaIndir(url, veriTuru)
                print(str(get_config(base_warnings + "warning3")).format(url=url))
                self.klasorDegistir("../")
            else:
                show_in_console(str(get_config(base_warnings + "warning4")).format(
                    url=url), 2)
            self.gonderiIndir()
        except Exception as error:
            print(
                show_in_console(str(get_config(base_warnings + "warning5")).format(hata=error), 2))
            self.gonderiIndir()

    def kullaniciTakipcileriniTakipEt(self, kullanici, secim, secilenIslem=None):
        base_warnings = self.BASE_TRANSLATE(metod=self.kullaniciTakipcileriniTakipEt, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.kullaniciTakipcileriniTakipEt, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.kullaniciTakipcileriniTakipEt)

        try:
            self.kullaniciProfilineYonlendir(kullanici)
            hedefTakipciSayisi = None

            if secilenIslem is None:
                for secenek in get_config(base_warnings + "warning1"):
                    show_in_console(secenek, 3)
                secilenIslem = str(input(get_config(base_inputs + "input1")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                show_in_console(get_config(base_warnings + "warning2"), 1)
            elif secilenIslem == "2":
                show_in_console(get_config(base_warnings + "warning3"), 1)
                hedefTakipciSayisi = input(get_config(base_inputs + "input2")).strip()
                self.anaMenuyeDonsunMu(hedefTakipciSayisi)
                if hedefTakipciSayisi.isnumeric():
                    hedefTakipciSayisi = int(hedefTakipciSayisi)
                else:
                    show_in_console(get_config(base_warnings + "warning4"), 2)
                    print("")
                    self.kullaniciTakipcileriniTakipEt(kullanici=kullanici,secim= secim, secilenIslem=secilenIslem)
            else:
                show_in_console(get_config(base_warnings + "warning5"), 2)
                print("")
                self.kullaniciTakipcileriniTakipEt(kullanici=kullanici,secim= secim, secilenIslem=None)

            if not self.hesapGizliMi():
                print(str(get_config(base_warnings + "warning6")).format(kullanici=kullanici))
                devamEtsinMi = True
                self.indexOne()

                if hedefTakipciSayisi is None:
                    takipciSayisi = self.driver.find_elements_by_css_selector("a.-nal3 > span.g47SY")[0].get_attribute(
                        'title')
                    takipciSayisi = int(self.metindenKarakterSil(takipciSayisi, ','))
                else:
                    kaynakTakipciSayisi = self.driver.find_element_by_css_selector(
                        "a.-nal3 > span.g47SY").get_attribute('title')
                    kaynakTakipciSayisi = int(self.metindenKarakterSil(kaynakTakipciSayisi, ','))
                    takipciSayisi = self.hedefKaynaktanBuyukMu(hedefTakipciSayisi, kaynakTakipciSayisi)

                btn_takipciler = self.takipcilerButon()
                btn_takipciler.click()
                sleep(get_config("{base}sleep1".format(base=base_sleep)))
                kontrolEdilenKullanicilar = set()
                while devamEtsinMi:
                    dialog_popup = self.driver.find_element_by_css_selector('div._1XyCr')
                    takipciListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                    for takipci in takipciListe:
                        takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                        takipciKullaniciAdi = takipciKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                        try:
                            btn_takip = takipci.find_element_by_css_selector('button.sqdOP')
                            if btn_takip.text == "Follow":
                                print(str(get_config(base_warnings + "warning7")).format(
                                    index=self.index, kullanici=takipciKullaniciAdi))
                                btn_takip.click()
                                self.indexUp()
                                if self.index-1  >= takipciSayisi:
                                    devamEtsinMi = False
                                    break
                                sleep2 = get_config("{base}sleep2".format(base=base_sleep))
                                sleep(self.beklemeSuresiGetir(sleep2[0], sleep2[1]))
                        except:
                            pass
                        kontrolEdilenKullanicilar.add(takipciKullaniciAdi)
                        if hedefTakipciSayisi:
                            if len(kontrolEdilenKullanicilar) >= kaynakTakipciSayisi:
                                devamEtsinMi = False
                        else:
                            if len(kontrolEdilenKullanicilar) >= takipciSayisi:
                                devamEtsinMi = False

                    if devamEtsinMi:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                        sleep(get_config("{base}sleep3".format(base=base_sleep)))
                print(str(get_config(base_warnings + "warning8")).format(kullanici=kullanici))
            else:
                show_in_console(str(get_config(base_warnings + "warning9")).format(kullanici=kullanici),
                                  2)
            self.profilSec(secim)
        except Exception as error:
            show_in_console(
                str(get_config(base_warnings + "warning10")).format(kullanici=kullanici, hata=str(error)), 2)
            self.profilSec(secim)

    def kullaniciListesiTakipEt(self,secim):
        dosya = self.dosyaSec()
        kullanicilar = self.dosyaİceriginiAl(dosya)
        if self.dosyaİcerigiAlindiMi(kullanicilar):
            self.kullanicilariTakipEt(kullanicilar, secim)
        else:
            self.kullaniciListesiTakipEt(secim)
        self.kullaniciListesiTakipEt(secim)

    def gonderiBegenenleriTakipEt(self, url=None,secilenIslem=None):
        base_warnings = self.BASE_TRANSLATE(metod=self.gonderiBegenenleriTakipEt, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.gonderiBegenenleriTakipEt, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.gonderiBegenenleriTakipEt)
        try:
            if url is None:
                url = input(get_config(base_inputs+"input1")).strip()
                self.anaMenuyeDonsunMu(url)
                self.urlGirildiMi(url=url,metod=self.gonderiBegenenleriTakipEt)
                self.urlGecerliMi(url=url,metod=self.gonderiBegenenleriTakipEt)
                print(str(get_config(base_warnings+"warning1")).format(url=url))
                self.urlYonlendir(url)

            hedefBegenenSayisi = None

            if secilenIslem is None:
                for secenek in get_config(base_warnings + "warning2"):
                    show_in_console(secenek,3)
                secilenIslem = str(input(get_config(base_inputs+"input2")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                show_in_console(get_config(base_warnings+"warning3"), 1)
            elif secilenIslem == "2":
                show_in_console(get_config(base_warnings+"warning4"), 1)
                hedefBegenenSayisi = input(get_config(base_inputs+"input3")).strip()
                self.anaMenuyeDonsunMu(hedefBegenenSayisi)
                if hedefBegenenSayisi.isnumeric():
                    hedefBegenenSayisi = int(hedefBegenenSayisi)
                else:
                    show_in_console(get_config(base_warnings+"warning5"), 2)
                    print("")
                    self.gonderiBegenenleriTakipEt(url=url,secilenIslem=secilenIslem)
            else:
                show_in_console(get_config(base_warnings+"warning6"), 2)
                print("")
                self.gonderiBegenenleriTakipEt(url=url,secilenIslem=None)

            if not self.hesapGizliMi():
                if not self.gonderiTipiVideoMu():
                    print(str(get_config(base_warnings+"warning7")).format(url=url))
                    devamEtsinMi = True
                    self.indexOne()


                    if hedefBegenenSayisi is None:
                        begenenSayisi = self.driver.find_element_by_css_selector(
                            "div.Nm9Fw > button.sqdOP > span").text
                        begenenSayisi = int(self.metindenKarakterSil(begenenSayisi, ','))
                    else:
                        kaynakBegenenSayisi = self.driver.find_element_by_css_selector(
                            "div.Nm9Fw > button.sqdOP > span").text
                        kaynakBegenenSayisi = int(self.metindenKarakterSil(kaynakBegenenSayisi, ','))
                        begenenSayisi = int(self.hedefKaynaktanBuyukMu(hedefBegenenSayisi, kaynakBegenenSayisi))

                    btn_begenenler = self.driver.find_element_by_css_selector("div.Nm9Fw > button.sqdOP")
                    btn_begenenler.click()
                    sleep(get_config("{base}sleep1".format(base=base_sleep)))
                    kontrolEdilenKullanicilar=set()
                    while devamEtsinMi:
                        dialog_popup = self.driver.find_element_by_css_selector("div.pbNvD")
                        begenenlerKullanicilar = dialog_popup.find_elements_by_css_selector('div.HVWg4')
                        for begenenKullanici in begenenlerKullanicilar:
                            begenenKullaniciAdi = begenenKullanici.find_element_by_css_selector(
                                "div.Igw0E > div.Igw0E > div._7UhW9  a").get_attribute('href')
                            begenenKullaniciAdi = begenenKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                            btn_takip = begenenKullanici.find_element_by_css_selector("div.Igw0E > button.sqdOP")
                            if btn_takip.text == "Follow":
                                print(str(get_config(base_warnings+"warning8")).format(
                                    index=self.index, kullanici=begenenKullaniciAdi))
                                btn_takip.click()
                                self.indexUp()
                                if self.index-1 >= begenenSayisi:
                                    devamEtsinMi = False
                                    break
                                sleep2=get_config("{base}sleep2".format(base=base_sleep))
                                sleep(self.beklemeSuresiGetir(sleep2[0],sleep2[1]))

                            kontrolEdilenKullanicilar.add(begenenKullaniciAdi)

                            if hedefBegenenSayisi:
                                if len(kontrolEdilenKullanicilar) >= kaynakBegenenSayisi:
                                    devamEtsinMi = False
                                    break
                            else:
                                if len(kontrolEdilenKullanicilar) >= begenenSayisi:
                                    devamEtsinMi = False
                                    break
                        if devamEtsinMi:
                            self.popupAsagiKaydir(secici='div[role="dialog"]  .i0EQd > div:nth-child(1)')
                            sleep(get_config("{base}sleep3".format(base=base_sleep)))
                        else:
                            print(get_config(base_warnings+"warning9"))
                else:
                    print(str(get_config(base_warnings+"warning10")).format(
                        url=url))
            else:
                show_in_console(str(get_config(base_warnings+"warning11")).format(url=url),
                                  2)
            self.gonderiBegenenleriTakipEt()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning12")).format(hata=str(error)), 2)
            self.gonderiBegenenleriTakipEt()

    def followUsersByTag(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.followUsersByTag, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.followUsersByTag)
        try:
            etiket = self.etiketGetir()

            limit = self.etiketeGoreIslemLimitiGetir(2)

            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            self.ilkGonderiTikla()
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            self.indexOne()

            print(str(get_config(base_warnings+"warning1")).format(etiket=etiket))
            while True:
                kullaniciAdi =self.driver.find_element_by_css_selector("div.e1e1d a.sqdOP").text
                btn_takip = self.driver.find_element_by_css_selector("div.bY2yH >button.sqdOP")
                if btn_takip.text != "Following":
                    btn_takip.click()
                    show_in_console(
                        str(get_config(base_warnings+"warning2")).format(index=self.index,
                                                                               kullanici=kullaniciAdi), 1)
                    self.indexUp()
                    if self.index-1 >= limit:
                        break
                    sleep(get_config("{base}sleep2".format(base=base_sleep)))
                    self.gonderiIlerlet()
                    sleep3=get_config("{base}sleep3".format(base=base_sleep))
                    sleep(self.beklemeSuresiGetir(sleep3[0],sleep3[1]))
                else:
                    print(str(get_config(base_warnings+"warning3")).format(kullanici=kullaniciAdi))
                    self.gonderiIlerlet()
                    sleep(get_config("{base}sleep4".format(base=base_sleep)))
            print(str(get_config(base_warnings+"warning4")).format(etiket=etiket))
            self.followUsersByTag()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.followUsersByTag()

    def commentPostsByTag(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.likingPostsByTag, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.likingPostsByTag)
        try:
            etiket = self.etiketGetir()
            limit = self.etiketeGoreIslemLimitiGetir(1)
            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            self.ilkGonderiTikla()
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            self.indexOne()

            print(str(get_config(base_warnings+"warning1")).format(etiket=etiket))
            while True:
                btn_begen = self.begenButon()
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if begeniDurum != "unlike":
                    btn_begen.click()
                    show_in_console(str(get_config(base_warnings+"warning2")).format(index=self.index,url=self.driver.current_url),1)
                    self.indexUp()
                    if self.index-1 >= limit:
                        break
                    sleep(get_config("{base}sleep2".format(base=base_sleep)))
                    self.gonderiIlerlet()
                    sleep3=get_config("{base}sleep3".format(base=base_sleep))
                    sleep(self.beklemeSuresiGetir(sleep3[0],sleep3[1]))
                else:
                    print(str(get_config(base_warnings+"warning3")).format(url=self.driver.current_url))
                    self.gonderiIlerlet()
                    sleep(get_config("{base}sleep4".format(base=base_sleep)))
            print(str(get_config(base_warnings+"warning4")).format(etiket=etiket))
            self.likingPostsByTag()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.likingPostsByTag()

    def likingPostsByTag(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.likingPostsByTag, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.likingPostsByTag)
        try:
            etiket = self.etiketGetir()
            limit = self.etiketeGoreIslemLimitiGetir(1)
            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            self.ilkGonderiTikla()
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            self.indexOne()

            print(str(get_config(base_warnings+"warning1")).format(etiket=etiket))
            while True:
                btn_begen = self.begenButon()
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if begeniDurum != "unlike":
                    btn_begen.click()
                    show_in_console(str(get_config(base_warnings+"warning2")).format(index=self.index,url=self.driver.current_url),1)
                    self.indexUp()
                    if self.index-1 >= limit:
                        break
                    sleep(get_config("{base}sleep2".format(base=base_sleep)))
                    self.gonderiIlerlet()
                    sleep3=get_config("{base}sleep3".format(base=base_sleep))
                    sleep(self.beklemeSuresiGetir(sleep3[0],sleep3[1]))
                else:
                    print(str(get_config(base_warnings+"warning3")).format(url=self.driver.current_url))
                    self.gonderiIlerlet()
                    sleep(get_config("{base}sleep4".format(base=base_sleep)))
            print(str(get_config(base_warnings+"warning4")).format(etiket=etiket))
            self.likingPostsByTag()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.likingPostsByTag()

    def gonderiBegen(self, durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.gonderiBegen, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.gonderiBegen, inputs=True)

        try:
            if durum:
                url = input(get_config(base_inputs+"input1")).strip()
            else:
                url = input(get_config(base_inputs+"input2")).strip()

            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url=url, metod=self.gonderiBegen,metodDeger=durum)
            self.urlGecerliMi(url=url,metod=self.gonderiBegen,metodDeger=durum)
            print(str(get_config(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)
            if not self.hesapGizliMi():
                if durum:
                    print(str(get_config(base_warnings+"warning2")).format(url=url))
                else:
                    print(str(get_config(base_warnings+"warning3")).format(url=url))
                btn_begen = self.begenButon()
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if durum:
                    if begeniDurum == "like":
                        btn_begen.click()
                        print(
                            show_in_console(str(get_config(base_warnings+"warning4")).format(url=self.driver.current_url),
                                              1))
                    else:
                        print(str(get_config(base_warnings+"warning5")).format(url=self.driver.current_url))
                else:
                    if begeniDurum == "unlike":
                        btn_begen.click()
                        show_in_console(str(get_config(base_warnings+"warning6")).format(url=self.driver.current_url), 1)
                    else:
                        print(str(get_config(base_warnings + "warning7")).format(url=self.driver.current_url))
                if durum:
                    print(str(get_config(base_warnings+"warning8")).format(url=url))
                else:
                    print(str(get_config(base_warnings+"warning9")).format(url=url))
            else:
                if durum:
                    show_in_console(str(get_config(base_warnings+"warning10")).format(
                        url=url), 2)
                else:
                    show_in_console(str(get_config(base_warnings+"warning11")).format(
                        url=url), 2)
            self.gonderiBegen(durum)
        except Exception as error:
            if durum:
                show_in_console(str(get_config(base_warnings+"warning12")).format(hata=error),2)
            else:
                show_in_console(str(get_config(base_warnings+"warning13")).format(hata=error), 2)
            self.gonderiBegen(durum)

    def commentingPost(self, url=None, yorum=None):
        base_warnings = self.BASE_TRANSLATE(metod=self.commentingPost, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.commentingPost, inputs=True)
        try:

            if url is None:
                url = input(get_config(base_inputs+"input1")).strip()
                self.anaMenuyeDonsunMu(url)
            if not yorum:
                yorum = input(get_config(base_inputs+"input2")).strip()
                self.anaMenuyeDonsunMu(yorum)


            self.urlGirildiMi(url=url,metod=self.commentingPost,metodDeger=yorum)
            self.urlGecerliMi(url=url,metod=self.commentingPost,metodDeger=yorum)


            if not self.checkLength(yorum):
                show_in_console(get_config(base_warnings+"warning1"), 2)
                self.commentingPost(url=url, yorum=None)

            print(str(get_config(base_warnings+"warning2")).format(url=url))
            self.urlYonlendir(url)

            if not self.sayfaMevcutMu():
                show_in_console(get_config(base_warnings+"warning3"), 2)
                self.commentingPost()

            if not self.hesapGizliMi():
                yorum = yorum[0:250]
                print(str(get_config(base_warnings+"warning4")).format(url=url))
                self.yorumYap(yorum)
                print(str(get_config(base_warnings+"warning5")).format(url=url))
            else:
                show_in_console(str(get_config(base_warnings+"warning6")).format(url=url), 2)
            self.commentingPost()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning7")).format(url=url,hata=str(error)),
                              2)
            self.commentingPost()

    def kullaniciTakipEt(self, kullanici, secim,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.kullaniciTakipEt, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print(str(get_config(base_warnings+"warning1")).format(kullanici=kullanici))
            else:
                print(str(get_config(base_warnings+"warning2")).format(kullanici=kullanici))


            self.kullaniciTakipDurumDegistir(kullanici=kullanici,durum=durum)
            if durum:
                print(str(get_config(base_warnings+"warning3")).format(kullanici=kullanici))
            else:
                print(str(get_config(base_warnings+"warning4")).format(kullanici=kullanici))
            if secim != 13:
                self.profilSec(secim)
        except Exception as error:
            if durum:
                show_in_console(str(get_config(base_warnings+"warning5")).format(kullanici=kullanici,hata=str(error)),2)
            else:
                show_in_console(str(get_config(base_warnings+"warning6")).format(kullanici=kullanici,
                                                                                         hata=str(error)), 2)
            if secim != 13:
                self.profilSec(secim)

    def kullaniciEngelle(self, kullanici, secim,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.kullaniciEngelle, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print(str(get_config(base_warnings+"warning1")).format(kullanici=kullanici))
            else:
                print(str(get_config(base_warnings+"warning2")).format(kullanici=kullanici))

            if self.hesapGizliMi():
                btnText = str(self.driver.find_element_by_css_selector('div.BY3EC >button').text).lower()
                if durum:
                    if btnText!="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        show_in_console(str(get_config(base_warnings+"warning3")).format(kullanici=kullanici), 2)
                else:
                    if btnText=="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        show_in_console(str(get_config(base_warnings+"warning4")).format(kullanici=kullanici), 2)
            else:
                btnText =str(self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN').text).lower()
                if durum:
                    if btnText != "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        show_in_console(str(get_config(base_warnings+"warning5")).format(kullanici=kullanici), 2)
                else:
                    if btnText == "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        show_in_console(str(get_config(base_warnings+"warning6")).format(kullanici=kullanici), 2)

            if durum:
                print(str(get_config(base_warnings+"warning7")).format(kullanici=kullanici))
            else:
                print(str(get_config(base_warnings+"warning8")).format(kullanici=kullanici))
            self.profilSec(secim)
        except Exception as error:
            if durum:
                show_in_console(str(get_config(base_warnings+"warning9")).format(kullanici=kullanici,hata=str(error)),2)
            else:
                show_in_console(str(get_config(base_warnings+"warning10")).format(kullanici=kullanici,hata=str(error)), 2)
            self.profilSec(secim)

    def ayarlar(self,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.ayarlar, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.ayarlar,inputs=True)
        try:
            if durum:
                ayarlar=get_config("{base}ana_ekran.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    show_in_console(secenek,3)
            secilenIslem=input(get_config(base_inputs+"input1"))

            if secilenIslem=="1":
                self.dilAyarlari()
            elif secilenIslem=="2":
                self.tarayiciAyarlari()
            elif secilenIslem=="3":
                self.menu()
            else:
                show_in_console(get_config(base_warnings+"warning1"), 2)
                self.ayarlar(durum=False)
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)),2)

    def oturumKapat(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.oturumKapat, warnings=True)
        print(get_config(base_warnings+"warning1"))
        try:
            self.driver.find_elements_by_css_selector("div._47KiJ > div.Fifk5")[-1].click()
            sleep(0.10)
            self.driver.find_elements_by_css_selector("div.-qQT3")[-1].click()
            show_in_console(get_config(base_warnings+"warning2"), 1)
            self.driver.get(self.BASE_URL + 'accounts/login/')
            self.authStatus = False
            auth_login()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning3")).format(hata=str(error)), 2)
            self.menu()

    def quit(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.quit, warnings=True)
        try:
            print(get_config(base_warnings+"warning1"))
            self.driver.quit()
            show_in_console(get_config(base_warnings+"warning2"), 1)
            exit()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning3")).format(hata=str(error)), 2)
            self.driver.quit()
            exit()

    def getLanguage(self):
        self.dil=get_config("language")

    def dilGetir(self):
        if self.dil=="tr":
            return "Türkçe"
        else:
            return "English"

    def dilAyarlari(self,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.dilAyarlari, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.dilAyarlari,inputs=True)
        try:
            if durum:
                ayarlar=get_config("{base}dil_ayarlari.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    if "{dil}" in secenek:
                        show_in_console(str(secenek).format(dil=self.dilGetir()),3)
                    else:
                        show_in_console(secenek, 3)
            secilenIslem=input(get_config(base_inputs+"input1"))

            if secilenIslem=="1":
                self.dilSec()
            elif secilenIslem=="2":
                self.ayarlar()
            elif secilenIslem=="3":
                self.menu()
            else:
                show_in_console(get_config(base_warnings+"warning1"),2)
                self.dilAyarlari(durum=False)
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)),2)

    def tarayiciAyarlari(self,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.tarayiciAyarlari, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.tarayiciAyarlari,inputs=True)
        try:
            if durum:
                ayarlar=get_config("{base}tarayici_ayarlari.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    if "{path}" in secenek:
                        show_in_console(str(secenek).format(path=self.tarayiciPathGetir()),3)
                    elif "{durum}" in secenek:
                        show_in_console(str(secenek).format(durum=self.tarayiciHeadlessGetir()), 3)
                    else:
                        show_in_console(secenek, 3)
            secilenIslem=input(get_config(base_inputs+"input1"))

            if secilenIslem=="1":
                self.tarayiciGorunmeDurumuAyarlari()
            elif secilenIslem=="2":
                self.tarayiciPathAyarlari()
            elif secilenIslem=="3":
                self.ayarlar()
            elif secilenIslem=="4":
                self.menu()
            else:
                show_in_console(get_config(base_warnings+"warning1"),2)
                self.tarayiciAyarlari(durum=False)
        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning2")).format(hata=str(error)), 2)

    def tarayiciHeadlessGetir(self):
        headless=get_config("headless")
        durum=None
        if headless=="true":
            if self.dil=="tr":
                durum= "Açık"
            elif self.dil=="en":
                durum= "Open"
        else:
            if self.dil == "tr":
                durum= "Kapalı"
            elif self.dil == "en":
                durum= "Close"
        return durum

    def dilSec(self,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.dilSec, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.dilSec,inputs=True)
        try:
            if durum:
                ayarlar=get_config("{base}dil_ayarlari.dil_degistir.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    show_in_console(secenek,3)
            secilenIslem=input(get_config(base_inputs+"input1"))

            if secilenIslem in ["1","2"]:
                self.uygulamaDilDegistir(dilNo=secilenIslem)
                self.ayarlar()
            elif secilenIslem=="3":
                self.dilAyarlari()
            elif secilenIslem=="4":
                self.ayarlar()
            elif secilenIslem=="5":
                self.menu()
            else:
                show_in_console(get_config(base_warnings+"warning1"),2)
                self.dilSec(durum=False)
        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning2")).format(hata=str(error)), 2)

    def uygulamaDilDegistir(self,dilNo):
        base_warnings = self.BASE_TRANSLATE(metod=self.uygulamaDilDegistir, warnings=True)
        try:
            if dilNo=="1":
                dil="tr"
            elif dilNo=="2":
                dil="en"
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                veri = json.load(dosya)
                veri["language"]=dil
                dosya.seek(0)
                json.dump(veri, dosya, indent=4,ensure_ascii=False)
                dosya.truncate()
            show_in_console(get_config(base_warnings+"warning1"),1)
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)), 2)

    def tarayiciThreadOlustur(self):
        t1 = threading.Thread(target=self.tarayiciBaslat)
        t1.daemon = True
        t1.start()


    def tarayiciBaslat(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.tarayiciBaslat, warnings=True)
        try:
            print(get_config(base_warnings+"warning1"))
            firefox_options = Options()
            headless=get_config("headless")
            if headless=="false":
                firefox_options.add_argument('--headless')
            self.driver = webdriver.Firefox(firefox_profile=self.tarayiciDilDegistir(),options=firefox_options,executable_path=self.tarayiciPathGetir())
            self.driver.get(self.BASE_URL + 'accounts/login/')
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)),2)
            exit()

    def tarayiciPathGetir(self):
        return get_config("driver_path")

    def tarayiciDilDegistir(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'en-US, en')
        return profile

    def tarayiciPathAyarlari(self,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.tarayiciPathAyarlari, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.tarayiciPathAyarlari,inputs=True)
        try:
            if durum:
                ayarlar=get_config(self.BASE_AYARLAR()+"tarayici_ayarlari.path_degistir.secenekler")
                for secenek in ayarlar:
                    show_in_console(secenek,3)
            secilenIslem = input(get_config(base_inputs+"input1"))
            if secilenIslem=="1":
                self.tarayiciPathDegistir()
                self.ayarlar()
            elif secilenIslem=="2":
                self.tarayiciAyarlari()
            elif secilenIslem=="3":
                self.ayarlar()
            elif secilenIslem=="4":
                self.menu()
            else:
                show_in_console(get_config(base_warnings+"warning1"),2)
                self.tarayiciPathAyarlari(durum=False)
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)), 2)

    def tarayiciPathDegistir(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.tarayiciPathDegistir, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.tarayiciPathDegistir,inputs=True)
        try:
            path = input(get_config(base_inputs+"input1"))
            if self.dosyaMevcutMu(path):
                with open('config.json', 'r+', encoding="utf-8") as dosya:
                    veri = json.load(dosya)
                    veri["driver_path"]=path
                    dosya.seek(0)
                    json.dump(veri, dosya, indent=4,ensure_ascii=False)
                    dosya.truncate()
                show_in_console(get_config(base_warnings+"warning1"),1)
            else:
                show_in_console(get_config(base_warnings+"warning2"), 2)
                self.tarayiciPathAyarlari()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning3")).format(hata=str(error)), 2)

    def tarayiciGorunmeDurumuAyarlari(self,durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.tarayiciGorunmeDurumuAyarlari, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.tarayiciGorunmeDurumuAyarlari, inputs=True)
        try:
            if durum:
                ayarlar=get_config("{base}tarayici_ayarlari.gorunme_durumu_degistir.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    show_in_console(secenek,3)
            secilenIslem=input(get_config(base_inputs+"input1"))
            if secilenIslem in ["1","2"]:
                self.tarayiciGorunmeDurumDegistir(durum=secilenIslem)
                self.ayarlar()
            elif secilenIslem=="3":
                self.tarayiciAyarlari()
            elif secilenIslem=="4":
                self.ayarlar()
            elif secilenIslem=="5":
                self.menu()
            else:
                show_in_console(get_config(base_warnings+"warning1"),2)
                self.tarayiciGorunmeDurumuAyarlari(durum=False)
        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning2")).format(hata=str(error)), 2)

    def tarayiciGorunmeDurumDegistir(self,durum):
        base_warnings = self.BASE_TRANSLATE(metod=self.tarayiciGorunmeDurumDegistir, warnings=True)
        try:
            if durum=="1":
                headless="true"
            elif durum=="2":
                headless="false"
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                veri = json.load(dosya)
                veri["headless"]=headless
                dosya.seek(0)
                json.dump(veri, dosya, indent=4,ensure_ascii=False)
                dosya.truncate()
            show_in_console(get_config(base_warnings+"warning1"),1)
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)), 2)


    def takipcilerButon(self):
        return self.driver.find_elements_by_css_selector("ul.k9GMp >li.Y8-fY")[1]

    def takipEdilenlerButon(self):
        return self.driver.find_elements_by_css_selector("ul.k9GMp >li.Y8-fY")[2]

    def takipcileriGetir(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.takipcileriGetir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.takipcileriGetir)
        try:
            print(get_config(base_warnings + "warning1"))
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            takipciSayisi = self.takipciSayisiGetir()

            btn_takipciler = self.takipcilerButon()
            btn_takipciler.click()
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            takipciler = set()
            self.indexOne()
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipcilerPopup = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takipci in takipcilerPopup:
                    takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                    takipciKullaniciAdi = self.metindenKarakterSil(
                        self.metindenKarakterSil(takipciKullaniciAdi, self.BASE_URL), '/')
                    if takipciKullaniciAdi not in takipciler:
                        print(str(get_config(base_warnings + "warning2")).format(index=self.index,kullanici=takipciKullaniciAdi))
                        takipciler.add(takipciKullaniciAdi)
                        self.indexUp()
                        if (self.index - 1) >= takipciSayisi:
                            devamEtsinMi = False
                            break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        show_in_console(str(get_config(base_warnings + "warning3")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(get_config("{base}sleep2".format(base=base_sleep)))
            btn_close_dialog = self.driver.find_element_by_css_selector("div.WaOAr >button.wpO6b")
            btn_close_dialog.click()
            return takipciler
        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning4")).format(hata=str(error)), 2)
            self.menu()

    def takipEdilenleriGetir(self, takipciler):
        base_warnings = self.BASE_TRANSLATE(metod=self.takipEdilenleriGetir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.takipEdilenleriGetir)
        try:
            takipEdilenSayisi = self.takipEdilenSayisiGetir()
            btn_takipEdilenler = self.takipEdilenlerButon()
            btn_takipEdilenler.click()
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
            self.indexOne()
            islemIndex = 0
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = self.takipEdilenKullaniciAdiGetir(element=takip)

                    if takipEdilenKullanıcıAdi not in takipciler:
                        btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                        if btn_takip.text == "Following":
                            btn_takip.click()
                            sleep(get_config("{base}sleep2".format(base=base_sleep)))
                            try:
                                btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                                btn_onay.click()
                            except Exception as error:
                                show_in_console(str(get_config(base_warnings + "warning1")).format(
                                    kullanici=takipEdilenKullanıcıAdi, hata=str(error)), 2)
                                continue
                            show_in_console(str(get_config(base_warnings + "warning2")).format(
                                index=self.index, kullanici=takipEdilenKullanıcıAdi), 1)
                            self.indexUp()
                            if self.index - 1 >= takipEdilenSayisi:
                                devamEtsinMi = False
                                break
                            sleep3 = get_config("{base}sleep3".format(base=base_sleep))
                            sleep(self.beklemeSuresiGetir(sleep3[0], sleep3[1]))
                    islemIndex = islemIndex + 1
                    if islemIndex >= takipEdilenSayisi:
                        devamEtsinMi = False
                        break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        show_in_console(str(get_config(base_warnings + "warning3")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(get_config("{base}sleep4".format(base=base_sleep)))

        except Exception as error:
            show_in_console(str(get_config(base_warnings + "warning4")).format(
                hata=str(error)), 2)
            self.menu()

    def takipEdilenSayisiGetir(self):
        takipEdilenSayisi = self.driver.find_elements_by_css_selector("ul.k9GMp li.Y8-fY >a.-nal3 >span.g47SY")[-1].text
        return int(self.metindenKarakterSil(takipEdilenSayisi, ','))

    def takipciSayisiGetir(self):
        takipciSayisi = self.driver.find_elements_by_css_selector("ul.k9GMp li.Y8-fY >a.-nal3 >span.g47SY")[0].get_attribute('title')
        return int(self.metindenKarakterSil(takipciSayisi, ','))

    def takipEdilenKullaniciAdiGetir(self, element):
        takipEdilenKullanıcıAdi = element.find_element_by_css_selector("a.FPmhX").get_attribute('href')
        return self.metindenKarakterSil(self.metindenKarakterSil(takipEdilenKullanıcıAdi, self.BASE_URL), '/')

    def girisKontrol(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.girisKontrol, warnings=True)
        if "The username you entered doesn't belong to an account. Please check your username and try again." in self.driver.page_source:
            show_in_console(get_config(base_warnings+"warning1"),2)
        elif "Sorry, your password was incorrect. Please double-check your password." in self.driver.page_source:
            show_in_console(get_config(base_warnings+"warning2"), 2)
        elif self.BASE_URL + "accounts/login/two_factor" in self.driver.current_url:
            self.girisDogrulama()
        elif self.driver.current_url != self.BASE_URL + "accounts/login/":
            show_in_console(get_config(base_warnings+"warning3"), 1)
            self.authStatus = True
        else:
            show_in_console(get_config(base_warnings+"warning4"), 2)

    def girisDogrulama(self, durum=True):
        base_warnings = self.BASE_TRANSLATE(metod=self.girisDogrulama, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.girisDogrulama, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.girisDogrulama)

        kod = input(get_config(base_inputs+"input1")).strip()
        if not kod:
            #auth_logout()
            auth_login()

        if durum:
            sleep(get_config("{base}sleep1".format(base=base_sleep)))
        kodInput = self.driver.find_elements_by_css_selector('form input')[0]
        kodInput.send_keys(kod)
        kodInput.send_keys(Keys.ENTER)
        sleep(get_config("{base}sleep2".format(base=base_sleep)))
        if "A security code is required." in self.driver.page_source:
            show_in_console(get_config(base_warnings+"warning1"), 2)
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif "Please check the security code and try again." in self.driver.page_source:
            show_in_console(get_config(base_warnings+"warning2"), 2)
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif self.BASE_URL + "accounts/login/two_factor" not in self.driver.current_url:
            self.authStatus = True
            show_in_console(get_config(base_warnings+"warning3"),1)
        else:
            show_in_console(get_config(base_warnings+"warning4"),2)

    def etiketGetir(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.etiketGetir, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.etiketGetir, inputs=True)
        try:
            etiket = input(get_config(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(etiket)

            if self.checkLength(etiket):
                url = "{BASE_URL}explore/tags/{etiket}".format(BASE_URL=self.BASE_URL, etiket=str(etiket))
                print(str(get_config(base_warnings+"warning1")).format(url=url))
                self.urlYonlendir(url)
                if not self.sayfaMevcutMu():
                    show_in_console(str(get_config(base_warnings+"warning2")).format(etiket=etiket),
                                      2)
                    return self.etiketGetir()
                return etiket
            else:
                show_in_console(get_config(base_warnings+"warning3"), 2)
                return self.etiketGetir()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning4")).format(hata=str(error)), 2)

    def etiketeGoreIslemLimitiGetir(self, islemNo):
        base_warnings = self.BASE_TRANSLATE(metod=self.etiketeGoreIslemLimitiGetir, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.etiketeGoreIslemLimitiGetir, inputs=True)
        try:
            if islemNo == 1:
                limit = input(get_config(base_inputs+"input1")).strip()
            elif islemNo == 2:
                limit = input(get_config(base_inputs+"input2")).strip()

            self.anaMenuyeDonsunMu(limit)
            if limit.isnumeric() and int(limit) > 0:
                return int(limit)
            else:
                show_in_console(get_config(base_warnings+"warning1"), 2)
                return self.etiketeGoreIslemLimitiGetir(islemNo=islemNo)
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)), 2)
            if islemNo == 1:
                self.likingPostsByTag()
            elif islemNo == 2:
                self.followUsersByTag()

    def hikayeVarMi(self):
        try:
            durum = self.driver.find_element_by_css_selector("div.RR-M-").get_attribute("aria-disabled")
            if durum == "false":
                return True
            else:
                return False
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.hikayeVarMi, warnings=True)
            show_in_console(
                str(get_config(base_warnings+"warning1")).format(hata=str(error)),
                2)

    def hikayeVideoMu(self):
        try:
            self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5")
            return True
        except:
            return False

    def hikayeSayisiGetir(self):
        try:
            hikayeSayisi = self.driver.find_elements_by_css_selector("div.w9Vr-  > div._7zQEa")
            return len(hikayeSayisi)
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.hikayeSayisiGetir, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)), 2)

    def hikayeleriGetir(self):
        base_sleep = self.BASE_SLEEP(metod=self.hikayeleriGetir)

        try:
            for i in range(self.hikayeSayisiGetir()):
                if self.hikayeVideoMu():
                    url = self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5 > source").get_attribute(
                        "src")
                    self.dosyaIndir(url, 2)
                else:
                    foto_srcset = str(
                        self.driver.find_element_by_css_selector("div.qbCDp >  img.y-yJ5").get_attribute("srcset"))
                    url = (foto_srcset.split(",")[-1]).split(" ")[0]
                    self.dosyaIndir(url, 1)
                btn_ileri = self.driver.find_element_by_css_selector("button.ow3u_")
                btn_ileri.click()
                sleep(get_config("{base}sleep1".format(base=base_sleep)))
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.hikayeleriGetir, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)), 2)

    def yorumUzunlukBelirle(self, yorum):
        return yorum[0:randint(5, 100)]

    def yorumYap(self, yorum):
        try:

            textarea = self.driver.find_element_by_class_name('Ypffh')
            self.inputTemizle(textarea)
            textarea.click()
            textarea = self.driver.find_element_by_class_name('Ypffh')

            textarea.send_keys(yorum)
            textarea.send_keys(Keys.ENTER)
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.yorumYap, warnings=True)
            show_in_console(str(get_config(base_warnings + "warning1")).format(hata=str(error)), 2)

    def rastgeleYorumGetir(self):
        try:
            return requests.get("http://metaphorpsum.com/paragraphs/1/1").text
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.rastgeleYorumGetir, warnings=True)
            show_in_console(
                str(get_config(base_warnings + "warning1")).format(hata=str(error)), 2)

    def yorumLimitiAsildiMi(self, yorumSayisi):
        if yorumSayisi > 50:
            return True
        else:
            return False

    def mesajSil(self,mesaj):
        mesaj.click()
        base = self.BASE_SLEEP(metod=self.mesajSil)
        sleep1=get_config(base + "sleep1")
        sleep(self.beklemeSuresiGetir(sleep1[0],sleep1[1]))
        self.driver.find_element_by_css_selector("div.PjuAP button.wpO6b").click()
        sleep(get_config(base + "sleep2"))
        self.driver.find_elements_by_css_selector("div._9XapR >div._7zBYT button.sqdOP")[0].click()
        sleep(get_config(base + "sleep3"))
        self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()

    def kullaniciEngelDurumDegistir(self):
        base_sleep = self.BASE_SLEEP(metod=self.kullaniciEngelDurumDegistir)
        self.driver.find_element_by_css_selector("button.wpO6b").click()
        sleep(get_config("{base}sleep1".format(base=base_sleep)))
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()
        sleep(get_config("{base}sleep2".format(base=base_sleep)))
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()

    def kullaniciTakipDurumDegistir(self,kullanici,durum):
        base_warnings = self.BASE_TRANSLATE(metod=self.kullaniciTakipDurumDegistir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.kullaniciTakipDurumDegistir)

        if self.hesapGizliMi():
            btn_takip = self.driver.find_element_by_css_selector("div.BY3EC >button")
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    show_in_console(str(get_config(base_warnings+"warning1")).format(kullanici=kullanici), 1)
                elif btn_text == "requested":
                    print(str(get_config(base_warnings+"warning2")).format(kullanici=kullanici))
                elif btn_text == "unblock":
                    show_in_console(str(get_config(base_warnings+"warning3")).format(
                        kullanici=kullanici), 2)
            else:
                if btn_text=="requested":
                    btn_takip.click()
                    sleep(get_config("{base}sleep1".format(base=base_sleep)))
                    self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()
                    show_in_console(str(get_config(base_warnings + "warning8")).format(kullanici=kullanici), 1)
                else:
                    print(str(get_config(base_warnings+"warning4")).format(kullanici=kullanici))

        else:
            btn_takip = self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN')
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    show_in_console(str(get_config(base_warnings+"warning5")).format(kullanici=kullanici), 1)
                elif btn_text == "unblock":
                    show_in_console(str(get_config(base_warnings+"warning6")).format(kullanici=kullanici), 2)
                else:
                    ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                    if ariaLabel == "Following":
                        print(str(get_config(base_warnings+"warning7")).format(kullanici=kullanici))
            else:
                try:
                    ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                    if ariaLabel == "Following":
                        btn_takip.click()
                        sleep(get_config("{base}sleep1".format(base=base_sleep)))
                        self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()
                        show_in_console(str(get_config(base_warnings + "warning8")).format(kullanici=kullanici),
                                          1)
                    else:
                        print(str(get_config(base_warnings + "warning4")).format(kullanici=kullanici))
                except:
                    print(str(get_config(base_warnings + "warning4")).format(kullanici=kullanici))


    def gonderiIlerlet(self):
        try:
            self.driver.find_element_by_css_selector("a._65Bje").click()
        except:
            pass

    def gonderiBegenDurumDegistir(self, btn):
        base_sleep = self.BASE_SLEEP(metod=self.gonderiBegenDurumDegistir)
        btn.click()
        self.indexUp()
        sleep(get_config("{base}sleep1".format(base=base_sleep)))
        self.gonderiIlerlet()
        sleep2=get_config("{base}sleep2".format(base=base_sleep))
        sleep(self.beklemeSuresiGetir(sleep2[0],sleep2[1]))

    def begenButon(self):
        return self.driver.find_element_by_css_selector("article.M9sTE section.ltpMr >span.fr66n >button")

    def begenButonuDurumGetir(self, buton):
        return str(buton.find_element_by_tag_name("svg").get_attribute("aria-label")).lower()

    def gonderiVarMi(self, kullanici, gonderiSayisi, secim):
        if gonderiSayisi < 1:
            base_warnings = self.BASE_TRANSLATE(metod=self.gonderiVarMi, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(kullanici=kullanici), 2)
            self.profilSec(secim)

    def gonderiSayisi(self):
        return self.driver.find_element_by_css_selector("ul.k9GMp >li.Y8-fY >span >span.g47SY").text

    def gonderiTipiVideoMu(self, element=None):
        try:
            if element:
                element.find_element_by_css_selector("video.tWeCl")
            else:
                self.driver.find_element_by_css_selector("video.tWeCl")
            return True
        except:
            return False

    def gonderiUrlGetir(self):
        try:
            veriTuru = None
            if self.gonderiTipiVideoMu():
                url = self.driver.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                veriTuru = 2
            else:
                url = self.driver.find_element_by_css_selector("article.M9sTE div.KL4Bh > img.FFVAD").get_attribute("src")
                veriTuru = 1
            return url, veriTuru
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.gonderiUrlGetir, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)), 2)
            return None, None

    def gonderiAlbumMu(self):
        try:
            self.driver.find_element_by_css_selector("div.Yi5aA")
            return True
        except:
            return False

    def getAlbumUrl(self):
        base_sleep = self.BASE_SLEEP(metod=self.getAlbumUrl)

        try:
            album = set()
            ul = self.driver.find_element_by_css_selector("article ul.vi798")
            for i in range(self.albumIcerikSayisiGetir()):
                liste = ul.find_elements_by_css_selector("li.Ckrof")
                for li in liste:
                    [url, veriTuru] = self.albumIcerikUrlGetir(li)
                    if url not in album and url is not None:
                        album.add(url)
                        self.dosyaIndir(url, veriTuru)
                btn_ileri = self.driver.find_element_by_css_selector("button._6CZji div.coreSpriteRightChevron")
                btn_ileri.click()
                sleep(get_config("{base}sleep1".format(base=base_sleep)))
        except:
            pass

    def albumIcerikSayisiGetir(self):
        try:
            return len(self.driver.find_elements_by_css_selector("div.Yi5aA"))
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.albumIcerikUrlGetir, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format( url=str(self.driver.current_url), hata=str(error)), 2)
            return None

    def albumIcerikUrlGetir(self, element):
        try:
            veriTuru = None
            if self.gonderiTipiVideoMu(element):
                url = element.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                veriTuru = 2
            else:
                url = element.find_element_by_css_selector("img.FFVAD").get_attribute("src")
                veriTuru = 1
            return url, veriTuru
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.albumIcerikUrlGetir, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)), 2)
            return None, None

    def aktifKullaniciGetir(self):
        try:
            self.driver.find_elements_by_css_selector("div._47KiJ > div.Fifk5")[-1].click()
            kullanici = self.driver.find_elements_by_css_selector("div._01UL2 >a.-qQT3")[0].get_attribute(
                "href")
            self.aktifKullanici = str(kullanici).replace(self.BASE_URL, "")
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.aktifKullaniciGetir, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)), 2)
            self.aktifKullaniciGetir()

    def anaMenuyeDonsunMu(self, deger):
        if deger == "menu":
            self.menu()

    def BASE_AYARLAR(self):
        try:
            return "languages.{dil}.ayarlar.".format(dil=self.dil)
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.BASE_AYARLAR, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)),2)

    def BASE_SLEEP(self,metod):
        try:
            return "time.{metod}.".format(metod=metod.__name__)
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.BASE_SLEEP, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)),2)

    def BASE_TRANSLATE(self, metod, warnings=None, inputs=None):
        try:
            if warnings:
                return "languages.{dil}.warnings.{metod}.warnings.".format(dil=self.dil, metod=metod.__name__)
            elif inputs:
                return "languages.{dil}.warnings.{metod}.inputs.".format(dil=self.dil, metod=metod.__name__)
            else:
                return "languages.{dil}.warnings.{metod}.".format(dil=self.dil, metod=metod.__name__)
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.BASE_TRANSLATE, warnings=True)
            show_in_console(str(get_config(base_warnings + "warning1")).format(hata=str(error)))

    def beklemeSuresiGetir(self, baslangic, bitis):
        return randint(baslangic, bitis)

    def bildirimThreadOlustur(self):
        t1 = threading.Thread(target=self.bildirimPopupKapat)
        t1.daemon = True
        t1.start()

    def bildirimPopupKapat(self):
        base_sleep = self.BASE_SLEEP(metod=self.bildirimPopupKapat)
        try:
            for i in range(2):
                sleep(get_config("{base}sleep1".format(base=base_sleep)))
                btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
                self.driver.execute_script("arguments[0].click();", btn)
        except:
            pass

    def popupAsagiKaydir(self, secici):
        self.driver.execute_script('''
                                     var fDialog = document.querySelector('{secici}');
                                     fDialog.scrollTop = fDialog.scrollHeight
                                  '''.format(secici=secici))

    def hesapGizliMi(self):
        if "This Account is Private" in self.driver.page_source:
            return True
        else:
            return False

    def sayfaMevcutMu(self):
        if "Sorry, this page isn't available." not in self.driver.page_source:
            return True
        else:
            return False

    def kullanicilariTakipEt(self, kullaniciListesi, secim):
        base_sleep = self.BASE_SLEEP(metod=self.kullanicilariTakipEt)
        base_warnings = self.BASE_TRANSLATE(metod=self.kullanicilariTakipEt, warnings=True)
        print(get_config(base_warnings + "warning1"))
        sleep1 = get_config("{base}sleep1".format(base=base_sleep))
        for kullanici in kullaniciListesi:
            if self.kullaniciKontrol(kullanici):
                self.kullaniciTakipEt(kullanici=kullanici.strip(),secim=secim)
                sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
        print(get_config(base_warnings + "warning2"))

    def kullaniciKontrol(self, kullanici):
        return self.urlKontrol(self.BASE_URL + kullanici)

    def kullaniciProfilineYonlendir(self, kullanici):
        self.driver.get(self.BASE_URL + kullanici)
        base = self.BASE_SLEEP(metod=self.kullaniciProfilineYonlendir)
        sleep(get_config("{base}sleep1".format(base=base)))

    def urlGirildiMi(self, url, metod, metodDeger=None):
        base_warnings = self.BASE_TRANSLATE(metod=self.urlGirildiMi, warnings=True)
        if url is None or len(url) < 12:
            show_in_console(get_config(base_warnings + "warning1"), 2)
            if metodDeger:
                if "commentingPost" == metod.__name__:
                    metod(yorum=metodDeger)
                metod(metodDeger)
            metod()

    def urlGecerliMi(self, url, metod, metodDeger=None):
        if not self.urlKontrol(url):
            base_warnings = self.BASE_TRANSLATE(metod=self.urlGecerliMi, warnings=True)
            show_in_console(get_config(base_warnings + "warning1"), 2)
            if metodDeger:
                if "commentingPost" == metod.__name__:
                    metod(yorum=metodDeger)
                metod(metodDeger)
            metod()

    def urlKontrol(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 404:
                return False
            else:
                return True
        except:
            return False

    def urlYonlendir(self, url):
        self.driver.get(url)
        base = self.BASE_SLEEP(metod=self.urlYonlendir)
        sleep(get_config("{base}sleep1".format(base=base)))

    def dosyaAdiOlustur(self,veriTuru):
        dt=str(datetime.now()).replace(":", "_").replace(" ", "")
        if veriTuru == 1:
            isim="{index}_{tarih}.jpg".format(index=str(self.index),tarih=dt)
        elif veriTuru == 2:
            isim = "{index}_{tarih}.mp4".format(index=str(self.index), tarih=dt)
        return isim

    def dosyaIndir(self, url, veriTuru):
        base_warnings = self.BASE_TRANSLATE(metod=self.dosyaIndir, warnings=True)
        try:
            dosyaAdi=self.dosyaAdiOlustur(veriTuru)
            urllib.request.urlretrieve(url, dosyaAdi)
            show_in_console(str(get_config(base_warnings+"warning1")).format(url=url), 1)
            self.indexUp()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)), 2)

    def dosyaSec(self):
        base_warnings = self.BASE_TRANSLATE(metod=self.dosyaSec, warnings=True)
        base_inputs = self.BASE_TRANSLATE(metod=self.dosyaSec, inputs=True)
        try:
            dosyaAdi = input(get_config(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(dosyaAdi)
            if self.dosyaMevcutMu(dosyaAdi) and self.txtDosyasiMi(dosyaAdi):
                return str(dosyaAdi)
            else:
                show_in_console(get_config(base_warnings+"warning1"), 2)
                return self.dosyaSec()
        except Exception as error:
            show_in_console(str(get_config(base_warnings+"warning2")).format(hata=str(error)), 2)
            return self.dosyaSec()

    def dosyaİceriginiAl(self, dosya):
        try:
            icerik = set()
            with open(dosya, "r", encoding="utf-8") as satirlar:
                for satir in satirlar:
                    if len(satir.strip()) > 0:
                        icerik.add(satir.strip())
            return icerik
        except Exception as error:
            base_warnings = self.BASE_TRANSLATE(metod=self.dosyaİceriginiAl, warnings=True)
            show_in_console(str(get_config(base_warnings+"warning1")).format(hata=str(error)), 2)
            return False

    def dosyaİcerigiAlindiMi(self, icerik):
        if icerik:
            return True
        else:
            return False

    def txtDosyasiMi(self, dosya):
        if os.path.splitext(dosya)[-1].lower() == ".txt":
            return True
        else:
            return False

    def klasorOlustur(self, klasor):
        base_warnings = self.BASE_TRANSLATE(metod=self.klasorOlustur, warnings=True)
        if not os.path.exists(klasor):
            os.mkdir(klasor)
            show_in_console(str(get_config(base_warnings+"warning1")).format(klasor=klasor), 1)
        else:
            print(str(get_config(base_warnings+"warning2")).format(klasor=klasor))
        self.klasorDegistir(klasor)
        print(str(get_config(base_warnings+"warning3")).format(klasor=klasor))

    def klasorDegistir(self, klasor):
        os.chdir(klasor)

    def metindenKarakterSil(self, metin, silinecekKarakterler):
        return metin.replace(silinecekKarakterler, '')

    def inputTemizle(self, inpt):
        inpt.clear()

    def hedefKaynaktanBuyukMu(self, hedef, kaynak):
        if hedef > kaynak:
            hedef = kaynak
        return hedef

    def indexOne(self):
        self.index = 1

    def indexUp(self):
        self.index = self.index + 1

    def checkLength(self, yorum):
        if len(yorum) > 0:
            return True
        else:
            return False

try:
    instagram = Instagram()
except KeyboardInterrupt:
    print("\n [*] Signing out from the application...")
    exit()


