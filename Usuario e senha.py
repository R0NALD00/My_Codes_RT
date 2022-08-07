usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'ronaldo'
senha_bd = 'rona123'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')

input('Pressione enter para fechar.')
