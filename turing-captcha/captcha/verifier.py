import time

TOO_FAST_THRESHOLD = 1.5
MAX_ATTEMPTS       = 3

class Verifier:
    def __init__(self):
        self.attempts = 0

    def run(self, challenge):
        self.attempts = 0
        content  = challenge.generate()
        rendered = challenge.render(content)

        while self.attempts < MAX_ATTEMPTS:
            self.attempts += 1
            start     = time.time()
            answer    = yield rendered
            elapsed   = time.time() - start

            if elapsed < TOO_FAST_THRESHOLD:
                yield ("fail", f"Response in {elapsed:.2f}s — too fast for a human. Bot suspected.")
                return

            if challenge.verify(answer):
                yield ("pass", f"Correct in {elapsed:.1f}s after {self.attempts} attempt(s).")
                return
            else:
                remaining = MAX_ATTEMPTS - self.attempts
                if remaining > 0:
                    yield ("retry", f"Incorrect. {remaining} attempt(s) remaining.")
                    content  = challenge.generate()
                    rendered = challenge.render(content)
                else:
                    yield ("fail", f"Maximum attempts reached. Access denied.")
                    return
