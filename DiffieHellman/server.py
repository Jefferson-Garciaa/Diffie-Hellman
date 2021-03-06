import socket
from random import randint
from simplecrypt import encrypt, decrypt
#import des

HOST = 'localhost'
PORT = 50000

MIN = 1
MAX = 10 ** 3

#objeto s é um socket, os paramentros são 
#(familia de protocolos, tipo de protocolo)
#onde socket.AFK_INET == IPv4 e socket.SOCK_STRAM == TCP.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão do Cliente')
conn, adress = s.accept()
print('Conectado em', adress)
print(" \n")

try:
    buffer = conn.recv(1024)
    SPublicKey = int.from_bytes(buffer, "little")
    print("CHAVE PÚBLICA RECEBIDA : ", SPublicKey)

    print("GERANDO ALEATORIAMENTE CHAVE PRIVADA DO SERVIDOR")
    SPrivateKey = randint(MIN, MAX)
    print("VALOR DA CHAVE PRIVADA DO SERVIDOR : ", SPrivateKey)
    

    buffer = conn.recv(1024)
    KeyMod = int.from_bytes(buffer, "little")
    print("CHAVE PÚBLICA MOD RECEBIDA :", KeyMod)


    #criando a chave parcial
    print("CIANDO A CHAVE PARCIAL")
    SPartialKey = SPublicKey ** SPrivateKey
    SPartialKey = SPartialKey % KeyMod
    print("CHAVE PARCIAL GERADA : ", SPartialKey)

    #recebendo chave parcial do cliente
    print("RECEBENDO A CHAVE PARCIAL DO CLIENTE")
    CPartialKey = int(conn.recv(32))
    print("CHAVE PARCIAL RECEBIDA DO CLIENTE : ", CPartialKey)

    #enviando chave parcial p/ cliente
    print("ENVIANDO A CHAVE PARCIAL DO SERVIDOR PARA O CLIENTE")
    conn.sendall(repr(SPartialKey).encode())

    #GERANDO A CHAVE COMPLETA
    print("GERANDO CHAVE COMPLETA")
    KeyFull = CPartialKey ** SPrivateKey
    KeyFull = KeyFull % KeyMod
    print("VALOR DA CHAVE COMPLETA: ", KeyFull)
    print(" \n")
    #------------------Troca de chaves concluída-------------#
    #
    #***************Início da descriptação********************#
    print("RECEBENDO PRIMEIRA MENSAGEM CRIPTOGRAFADA")
    ciphertext = conn.recv(128)
    msg1 = str(decrypt(str(KeyFull), ciphertext))
    print("MENSAGEM APÓS DESCRIPTOGRAFIA USANDO A CHAVE = ", msg1)
    print(" \n")


    print("RECEBENDO SEGUNDA MENSAGEM CRIPTOGRAFADA")
    ciphertext = conn.recv(128)
    msg2 = str(decrypt(str(KeyFull), ciphertext))
    print("MENSAGEM APÓS DESCRIPTOGRAFIA USANDO A CHAVE = ", msg2)
    print(" \n")


    print("RECEBENDO TERCEIRA MENSAGEM CRIPTOGRAFADA")
    ciphertext = conn.recv(128)
    msg3 = str(decrypt(str(KeyFull), ciphertext))
    print("MENSAGEM APÓS DESCRIPTOGRAFIA USANDO A CHAVE = ", msg3)
    print(" \n")

    print("RECEBENDO QUARTA MENSAGEM CRIPTOGRAFADA")
    ciphertext = conn.recv(128)
    msg4 = str(decrypt(str(KeyFull), ciphertext))
    print("MENSAGEM APÓS DESCRIPTOGRAFIA USANDO A CHAVE = ", msg4)
    print(" \n")


    print("USANDO UMA CHAVE ERRADA")
    print("A CHAVE ERRADA SERÁ A CHAVE COMPLETA + 10")
    ChaveErrada = KeyFull + 10
    print("RECEBENDO MENSAGEM CRIPTOGRAFADA")
    ciphertext = conn.recv(128)
    msgErrada = str(decrypt(str(ChaveErrada), ciphertext))
    print("MENSAGEM APÓS DESCRIPTOGRAFIA USANDO A CHAVE ERRADA = ", msgErrada)
    print(" \n")
  
  
  

finally:
    conn.close()