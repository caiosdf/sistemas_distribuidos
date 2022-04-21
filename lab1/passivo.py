# Servidor de echo
# envia de volta para o emissor a mesma mensagem recebida

# lado passivo

import socket
host = '' # interface padrão de comunicação da máquina
port = 6000 # identifica o processo na máquina que recebrá a mensagem

# cria o descritor socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet e TCP

# vincula endereço e porta
sock.bind((host, port))

# coloca em modo de espera
sock.listen(1) # aceita no máximo 1 conexão pendente

# aceitar conexão
novoSock, endereco = sock.accept()
print(f"Conectado com: {str(endereco)}")

while True:
    # esperar por mensagem do lado ativo
    msg = novoSock.recv(1024) # argumento indica o máximo de bytes que será aceito
    if not msg: break
    print(str(msg, encoding='UTF-8'))
    novoSock.send(msg) # envia de volta a mensagem recebida

# fechar o descritor de socket da conexão
novoSock.close()

# fechar o descritor socket principal
sock.close()