import socket

target_host = "192.168.0.4"
target_port = 80

#　ソケットオブジェクトの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#サーバへ接続
client.connect((target_host,target_port))

#データの送信
client.send(b"hi")

#データ受信
response = client.recv(4096)

print(response)
