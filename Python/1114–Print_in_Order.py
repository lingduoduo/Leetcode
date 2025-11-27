class Foo:
    def __init__(self):
        self.d = {}
        self.d[1] = False
        self.d[2] = False

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.d[1] = True

    def second(self, printSecond: "Callable[[], None]") -> None:
        while not self.d[1]:
            time.sleep(0.01)

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.d[2] = True

    def third(self, printThird: "Callable[[], None]") -> None:
        while not self.d[2]:
            time.sleep(0.01)

        # printThird() outputs "third". Do not change or remove this line.
        printThird()
