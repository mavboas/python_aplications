'''
Versão 1.1 Marcelo Vilas Boas - 22/10/2019 10:51

Requisitos: - Instalação das biblioteca Selenium
'''

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

def conecta_sessao(executor_url, session_id):

    original_execute = WebDriver.execute

    def executa_novo_comando(self, command, params=None):

        if command == "newSession":
            # Simula resposta
            return {'successo': 0, 'valor': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)

    # correção da funcao antes de criar o objeto do driver

    WebDriver.execute = executa_novo_comando
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id

    # Substitui funcao corrigida pela original

    WebDriver.execute = original_execute

    return driver
