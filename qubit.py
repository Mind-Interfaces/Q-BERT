import math
import random

class Qubit:
    def __init__(self, a=1, b=0):
        self.zero = complex(a)
        self.one = complex(b)
        self.normalize()

    def xgate(self):
        self.zero, self.one = self.one, self.zero
        return self

    def zgate(self):
        self.one *= -1
        return self

    def hgate(self):
        a = self.zero
        b = self.one
        factor = 1 / (2 ** 0.5)
        self.zero = factor * (a + b)
        self.one = factor * (a - b)
        return self

    def measure(self):
        zeroprob = abs(self.zero) ** 2
        randomchoice = random.random()
        if randomchoice < zeroprob:
            self.zero = complex(1)
            self.one = complex(0)
            return 0
        else:
            self.zero = complex(0)
            self.one = complex(1)
            return 1

    def normalize(self):
        norm = (abs(self.zero) ** 2 + abs(self.one) ** 2) ** 0.5
        self.zero /= norm
        self.one /= norm
        return self

    def __repr__(self):
        return str(self.zero) + " |0> + " + str(self.one) + " |1>"


class TwoQubit:
    def __init__(self, a=1, b=0, c=0, d=0):
        self.zerozero = complex(a)
        self.zeroone = complex(b)
        self.onezero = complex(c)
        self.oneone = complex(d)
        self.normalize()

    def cnot(self):
        self.onezero, self.oneone = self.oneone, self.onezero
        return self

    def hgate(self, target=1):
        if target == 1:
            a = self.zerozero
            b = self.onezero
            c = self.zeroone
            d = self.oneone
            factor = 1 / (2 ** 0.5)
            self.zerozero = factor * (a + b)
            self.onezero = factor * (a - b)
            self.zeroone = factor * (c + d)
            self.oneone = factor * (c - d)
        elif target == 2:
            a = self.zerozero
            c = self.zeroone
            b = self.onezero
            d = self.oneone
            factor = 1 / (2 ** 0.5)
            self.zerozero = factor * (a + c)
            self.zeroone = factor * (a - c)
            self.onezero = factor * (b + d)
            self.oneone = factor * (b - d)
        self.normalize()
        return self

    def xgate(self, target=1):
        if target == 1:
            self.zerozero, self.onezero = self.onezero, self.zerozero
            self.zeroone, self.oneone = self.oneone, self.zeroone
        elif target == 2:
            self.zerozero, self.zeroone = self.zeroone, self.zerozero
            self.onezero, self.oneone = self.oneone, self.onezero
        return self

    def zgate(self, target=1):
        if target == 1:
            self.onezero *= -1
            self.oneone *= -1
        elif target == 2:
            self.zeroone *= -1
            self.oneone *= -1
        return self

    def measure(self):
        zerozeroprob = abs(self.zerozero) ** 2
        zerooneprob = abs(self.zeroone) ** 2
        onezeroprob = abs(self.onezero) ** 2
        oneoneprob = abs(self.oneone) ** 2
        randomchoice = random.random()
        cumulative_prob = 0
        states = [(self.zerozero, (0, 0)), (self.zeroone, (0, 1)), 
                  (self.onezero, (1, 0)), (self.oneone, (1, 1))]
        
        for prob, state in zip([zerozeroprob, zerooneprob, onezeroprob, oneoneprob], states):
            cumulative_prob += prob
            if randomchoice < cumulative_prob:
                self.zerozero, self.zeroone, self.onezero, self.oneone = [0, 0, 0, 0]
                setattr(self, state[0], 1)
                return state[1]

    def normalize(self):
        norm = (abs(self.zerozero) ** 2 + abs(self.zeroone) ** 2 +
                abs(self.onezero) ** 2 + abs(self.oneone) ** 2) ** 0.5
        self.zerozero /= norm
        self.zeroone /= norm
        self.onezero /= norm
        self.oneone /= norm
        return self

    def __repr__(self):
        terms = [(self.zerozero, "|00>"), (self.zeroone, "|01>"), 
                 (self.onezero, "|10>"), (self.oneone, "|11>")]
        repr_str = " + ".join([f"{coef.real if coef.real == coef else coef} {term}" 
                               for coef, term in terms if abs(coef) > 0])
        return repr_str

# Create instances to test the improved classes
qubit = Qubit(1, 1)
qubit.hgate()
two_qubit = TwoQubit(1, 1, 1, 1)
two_qubit.hgate()

qubit, two_qubit
