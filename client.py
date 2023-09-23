import socket
import sys
import json

HOST, PORT = "localhost", 9999
data = 100
while (True):
    print("Python DB Menu\n")
    print("1. Find Customer")
    print("2. Add Customer")
    print("3. Delete Customer")
    print("4. Update Customer age")
    print("5. Update Customer address")
    print("6. Update Customer phone")
    print("7. Print report")
    print("8. Exit \n")
    data = input("Select: ")
    if data == "1":
        name = input("Customer Name: ").strip()
        data = data+","+name
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            #alist = json.loads(received)
            print("Recieved: "+received)
    if data == "2":
        name = input("Enter name of new customer: ")
        age = input("Enter age of new customer: ")
        address = input("Enter address of new customer: ")
        phoneNumber = input("Enter phone number of new customer: ")
        data = data+","+name+","+age+","+address+","+phoneNumber
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            #alist = json.loads(received)
    if data == "3":
        name = input("Customer Name: ").strip()
        data = data+","+name
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            #alist = json.loads(received)
    if data == "4":
        name = input("Customer name: ")
        age = input("Enter new customer address: ")
        data = data+","+name+","+age
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            #alist = json.loads(received)
    if data == "5":
        name = input("Customer name: ")
        address = input("Enter new customer address: ")
        data = data+","+name+","+address
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            #alist = json.loads(received)
    if data == "6":
        name = input("Customer name: ")
        phoneNumber = input("Enter new customer address: ")
        data = data+","+name+","+phoneNumber
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            #alist = json.loads(received)
    if data == "7":
        print("** Python DB contents **")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            alist = json.loads(received)
            for x in alist:
                print(x)
    if data == "8":
        sys.exit("Thank you for using our application and we hope to see you in the near future.")