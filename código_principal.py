from interface import interface, perguntas, titulo, subtitulo, mensagens
from aluno import Aluno
# from gerar_arquivo import manipular_arquivo
while True:
    titulo('gym app')
    escolha = interface()
    if escolha == 1:
        subtitulo('add new studant')
        informações_aluno = perguntas()
        aluno = Aluno(informações_aluno)
        aluno.adicionar_novo_aluno()
    elif escolha == 2:
        print('ver alunos pendentes')
    else:
        print('sair')
        break