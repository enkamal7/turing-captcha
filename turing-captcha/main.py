import sys
from core import display as D
from core.session import Session
from turing import judge
from captcha import gate

def show_summary(session):
    D.clear()
    D.banner("SESSION SUMMARY", "End of demonstration", color=D.MAGENTA)
    D.divider()
    summary = session.summary()
    D.status("Time elapsed",       f"{summary['elapsed_seconds']}s")
    D.status("Turing rounds",      str(summary["turing_rounds"]))
    D.status("Turing correct",     str(summary["turing_correct"]))
    D.status("Turing accuracy",    summary["turing_accuracy"])
    D.status("CAPTCHA passed",     str(summary["captcha_passed"]))
    D.status("CAPTCHA failed",     str(summary["captcha_failed"]))
    D.status("CAPTCHA accuracy",   summary["captcha_accuracy"])
    D.divider()
    print(f"\n  {D.GRAY}Thank you for running the demo.{D.RESET}\n")

def main():
    session = Session()
    D.clear()
    D.banner(
        "TURING TEST  &  CAPTCHA",
        "Artificial Intelligence — Agent Design Demonstration",
        color=D.CYAN,
    )
    D.typewrite(
        "  Two sides of the same question: can you tell human from machine?",
        delay=0.022,
        color=D.GRAY,
    )
    print()
    D.box([
        "TURING TEST  (you judge the machine)",
        "  Alan Turing, 1950. The Imitation Game.",
        "  A human judge converses with an unknown entity.",
        "  If the judge cannot tell AI from human — the AI passes.",
        "",
        "CAPTCHA  (the machine judges you)",
        "  von Ahn et al., 2003. Reverse Turing Test.",
        "  The system challenges the user.",
        "  If the user cannot pass — they are classified as a bot.",
    ], color=D.GRAY)

    while True:
        choice = D.menu(
            "MAIN MENU",
            [
                ("1", "Turing Test Simulator    — you are the judge"),
                ("2", "CAPTCHA Challenges       — prove you are human"),
                ("3", "View Session Summary"),
                ("Q", "Quit"),
            ],
            color=D.CYAN,
        )

        if choice == "1":
            judge.run(session)
        elif choice == "2":
            gate.run(session)
        elif choice == "3":
            show_summary(session)
            D.pause()
        elif choice.upper() == "Q":
            show_summary(session)
            sys.exit(0)
        else:
            D.result_warn("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
