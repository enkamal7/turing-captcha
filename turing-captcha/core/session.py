import time

class Session:
    def __init__(self):
        self.start_time      = time.time()
        self.turing_rounds   = 0
        self.turing_correct  = 0
        self.captcha_passed  = 0
        self.captcha_failed  = 0
        self.events          = []

    def log(self, event):
        self.events.append({"time": time.time(), "event": event})

    def elapsed(self):
        return round(time.time() - self.start_time, 1)

    def turing_accuracy(self):
        if self.turing_rounds == 0:
            return 0
        return round((self.turing_correct / self.turing_rounds) * 100, 1)

    def captcha_accuracy(self):
        total = self.captcha_passed + self.captcha_failed
        if total == 0:
            return 0
        return round((self.captcha_passed / total) * 100, 1)

    def summary(self):
        return {
            "elapsed_seconds":   self.elapsed(),
            "turing_rounds":     self.turing_rounds,
            "turing_correct":    self.turing_correct,
            "turing_accuracy":   f"{self.turing_accuracy()}%",
            "captcha_passed":    self.captcha_passed,
            "captcha_failed":    self.captcha_failed,
            "captcha_accuracy":  f"{self.captcha_accuracy()}%",
        }
