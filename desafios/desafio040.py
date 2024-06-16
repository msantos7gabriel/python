import datetime as dt

data_hj = dt.date.today()
data_hj = dt.strptime(data_hj, "%d/%m/%Y")
nascimento = input('Escreva sua data de nascimento: ')
nascimento = dt.strptime(nascimento, "%d/%m/%Y")
