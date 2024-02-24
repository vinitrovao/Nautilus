print("Questão 1:")


def verifica_primeiro_ultimo_iguais(lista):
    return lista[:1] == lista[-1:] and len(lista) > 0


num_elementos = int(input
                    ("Digite o número de elementos que você deseja na lista: "
                     ))
minha_lista = []

for i in range(num_elementos):
    elemento = input(f"Digite o elemento {i + 1}: ")
    minha_lista.append(elemento)

resultado = verifica_primeiro_ultimo_iguais(minha_lista)

if resultado:
    print("O primeiro e o último elemento da lista são iguais.")
else:
    print("O primeiro e o último elemento da lista são diferentes.")


print("Questão 2:")


def maior_divisor_primo(numero):
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            numero //= divisor
        else:
            divisor += 1

    return divisor


numero = int(input("Digite um número inteiro positivo: "))

resultado = maior_divisor_primo(numero)
print(f"O maior divisor primo de {numero} é: {resultado}")


print("Questão 3:")


def eh_palindromo(numero):
    numero_str = str(numero)
    invertido_str = numero_str[::-1]

    return numero_str == invertido_str


numero_usuario = int(input("Digite um número: "))


if eh_palindromo(numero_usuario):
    print(f"{numero_usuario} é um palíndromo.")
else:
    print(f"{numero_usuario} não é um palíndromo.")


print("Questão 4:")


def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


soma_primos = 0
limite_superior = 1000

for num in range(2, limite_superior):
    if eh_primo(num):
        soma_primos += num

print(
    "A soma de todos os números primos menores que {} é: {}".format(
        limite_superior, resultado
    )
)

print("Atividade Extra:")


class Drone:
    def __init__(self, num_motores, qtd_cameras, ano_construcao, nome, peso, bateria):
        self.num_motores = num_motores
        self.qtd_cameras = qtd_cameras
        self.ano_construcao = ano_construcao
        self.nome = nome
        self.peso = peso
        self.bateria = bateria

    def exibir_dados(self):
        print(f"{self.nome} | {self.num_motores} motores |"
              f"{self.qtd_cameras} câmeras | {self.ano_construcao}"
              f"| Peso: {self.peso} g | Bateria: {self.bateria} min")


class DroneFleet:
    def __init__(self):
        self.drones = []

    def adicionar_drone(self, drone):
        self.drones.append(drone)

    def exibir_todos(self):
        print("Todos os Drones em Tabela:")
        print("{:<30} | {:<13} | {:<26} | {:<20} | {:<10} | {:<10}".format(
             "Nome do Veículo", "Número de Motores", "Quantidade de Câmeras",
             "Ano de Construção", "Peso", "Bateria"))
        print("-" * 125)
        for drone in self.drones:
            drone.exibir_dados()

    def exibir_individual(self, nome_veiculo):
        for drone in self.drones:
            if drone.nome == nome_veiculo:
                drone.exibir_dados()
                return
        print(f"Drone com nome {nome_veiculo} não encontrado.")
     
    def rankear_por_ano(self):
        ranked_drones = sorted(self.drones, key=lambda x: x.ano_construcao,
                               reverse=True)
        print("Ranking por Ano de Construção:")
        for drone in ranked_drones:
            print(f"{drone.nome}: {drone.ano_construcao}")
   
    def rankear_por_bateria(self):
        ranked_drones = sorted(self.drones, key=lambda x: x.bateria,
                               reverse=True)
        print("Ranking por Bateria:")
        for drone in ranked_drones:
            print(f"{drone.nome}: {drone.bateria} min")

    def menu_interativo(self):
        while True:
            print("\nEscolha uma opção:")
            print("1 - Exibir todos os drones em tabela")
            print("2 - Exibir drone individualmente")
            print("3 - Rankear drones por ano de construção")
            print("4 - Rankear drones por bateria")
            print("0 - Sair")
            
            opcao = input("Opção: ")

            if opcao == "1":
                self.exibir_todos()
            elif opcao == "2":
                nome_veiculo = input("Digite o nome do drone: ")
                self.exibir_individual(nome_veiculo)
            elif opcao == "3":
                self.rankear_por_ano()
            elif opcao == "4":
                self.rankear_por_bateria()
            elif opcao == "0":
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")


drone1 = Drone(4, 1, 2019, "Drone Multilaser Eagle", 180, 14)
drone2 = Drone(4, 1, 2021, "Drone e88 pro 4k", 60, 15)
drone3 = Drone(4, 1, 2020, "Drone Fênix GPS", 185, 16)

fleet = DroneFleet()
fleet.adicionar_drone(drone1)
fleet.adicionar_drone(drone2)
fleet.adicionar_drone(drone3)

fleet.menu_interativo()

