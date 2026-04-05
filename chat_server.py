import socket

# REGRA: Use os 5 primeiros números do seu TIA
PORTA = 12345 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', PORTA))
s.listen(1)
print("Chat Questão 2 iniciado. Aguardando cliente...")

conn, addr = s.accept()
while True:
    data = conn.recv(1024).decode()
    print(f"Cliente: {data}")
    if data.upper() == "QUIT": # REGRA: Comando QUIT encerra
        break
        
    msg = input("Você: ")
    conn.send(msg.encode())
    if msg.upper() == "QUIT":
        break

conn.close()