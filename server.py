import socket
import threading
import random
import base64
import string
import time


def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
massiv = []
for _ in range(100):
    random_string = generate_random_string(16)
    base64_encoded = base64.b64encode(random_string.encode()).decode()
    massiv.append([random_string, base64_encoded])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 8888
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(5)
active_clients = []

def handle_client(client_socket):
    try:
        client_socket.send('\nПривет, нужна твоя помощь!\nЯ получаю странные данные, которые нужно расшифровать и отправить оригинальные данные обратно.\nНо есть 2 проблемы, на каждый ответ нужно тратить не больше 5 секунд и это нужно сделать 100 раз!\n\nНачнем:\n'.encode())
        for i in range(100):
            time_start = time.time()
            a = random.randint(0, 4)
            client_socket.send('{}/100 {}: '.format(i+1, massiv[a][1]).encode())
            b = client_socket.recv(1024).decode().strip()
            if b == massiv[a][0]:
                time_end = time.time()
                if (time_end - time_start) <= 5:
                    client_socket.send('Верно!\n'.encode())
                else:
                    client_socket.send('Сожалею, ты не успел. Попробуй заново!\n'.encode())
                    break
            else:
                client_socket.send('Неправильно! Попробуй заново!\n'.encode())
                break
    finally:
        client_socket.close()
        active_clients.remove(client_socket)

while True:
    client_socket, client_address = server_socket.accept()
    active_clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
