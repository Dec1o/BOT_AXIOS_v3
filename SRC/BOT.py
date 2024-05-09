from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def clicar_se_existir(xpath, navegador):
    try:
        navegador.find_element(By.XPATH, xpath).click()
        return True
    except NoSuchElementException:
        print(f"Elemento {xpath} não encontrado. Continuando...")
        return False


def iniciar_assyst(navegador):
    # Abrir o Assyst no Google Chrome:
    time.sleep(4)
    navegador.get("LINK_DO_ASSYST")

    # Fazer login no Assyst:
    time.sleep(4)
    navegador.find_element(By.XPATH, '//*[@id="login-user"]').send_keys("seu_user")
    navegador.find_element(By.XPATH, '//*[@id="login-password"]').send_keys("seu_password")
    navegador.find_element(By.XPATH, '//*[@id="loginSubmit"]').click()

    # Clicar em "Pesquisar":
    time.sleep(10)
    navegador.find_element(By.XPATH, '//*[@id="dijit__TreeNode_11_label"]').click()

    # Clicar em "Monitor de eventos":
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="dijit__TreeNode_15_label"]').click()

    # Atualizar pela aba do menu:
    time.sleep(4)
    navegador.find_element(By.XPATH, '//*[@id="dijit__TreeNode_22_label"]').click()


def reiniciar_navegador(navegador):
    navegador.quit()
    navegador = webdriver.Chrome(service=servico, options=chrome_options)
    iniciar_assyst(navegador)  # Chamar a função iniciar_assyst após reiniciar o navegador
    return navegador


# Iniciar o Google Chrome e assyst:
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
iniciar_assyst(navegador)

while True:
    contador = 0

    # Atualizar pelo botão refresh:
    try:
        time.sleep(5)
        WebDriverWait(navegador, 10).until(EC.invisibility_of_element_located((By.ID, "contentOverlay")))
        navegador.find_element(By.XPATH, '//*[@id="emRefresh_button"]/div[1]').click()
    except ElementClickInterceptedException:
        print("Elemento obstrutivo ainda presente. Tentando novamente...")
        continue
    except TimeoutException:
        print("TimeoutException ocorreu. Reiniciando o navegador...")
        navegador = reiniciar_navegador(navegador)
        continue

    # Clicar em ações:
    time.sleep(3)
    if not clicar_se_existir('//*[@id="menuActions_label"]', navegador):
        continue

    # Clicar em "reconhecer chamado":
    time.sleep(2)
    if not clicar_se_existir('//*[@id="menuActions_$DisplayOnceAction(USER_CALLBACK)_text"]', navegador):
        continue

    # Clicar em "Salvar Ações":
    time.sleep(2)
    if not clicar_se_existir('//*[@id="ManageActionForm.btSave_label"]', navegador):
        continue
    else:
        contador += 1

    # Atualizar pela aba do menu:
    time.sleep(4)
    navegador.find_element(By.XPATH, '//*[@id="dijit__TreeNode_22_label"]').click()

    # Realizar ligação após reconhecer chamado:
    if contador == 1:
        time.sleep(1)
        from SRC.CALL import solicitar_token_e_realizar_chamada
