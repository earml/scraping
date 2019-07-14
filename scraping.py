# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:14:57 2017

@author: elisalvo
"""

import selenium
#import lxml.html as lh
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://sinda.crn2.inpe.br/PCD/SITE/novo/site/historico")
escolhe_cidade = "//option[@value='31783']"
button = driver.find_element_by_xpath(escolhe_cidade).click()
botao_cidade = "//input[@type='submit']"
button = driver.find_element_by_xpath(botao_cidade).click()

#preenchendo as datas
dia_inicial = driver.find_element_by_id('element_1_1')
mes_inicial = driver.find_element_by_id('element_1_2')
ano_inicial = driver.find_element_by_id('element_1_3')
dia_inicial.send_keys("01")
mes_inicial.send_keys("01")
ano_inicial.send_keys("2010")
dia_final = driver.find_element_by_id('element_2_1')
mes_final = driver.find_element_by_id('element_2_2')
ano_final = driver.find_element_by_id('element_2_3')
dia_final.send_keys("30")
mes_final.send_keys("12")
ano_final.send_keys("2010")

dia_inicial.send_keys(Keys.RETURN)
ano_inicial.clear()
ano_final.clear()
