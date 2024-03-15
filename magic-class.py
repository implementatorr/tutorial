class Banknote:
    def __init__(self, value: int):
        # Initializes the Banknote with a specific value
        self.value = value

    def __repr__(self):
        # Official string representation of Banknote
        return f"Banknote({self.value})"

    def __str__(self):
        # Informal string representation of Banknote
        return f'Banknote with a value of {self.value} rubles'

    def __eq__(self, other):
        # Checks equality, by default compares memory address, here compares value
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other):
        # Less than comparison method
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value < other.value

    def __gt__(self, other):
        # Greater than comparison method
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value > other.value

    def __le__(self, other):
        # Less than or equal to comparison method
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value <= other.value

    def __ge__(self, other):
        # Greater than or equal to comparison method
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value >= other.value


class Wallet:
    def __init__(self, *banknotes: Banknote):
        # Initializes the Wallet with a collection of Banknote objects
        self.container = []
        self.container.extend(banknotes)

    def __repr__(self):
        # Official string representation of Wallet
        return f"Wallet({self.container})"

    def __contains__(self, item):
        # Checks if a Banknote is in the Wallet
        return item in self.container

    def __bool__(self):
        # Returns True if the Wallet contains any Banknotes
        return bool(self.container)

    def __len__(self):
        # Returns the number of Banknotes in the Wallet
        return len(self.container)

    def __call__(self):
        # When the Wallet object is called, it returns the total sum of Banknotes
        return f"{sum(i.value for i in self.container)} rubles"

    def __iter__(self):
        # Allows iteration over the Wallet's contents
        self.index = 0
        return self

    def __next__(self):
        # Iterates through the Wallet's Banknotes
        if self.index >= len(self.container):
            raise StopIteration
        result = self.container[self.index]
        self.index += 1
        return result
