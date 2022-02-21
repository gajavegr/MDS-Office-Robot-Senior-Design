import paramiko
import tkinter as tk

host = "gajavegr-pi.wlan.rose-hulman.edu"
port = 22
username = "pi"
password = "password"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)  

def write_slogan():
    print("Hello robot! (from server)")
    command = "echo hi"
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    print(f"{lines} (from pi)")  

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()