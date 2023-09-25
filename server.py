from random import randint
import socket

massiv = [
    ['CTF', 'Q1RG'],
    ['KVVU', 'S1ZWVQ=='],
    ['TEAM8', 'VEVBTTg='],
    ['TITOV', 'VElUT1Y='],
    ['DANILOV', 'REFOSUxPVg=='],
]
# print('You should send the answer 10 times!')
# print('Let\'s start:')


HOST = "0.0.0.0"
PORT = 2012

def socket_server():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.sendall('Привет, нужна твоя помощь!\nЯ получаю странные данные, которые нужно расшифровать и отправить оригинальные данные обратно.\nНо есть проблема, это нужно сделать 100 раз!\n\nНачнем:\n'.encode())
        for i in range(100):
            a = randint(0, 4)
            conn.send('{}/100 {}: '.format(i+1, massiv[a][1]).encode())
            b = conn.recv(1024).decode().strip()
            if b == massiv[a][0]:
                conn.send('Верно!\n'.encode())
            else:
                conn.send('Неправильно!\nПопробуй заново!'.encode())
                break
    s.close()

if __name__ == '__main__':
    socket_server()