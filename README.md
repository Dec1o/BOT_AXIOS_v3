![123](https://github.com/Dec1o/BOT_AXIOS_v3/assets/104839239/b8140e7f-4f71-4c7d-a2c5-2ec85b490b2f)


# Documentação BOT ASSYST:



# Módulo "BOT.py":


# Descrição:

O BOT ASSYST v3 é uma automação desenvolvida por mim "Décio Carvalho Faria", sob medida, para automatizar o sistema AXIOS ASSYST, de forma que, reconheça os chamados com SLA de curto prazo em poucos segundos e em 
seguida realize uma ligação para o profissional designado a resolução dos referidos chamados.


# Bibliotecas Utilizadas:

Selenium: Utilizada para automatizar a interação com o navegador web.

Webdriver_manager: Utilizada para gerenciar o driver do navegador Chrome automaticamente.

time: Utilizada para adicionar pausas entre as operações.


# Instalação das Dependências Externas:

pip install selenium webdriver-manager


# Funções Principais:

clicar_se_existir(xpath, navegador): Clica em um elemento se ele existir na página.

iniciar_assyst(navegador): Realiza o login no sistema Assyst e navega até a seção desejada.

reiniciar_navegador(navegador): Reinicia o navegador.

Loop principal: Atualiza a página, executa ações no sistema Assyst e realiza chamadas para o script "CALL.py".


# Variáveis Globais:
chrome_options: Opções de inicialização do navegador Chrome.

servico: Serviço do driver do Chrome.

navegador: Instância do navegador Chrome.



# Módulo "CALL.py":


# Descrição:

O "CALL.py" é um script que realiza chamadas telefônicas utilizando a API da DirectCall. Ele solicita um token de acesso, realiza a chamada e retorna o resultado.


# Bibliotecas Utilizadas:

requests: Utilizada para fazer requisições HTTP.
dotenv: Utilizada para carregar variáveis de ambiente a partir do arquivo. env.
os: Utilizada para acessar variáveis de ambiente.


#Instalação das Dependências Externas:

pip install selenium webdriver-manager
pip install python-dotenv
Funções Principais:
solicitar_token_e_realizar_chamada(origem, destino, gravar='n'): Solicita um token de acesso e realiza uma chamada telefônica



# Arquivo ".env":


# Variáveis de Ambiente:

CLIENT_ID: ID do cliente para autenticação na API da DirectCall.

CLIENT_SECRET: Chave secreta para autenticação na API da DirectCall.

ORIGEM: Número de telefone de origem da chamada.

DESTINO: Número de telefone de destino da chamada.


# Uso:

Substitua os valores de ORIGEM e DESTINO pelas informações desejadas e execute o script para realizar a chamada.
