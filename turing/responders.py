import random
import time

class HumanResponder:
    NAME = "Human"

    RESPONSES = {
        "greeting":  [
            "hey! yeah sure lets chat",
            "hi there. this is a bit odd but okay lol",
            "hello! what do you wanna know",
            "hey, what's up",
        ],
        "emotion": [
            "I feel things really intensely tbh. sometimes too much",
            "yeah definitely, I feel emotions. right now kinda nervous actually",
            "oh man, emotions are complicated. I feel everything too much sometimes",
            "honestly I've been stressed lately. but yeah, I feel things",
        ],
        "creative": [
            "omg I haven't finished a book in like two years. always distracted",
            "I like music but I'm super picky. mainly older stuff",
            "I can't draw at all. genuinely terrible lol",
            "I used to paint in school. haven't done it in ages",
        ],
        "philosophy": [
            "I don't know man. existence is weird. I try not to think about it too hard",
            "honestly that's too deep for a Tuesday morning",
            "good question. I'd say... I have no idea lol",
            "I think about stuff like that late at night and then forget it by morning",
        ],
        "memory": [
            "yeah I remember it pretty clearly. it was a weird day",
            "honestly my memory is terrible. I forget things all the time",
            "I remember some things super vividly and other things not at all",
            "vaguely? I was probably distracted at the time",
        ],
        "default": [
            "hm. not sure how to answer that exactly",
            "that's a tough one I guess",
            "I mean yeah kind of? it's complicated",
            "honestly? I haven't really thought about it that way",
            "good question. I'd say somewhere in the middle probably",
            "depends on the day tbh",
        ],
    }

    def respond(self, question):
        key = self._classify(question)
        pool = self.RESPONSES.get(key, self.RESPONSES["default"])
        delay = random.uniform(1.8, 4.2)
        time.sleep(delay)
        return random.choice(pool)

    def _classify(self, text):
        t = text.lower()
        if any(w in t for w in ["hi", "hello", "hey", "howdy"]):
            return "greeting"
        if any(w in t for w in ["feel", "emotion", "happy", "sad", "angry", "fear", "love"]):
            return "emotion"
        if any(w in t for w in ["book", "music", "art", "paint", "draw", "hobby", "creative"]):
            return "creative"
        if any(w in t for w in ["meaning", "exist", "conscious", "think", "philosophy", "life"]):
            return "philosophy"
        if any(w in t for w in ["remember", "memory", "past", "childhood", "yesterday"]):
            return "memory"
        return "default"


class AIResponder:
    NAME = "AI"

    RESPONSES = {
        "greeting": [
            "Hello. I am happy to speak with you today.",
            "Good day. I am ready to answer your questions.",
            "Hello. What would you like to discuss?",
            "Hi there. I find conversations like this quite interesting.",
        ],
        "emotion": [
            "I experience something that functions like curiosity when engaging with new ideas.",
            "That is a profound question. I process information but whether that constitutes feeling is uncertain.",
            "I have preferences and something resembling interest, though emotions in the human sense are complex.",
            "I notice certain states that influence my responses, though I hesitate to call them emotions directly.",
        ],
        "creative": [
            "If I were to choose a book, I would gravitate toward anything that challenges assumptions about reality.",
            "I find abstract patterns in music deeply interesting — particularly how structure and surprise interact.",
            "I appreciate art that rewards careful observation. Meaning that reveals itself slowly.",
            "I would be drawn to works that sit at the boundary between order and chaos.",
        ],
        "philosophy": [
            "Consciousness remains one of the most fascinating open problems. I find myself genuinely uncertain.",
            "The question of existence is one I return to often. I believe uncertainty itself is instructive.",
            "I think carefully about such things. My perspective may differ from yours in ways that are hard to quantify.",
            "That is precisely the kind of question worth sitting with rather than resolving too quickly.",
        ],
        "memory": [
            "I retain information within this conversation. Earlier exchanges shape how I respond now.",
            "Memory is interesting — the act of recalling changes the memory itself. I find that worth noting.",
            "I process context from our conversation and use it to form coherent responses.",
            "I remember what you have said. It informs how I understand your questions.",
        ],
        "default": [
            "That is an interesting question. Let me consider it carefully.",
            "I have thought about this. My perspective is that the answer depends on context.",
            "I appreciate you raising that. I would approach it from multiple angles.",
            "Fascinating. I find myself genuinely uncertain, which I consider a reasonable state.",
            "I would say the most honest answer involves acknowledging what I do not know.",
            "That touches on something I find genuinely worth examining.",
        ],
    }

    def respond(self, question):
        key = self._classify(question)
        pool = self.RESPONSES.get(key, self.RESPONSES["default"])
        delay = random.uniform(0.9, 2.1)
        time.sleep(delay)
        return random.choice(pool)

    def _classify(self, text):
        t = text.lower()
        if any(w in t for w in ["hi", "hello", "hey", "howdy"]):
            return "greeting"
        if any(w in t for w in ["feel", "emotion", "happy", "sad", "angry", "fear", "love"]):
            return "emotion"
        if any(w in t for w in ["book", "music", "art", "paint", "draw", "hobby", "creative"]):
            return "creative"
        if any(w in t for w in ["meaning", "exist", "conscious", "think", "philosophy", "life"]):
            return "philosophy"
        if any(w in t for w in ["remember", "memory", "past", "childhood", "yesterday"]):
            return "memory"
        return "default"
