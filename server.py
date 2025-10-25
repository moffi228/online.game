from socket import*
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 90909))
sock.listen(5)
sock.setblocking(False)
conn, adr = sock.accept()
players= {}
conn_ids ={}
id_counter = 0
players_data=packet.split("|")