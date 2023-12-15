from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import time

url = 'https://exoplanets.nasa.gov/exoplanet-catalog/'

servico = webdriver.ChromeService(executable_path='C:\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=servico)
driver.get(url)
time.sleep(5)

dados_planetas = []

def scrape():
    for i in range(1,2):
        while True:
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            #pegar o numero da página
            
            break
        
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            lista = []
            for i, li_tag in enumerate(li_tags):
                if i == 0:
                    conteudo = li_tag.find_all("a")[0].contents[0]
                else:
                    try:
                        conteudo = li_tag.contents[0]
                    except:
                        conteudo = ''
                lista.append(conteudo)
            #acessando o link do planeta
            

            #add o link do planeta na lista

            dados_planetas.append(lista)

        driver.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(f"Coleta de dados da página {i} concluída")
scrape()
#add o hyperlink
headers = ['nome', 'anos_luz_terra', 'massa', 'magnitude_estela', 'data_descoberta']

dataframe = pd.DataFrame(dados_planetas, columns=headers)
dataframe.to_csv('dados.csv', index=True, index_label='id')