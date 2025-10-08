from selenium import webdriver
from selenium.webdriver import firefox

if  __name__== "__main__":
    url = "https://www.in.gov.br/en/web/dou/-/portaria-mgi-n-8.730-de-7-de-outubro-de-2025-661024013"
    opcoes = firefox.options.Options()
    opcoes.add_argument("--headless")
    servico = firefox.Service("/snap/bin/geckodriver")
    driver = webdriver.Firefox(service=servico, options=opcoes)
    driver.get(url)
    html = driver.page_source
    driver.close()
    print(html)
    

