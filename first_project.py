def get_all_generators():
    losses_on_system = 0
    sum_of_generators = 0
    list_of_generator = []
    f_ask = float(input("Digite a potência da primeira usina geradora: "))
    list_of_generator.append(f_ask)
    number_of_generators = 1
    while True:
        cont = " "
        while cont not in ("no", "yes"):
            cont = str(input("Deseja continuar? ")).strip().lower()
        if cont == "yes":
            ask = float(input("Digite a potência da próxima usina geradora: "))
            list_of_generator.append(ask)
            number_of_generators += 1
        if cont == "no":
            break

    sum_of_consumers = 0
    list_of_consumers = []
    f_ask = float(input("Digite a potência do primeiro consumidor: "))
    list_of_consumers.append(f_ask)
    number_of_consumers = 1
    while True:
        cont = " "
        while cont not in ("no", "yes"):
            cont = str(input("Deseja continuar? ")).strip().lower()
        if cont == "yes":
            ask = float(input("Digite a potência do próximo consumidor: "))
            list_of_consumers.append(ask)
            number_of_consumers += 1
        if cont == "no":
            break

    for generators in list_of_generator:
        sum_of_generators += generators

    for consumers in list_of_consumers:
        sum_of_consumers += consumers

    losses_on_system = sum_of_generators - sum_of_consumers

    print(f"A quantidade de geradoras:{number_of_generators}")
    print(f"A lista das potências das geradoras: {list_of_generator} ")
    print(f"A soma das potências das geradoras: {sum_of_generators}")
    print("-" * 50)
    print(f"A quantidade de consumidores:{number_of_consumers}")
    print(f"A lista das potências dos consumidores: {list_of_consumers} ")
    print(f"A soma das potências dos consumidores: {sum_of_consumers}")
    print("/" * 50)
    print(f"A perda no sistema: {losses_on_system}")
    return "oi"


get_all_generators()
