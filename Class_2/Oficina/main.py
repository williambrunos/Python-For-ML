import random


def check_jokempo_player_win(player_choice, machine_choice):
    if player_choice == "pedra" and machine_choice == "tesoura":
        return True
    elif player_choice == "papel" and machine_choice == "pedra":
        return True
    elif player_choice == "tesoura" and machine_choice == "papel":
        return True
    else:
        return False


def check_jokempo_draw(player_choice, machine_choice):
    return player_choice == machine_choice


def jokempo_game():
    quit = False

    while quit == False:
        jokempo_player_choice = ""
        jokempo_choices = ["pedra", "papel", "tesoura"]
        jokempo_player_choices = []
        matches = 0
        print("Escolha uma opção (1, 2, 3 ou 4) \n\n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Sair\n\n")
        choice = int(input("->"))

        if choice == 1:
            jokempo_player_choice = "pedra"
        elif choice == 2:
            jokempo_player_choice = "papel"
        elif choice == 3:
            jokempo_player_choice = "tesoura"
        elif choice == 4:
            quit = True
            print("Saindo...")
            continue
        else:
            print("Por favor, tecle uma opção válida")
            continue

        jokempo_player_choices.append(jokempo_player_choice)

        if matches < 5:
            random_index_of_jokempo_choices = random.randint(0, 2)
            jokempo_machine_choice = jokempo_choices[random_index_of_jokempo_choices]
        else:
            probability_of_learning = random.uniform(0, 100)

            if probability_of_learning > 40:
                count_of_pedras = jokempo_choices.count("pedra")
                count_of_papeis = jokempo_choices.count("papel")
                count_of_tesouras = jokempo_choices.count("tesoura")

                if count_of_pedras > count_of_papeis and count_of_pedras > count_of_tesouras:
                    jokempo_machine_choice = "papel"
                elif count_of_papeis > count_of_pedras and count_of_papeis > count_of_tesouras:
                    jokempo_machine_choice = "tesoura"
                elif count_of_tesouras > count_of_pedras and count_of_tesouras > count_of_papeis:
                    jokempo_machine_choice = "pedra"
                else:
                    random_index_of_jokempo_choices = random.randint(0, 2)
                    jokempo_machine_choice = jokempo_choices[random_index_of_jokempo_choices]
            else:
                random_index_of_jokempo_choices = random.randint(0, 2)
                jokempo_machine_choice = jokempo_choices[random_index_of_jokempo_choices]

        print(f'Sua jogada -> {jokempo_player_choice}\nJogada da Máquina -> {jokempo_machine_choice}')

        if (check_jokempo_player_win(jokempo_player_choice, jokempo_machine_choice)):
            print("VOCÊ GANHOU!")
        elif (check_jokempo_draw(jokempo_player_choice, jokempo_machine_choice)):
            print("EMPATE!")
        else:
            print("MÁQUINA VENCEU!")

        matches += 1


if __name__ == "__main__":
    jokempo_game()
