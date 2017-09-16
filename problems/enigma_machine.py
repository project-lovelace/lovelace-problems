# problem6.py
# Simulating the Enigma machine

import random
import string
import numpy as np

from problems.abstract_problem import AbstractProblem


class Problem6(AbstractProblem):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @staticmethod
    def generate_scrambler():
        s = list(Problem6.alphabet)
        random.shuffle(s)
        return ''.join(s)

    @staticmethod
    def generate_scrambler_arrangement():
        arrangement = [1, 2, 3]
        random.shuffle(arrangement)
        return arrangement

    @staticmethod
    def generate_scrambler_orientation():
        orientation = ''
        for _ in range(3):
            orientation += random.choice(Problem6.alphabet)
        return orientation

    @staticmethod
    def generate_plugboard_setting():
        s = list(Problem6.alphabet)
        random.shuffle(s)
        return ''.join(s)[:12]

    @staticmethod
    def rotate_scrambler(scrambler, ticks):
        ticks = np.mod(ticks, len(Problem6.alphabet))
        return scrambler[ticks:] + scrambler[:ticks]

    @staticmethod
    def plugboard_propagate(ps, ch):
        plugboard = {}

        pairs = [ps[i:i+2] for i in range(0, len(ps), 2)]
        for p in pairs:
            plugboard[p[0]] = p[1]

        print(plugboard)
        print('{:s} -> {:s}'.format(ch, plugboard[ch]))
        if ch in plugboard.keys():
            return plugboard[ch]
        else:
            return ch

    @staticmethod
    def scrambler_propagate(scrambler_setting, ch):
        scrambler = {}
        for i in range(len(Problem6.alphabet)):
            scrambler[Problem6.alphabet[i]] = scrambler_setting[i]

        cipher = scrambler[ch]
        return cipher

    @staticmethod
    def reflector_propagate(rs, ch):
        reflector = {}

        pairs = [rs[i:i + 2] for i in range(0, len(rs), 2)]
        for p in pairs:
            reflector[p[0]] = p[1]
            reflector[p[1]] = p[0]

        cipher = reflector[ch]
        return cipher

    @staticmethod
    def scrambler_reverse_propagate(scrambler_setting, ch):
        scrambler = {}
        for i in range(len(Problem6.alphabet)):
            scrambler[Problem6.alphabet[i]] = scrambler_setting[i]

        cipher = next(k for k, v in scrambler.items() if v == ch)
        return cipher

    def generate(self):
        problem = {
            'scrambler1': self.generate_scrambler(),
            'scrambler2': self.generate_scrambler(),
            'scrambler3': self.generate_scrambler(),
            'reflector': self.generate_scrambler(),
            'scrambler_arrangement': self.generate_scrambler_arrangement(),
            'scrambler_orientation': self.generate_scrambler_orientation(),
            'plugboard_setting': self.generate_plugboard_setting(),
            'plaintext': 'AAA'
        }
        return problem

    def solve(self, problem):
        s1 = problem['scrambler1']
        s2 = problem['scrambler2']
        s3 = problem['scrambler3']
        rs = problem['reflector']
        sa = problem['scrambler_arrangement']
        so = problem['scrambler_orientation']
        ps = problem['plugboard_setting']
        text = problem['plaintext']

        scrambler_box = {1: s1, 2: s2, 3: s3}
        scramblers = {}
        for i in [1, 2, 3]:
            scramblers[i] = scrambler_box[int(sa[i-1])]

            ticks = string.ascii_uppercase.index(so[i-1])
            scramblers[i] = self.rotate_scrambler(scramblers[i], ticks)

        cipher = ''
        for cc in range(len(text)):
            ch = text[cc]
            ch = self.plugboard_propagate(ps, ch)

            ch = self.scrambler_propagate(scramblers[1], ch)
            scramblers[1] = self.rotate_scrambler(scramblers[1], 1)

            ch =  self.scrambler_propagate(scramblers[2], ch)
            if np.mod(cc, len(Problem6.alphabet)) == 0:
                scramblers[2] = self.rotate_scrambler(scramblers[2], 1)

            ch =  self.scrambler_propagate(scramblers[3], ch)
            if np.mod(cc, len(Problem6.alphabet)**2) == 0:
                scramblers[3] = self.rotate_scrambler(scramblers[3], 1)

            ch = self.reflector_propagate(rs, ch)
            ch = self.scrambler_reverse_propagate(scramblers[3], ch)
            ch = self.scrambler_reverse_propagate(scramblers[2], ch)
            ch = self.scrambler_reverse_propagate(scramblers[1], ch)

            cipher += ch

        return {'ciphertext': cipher}

    def verify(self, proposed, actual):
        return proposed == actual

    def test(self):
        problem = self.generate()
        print(problem)

        solution = self.solve(problem)
        print(solution)

        problem['plaintext'] = solution['ciphertext']
        print(problem)
        solution2 = self.solve(problem)
        print(solution2)

if __name__ == '__main__':
    Problem6().test()