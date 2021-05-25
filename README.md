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
