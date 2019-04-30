from conjuntos import conjunto
from filas import fila
from listas import lista_ligada, lista_duplamente_ligada
from pilhas import pilha
from vetores import vetor

# vetor_inteiros = array('b', [1, 2, 3])
# print(vetor_inteiros)
# # 1 / 2 / 3 / 4
# vetor_inteiros.insert(3, 4)
# print(vetor_inteiros)
# print(vetor_inteiros.index(2))

flag = True

while flag:
    print(30 * "-", "MENU", 30 * "-")
    print("1. Vetores")
    print("2. Listas Ligadas")
    print("3. Listas Duplamente Ligadas")
    print("4. Pilhas")
    print("5. Filas")
    print("6. Conjuntos")
    print("0. Sair")
    opcoes = [0, 1, 2, 3, 4, 5, 6]
    try:
        op = int(input("Digite a opção desejada: "))
        if op not in opcoes:
            raise ValueError
    except ValueError:
        print("Não existe essa opção.")

    if op == 0:
        flag = False

    elif op == 1:
        vetor_teste = vetor.Vetor(0)
        vetor_teste.inserir_elemento_posicao(1, 0)
        vetor_teste.inserir_elemento_posicao(2, 1)
        vetor_teste.inserir_elemento_posicao(3, 2)
        vetor_teste.inserir_elemento_posicao(4, 2)
        vetor_teste.inserir_elemento_posicao(5, 2)
        vetor_teste.inserir_elemento_final(1)
        print(vetor_teste.tamanho_vetor())
        print(vetor_teste)
        # print(vetor_teste.contem(8))
        print(vetor_teste.indice(4))
        vetor_teste.remover_elemento_indice(3)
        print(vetor_teste)
        vetor_teste.remover_elemento(5)
        print(vetor_teste)
        # print(vetor_teste)

    elif op == 2:
        lista_teste = lista_ligada.ListaLigada()
        lista_teste.inserir(1)
        lista_teste.inserir(4)
        lista_teste.inserir(5)
        lista_teste.inserir_posicao(2, 10)
        print(lista_teste)
        lista_teste.remover_elemento(4)
        print(lista_teste)
        # print(lista_teste.contem(5))
        # print(lista_teste.indice(55))

        # print(lista_teste.recuperar_elemento_no(3))

    elif op == 3:
        lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
        lista_teste.inserir(1)
        lista_teste.inserir(4)
        lista_teste.inserir(5)
        lista_teste.inserir_posicao(2, 10)
        print(lista_teste)
        # lista_teste.remover_elemento(4)
        lista_teste.remover_posicao(1)
        print(lista_teste)
        # print(lista_teste.contem(5))
        # print(lista_teste.indice(55))

        # print(lista_teste.recuperar_elemento_no(3))

    elif op == 4:
        pilha_teste = pilha.Pilha()
        pilha_teste.empilhar(5)
        print(pilha_teste.desempilhar())

    elif op == 5:
        fila_teste = fila.Fila()
        fila_teste.enfileirar(1)
        fila_teste.enfileirar(2)
        fila_teste.enfileirar(3)
        fila_teste.enfileirar(4)
        print(fila_teste)  # 1 2 3 4
        print(fila_teste.desenfileirar())
        print(fila_teste)  # 2 3 4
        print(fila_teste.desenfileirar())
        print(fila_teste)  # 3 4
        fila_teste.enfileirar(6)
        print(fila_teste)

    elif op == 6:
        teste_conjuntos = conjunto.Conjunto()
        teste_conjuntos.inserir(1)
        # print(teste_conjuntos.__str__())
        teste_conjuntos.inserir(2)
        # print(teste_conjuntos.__str__())
        teste_conjuntos.inserir(2)
        # print(teste_conjuntos.__str__())
        teste_conjuntos.inserir(3)
        print(teste_conjuntos)
        teste_conjuntos.remover_elemento(2)
        print(teste_conjuntos)
        # teste_conjuntos.inserir_posicao(10, 0)
        # teste_conjuntos.inserir_posicao(11, 1)
        # teste_conjuntos.inserir_posicao(11, 3)
        # print(teste_conjuntos.__str__())
