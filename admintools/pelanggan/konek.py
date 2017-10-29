import paramiko
import os
import pprint

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('156.67.218.8',65001,'root','hesoyam889.')

print('connect')
stdin, stdout, stderr = client.exec_command('ifconfig')
output = stdout.read()
pprint.pprint (output)
