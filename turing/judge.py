import time
from turing.responders import HumanResponder, AIResponder
from turing.relay import Relay
from core import display as D

MIN_EXCHANGES = 3
MAX_EXCHANGES = 8

def run(session):
    D.clear()
    D.banner(
        "TURING TEST SIMULATOR",
        "You are the judge. Determine: Human or AI?",
        color=D.CYAN,
    )

    D.box([
        "RULES",
        "",
        "  You will exchange messages with an unknown entity.",
        "  It is either a Human (scripted) or an AI responder.",
        "  After at least 3 exchanges, submit your verdict.",
        "  The entity has NO idea you are testing it.",
        "",
        f"  Min exchanges : {MIN_EXCHANGES}    Max exchanges : {MAX_EXCHANGES}",
    ], color=D.GRAY)

    D.pause("Press ENTER to begin the session...")

    relay     = Relay(HumanResponder(), AIResponder())
    exchanges = 0
    history   = []

    while exchanges < MAX_EXCHANGES:
        D.clear()
        D.banner("TURING TEST", f"Exchange {exchanges + 1} of {MAX_EXCHANGES}", color=D.CYAN)

        if history:
            print(f"\n  {D.GRAY}--- Conversation so far ---{D.RESET}")
            for role, text in history:
                tag   = f"{D.CYAN}YOU   {D.RESET}" if role == "you" else f"{D.YELLOW}ENTITY{D.RESET}"
                print(f"  {tag}  {text}")
            print()

        if exchanges >= MIN_EXCHANGES:
            print(f"  {D.GRAY}Type your question, or one of:{D.RESET}")
            print(f"  {D.YELLOW}[H]{D.RESET} Human   {D.YELLOW}[A]{D.RESET} AI   {D.YELLOW}[U]{D.RESET} Unsure\n")
        else:
            remaining = MIN_EXCHANGES - exchanges
            print(f"  {D.GRAY}Ask at least {remaining} more question(s) before submitting a verdict.{D.RESET}\n")

        question = D.prompt("Your question")

        if exchanges >= MIN_EXCHANGES and question.upper() in ("H", "A", "U"):
            verdict_map = {"H": "Human", "A": "AI", "U": "Unsure"}
            verdict     = verdict_map[question.upper()]
            _show_verdict(relay, verdict, exchanges, session)
            return

        if not question:
            continue

        history.append(("you", question))
        D.thinking("Entity is responding", duration=1.0 + 0.3 * exchanges)
        response = relay.send(question)
        history.append(("entity", response))
        exchanges += 1

    D.clear()
    D.banner("TURING TEST", "Maximum exchanges reached. Submit your verdict.", color=D.YELLOW)
    print(f"\n  {D.GRAY}--- Full Conversation ---{D.RESET}")
    for role, text in history:
        tag = f"{D.CYAN}YOU   {D.RESET}" if role == "you" else f"{D.YELLOW}ENTITY{D.RESET}"
        print(f"  {tag}  {text}")

    print()
    choice = D.menu("Your verdict:", [("H", "This entity is Human"), ("A", "This entity is an AI"), ("U", "I cannot tell (Unsure)")])
    verdict_map = {"H": "Human", "A": "AI", "U": "Unsure"}
    verdict     = verdict_map.get(choice.upper(), "Unsure")
    _show_verdict(relay, verdict, exchanges, session)


def _show_verdict(relay, verdict, exchanges, session):
    actual = relay.reveal()
    passed = relay.passed(verdict)

    D.clear()
    D.banner("TURING TEST  —  RESULT", color=D.CYAN)

    D.divider()
    D.status("Your verdict",  verdict,                lc=D.CYAN,    vc=D.WHITE)
    D.status("Entity was",    actual,                 lc=D.CYAN,    vc=D.YELLOW)
    D.status("Exchanges",     str(exchanges),         lc=D.CYAN,    vc=D.WHITE)
    D.divider()

    session.turing_rounds += 1
    if verdict == actual or (verdict == "Unsure" and actual == "AI"):
        session.turing_correct += 1

    if actual == "AI" and passed:
        D.result_pass("AI passed the Turing Test — you were deceived.")
        print(f"\n  {D.GRAY}The AI successfully imitated human conversation.{D.RESET}")
        print(f"  {D.GRAY}Loebner Prize criterion: fooled > 30% of judges.{D.RESET}")
    elif actual == "AI" and not passed:
        D.result_fail("AI failed — you correctly identified it as non-human.")
        print(f"\n  {D.GRAY}Telltale signs: response patterns, word choice, cadence.{D.RESET}")
    elif actual == "Human" and verdict == "Human":
        D.result_pass("Correct — it was a human and you identified them.")
    else:
        D.result_warn(f"You said {verdict}, but the entity was {actual}.")

    print(f"\n  {D.BOLD}Session accuracy: {session.turing_accuracy()}%{D.RESET}")
    session.log(f"Turing: verdict={verdict}, actual={actual}, passed={passed}")
    D.pause()
