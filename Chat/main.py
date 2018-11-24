import player_pb2
import tcp_packet_pb2
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


# create a lobby 
def create_lobby():
	lobby = tcp_packet_pb2.TcpPacket.CreateLobbyPacket()
	lobby.type = tcp_packet_pb2.TcpPacket.CREATE_LOBBY
	lobby.max_players = 3
	client_socket.send(lobby.SerializeToString())
	data = client_socket.recv(1024)
	lobby.ParseFromString(data)
	print("Created lobby", lobby.lobby_id)
	return lobby.lobby_id

# join a lobby
def join_lobby(lobbyId):
	connection = tcp_packet_pb2.TcpPacket.ConnectPacket()
	connection.type = tcp_packet_pb2.TcpPacket.CONNECT
	connection.lobby_id = lobbyId
	connection.player.CopyFrom(player)
	client_socket.send(connection.SerializeToString())
	connect_data = client_socket.recv(1024)
	connection.ParseFromString(connect_data)
	print("Connected to", connection.lobby_id)

# receive messages
def receive_msg():
    while True:
    	chat_data = client_socket.recv(1024)
    	tcp_packet = tcp_packet_pb2.TcpPacket()
    	tcp_packet.ParseFromString(chat_data)
    	if tcp_packet.type == tcp_packet_pb2.TcpPacket.CHAT:
    		chat_packet = tcp_packet_pb2.TcpPacket.ChatPacket()
    		chat_packet.ParseFromString(chat_data)
    		player_name = chat_packet.player.name
    		msg = chat_packet.message
    		print(player_name,":", msg)

# send messages
def send_msg(): 
	while True:
		msg = input()
		chat = tcp_packet_pb2.TcpPacket.ChatPacket()
		chat.type = tcp_packet_pb2.TcpPacket.CHAT
		chat.message = msg  
		client_socket.send(chat.SerializeToString())
  

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("202.92.144.45", 80))
print("Connected to server!\n")

choice = 0
#get player name
player_name = input("Enter name: ")	

# create player 
player = player_pb2.Player()
player.name = player_name

# display menu
while choice != 3:
	print("What do you wish to do?")
	print("[1] Create a lobby")
	print("[2] Join a lobby")
	print("[3] Leave")
	choice = int(input(">> "))

	# create a lobby
	if choice == 1:
		lobbyId = create_lobby()
		join_lobby(lobbyId)
		
		# allows player to send and receive msgs
		receive_thread = Thread(target=receive_msg)
		send_thread = Thread(target=send_msg)
		receive_thread.start()
		send_thread.start()
		break;
	
	# join a lobby
	if choice == 2:
		lobbyId = input("Enter lobby id: ")
		join_lobby(lobbyId)
		
		# allows player to send and receive msgs
		receive_thread = Thread(target=receive_msg)
		send_thread = Thread(target=send_msg)
		receive_thread.start()
		send_thread.start()
		break;

	# leave chat room
	if choice == 3:
		print("Leaving...")
		break;

	client_socket.close();






