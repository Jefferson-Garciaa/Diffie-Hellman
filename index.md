## Diffie-Hellman - Redes 2
## Aluno: Jefferson Garcia
## Professor: Elias P. Duarte Jr.

### Códigos Fontes

[Client.py](https://github.com/Jefferson-Garciaa/Diffie-Hellman/blob/main/Page/client.py.txt) |
[Server.py](https://github.com/Jefferson-Garciaa/Diffie-Hellman/blob/main/Page/server.py.txt) |
[Log Client](https://github.com/Jefferson-Garciaa/Diffie-Hellman/blob/main/Page/log_client.txt.txt) |
[Log Server](https://github.com/Jefferson-Garciaa/Diffie-Hellman/blob/main/Page/log_server.txt.txt)

### Relatório
O trabalho consiste em 3 partes principais:
1-	Estabelecer uma conexão socket entre servidor e cliente.
2-	Fazer o passo a passo do algoritmo de Diffie-Hellman para obter a chave secreta.
3-	Trabalhar toda a parte de criptografia usando a chave obtida.

#### Estabelecendo conexão
Primeiramente falarei sobre a conexão socket que foi estabelecida.
Usando a biblioteca Python “socket” ficou fácil estabelecer a conexão em poucas linhas de código.
Foi usado HOST = ‘localhost’ e PORT = 50000.
A conexão foi uma etapa tranquila, sem complicações.

#### Gerando as chaves
Passando para o Diffie-Hellman, foi usado como referência a seguinte página: [https://medium.com/@sadatnazrul/diffie-hellman-key-exchange-explained-python-8d67c378701c](https://medium.com/@sadatnazrul/diffie-hellman-key-exchange-explained-python-8d67c378701c).

É importante destacar que em um cenário real os números usados seriam diferentes em alguns aspectos: seriam números realmente grandes, da ordem de centenas de dígitos, a chave pública que é usada como mod deveria ser primo, ou um produto de primos, pela dificuldade de fatoração. Neste trabalho não levei em consideração esses fatores por não serem relevantes na ocasião.
A execução começa com client.py gerando aleatoriamente as duas chaves públicas, uma servirá como base (na imagem abaixo é o 197) e outra servirá como módulo (151).  
Client.py também gera aleatoriamente a sua chave privada (157). Client passa as chaves públicas para server.py, através da conexão secket, e mantém a chave privada somente para si, ao passo que server.py recebe as chaves e aleatoriamente gera uma chave privada, que também será mantida somente para si (199).

![Image](https://github.com/Jefferson-Garciaa/Diffie-Hellman/blob/main/Page/imagens/imagem1.png?raw=true)

Após estabelecidas as chaves, são feitos os primeiros cálculos, a ideia neste primeiro momento é gerar as respectivas chaves parciais. A equação é a seguinte:

![Image](https://github.com/Jefferson-Garciaa/Diffie-Hellman/blob/main/Page/imagens/imagem2.png?raw=true)

Após ambos obterem suas chaves parciais, elas são enviadas, ou seja, o server recebe a chave parcial do client e vice-versa.


Agora o último passo para obter a chave completa é a seguinte equação:

![Image](https://github.com/Jefferson-Garciaa/Diffie-Hellman/blob/main/Page/imagens/imagem3.png?raw=true)

Necessariamente o mesmo resultado deve ser obtido, pois ele será usado para criptografar a mensagem e sem ele a mensagem não pode ser descriptografada corretamente, exemplos serão mostrados ao final do relatório.















