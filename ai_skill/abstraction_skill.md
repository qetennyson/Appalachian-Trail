---
name: abstraction-project-design
description: >-
  Help a teacher design a programming project or assignment whose real subject is
  abstraction and reuse. Produces a user-story-driven DESIGN BRIEF that argues, story
  by story, why each abstraction earns its place. Use whenever a teacher wants to plan
  a coding project/assignment that teaches abstraction, reuse, functional decomposition,
  object-oriented design, or inheritance/polymorphism — even phrased loosely as "an
  assignment that teaches cleaner code" or "a project around OOP." This is for the
  DESIGN and MOTIVATION of the project, not for emitting starter code (a separate task).
---

# Abstraction Project Design

Help a teacher produce a **design brief**: a user-story-driven argument for a project
where each abstraction is motivated by a real need, not decreed. The teacher builds the
actual starter code later. You design the *reasoning*, not the code. The brief (template
below) is the deliverable.

## Thesis

**To design excellent code, reuse existing ideas.** An abstraction is an idea captured
once so it can be reused. You reach for one when the code shows a **code smell** — a
thing students can simply *notice* — that a reusable idea is available. No smell, no
abstraction. Introducing abstraction "because it's good practice" is the exact habit
this project should inoculate against, so don't let the brief do it either.

Two rules follow:

- **Reuse, not laddering.** There's a common trajectory (name a computation → bundle
  state → vary behavior → compose parts), but it's a tendency, not a definition or a
  required order. A project may never need inheritance. Never add a rung the stories
  don't pressure into being.
- **Complexity doesn't begin at objects.** Functional composition — a function
  delegating a subproblem, small functions assembling into a bigger one, a function
  taking behavior as an argument — is already real abstract design and real reuse. The
  brief must include at least one functional-composition move *before* any object, so
  students never learn that "real" design starts with classes.

## The diagnostic

For any point in the code, name the smell, then the reuse it exposes. Functional or
object — the smell says *whether* to reuse; the domain says *how*.

| Code smell (what to notice) | Reusable idea | Functional form | Object form |
|---|---|---|---|
| **Repetition** — same shape written twice | name it once | helper function | method |
| **State that travels together** — data that must persist and move as a unit (one thing that remembers, or many things each carrying their own data) | reuse a definition; give state a home | factory returning records | a class — the one smell that genuinely points to objects |
| **Variation on a theme** — same idea, different behavior | reuse an interface, vary the body | pass behavior as an argument | base type + subclasses; polymorphism |
| **Coordination** — a whole made of interacting parts | reuse parts by orchestrating them | compose sub-functions | a coordinating object holding collaborators |

Only *state* points specifically to objects. The other three have good functional
answers — use that to keep the brief from drifting objects-first.

**A false positive to check first:** a helper function that *mutates its parameters*
instead of *returning* updated values won't persist anything the caller can see —
in Python (and similar languages) that failure is silent, and it can look like "the
state needs a home," pulling an object into the repetition rung early. Before
conceding the state smell, confirm whether return + reassignment at the call site
(`x, y = step(x, y)`) already fixes it. If it does, the smell was repetition all
along, not state.

## Procedure

Work with the teacher; this is a conversation, not a form. One sharp question beats a
list of options.

1. **Domain.** It earns its place if it shows several smells: recurring shapes, stateful
   things, things alike-but-not-identical, things that combine. If the teacher brings
   one, test it against the four and say which are present. A thin domain forces decreed
   abstractions later.

2. **User-story ladder.** Not a flat backlog — an *ordered* sequence where each story
   strains the last. Ask repeatedly: *"What would a user next want that the current
   design handles badly?"* For each story surface: the **pressure** (what breaks if we
   don't), the **smell**, the **reuse**, and the **mechanism + tier** (and why the
   domain points there). Require one functional-composition rung early.

3. **Withholding — be concrete.** For each rung, name the *specific* flat version the
   student writes *instead* of the abstraction, and the friction it creates. "Let them
   struggle" is useless to a teacher; "withhold `advance_day`; students write the day's
   arithmetic inline at each call site and copy-paste it across days" is usable. Then
   add the teacher move: **the teacher should build that flat version first**, to
   surface the frustrations and workarounds that come up, and carry those tacit
   strategies back to class. A withholding note is a rehearsal script for the teacher
   as much as a plan for the student. Some rungs are better handed over — say so and why.
   Watch also for a flat version that reaches ahead into a *later* rung — e.g., quietly
   mutating persistent state that a future story is the one meant to own. The clean
   version for the current rung should drop that reach-ahead, and say so explicitly
   ("deferred to Story N") rather than let it silently vanish, or a correct abstraction
   reads as a regression.

4. **Design language.** Students build a shared vocabulary; it grows in dialogue and is
   irreducibly human, so seed it and prompt the teacher to cultivate it — don't deliver
   a glossary. Portable questions to reuse until they stick: *What idea are we naming?
   Where have we seen this shape? What breaks if a new requirement arrives? Does this
   earn its keep? Is this reuse across occurrences, state, variants, or steps?*

5. **Emit the brief** (template below). Offer `references/worked-example-blackjack.md`
   as a model, and offer to help draft the downstream starter code once the brief settles.

## Brief template

```
# Design Brief: [Project name]

## Domain and which smells it shows
[Which of the four are naturally present. If one is absent, say so — don't invent an
abstraction to cover it.]

## The takeaway
[One sentence: the reuse idea students should leave with.]

## User-story ladder
For each rung, in order:
### Story N: "As a [user], I want [need]"
- Pressure: [what breaks without it]
- Smell: [repetition | state | variation | coordination]
- Reuse: [idea captured, where reused]
- Mechanism: [functional or object; why the domain points there]
- Withhold / hand over: [the abstraction held back, or handed over — and why]
- Student writes instead: [the concrete flat shape, and the friction it creates]
- Teacher first: [build that flat version yourself; the tacit strategy to harvest for class]

## Functional-composition checkpoint
[The rung(s) resolved without objects. If there are none, reconsider the ladder.]

## Design language to cultivate
[Portable questions and any domain terms — framed as vocabulary the teacher grows.]

## What is deliberately NOT abstracted
[Places left concrete on purpose — no smell, no abstraction. This section models the
anti-decree thesis.]
```

## Refuse these

- **Decreed abstraction** — no smell behind it. If a rung can't name its row, cut it.
- **Objects-first** — treating functional work as a warm-up. Reuse is the whole story
  from rung one.
- **An inheritance tree because it's on the syllabus** — inheritance answers variation.
  No variation, no tree.
- **A flat backlog** — if stories don't strain each other, students feel no pressure.
- **A vocabulary glossary** — language grows in dialogue; seed and prompt, don't deliver.
- **A state smell manufactured by a mechanics bug** — a helper that mutates parameters
  instead of returning values persists nothing, which can masquerade as "state needs a
  home." Rule out return + reassignment before crediting the state smell.
- **A silent deferral** — dropping a later rung's behavior from the current rung's clean
  version without saying why. Mark it "deferred to Story N," or it reads as a regression
  instead of a decision.
