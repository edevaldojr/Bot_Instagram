from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import random


class InstagramBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\PICHAU\Desktop\Area de Trabalho\BOT INSTA\geckodriver.exe")

    def login(self):
            driver = self.driver
            driver.get("https://www.instagram.com")
            time.sleep(2)
            #botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
            #botao_login.click()
            campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
            campo_usuario.click()
            campo_usuario.clear()
            campo_usuario.send_keys(self.username)
            campo_senha = driver.find_element_by_xpath("//input[@name='password']")
            campo_senha.click()
            campo_senha.clear()
            campo_senha.send_keys(self.password)
            campo_senha.send_keys(Keys.RETURN)
            time.sleep(5)
            driver.find_element_by_xpath("//button[contains(text(),'Agora')]").click()
            self.comente_nas_fotos_com_hastag('hashtag_Here')

        
    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comente_nas_fotos_com_hastag(self,hastag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hastag +"/")
        time.sleep(3)

        for i in range(1,3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hastag in href]
        print(hastag + 'fotos ' + str(len(pic_hrefs)))

        for pic_hrefs in pic_hrefs:
            driver.get(pic_hrefs)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            try:
                comentarios = ["comentario[1]","comentario [2]","comentario [3]"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                for i in range(1, 5000):
                    time.sleep(random.randint(2,7))
                    self.digite_como_uma_pessoa(random.choice(comentarios), campo_comentario)
                    time.sleep(random.randint(60,80))
                    driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                    time.sleep(3)
                    print(i)
            except Exception as e:
                print(e)
                time.sleep(5)



edevaldoBot = InstagramBot('email','senha')
edevaldoBot.login()
