import socket
from fish import Fish

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = "Hello, Server"

clientSocket =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))

counter = 0
while (counter != 3):
	Message = input("Input Message to send to server: ")
	if(Message.startswith("SEND")):
		playerFish = Fish(bright_blue, 45, 45)
		playerFish.rect.x = 50 # initial x pos
		playerFish.rect.y = 50 # initial y pos
		clientSocket.sendto(playerFish.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
		counter += 1