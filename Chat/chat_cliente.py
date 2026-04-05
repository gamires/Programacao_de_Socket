import socket

PORTA = 10443 # Mesma porta do servidor
IP_SERVIDOR = 'localhost'

def iniciar_cliente():
    # Criação do socket TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conecta ao servidor que deve estar rodando primeiro
        cliente.connect((IP_SERVIDOR, PORTA))
        print(f"--- Chat Conectado na porta {PORTA} ---")
        print("Digite as mensagens abaixo. Envie 'QUIT' para sair.")
        
        while True:
            # 1. Enviar mensagem para o servidor
            msg = input("Você: ")
            cliente.send(msg.encode('utf-8'))
            
            # Verifica se o cliente quer sair
            if msg.upper() == "QUIT":
                print("Você encerrou o chat.")
                break
            
            # 2. Receber resposta do servidor
            print("Aguardando servidor...")
            resposta = cliente.recv(1024).decode('utf-8')
            
            # Verifica se o servidor enviou QUIT ou fechou a conexão
            if not resposta or resposta.upper() == "QUIT":
                print("O servidor encerrou o chat.")
                break
                
            print(f"Servidor: {resposta}")
            
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar. O servidor está ligado?")
    finally:
        cliente.close()

if __name__ == "__main__":
    iniciar_cliente()