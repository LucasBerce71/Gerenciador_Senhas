import sqlite3

conn = sqlite3.connect("passwords.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin(
        login TEXT NOT NULL,
        senha TEXT NOT NULL
    )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("===============================")
    print("i : inserir uma nova senha")
    print("l : listar serviços salvos")
    print("a : modificar sua senha de administrador")
    print("c : cadastrar um novo acesso de administrador")
    print("s : sair")
    print("===============================")

if cursor.rowcount == 0:
    print("Serviço não cadastrado! use 'l' para listar todos os serviços!")
else:
    for user in cursor.fetchall():
        print(user)

def updateSenhaAdm(login, senha):
    cursor.execute(f'''
        UPDATE admin SET 
        login = '{login}',
        senha = '{senha}'
    ''')
    conn.commit()

def cadSenhaAdm(login, senha):
    cursor.execute(f'''
        INSERT INTO admin (login, senha)
        VALUES ('{login}', '{senha}')
    ''')
    conn.commit()

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service, password FROM users;
    ''')

    for service in cursor.fetchall():
        print(service)

while True:
    
    login = input("Login: ")
    senha = input("senha: ")

    cursor.execute('SELECT * from admin WHERE login="%s" AND senha="%s"' % (login, senha))
    if cursor.fetchone() is not None:
        print ("Seja Bem Vindo Lucas Bercê de Jesus")
    else:
        print ("Acesso Inválido! Encerrando...")
        exit()

    menu()

    op = input("O que deseja fazer? ")
    if op not in ['l', 'i', 'r', 'a', 'c', 's']:
        print("Operação inválida!")
        continue
    
    if op == 's':
        break

    if op == 'a':
        login = input('Digite seu novo login de acesso: ')
        senha = input('Digite sua nova senha de acesso: ')
        cSenha = input('Confirme a senha digitada acima: ')
        if cSenha != senha:
            print('As duas senhas não conferem!')
            menu()
        else:
            cadSenhaAdm(login, senha)

    if op == 'c':
        login = input('Digite o login de acesso desse adm: ')
        senha = inpu

    if op == 'i':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuário? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)

    if op == 'l':
        show_services()

conn.close()        
