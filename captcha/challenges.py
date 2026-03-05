import random
import string
import time
import math

class TextChallenge:
    NAME = "Distorted Text Recognition"
    HINT = "Read the scrambled characters and type them exactly."

    CHARSET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"

    def generate(self):
        self.answer = "".join(random.choices(self.CHARSET, k=5))
        return self.answer

    def render(self, answer):
        lines = []
        lines.append("+" + "-" * 38 + "+")
        lines.append("|" + " " * 38 + "|")

        scrambled = ""
        for i, ch in enumerate(answer):
            noise_before = random.choice([".", "|", "/", "\\", "~", " "])
            noise_after  = random.choice([".", "|", "/", "\\", "~", " "])
            offset       = " " if i % 2 == 0 else ""
            scrambled   += f"{noise_before}{offset}{ch}{noise_after} "

        lines.append("|   " + scrambled.ljust(35) + "|")
        lines.append("|" + " " * 38 + "|")

        noise_line = "".join(random.choices(".-~|/\\", k=36))
        lines.append("|  " + noise_line + "  |")
        lines.append("+" + "-" * 38 + "+")
        return lines

    def verify(self, user_input):
        return user_input.upper().strip() == self.answer


class MathChallenge:
    NAME = "Arithmetic Challenge"
    HINT = "Solve the math problem. Humans do this faster than bots expect."

    OPS = ["+", "-", "*"]

    def generate(self):
        self.op = random.choice(self.OPS)
        if self.op == "+":
            self.a, self.b = random.randint(10, 99), random.randint(10, 99)
            self.answer    = self.a + self.b
        elif self.op == "-":
            self.a = random.randint(20, 99)
            self.b = random.randint(1, self.a - 1)
            self.answer    = self.a - self.b
        else:
            self.a, self.b = random.randint(2, 12), random.randint(2, 12)
            self.answer    = self.a * self.b
        symbol = "x" if self.op == "*" else self.op
        return f"{self.a} {symbol} {self.b} = ?"

    def render(self, question):
        w = 38
        lines = []
        lines.append("+" + "-" * w + "+")
        lines.append("|" + " " * w + "|")
        lines.append("|   " + f"What is:  {question}".ljust(w - 3) + "|")
        lines.append("|" + " " * w + "|")
        lines.append("+" + "-" * w + "+")
        return lines

    def verify(self, user_input):
        try:
            return int(user_input.strip()) == self.answer
        except ValueError:
            return False


class WordChallenge:
    NAME = "Scrambled Word Recognition"
    HINT = "Unscramble the word. Humans recognise patterns, bots brute-force."

    WORDS = [
        "python", "nature", "bridge", "castle", "jungle",
        "mirror", "planet", "rocket", "school", "garden",
        "window", "forest", "flight", "sunset", "canvas",
        "dragon", "silver", "circle", "bottle", "marble",
    ]

    def generate(self):
        self.answer = random.choice(self.WORDS)
        chars = list(self.answer)
        while "".join(chars) == self.answer:
            random.shuffle(chars)
        self.scrambled = "".join(chars).upper()
        return self.scrambled

    def render(self, scrambled):
        hint = f"({len(self.answer)} letters)"
        lines = []
        lines.append("+" + "-" * 38 + "+")
        lines.append("|" + " " * 38 + "|")
        lines.append("|   Unscramble this word:".ljust(39) + "|")
        lines.append("|" + " " * 38 + "|")
        lines.append("|       " + "  ".join(scrambled).ljust(31) + "|")
        lines.append("|" + " " * 38 + "|")
        lines.append("|   " + hint.ljust(35) + "|")
        lines.append("+" + "-" * 38 + "+")
        return lines

    def verify(self, user_input):
        return user_input.lower().strip() == self.answer


class SequenceChallenge:
    NAME = "Pattern Sequence Completion"
    HINT = "Complete the pattern. Humans spot rules instantly."

    def generate(self):
        kind = random.choice(["arithmetic", "geometric", "fibonacci", "squares"])

        if kind == "arithmetic":
            start = random.randint(1, 20)
            step  = random.randint(2, 9)
            seq   = [start + step * i for i in range(5)]
            self.answer = str(start + step * 5)
            self.display = ", ".join(str(x) for x in seq) + ", ?"

        elif kind == "geometric":
            start = random.randint(1, 5)
            ratio = random.randint(2, 4)
            seq   = [start * (ratio ** i) for i in range(5)]
            self.answer = str(start * (ratio ** 5))
            self.display = ", ".join(str(x) for x in seq) + ", ?"

        elif kind == "fibonacci":
            a, b = random.randint(1, 5), random.randint(1, 5)
            seq  = [a, b]
            for _ in range(4):
                seq.append(seq[-1] + seq[-2])
            self.answer  = str(seq[-1] + seq[-2])
            self.display = ", ".join(str(x) for x in seq) + ", ?"

        else:
            n    = random.randint(1, 5)
            seq  = [(n + i) ** 2 for i in range(5)]
            self.answer  = str((n + 5) ** 2)
            self.display = ", ".join(str(x) for x in seq) + ", ?"

        self.kind = kind
        return self.display

    def render(self, display):
        lines = []
        lines.append("+" + "-" * 42 + "+")
        lines.append("|" + " " * 42 + "|")
        lines.append("|   Complete the sequence:".ljust(43) + "|")
        lines.append("|" + " " * 42 + "|")
        lines.append("|   " + display.ljust(39) + "|")
        lines.append("|" + " " * 42 + "|")
        lines.append("+" + "-" * 42 + "+")
        return lines

    def verify(self, user_input):
        return user_input.strip() == self.answer
