from listas import lista_ligada as ll


class TabelaEspalhamento():
    def __init__(self):
        self.__elementos = ll.ListaLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0

        for index in range(self.__numero_categorias):
            self.__elementos.inserir(ll.ListaLigada())

    @property
    def tamanho(self):
        return self.__tamanho

    def __gerar_numero_espalhamento(self, elemento):
        return hash(elemento) % self.__numero_categorias

    def inserir(self, elemento):
        if not self.__elementos.esta_vazia():
            return
        else:
            numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
            categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
            categoria.inserir(elemento)
            self.__tamanho += 1

    def contem(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        return categoria.contem(elemento)

    def remover(self, elemento):
        if not self.contem(elemento):
            return
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.remover_elemento(elemento)
        self.__tamanho -= 1

    def __str__(self):
        return self.__elementos.__str__()
