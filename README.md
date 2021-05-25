# TOR Nodes RestAPI

 Uma Rest API que obtem e apresenta IPs de redes TOR obtidos a partir de fontes específicas e apresenta
os mesmos em uma interface web que roda como servidor na máquina do próprio usuário como um servidor
Flask.


# Introdução

 Este é um projeto proposto em um processo seletivo que eu participei. A aplicação consiste
em uma Rest API que obtem de duas fontes predefinidas listas de nós e endereços TOR, a partir 
destes dados a aplicação deve apresentar uma interface capaz de "apresentá-los de maneira unificada".
 Por meio de tal interface o usuário deve ser capaz de inserir endereços IP, os quais o usuário não 
quer que apareçam na lista.


# Tecnologias utilizadas

 A escolha das tecnologias utlizadas estava em minhas mãos, portanto optei pelo uso do Python no backend 
e o framework Flask para gerar a web interface, como base de dados utilizei o SQLite. O fator que me
motivou no momento de escolher tais tecnologias, além claro da minha familiaridade com elas, foi o "lado
multi-plataforma" do python, bem como sua performance e versatilidade.


# Requisitos

 Você deve obter primeiramente a [imagem Docker](https://hub.docker.com/r/0x0th30/challenge_api) do projeto.

 Como estou utilizando o recurso de "containers", o projeto não irá apresentar problemas de dependências,
porém você deve ter instalado em sua máquina o client do Docker.

### Em ambientes UNIX/Linux
 Na minha máquina estou utilizando como sistema operacional um Debian Buster (10), portanto estou 
utilizando a versão do Docker correspondente para o mesmo, versão (20.10.6):

- https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce-cli_20.10.6~3-0~debian-buster_amd64.deb
- https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/containerd.io_1.4.4-1_amd64.deb
- https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce_20.10.6~3-0~debian-buster_amd64.deb

### Em ambientes Windows
 Para sistemas operacionais Windows, recomendo esta versão:
 
 - https://download.docker.com/win/static/stable/x86_64/docker-20.10.6.zip

OBS: Certifique-se de que seu usuário esteja no grupo "docker-users" para poder executar o mesmo.


# Executando a aplicação

### Em ambientes UNIX/Linux 
 Para utilizar a aplicação, você deve realizar um clone deste projeto ou baixar um arquivo compactado (.zip)
do mesmo. Feito isso, acesse a pasta raiz do projeto e execute o seguinte comando em seu terminal:

```
docker-compose up
```
ou caso não esteja logado como root:
```
sudo docker-compose up
```


# Utilizando a aplicação

 No momento que você iniciar o container como citado anteriormente, você verá algo do tipo em seu terminal:
 ```
theo@mint:~/Projects/challenge$ sudo docker-compose up
Starting challenge_api_1 ... done
Attaching to challenge_api_1
api_1  |  * Serving Flask app "main" (lazy loading)
api_1  |  * Environment: production
api_1  |    WARNING: This is a development server. Do not use it in a production deployment.
api_1  |    Use a production WSGI server instead.
api_1  |  * Debug mode: off
api_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 ```
Feito isso acesse o endereço retornado e terá acesso á aplicação. O uso dela é realmente bem simples, você terá 
as opções de ver ou banir endereços IP. Para banir algum IP, escreva o mesmo no campo de entrada da página e
clique no botão "Submit", se desejar ver a sua lista de IP's clique no primeiro botão, "Ver IP's encontrados".
