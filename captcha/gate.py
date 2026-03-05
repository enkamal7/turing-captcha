import time
import random
from captcha.challenges import TextChallenge, MathChallenge, WordChallenge, SequenceChallenge
from core import display as D

CHALLENGES = [TextChallenge, MathChallenge, WordChallenge, SequenceChallenge]
TOO_FAST   = 1.5
MAX_TRIES  = 3

def _render(lines):
    print()
    for line in lines:
        print(f"  {D.CYAN}{line}{D.RESET}")
    print()

def _run_challenge(challenge, session):
    content  = challenge.generate()
    rendered = challenge.render(content)
    attempts = 0

    while attempts < MAX_TRIES:
        D.clear()
        D.banner("CAPTCHA VERIFICATION", challenge.NAME, color=D.YELLOW)
        print(f"\n  {D.GRAY}{challenge.HINT}{D.RESET}")
        _render(rendered)

        if attempts > 0:
            print(f"  {D.RED}Attempt {attempts + 1} of {MAX_TRIES}{D.RESET}\n")

        start  = time.time()
        answer = D.prompt("Your answer")
        elapsed = time.time() - start

        if elapsed < TOO_FAST:
            D.result_fail(f"Response in {elapsed:.2f}s — suspiciously fast. Regenerating.")
            session.captcha_failed += 1
            session.log(f"CAPTCHA fail: too fast ({elapsed:.2f}s)")
            time.sleep(1.5)
            content  = challenge.generate()
            rendered = challenge.render(content)
            attempts += 1
            continue

        attempts += 1

        if challenge.verify(answer):
            D.result_pass(f"Correct in {elapsed:.1f}s. Human verified.")
            session.captcha_passed += 1
            session.log(f"CAPTCHA pass: {challenge.NAME} in {elapsed:.1f}s")
            D.pause()
            return True
        else:
            if attempts < MAX_TRIES:
                D.result_fail(f"Wrong answer. {MAX_TRIES - attempts} attempt(s) left.")
                session.log(f"CAPTCHA retry: {challenge.NAME}")
                time.sleep(1.0)
                content  = challenge.generate()
                rendered = challenge.render(content)
            else:
                D.result_fail("Maximum attempts reached. Access denied.")
                session.captcha_failed += 1
                session.log(f"CAPTCHA fail: {challenge.NAME} - max attempts")
                D.pause()
                return False

    return False


def run(session):
    D.clear()
    D.banner("CAPTCHA SYSTEM", "Prove you are human — the machine is the judge.", color=D.YELLOW)

    D.box([
        "HOW IT WORKS",
        "",
        "  CAPTCHA is the reverse Turing Test.",
        "  The SYSTEM evaluates YOU — not the other way around.",
        "  Four challenge types, each testing a different human ability:",
        "",
        "  [1] Text Recognition   - read distorted characters",
        "  [2] Math Challenge      - solve arithmetic problems",
        "  [3] Word Unscramble     - recognise scrambled words",
        "  [4] Pattern Sequence    - complete number patterns",
        "",
        "  Timing is measured. Too fast = bot. Too wrong = bot.",
    ], color=D.GRAY)

    D.pause()

    options = [
        ("1", "Text Recognition   — read distorted characters"),
        ("2", "Math Challenge      — solve arithmetic"),
        ("3", "Word Unscramble     — decode scrambled words"),
        ("4", "Pattern Sequence    — complete the series"),
        ("R", "Random challenge"),
        ("A", "Run all four challenges in sequence"),
    ]

    choice = D.menu("Select a CAPTCHA challenge:", options, color=D.YELLOW)

    challenge_map = {
        "1": [TextChallenge],
        "2": [MathChallenge],
        "3": [WordChallenge],
        "4": [SequenceChallenge],
        "R": [random.choice(CHALLENGES)],
        "A": CHALLENGES,
    }

    selected = challenge_map.get(choice.upper(), [random.choice(CHALLENGES)])

    passed_all = True
    for cls in selected:
        result = _run_challenge(cls(), session)
        if not result:
            passed_all = False

    D.clear()
    D.banner("CAPTCHA  —  SESSION RESULT", color=D.YELLOW)
    D.divider()
    D.status("Challenges passed", str(session.captcha_passed), lc=D.CYAN, vc=D.GREEN)
    D.status("Challenges failed", str(session.captcha_failed), lc=D.CYAN, vc=D.RED)
    D.status("Accuracy",          session.captcha_accuracy(),  lc=D.CYAN, vc=D.WHITE)
    D.divider()

    if passed_all:
        D.result_pass("All challenges passed. You are classified as HUMAN.")
    else:
        D.result_fail("One or more challenges failed. Bot activity suspected.")

    D.pause()
