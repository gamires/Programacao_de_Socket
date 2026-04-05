import socket
import conect4 # Importa as funções do seu arquivo conect4.py

PORTA_TIA = 10443 

def iniciar_servidor():
    # Configurando o Socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORTA_TIA))
    server_socket.listen(1)
    
    print(f"Aguardando o Jogador 2 conectar na porta {PORTA_TIA}...")
    conn, addr = server_socket.accept()
    print(f"Jogador 2 conectado: {addr}")

    tabuleiro = conect4.criar_tabuleiro()
    conect4.printa_tabuleiro(tabuleiro)
    fin_jogo = False

    while not fin_jogo:
        # 1. VEZ DO SERVIDOR (JOGADOR 1)
        coluna = int(input("Sua vez (Jogador 1) - Escolha uma coluna (0-5): "))
        
        if conect4.pozicao_valida(tabuleiro, coluna):
            linha = conect4.pega_proxima_coluna(tabuleiro, coluna)
            conect4.joga_peca(tabuleiro, linha, coluna, 1)
            conect4.printa_tabuleiro(tabuleiro)
            
            # Envia a jogada (coluna) para o Jogador 2
            conn.send(str(coluna).encode())

            if conect4.lance_ganhador(tabuleiro, 1):
                print("Você (Jogador 1) ganhou!!!")
                break
        
        # 2. AGUARDA A VEZ DO CLIENTE (JOGADOR 2)
        print("Aguardando a jogada do Jogador 2...")
        jogada_recebida = conn.recv(1024).decode()
        coluna_adversario = int(jogada_recebida)
        
        # Atualiza o tabuleiro com a jogada que veio da rede
        linha_adv = conect4.pega_proxima_coluna(tabuleiro, coluna_adversario)
        conect4.joga_peca(tabuleiro, linha_adv, coluna_adversario, 2)
        print(f"O Jogador 2 jogou na coluna {coluna_adversario}")
        conect4.printa_tabuleiro(tabuleiro)

        if conect4.lance_ganhador(tabuleiro, 2):
            print("O Jogador 2 ganhou!!!")
            break

    conn.close()

iniciar_servidor()