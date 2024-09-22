aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'


print(f'Nome é igual a {aluno['nome']}')
print(f'Media é igual a {aluno['media']:.1f}')
print(f'A situação é igual a {aluno['situação']}')
