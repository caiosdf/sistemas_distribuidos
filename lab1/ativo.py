# lado ativo

import socket

host = 'localhost'
port = 6000

# criar descritor de socket
sock = socket.socket() # AF_INET, SOCK_STREAM

# estabelecer conexão
sock.connect((host, port))

# repetir o processo enquanto o usuário nao digitar 'exit'
while True:
    # instrução para parar o programa
    print("Para sair digite 'exit'")
    # recebe a mensagem do usuário
    input_msg = input('digite aqui sua mensagem: ')
    # quebra o loop caso o usuário digite a palavra 'exit'
    if(input_msg.lower() == 'exit' or not input_msg.lower()): break
    # enviar mensagem digitada pelo usuário   
    sock.send(input_msg.encode('UTF-8'))
    # receber resposta do lado passivo
    msg = sock.recv(1024)
    print(str(msg, encoding='UTF-8'))
    print('\n')

# encerrar conexão
sock.close()