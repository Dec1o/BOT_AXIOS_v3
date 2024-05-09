import requests
import dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

def solicitar_token_e_realizar_chamada(origem, destino, gravar='n'):
    # Obter o client_id e client_secret das variáveis de ambiente
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    # Solicitar token de acesso
    url_token = "https://api.directcallsoft.com/request_token"
    data_token = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    response_token = requests.post(url_token, data=data_token)

    if response_token.status_code == 200:
        access_token = response_token.json()['access_token']

        # Realizar chamada telefônica
        url_chamada = "https://api.directcallsoft.com/voz/call"
        data_chamada = {
            'origem': origem,
            'destino': destino,
            'access_token': access_token
        }
        response_chamada = requests.post(url_chamada, data=data_chamada)

        return response_chamada.json()
    else:
        print("Falha ao solicitar token.")
        return None

# Substitua 'origem' e 'destino' pelos valores desejados
origem = os.getenv('ORIGEM')
destino = os.getenv('DESTINO')

# Realizar chamada telefônica
resultado_chamada = solicitar_token_e_realizar_chamada(origem, destino)

if resultado_chamada:
    print(resultado_chamada)
else:
    print("Não foi possível obter o token de acesso ou realizar a chamada.")