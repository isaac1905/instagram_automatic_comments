from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as sel_excs
import time
import random
import userconfigs as uc

true = 1


class PixBot:
    
    # Inicialização do Geckodriver, navegador adaptado para automatização na instância do Firefox
    
    def __init__(self, username, password, link_sorteio):
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./geckodriver"
        )
        self.username = username
        self.password = password
        self.link_sorteio = link_sorteio
        
    
    # Método para simulação de digitação de maneira mais humana e não instantânea como máquina para evitar a verificação do instagram contra
    # processos automatizados
    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)
            

# Método principal do programa 
    def Execute(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(7)
        input_Username = driver.find_element_by_xpath('//input[@name = "username"]')
        input_Password = driver.find_element_by_xpath('//input[@name = "password"]')
        
        input_Username.click()
        input_Username.clear()
        self.type_like_a_person(self.username,input_Username)
        time.sleep(1)
        input_Password.click()
        input_Password.clear()
        self.type_like_a_person(self.password,input_Password)
        time.sleep(1)
        input_Password.send_keys(Keys.RETURN)
        time.sleep(5)
            
            
        comentarios=["Quero ganhar", "Já to ansioso pelo sorteio", "Esse prêmio é meu", "Já tem dono", "Vai ser meu", "Já tô fazendo planos", "Ansiosoooo", "Louco pra ganhar", "Chega logo o dia", "Vou ganhar", "Pelo menos um","Esse eu ganho com certeza"]
        driver.get(self.link_sorteio)
        time.sleep(3)
            
        true = 1
        while true == 1:
            try:
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.type_like_a_person(random.choice(comentarios), comment_input_box)
                time.sleep(random.randint(3, 5))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(random.randint(30, 60))
                
            except Exception as e:
                print(e)
                true = 2
                
                
Bot = PixBot(uc.username, uc.password, uc.link_sorteio)
Bot.Execute()
