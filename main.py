"""
Напишите класс SuperStack, который реализует структуру данных "стек".
Использовать стандартные списковые типы Питона (list, deque и т.д.) для хранения элементов стека нельзя.
Вместо этого определите класс SuperStackElement и храните в его объектах значение элемента и объект предыдущего элемента.

У класса SuperStack должны быть следующие методы:

- push (добавляет значение на верхушку стека)
- peek (возвращает значение с верхушки стека)
- pop (возвращает и удаляет значение с верхушки стека)

"""


class SuperStackElement:
    """ Класс созданый для реализации работы класса SuperStack,
     принимает 2 значения, последний и предпоследний элементы.
    """

    def __init__(self, element=None, old_element=None):
        self.old_element = old_element
        self.element = element


class SuperStack:
    """ Класс имитирующий работу стэка.
    """

    def __init__(self):
        self.ss_element = None

    def push(self, element):
        """ Добавляет элемент в очередь СуперСтека
        """
        self.ss_element = SuperStackElement(element, self.ss_element)

    def peek(self):
        """ Возвращает последний добавленный элемент
         Бросает IndexError если СуперСтек пустой"""
        if self.ss_element is None:
            raise IndexError("Peek out of index")
        return self.ss_element.element

    def pop(self):
        """ Удаляет и возвращает последний добавленный элемент
         Бросает IndexError если СуперСтек пустой"""
        if self.ss_element is None:
            raise IndexError("Pop out of index")

        pop_element = self.ss_element
        old_element = self.ss_element.old_element

        if old_element is None:
            self.ss_element = None
            return pop_element.element

        self.ss_element = old_element
        return pop_element.element


def main():
    pass


if __name__ == "__main__":
    main()
