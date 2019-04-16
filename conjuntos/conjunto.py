from listas import lista_ligada as ll


class Conjunto():
    def __init__(self):
        self.__elementos = ll.ListaLigada()

    def inserir(self, elemento):
        if self.contem(elemento):
            return
        else:
            self.__elementos.inserir(elemento)

    def inserir_posicao(self, elemento, posicao):
        if self.contem(elemento):
            return
        else:
            self.__elementos.inserir_posicao(posicao, elemento)

    def __str__(self):
        return self.__elementos.__str__()

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    def indice(self, elemento):
        return self.__elementos.indice(elemento)

    def esta_vazia(self):
        return self.__elementos.esta_vazia()

    def recuperar_elemento_no(self, posicao):
        return self.__elementos.recuperar_elemento_no(posicao)

    def recuperar_no(self, posicao):
        return self.__elementos.recuperar_no(posicao)

    def tamanho(self):
        return self.__elementos.tamanho

    def remover_posicao(self, posicao):
        self.__elementos.remover_posicao(posicao)

    def remover_elemento(self, elemento):
        self.__elementos.remover_elemento(elemento)
