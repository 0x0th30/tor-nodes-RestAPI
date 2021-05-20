# aqui eu realizei a importação das bibliotecas necessárias
import requests, json

# array que irá armazenar os nosso IP's
ipList = list()


# e nesta rotina é realizada a requisição GET para o primeiro endereço
def firstTarget():
    bruteJSON = requests.get("https://onionoo.torproject.org/summary?limit=5000")
    newJSON = json.loads(bruteJSON.text)                     # conversão para JSON
    relays = newJSON['relays']                               # acesso ao objeto "relays" do nosso JSON
    
    # iteração for que adiciona os IP's encontrados a um array pré-definido
    for ip in relays:
        ipList.append(ip['a'][0])


# e nesta rotina é realizada a requisição GET para o segundo endereço
def secndTarget():
    url = requests.get("https://www.dan.me.uk/torlist")
    bruteIPs = url.text
    
    # iteração for que adiciona os IP's encontrados a um array pré-definido
    ipList.append(bruteIPs)


# método que irá chamar as duas funções
def getAll():
    firstTarget()
    secndTarget()
    
    # laço for para verificação de possíveis erros
    i = 1
    for ip in ipList:
        print(f'IP: {i}   ==>  {ip}')
        i += 1


getAll()
