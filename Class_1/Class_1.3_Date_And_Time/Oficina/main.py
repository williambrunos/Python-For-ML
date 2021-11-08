from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')


def change_date_to_ansi_calendar(dates_string_list):
    dates_as_date_time_objects = []
    for date_string in dates_string_list:
        try:
            date_string_object = datetime.strptime(date_string, "%d/%m/%Y")
        except:
            try:
                date_string_object = datetime.strptime(date_string, "%d de %B de %Y")
            except:
                try:
                    date_string_object = datetime.strptime(date_string, "%Y-%B-%d")
                except:
                    try:
                        date_string_object = datetime.strptime(date_string, "%d %B %Y")
                    except:
                        try:
                            date_string_object = datetime.strptime(date_string, "%d/%b/%Y")
                        except:
                            print("please, give a good string datetime format")
        dates_as_date_time_objects.append(date(date_string_object.year, date_string_object.month, date_string_object.day))
    return dates_as_date_time_objects


aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10',
                '12 Julho 1989', '16 de Junho de 1987', '04/07/1990']

aniversarios_como_objetos = change_date_to_ansi_calendar(aniversarios)
aniversarios_como_objetos_ordenados = sorted(aniversarios_como_objetos, key = lambda d : (d.year, d.month, d.day))

print('----LISTA DE ANIVERSÁRIOS EM ORDEM: (ANO, MÊS, DIA)----\n\n')

for aniversario in aniversarios_como_objetos_ordenados:
    print(f'{aniversario.day}/{aniversario.month}/{aniversario.year}', end='\n')

data_hoje = date.today()

if data_hoje in aniversarios_como_objetos_ordenados:
    print(f'HOJE, {data_hoje.day}/{data_hoje.month}/{data_hoje.year} TEM ANIVERSÁRIO!')
else:
    print('Hoje não tem aniversário :(')
