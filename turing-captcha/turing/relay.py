import random

class Relay:
    def __init__(self, entity_a, entity_b):
        order = [entity_a, entity_b]
        random.shuffle(order)
        self._entity   = order[0]
        self._identity = self._entity.NAME

    def send(self, question):
        return self._entity.respond(question)

    def reveal(self):
        return self._identity

    def passed(self, verdict):
        if self._identity == "AI":
            return verdict != "AI"
        return verdict == "Human"
