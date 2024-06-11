cidade = str(input('Qual é o Nome de Sua cidade ? '))
cidade = cidade.upper()

if cidade.find('SANTO') == 0:
    print('A cidade Possui \'Santo\' Em Seu Nome ')
else:
    print('A não cidade Possui \'Santo\' Em Seu Nome ')
