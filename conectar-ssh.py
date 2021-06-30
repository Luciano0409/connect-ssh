import paramiko, os

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname= '127.0.0.1', username= 'nome-do-usuario', password= 'senha-do-usuario') #Neste é onde acontece a conexão 

stdin, stdout, stderr = ssh.exec_command('hostname')  # Nesta linha é executado o comando "hostname"
hostname = stdout.readlines() # Guarda a saída do comando "hostname" na dentro da variavel "hostname"
stdin.close() 

print(hostname) # Mostra na tela a saida do comando "hostname"

