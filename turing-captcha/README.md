# Turing Test & CAPTCHA — Terminal Implementation

Artificial Intelligence course demonstration.
Two sides of the same question: **can you tell human from machine?**

---

## Members

| Name                | Roll Number  |
|---------------------|--------------|
| Kamal Kumar Nampally| SE24UCSE110  |

---

## Concept

### The Turing Test (1950)
Alan Turing proposed the **Imitation Game** — a test of machine intelligence.
A human judge converses with two entities (one human, one machine) without knowing which is which.
If the judge **cannot reliably distinguish** the machine from the human, the machine is said to have passed.

### CAPTCHA (2003)
von Ahn et al. proposed the **reverse Turing Test**.
The system is the judge. The user is tested.
Challenges exploit tasks that are trivial for humans but computationally hard for bots —
distorted text, arithmetic, word recognition, pattern sequences.

### Key Difference

```
Turing Test   →  AI tries to pass as human   →  Human is the judge
CAPTCHA       →  Human tries to prove humanity →  Machine is the judge
```

---

## Architecture

```
+------------------------------------------------------------------+
|                        TURING TEST                               |
|                                                                  |
|   JUDGE (you)                                                    |
|       |                                                          |
|       |  question                                                |
|       v                                                          |
|   RELAY / ANONYMIZER  <-- hides identity, adds realistic delay   |
|       |                                                          |
|       |  routes to one of:                                       |
|       |                                                          |
|   HumanResponder          AIResponder                            |
|   (scripted, informal)    (formal, measured)                     |
|       |                                                          |
|       |  response                                                |
|       v                                                          |
|   JUDGE submits verdict: Human / AI / Unsure                     |
|       |                                                          |
|       v                                                          |
|   SCORER  -- tracks accuracy across rounds                       |
+------------------------------------------------------------------+

+------------------------------------------------------------------+
|                          CAPTCHA                                 |
|                                                                  |
|   USER (you)                                                     |
|       |                                                          |
|       v                                                          |
|   CHALLENGE GENERATOR                                            |
|       selects one of four challenge types:                       |
|       TextChallenge / MathChallenge / WordChallenge / Sequence   |
|       |                                                          |
|       |  challenge rendered to terminal                          |
|       v                                                          |
|   USER submits answer                                            |
|       |                                                          |
|       v                                                          |
|   VERIFIER ENGINE                                                |
|       checks: correctness + timing (< 1.5s = bot)               |
|       max 3 attempts before lockout                              |
|       |                                                          |
|       v                                                          |
|   GATE: PASS (human) or FAIL (bot suspected)                     |
+------------------------------------------------------------------+
```

### Project Structure

```
turing-captcha/
|
+-- main.py                    Entry point, main menu, session summary
|
+-- core/
|   +-- display.py             All terminal output, colors, prompts
|   +-- session.py             Tracks accuracy across both systems
|
+-- turing/
|   +-- responders.py          HumanResponder and AIResponder classes
|   +-- relay.py               Anonymizer — hides entity identity
|   +-- judge.py               Turing Test game loop
|
+-- captcha/
|   +-- challenges.py          Four challenge types (all inherit base)
|   +-- verifier.py            Timing + correctness verification
|   +-- gate.py                CAPTCHA game loop
```

---

## CAPTCHA Challenge Types

| Challenge         | Human Advantage                    | Why Bots Fail                          |
|-------------------|------------------------------------|----------------------------------------|
| Text Recognition  | Visual perception of noisy text    | OCR fails on noise and distortion      |
| Math Challenge    | Instant arithmetic recognition     | Requires parsing, slower pipeline      |
| Word Unscramble   | Pattern recognition of word shapes | Brute-force takes measurable time      |
| Pattern Sequence  | Rule detection is intuitive        | Statistical analysis, not perceptual   |

All four also measure **response time**. Answers faster than 1.5 seconds are flagged as bot behaviour.

---

## Turing Test — How the Relay Works

```python
relay = Relay(HumanResponder(), AIResponder())
```

The relay randomly assigns one of the two responders as the active entity.
The judge never sees which is which — only the response is shown.

- `HumanResponder` uses informal language, typos, hesitation
- `AIResponder` uses measured, structured, thoughtful language
- Response delay is randomised to simulate realistic typing time

The judge submits a verdict after at least 3 exchanges.
The AI **passes** if the judge says Human or Unsure when the entity was actually AI.

---

## Setup

No external libraries required. Pure Python standard library.

```bash
python main.py
```
### Step 1 — Clone the repository

```bash
git clone https://github.com/enkamal7/turing-captcha.git
cd turing-captcha
```
---

## Step-2 Usage

```
MAIN MENU
  [1]  Turing Test Simulator    -- you are the judge
  [2]  CAPTCHA Challenges       -- prove you are human
  [3]  View Session Summary
  [Q]  Quit
```

Inside the Turing Test, type your questions freely.
After 3+ exchanges, enter `H` (Human), `A` (AI), or `U` (Unsure) to submit your verdict.

Inside CAPTCHA, choose a challenge type or run all four in sequence.

---

## Upgrading as the Course Progresses

The architecture is designed to grow:

```
Add a new CAPTCHA type:
    1. Create a class in captcha/challenges.py
    2. Inherit from the same pattern (generate / render / verify)
    3. Add it to the CHALLENGES list in captcha/gate.py
    Nothing else changes.

Add a smarter AI responder:
    1. Add a new class to turing/responders.py
    2. Pass it to Relay() in turing/judge.py
    Nothing else changes.

Connect to a real LLM (GPT, Claude):
    1. Replace AIResponder.respond() with an API call
    2. The rest of the system is unchanged.
```

---

## References

- Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, 59(236), 433-460.
- von Ahn, L., Blum, M., Hopper, N., & Langford, J. (2003). CAPTCHA: Using Hard AI Problems for Security.
- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*. Chapter 2: Intelligent Agents.
