from selenium import webdriver  #importar o navegador



class Browser(object):
    # Inicia o browser chrome, mas pode ser feito com outros como Firefox, Safari e IE
    driver = webdriver.Chrome()




# Define o tempo máximo para carregamento da página
    driver.set_page_load_timeout(30)

#Para abrir em nova aba
webbrowser.open('nabinkhadka.com.np', new = 2)
