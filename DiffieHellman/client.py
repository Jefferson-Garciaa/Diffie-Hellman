import socket
from random import randint
from simplecrypt import encrypt, decrypt
#import des

HOST = 'localhost'
PORT = 50000

MIN = 1
MAX = 10 ** 3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

msg1 = 'Porque Deus tanto amou o mundo'

msg2 = 'que deu o seu Filho Unigenito'

msg3 = 'para que todo o que nEle crer' 

msg4 = 'nao pereca, mas tenha a vida eterna.'

msgErrada = 'Esta eh a mensagem que usarei a chave errada'

try:
    #------PROCESSO DE CRIAÇÃO DE CHAVES------
    print("GERANDO ALEATORIAMENTE A CHAVE PÚBLICA")
    CPublicKey = randint(MIN, MAX)
    print("CHAVE PÚBLICA GERADA : ", CPublicKey)
    print("ENVIANDO CHAVE ALEATÓRIA PARA O SERVIDOR.")
    s.sendall(CPublicKey.to_bytes(5, "little"))
    print(" \n")

    print("GERANDO ALEATORIAMENTE CHAVE PRIVADA DO CLIENTE")
    CPrivateKey = randint(MIN, MAX)
    print("CHAVE PRIVADA DO CLIENTE GERADA : ", CPrivateKey)

    print("GERANDO ALEATORIAMENTE CHAVE PÚBLICA QUE SERVIRÁ COMO MOD")
    KeyMod = randint(MIN, MAX)
    print("VALOR DA CHAVE PÚBLICA MOD : ", KeyMod)
    s.sendall(KeyMod.to_bytes(5, "little"))
    print(" \n")

    #criando a chave parcial
    print("CRIANDO A CHAVE PARCIAL")
    CPartialKey = CPublicKey ** CPrivateKey
    CPartialKey = CPartialKey % KeyMod
    print("CHAVE PARCIAL GERADA : ", CPartialKey)
    
    #enviando chave parcial p/ servidor
    print("ENVIANDO CHAVE PARCIAL PARA O SERVIDOR")    
    s.sendall(repr(CPartialKey).encode())

    #recebendo chave parcial do servidor
    print("RECEBENDO A CHAVE PARCIAL DO SERVIDOR")
    SPartialKey = int(s.recv(32))
    print("CHAVE PARCIAL RECEBIDA : ", SPartialKey)

    #GERANDO A CHAVE COMPLETA
    print("GERANDO CHAVE COMPLETA")
    KeyFull = SPartialKey ** CPrivateKey
    KeyFull = KeyFull % KeyMod
    print("VALOR DA CHAVE COMPLETA : ", KeyFull)
    print(" \n")

    #------------------Troca de chaves concluída-------------#
    #
    #***************Início da encriptação********************#
    print("USANDO A CHAVE COMPLETA PARA CRIPTOGRAFAR A PRIMEIRA MENSAGEM")
    print("MENSAGEM ORIGINAL = ", msg1)
    print(" \n")
    ciphertext = encrypt(str(KeyFull), msg1)
    print("MENSAGEM CRIPTOGRAFADA : ")
    print (ciphertext)
    print(" \n")
    print("ENVIANDO MENSAGEM CRIPTOGRAFADA PARA O SERVIDOR")
    s.sendall(ciphertext)
    print(" \n")
    


    print("USANDO A CHAVE COMPLETA PARA CRIPTOGRAFAR A SEGUNDA MENSAGEM")
    print("MENSAGEM ORIGINAL = ", msg2)
    print(" \n")
    ciphertext = encrypt(str(KeyFull), msg2)
    print("MENSAGEM CRIPTOGRAFADA : ")
    print (ciphertext)
    print(" \n")
    print("ENVIANDO MENSAGEM CRIPTOGRAFADA PARA O SERVIDOR")
    s.sendall(ciphertext)
    print(" \n")
    


    print("USANDO A CHAVE COMPLETA PARA CRIPTOGRAFAR A TERCEIRA MENSAGEM")
    print("MENSAGEM ORIGINAL = ", msg3)
    print(" \n")
    ciphertext = encrypt(str(KeyFull), msg3)
    print("MENSAGEM CRIPTOGRAFADA : ")
    print (ciphertext)
    print(" \n")
    print("ENVIANDO MENSAGEM CRIPTOGRAFADA PARA O SERVIDOR")
    s.sendall(ciphertext)
    print(" \n")
    


    print("USANDO A CHAVE COMPLETA PARA CRIPTOGRAFAR A QUARTA MENSAGEM")
    print("MENSAGEM ORIGINAL = ", msg4)
    print(" \n")
    ciphertext = encrypt(str(KeyFull), msg4)
    print("MENSAGEM CRIPTOGRAFADA : ")
    print (ciphertext)
    print(" \n")
    print("ENVIANDO MENSAGEM CRIPTOGRAFADA PARA O SERVIDOR")
    s.sendall(ciphertext)
    print(" \n")


    print("USANDO A CHAVE COMPLETA PARA CRIPTOGRAFAR A MENSAGEM ERRADA")
    print("MENSAGEM ORIGINAL = ", msgErrada)
    print(" \n")
    ciphertext = encrypt(str(KeyFull), msgErrada)
    print("MENSAGEM CRIPTOGRAFADA : ")
    print (ciphertext)
    print(" \n")
    print("ENVIANDO MENSAGEM CRIPTOGRAFADA PARA O SERVIDOR")
    s.sendall(ciphertext)
    print(" \n")
    
   
   
  

finally:
    s.close()




