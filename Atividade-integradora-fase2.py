from collections import deque

# criação de fila de pouso
fila_pouso = deque()    # fila principal

# criação de listas

pousado = []           # lista de módulos que pousaram
espera = []            # lista de módulos em espera
alerta = []            # lista de módulos em alerta
historico = []         # pilha (registro de operações)

# criação de modulos
class Modulo:
    # definição de atributos dos modulos
    def __init__(self, nome: str, prioridade: int, combustivel: int, massa:float, criticidade: str, horario: str):
        self.nome = nome
        self.prioridade = prioridade
        self.combustivel = combustivel
        self.massa = massa
        self.criticidade = criticidade
        self.horario = horario

    def __str__(self):
        return f"{self.nome} | Prioridade: {self.prioridade} | Combustível: {self.combustivel} | Massa: {self.massa}"

# função para buscar módulo com menor combustivel
def buscar_menorCombustivel(fila):
    menor = fila[0]

    for i in fila:
        if i.combustivel < menor.combustivel:
            menor = i

    return menor

# função para buscar módulo com maior massa
def buscar_maiorPeso(fila):
    maior = fila[0]

    for i in fila:
        if i.massa > maior.massa:
            maior = i

    return maior

    
# ordenação de modulos de pouso com base na prioridade e em caso de igualdade na prioridade vai ser desempatado com base no combustivel
# sendo 1 a maior prioridade e 3 a menor

def deveVirAntes(m1, m2):
    # 1. prioridade (sendo 1 maior e 3 menor)
    if m1.prioridade < m2.prioridade:
        return True
    if m1.prioridade > m2.prioridade:
        return False
    
    # 2. combustivel (menor tem prioridade)
    if m1.combustivel < m2.combustivel:
        return True
    if m1.combustivel > m2.combustivel:
        return False
    
    # 3. massa (maior primeiro)
    return m1.massa > m2.massa
# buble sort
def ordenar_fila(fila):
    # recebe o tamanho da fila
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not deveVirAntes(fila[j], fila[j + 1]):
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Regras de decisão (lógica booleana)
def decidir_pouso(modulo):
    combustivel_ok = modulo.combustivel > 30
    massa_ok = modulo.massa < 20000
    prioridade_alta = modulo.prioridade == 1
    emergencia = modulo.criticidade == "alta"

    if combustivel_ok and massa_ok and (prioridade_alta or emergencia):
        return "pousar"
    elif not combustivel_ok:
        return "alerta"
    else:
        return "espera"

# cadastro de módulos
fila_pouso.append(Modulo("Habitacao", 1, 70, 1200, "alta", "10:00"))
fila_pouso.append(Modulo("Energia", 1, 60, 15000, "alta", "10:05"))
fila_pouso.append(Modulo("Laboratorio", 2, 80, 10000, "media", "10:10"))
fila_pouso.append(Modulo("Logistica", 3, 50, 20000, "media", "10:15"))
fila_pouso.append(Modulo("Medico", 1, 40, 9000, "alta", "10:20"))

historico.append("Módulos cadastrados")

#exibição das buscas
menorCombustivel = buscar_menorCombustivel(fila_pouso)
print("Módulo com menor combustível é:", menorCombustivel.nome,
      "com", menorCombustivel.combustivel, "%")

maiorPeso = buscar_maiorPeso(fila_pouso)
print("Módulo com maior peso é:", maiorPeso.nome,
      "com", maiorPeso.massa)

# exibição da fila assim que inserida
print("fila de pouso antes da ordenação: ")
for modulo in fila_pouso:
    print(modulo)

# ordenar fila
lista_fila = list(fila_pouso)
ordenar_fila(lista_fila)
fila_pouso = deque(lista_fila)

historico.append("Fila ordenada")

# exibir fila ordenada
print("\nFila de pouso após ordenação:")
for modulo in fila_pouso:
    print(modulo)

# simulação de pouso
while fila_pouso:
    modulo = fila_pouso.popleft()
    decisao = decidir_pouso(modulo)

    if decisao == "pousar":
        pousado.append(modulo)
        historico.append(f"{modulo.nome} pousou")
    elif decisao == "alerta":
        alerta.append(modulo)
        historico.append(f"{modulo.nome} em alerta")
    else:
        espera.append(modulo)
        historico.append(f"{modulo.nome} em espera")

# Resultados finais
print("\nMódulos pousados:")
for m in pousado:
    print(m)

print("\nMódulos em espera:")
for m in espera:
    print(m)

print("\nMódulos em alerta:")
for m in alerta:
    print(m)

# Histórico (pilha)
print("\nHistórico de operações:")
for h in historico:
    print(h)



    