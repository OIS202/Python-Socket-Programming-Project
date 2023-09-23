import socketserver
import json
lines = []
with open('data.txt') as f:
    line = f.readline()
    while line != '':
        space = False
        line = f.readline()
        parts = line.split("|")
        for x in parts:
            if(x.isspace()):
                space = True
        if(space == False):
            lines.append(line)
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
           
        self.data = str(self.request.recv(1024),"utf-8")
        parameters = self.data.split(",")
        if(parameters[0] == "1"):
            print("Find Customer")
            target = parameters[1].lower()
            found = False
            for i in range(len(lines)):
                record = ""
                for x in lines[i]:
                    if(x == "|"):
                        break
                    elif(x == " "):
                        continue
                    record = record + x
                record = record.lower()
                record = record.strip()
                if(record == target):
                    sending = bytes(lines[i],"utf-8")
                    found = True
                    print("yes")
            if (found == False):
                message = target+" not found in database"
                sending = bytes(message,"utf-8")
        if(parameters[0] == "2"):
            print("Add Customer")
            target = parameters[1].lower()
            found = False
            for i in range(len(lines)):
                record = ""
                for x in lines[i]:
                    if(x == "|"):
                        break
                    elif(x == " "):
                        continue
                    record = record + x
                record = record.lower()
                record = record.strip()
                if(record == target):
                    found = True
            if(found == True):
                message = "Customer already exists"
                sending = bytes(message,"utf-8")
            if(found == False):
                newRecord = parameters[1]+"|"+parameters[2]+"|"+parameters[3]+"|"+parameters[4]
                lines.append(newRecord)
                message = "We have successfully added "+parameters[1]+" into our database"
                sending = bytes(message,"utf-8")
        if(parameters[0] == "3"):
            print("Delete Customer")
            target = parameters[1].lower()
            found = False
            for i in range(len(lines)):
                record = ""
                for x in lines[i]:
                    if(x == "|"):
                        break
                    elif(x == " "):
                        continue
                    record = record + x
                record = record.lower()
                record = record.strip()
                if(record == target):
                    found = True
                    message = "Customer named "+target+" has been successfully deleted"
                    sending = bytes(message,"utf-8")
                    lines.pop(i)
                    break
            if(found == False):
                message = "Customer doesn't exist"
                sending = bytes(message,"utf-8")
        if(parameters[0] == "4"):
            print("Update Customer age")
            target = parameters[1].lower()
            newAge = parameters[2]
            found = False
            for i in range(len(lines)):
                record = ""
                for x in lines[i]:
                    if(x == "|"):
                        break
                    elif(x == " "):
                        continue
                    record = record + x
                record = record.lower()
                record = record.strip()
                if(record == target):
                    found = True
                    line = str(lines[i])
                    parts = line.split("|")
                    parts[1] = newAge
                    line = parts[0]+"|"+parts[1]+"|"+parts[2]+"|"+parts[3]
                    lines[i] = line
                    message = "Customer "+parts[0]+"'s age has been updated successfully"
                    sending = bytes(message,"utf-8")
                    break
            if(found == False):
                message = "Customer doesn't exist"
                sending = bytes(message,"utf-8")
        if(parameters[0] == "5"):
            print("Update Customer address")
            target = parameters[1].lower()
            newAddress = parameters[2]
            found = False
            for i in range(len(lines)):
                record = ""
                for x in lines[i]:
                    if(x == "|"):
                        break
                    elif(x == " "):
                        continue
                    record = record + x
                record = record.lower()
                record = record.strip()
                if(record == target):
                    found = True
                    line = str(lines[i])
                    parts = line.split("|")
                    parts[2] = newAddress
                    line = parts[0]+"|"+parts[1]+"|"+parts[2]+"|"+parts[3]
                    lines[i] = line
                    message = "Customer "+parts[0]+"'s address has been updated successfully"
                    sending = bytes(message,"utf-8")
                    break
            if(found == False):
                message = "Customer doesn't exist"
                sending = bytes(message,"utf-8")
        if(parameters[0] == "6"):
            print("Update Customer phone")
            target = parameters[1].lower()
            newPhoneNumber = parameters[2]
            found = False
            for i in range(len(lines)):
                record = ""
                for x in lines[i]:
                    if(x == "|"):
                        break
                    elif(x == " "):
                        continue
                    record = record + x
                record = record.lower()
                record = record.strip()
                if(record == target):
                    found = True
                    line = str(lines[i])
                    parts = line.split("|")
                    parts[3] = newPhoneNumber
                    line = parts[0]+"|"+parts[1]+"|"+parts[2]+"|"+parts[3]
                    lines[i] = line
                    message = "Customer "+parts[0]+"'s phone number has been updated successfully"
                    sending = bytes(message,"utf-8")
                    break
            if(found == False):
                message = "Customer doesn't exist"
                sending = bytes(message,"utf-8")
        if(self.data == "7"):
            print("Print report")
            names = []
            for i in range(len(lines)):
                line = str(lines[i])
                parts = line.split("|")
                names.append(parts[0].strip())
                for j in range(len(names)):
                    for w in range(len(names)):
                        if(names[j] < names[w]):
                            temp = names[w]
                            names[w] = names[j]
                            names[j] = temp
                            temp = lines[w]
                            lines[w] = lines[j]
                            lines[j] = temp
            self.jsonstr = json.dumps(lines)
            sending = self.jsonstr.encode('utf-8')
        if(self.data == "8"):
            print("Exit")
        self.request.sendall(sending)
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()