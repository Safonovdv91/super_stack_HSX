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
    """
    Класс созданый для реализации работы класса SuperStack, принимает 2 значения, последний и предпоследний элементы.
    """

    def __init__(self, el=None, old_el=None):
        self.old_el = old_el
        self.el = el


class SuperStack:
    """
    Класс имитирующий работу стэка.
    """
    def __init__(self):
        self.ss_element = None

    def push(self, element):
        self.ss_element = SuperStackElement(element, self.ss_element)

    def peek(self):
        if self.ss_element is None:
            return None
        return self.ss_element.el

    def pop(self):
        if self.ss_element is None:
            return None
        pop_element = self.ss_element
        old_element = self.ss_element.old_el
        if old_element is None:
            self.ss_element = None
            return pop_element.el
        self.ss_element = SuperStackElement(old_element, old_element.old_el)
        return pop_element.el


def main():
    ss = SuperStack()

    print(ss.push(110))
    print(ss.push(111))
    print(ss.push(112))
    print(ss.push(113))
    print(ss.push(114))
    print(ss.push(115))
    print(ss.peek())    #115
    print(ss.pop())     #115
    print(ss.pop())     #114
    print(ss.pop())     #113
    print(ss.peek())    #112
    print(ss.pop())     #112
    print(ss.pop())     #111
    print(ss.pop())     #110
    print(ss.peek())    # none
    print(ss.pop())     # none
    print(ss.push([12, 12]))


if __name__ == "__main__":
    main()





