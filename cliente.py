import socket
import conect4

PORTA_TIA = 12345 # Deve ser a mesma porta do servidor

def iniciar_cliente():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORTA_TIA))
    print("Conectado ao Servidor (Jogador 1)!")

    tabuleiro = conect4.criar_tabuleiro()
    conect4.printa_tabuleiro(tabuleiro)
    fin_jogo = False

    while not fin_jogo:
        # 1. AGUARDA A VEZ DO SERVIDOR (JOGADOR 1)
        print("Aguardando a jogada do Jogador 1...")
        jogada_recebida = client_socket.recv(1024).decode()
        coluna_adversario = int(jogada_recebida)
        
        linha_adv = conect4.pega_proxima_coluna(tabuleiro, coluna_adversario)
        conect4.joga_peca(tabuleiro, linha_adv, coluna_adversario, 1)
        print(f"O Jogador 1 jogou na coluna {coluna_adversario}")
        conect4.printa_tabuleiro(tabuleiro)

        if conect4.lance_ganhador(tabuleiro, 1):
            print("O Jogador 1 ganhou!!!")
            break

        # 2. VEZ DO CLIENTE (JOGADOR 2)
        coluna = int(input("Sua vez (Jogador 2) - Escolha uma coluna (0-5): "))
        
        if conect4.pozicao_valida(tabuleiro, coluna):
            linha = conect4.pega_proxima_coluna(tabuleiro, coluna)
            conect4.joga_peca(tabuleiro, linha, coluna, 2)
            conect4.printa_tabuleiro(tabuleiro)
            
            # Envia a jogada de volta para o Servidor
            client_socket.send(str(coluna).encode())

            if conect4.lance_ganhador(tabuleiro, 2):
                print("Você (Jogador 2) ganhou!!!")
                break

    client_socket.close()

iniciar_cliente()