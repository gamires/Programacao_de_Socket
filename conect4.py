import numpy as np
import pygame

LINHA_QTD = 6
COLUNA_QTD = 7



def criar_tabuleiro():
    tabuleiro = np.zeros((LINHA_QTD,COLUNA_QTD))
    return tabuleiro
def joga_peca(tabuleiro, linha, coluna, peca):
    tabuleiro[linha][coluna] = peca
      
def pozicao_valida(tabuleiro, coluna):
    return tabuleiro[LINHA_QTD-1][coluna] == 0
    
def pega_proxima_coluna(tabuleiro, coluna):
    for i in range(LINHA_QTD):
         if tabuleiro[i][coluna] == 0:
            return i 
def printa_tabuleiro(tabuleiro):
    print(np.flip(tabuleiro,0))

def lance_ganhador(tabuleiro, peca):
    for i in range(COLUNA_QTD):
         for j in range(LINHA_QTD-3):
            if tabuleiro[j][i] == peca and tabuleiro[j][i+1] == peca and tabuleiro[j][i+2] == peca and tabuleiro[j][i+3] == peca:
                return True
            

    for i in range(COLUNA_QTD-3):
         for j in range(LINHA_QTD):
            if tabuleiro[j][i] == peca and tabuleiro[j+1][i] == peca and tabuleiro[j+2][i] == peca and tabuleiro[j+3][i] == peca:
                return True
            

    for i in range(COLUNA_QTD-3):
         for j in range(LINHA_QTD-3):
            if tabuleiro[j][i] == peca and tabuleiro[j+1][i+1] == peca and tabuleiro[j+2][i+2] == peca and tabuleiro[j+3][i+3] == peca:
                return True


    for i in range(COLUNA_QTD-3):
         for j in range(3,LINHA_QTD):
            if tabuleiro[j][i] == peca and tabuleiro[j-1][i+1] == peca and tabuleiro[j-2][i+2] == peca and tabuleiro[j-3][i+3] == peca:
                return True



# tabuleiro = criar_tabuleiro()
# printa_tabuleiro(tabuleiro)
# fin_jogo = False
# jogada = 0

# while not fin_jogo:
#     #jogador 1 lance
#     if jogada == 0:
#         coluna = int(input("jogador 1 de o seu lance (0-5):"))
#         if pozicao_valida(tabuleiro, coluna):
#             linha = pega_proxima_coluna(tabuleiro, coluna)
#             joga_peca(tabuleiro, linha, coluna, 1)


#             if lance_ganhador(tabuleiro, 1):
#                 print("jogador 1 ganhou!!!")
#                 fin_jogo = True
    





#     #jogador 2 lance
#     else:
#         coluna = int(input("jogador 2 de o seu lance (0-5):"))
#         if pozicao_valida(tabuleiro, coluna):
#             linha = pega_proxima_coluna(tabuleiro, coluna)
#             joga_peca(tabuleiro, linha, coluna, 2)


#             if lance_ganhador(tabuleiro,2):
#                 print("jogador 2 ganhou!!!")
#                 fin_jogo = True

#     printa_tabuleiro(tabuleiro)
#     jogada += 1
#     jogada = jogada % 2