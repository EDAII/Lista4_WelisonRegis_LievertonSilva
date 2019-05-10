import os
from copy import deepcopy
from binarytree import build
from random import randint

class BinaryHeap:
    def __init__(self):
        self.items = []
 
    def size(self):
        return len(self.items)
 
    def parent(self, i):
        return (i - 1)//2
 
    def left(self, i):
        return 2*i + 1
 
    def right(self, i):
        return 2*i + 2
 
    def get(self, i):
        return self.items[i]
 
    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]
 
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest
 
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= self.size() - 1 and self.get(l) > self.get(i)):
            largest = l
        else:
            largest = i
        if (r <= self.size() - 1 and self.get(r) > self.get(largest)):
            largest = r
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)
 
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
 
    def insert(self, key):
        index = self.size()
        self.items.append(key)
 
        while (index != 0):
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p
    
    def heapsort(self):
        obj_copy = deepcopy(self)

        obj_len = len(obj_copy.items)

        top_value = 0
        ordered_vector = []
        while top_value != None:
            top_value = obj_copy.extract_max()
            if top_value != None:
                ordered_vector += [top_value]
        
        return ordered_vector

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_key():
    input('\n> PRESSIONE ENTER')

def painel():
    print('-----------------HEAP TREE-----------------')
    print('-------------------------------------------')
    print('|>>> 1. Inserir elemento na heap          |')
    print('|>>> 2. Retirar o maior elemento da heap  |')
    print('|>>> 3. Zerar valores da heap             |')
    print('|>>> 4. Ordenar com heapsort              |')
    print('|>>> 5. Mostrar heap atual                |')
    print('|>>> 0. Finalizar aplicação!              |')
    print('-------------------------------------------')
    print('\n\n>>> ', end='')


def print_heap(bheap):
    clear_terminal()

    root = build(bheap.items)
    print(root)

def randoms_into_tree(bheap, quantity):
    for i in range(quantity):
        number = randint(0, 9999)

        bheap.insert(number)

    return bheap

def make_action(bheap, choose):
    clear_terminal()
    if choose == 1:
        print('Digite um número para inserir na heap: ')
        print('>>> ', end='')

        number = input()
        try:
            number = int(number)
            bheap.insert(number)
        except:
            print('Valor inválido. Tente novamente!')  

    elif choose == 2:
        max = bheap.extract_max()

        if max is not None:
            print('Elemento extraído da heap: {}'.format(max))
        else:
            print('Não é possível remover de uma heap vazia!')

    elif choose == 3:
        bheap.items = []
    elif choose == 4:
        sorted_heap = bheap.heapsort()
        print('Heap ordenada:')
        print(sorted_heap)
    elif choose == 5:
        print_heap(bheap)
    elif choose == 0:
        clear_terminal()
        exit(0)

    return bheap

def main():
    bheap = BinaryHeap()

    valid, randoms_quantity = False, 0
    while not valid:
        randoms_quantity = input('>>> Quantidade de elementos inicias da heap (0-30): ')

        if randoms_quantity >= '0' and randoms_quantity <= '30':
            randoms_quantity = int(randoms_quantity)
            valid = True
        else:
            print('Digite um intervalo válido!')

    bheap = randoms_into_tree(bheap, randoms_quantity)

    sorted_heap = bheap.heapsort()

    done = False
    while not done:
        clear_terminal()
        painel()

        try:
            choose = int(input())
        except:
            print('Valor inválido. Tente novamente!')
            continue

        bheap = make_action(bheap, choose)

        wait_key()
    
        
if __name__ == '__main__':
    main()