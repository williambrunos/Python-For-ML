import numpy as np
import numpy.ma as ma


def discover_day_of_week(number):
    if number > 7:
        number = number % 7
    if number == 1:
        return 'Domingo'
    elif number == 2:
        return "Segunda"
    elif number == 3:
        return "Terça"
    elif number == 4:
        return "Quarta"
    elif number == 5:
        return "Quinta"
    elif number == 6:
        return "Sexta"
    else:
        return "Sábado"


visualizacao_stories = np.array([
                                [187, 120, 88, 70, 130, 168, 213],
                                [0, 0, 42, 0, 0, 55, 77],
                                [91, 0, 61, 0, 71, 121, 271],
                                [0, 0, 0, 0, 187, 0, 0],
                                [42, 23, 34, 0, 39, 29, 36]
])

print('ETAPA 1 - DADOS DA SEMANA PASSADA - \n\n')
pessoas = ['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson']
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

media_visualizacoes_semanal = visualizacao_stories.mean(axis=1)

print('====MÉDIA DE VISUALIZAÇÕES DIÁRIAS====')
for index, media_visualizacao in enumerate(media_visualizacoes_semanal):
    print(f'{pessoas[index]}: {media_visualizacao:.2f} visualizações por dia')

soma_visualizacoes_diarias = visualizacao_stories.sum(axis=0)
print(f'Dia com mais visualizações: {discover_day_of_week(soma_visualizacoes_diarias.argmax()+1)}')

print('\n\nETAPA 2 - DADOS DESSA SEMANA - \n\n')

visualizacao_stories_invalidos = np.array([
    [52, 68, 97, 55, -1, 98, -1],
    [53, -1, 38, -1, -1, 72, 49],
    [88, -1, 64, -1, 77, 130, 43],
    [-1, 30, -1, -1, -1, 182, -1],
    [41, 20, 33, -1, 37, 23, 7]
])

visualizacao_mascarada = ma.masked_where(visualizacao_stories_invalidos < 0, visualizacao_stories_invalidos)
media_visualizacoes_semanal_mascarada = visualizacao_mascarada.mean(axis=1)

for index, media_mascarada in enumerate(media_visualizacoes_semanal_mascarada):
    print(f'{pessoas[index]}: {media_mascarada:.2f} visualizações por dia')

soma_visualizacoes_diarias_mascaradas = visualizacao_mascarada.sum(axis=0)
print(f'Dia com mais visualizações: {discover_day_of_week(soma_visualizacoes_diarias_mascaradas.argmax()+1)}')
