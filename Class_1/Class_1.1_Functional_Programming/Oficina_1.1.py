notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]


def group_category_of_music(criteria, iterable):
    return list(filter(criteria, iterable))


rock_ruim = group_category_of_music(lambda x: 0 <= x <= 1, notas_rock)
rock_mediano = group_category_of_music(lambda x: 2 <= x <= 3, notas_rock)
rock_bom = group_category_of_music(lambda x: 4 <= x <= 5, notas_rock)

pop_ruim = group_category_of_music(lambda x: 0 <= x <= 1, notas_pop)
pop_mediano = group_category_of_music(lambda x: 2 <= x <= 3, notas_pop)
pop_bom = group_category_of_music(lambda x: 4 <= x <= 5, notas_pop)

print('\nROCK:\n')
print(f'Quantidade de rock ruim: {len(rock_ruim)}')
print(f'Quantidade de rock mediano: {len(rock_mediano)}')
print(f'Quantidade de rock bom: {len(rock_bom)}')

print('\nPOP:\n')
print(f'Qunaitdade de pop ruim: {len(pop_ruim)}')
print(f'Quantidade de pop mediano: {len(pop_mediano)}')
print(f'Quanitddade de pop bom: {len(pop_bom)}')

if len(rock_mediano) > 0:
    print('Há músicas medianas de rock')
else:
    print('Não há músicas medianas de rock')

if len(pop_bom) == len(notas_pop):
    print('Todas as músicas pop são boas')
else:
    print('Nem todas as músicas pop são boas')

if len(rock_bom) > len(pop_bom):
    print('Há mais rocks bons do que pops bons')
else:
    print('Há mais pops bons do que rocks bons')