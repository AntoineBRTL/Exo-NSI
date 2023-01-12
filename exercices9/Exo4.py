import socket, ssl

hostname = "maths-et-tiques.fr"
ctx = ssl.create_default_context()

s = socket.create_connection((hostname, 443))
ss = ctx.wrap_socket(s, server_hostname=hostname)

ss.write("GET index.html HTTP/1.1\n\n".encode())

buffer = ss.read(400)
while len(buffer) > 0:
    print(buffer.decode())
    buffer = ss.read(400)

ss.close()