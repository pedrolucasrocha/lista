class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def inserir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def exibir_lista(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def remover_duplicados(self):
        if self.head is None:
            return

        seen = set()
        current = self.head
        previous = None
        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

# Criando uma lista encadeada
lista = LinkedList()
lista.inserir(3)
lista.inserir(1)
lista.inserir(3)
lista.inserir(5)
lista.inserir(1)
lista.inserir(7)
lista.inserir(9)

# Exibindo lista antes da remoção de duplicatas
print("Lista original:")
lista.exibir_lista()

# Removendo duplicatas
lista.remover_duplicados()

# Exibindo lista após a remoção de duplicatas
print("Lista após a remoção de duplicatas:")
lista.exibir_lista()
