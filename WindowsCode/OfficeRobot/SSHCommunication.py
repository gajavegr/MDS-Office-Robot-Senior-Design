import sys
import asyncssh
import paramiko
import tkinter as tk
import asyncio

# host = "gajavegr-pi.wlan.rose-hulman.edu"
# port = 22
# username = "pi"
# password = "password"

class SSHCommunication:
    # def __init__(self, username, password, host, port):
    def __init__(self):
        # global ssh
        # self.username = username
        # self.password = password
        # self.host = host
        # self.port = port
        self.host = "gajavegr-pi.wlan.rose-hulman.edu"
        self.port = 22
        self.username = "pi"
        self.password = "password"
        self.connect()
        # print("Connected")
    
    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.username, self.password)

    # async def runAsync(self,command):
    #     async with asyncssh.connect(self.host, username=self.username, password=self.password) as conn:
    #         result = await conn.run(command, check=True)
    #         print(result.stdout, end='')
    #         return result.stdout

    def executeCommand(self, command):
        output = self.ssh.exec_command(command)
        stdout = output[1]
        lines = stdout.readlines()
        print("command executed")
        return lines
        # try:
        #     return asyncio.get_event_loop().run_until_complete(self.runAsync(command))
        # except (OSError, asyncssh.Error) as exc:
        #     sys.exit('SSH connection failed: ' + str(exc))
        # # return  asyncio.get_event_loop().run_until_complete(self.runAsync(command))
        
if __name__ == "__main__":
    # host = "gajavegr-pi.wlan.rose-hulman.edu"
    # port = 22
    # username = "pi"
    # password = "password"
    sshConn = SSHCommunication()
    print(sshConn.executeCommand("ls"))