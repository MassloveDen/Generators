'''import requests

class BruteForceGenerator:

    def __init__(self, alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'):
        self.alphabet = alphabet
        self.base = len(self.alphabet)
        self.i = 0
        self.lenght = 0

    def reset(self):
        self.i = 0
        self.lenght = 0

    def generate(self):

        x = self.i
        result = ''
        while len(result) < self.length:
            rest = x % self.base  # остаток от деления
            x = x // self.base  # целая часть от деления
            result = self.alphabet[rest] + result



        if result == self.alphabet[-1] * self.length:  # Все пароли длины length перебраны
            self.length += 1
            self.i = 0
        else:
            self.i += 1

            return result

with open('pop_passwords.txt') as f:
    pop_passwords = f.read()

pop_passwords = pop_passwords.split('\n')
i = 0


class ListGenerator():


    def __init__(self, tokens):
        self.i = 0
        self.tokens = tokens

    def reset(self):
        self.i = 0

    def generate(self):
        if self.i >= len(self.tokens):
            return

        tokens = self.tokens[self.i]
        self.i += 1
        return tokens

class FileGenerator(ListGenerator):

    def __init__(self, filename = 'pop_passwords.txt'):
        with open(filename) as f:
            pop_passwords = f.read().split('\n')

        super().__init__(tokens= pop_passwords)

        # self.i = 0
        # self.tokens = pop_passwords.split('\n')

    # def reset(self):
    #     self.i = 0
    #
    # def generate(self):
    #     password = self.pop_passwords[self.i]
    #     self.i += 1
    #     return password

g1 = ListGenerator(tokens= ["admin", "jack", "cat"])

print(g1.generate())
print(g1.generate())
print(g1.generate())
print(g1.generate())'''


class BruteForceGenerator:

    def __init__(self, alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'):
        self.alphabet = alphabet
        self.base = len(self.alphabet)
        self.i = 0
        self.length = 0


    def reset(self):
        self.i = 0
        self.length = 0



    def generate(self):
        global i, length
        x = self.i
        result = ''
        while len(result) < self.length:
            rest = x % self.base
            x = x // self.base
            result = self.alphabet[rest] + result

        if result == self.alphabet[-1] * self.length:
            self.length += 1
            self.i = 0
        else:
            self.i += 1

        return result


class ListGenerator:

    def __init__(self, tokens):

        self.tokens = tokens
        self.i = 0

    def reset(self):
        self.i = 0


    def generate(self):
        if self.i >= len(self.tokens):
            return None
        tokens = self.tokens[self.i]
        self.i += 1
        return tokens


class FileGenerator(ListGenerator):

    def __init__(self, filename = 'pop_passwords.txt'):
        with open(filename) as f:
            tokens = f.read().split('\n')

        super().__init__(tokens= tokens)



