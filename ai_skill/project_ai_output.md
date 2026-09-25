Running the skill against it now — reading its own procedure and producing the brief the way it should. One thing the skill would stop to ask a real teacher, which I'll assume: **small party, not solo hiker** (faithful to Oregon Trail, and it lets me test whether the skill correctly reads multiplicity-without-variation and still refuses a tree).

---

# Design Brief: Appalachian Trail

## Domain and which smells it shows
Repetition (every day runs the same update), **state that travels together** (the expedition's food, money, health, stamina, gear persist and mutate across the whole game), and coordination (a through-hike ties the party, the trail, and random events into one loop). **Variation is present but thin** — events differ, party members differ — and, as the ladder shows, none of it earns inheritance. That's the honest read of this domain.

## The takeaway
Give persistent state a home, then reuse one update shape across every day of the trail.

## User-story ladder

### Story 1: "As a hiker, I want each day to advance the trail and use up supplies."
- Pressure: the day's arithmetic gets rewritten wherever a day happens.
- Smell: repetition.
- Reuse: name the day-update once.
- Mechanism: **functional** — `advance_day(...)`.
- Withholding: Novices will repeat code again and again.  Other students might not recognize they need to return and reassign values.

### Story 2: "As a hiker, I want my daily miles to depend on pace, terrain, and stamina, and my food use to depend on party size and rations."
- Pressure: cramming those sub-rules into `advance_day` makes it unreadable.
- Smell: repetition inside a computation — sub-ideas worth their own names.
- Reuse: extract them; the day-update delegates.
- Mechanism: **functional composition** — `advance_day` calls `miles_today(pace, terrain, stamina)` and `food_needed(party_size, ration_level)`. *Real abstraction, no object anywhere — the objects-first antidote.*
- Withholding: let them nest the pace/terrain math inline and watch it tangle.

### Story 3: "As a hiker, I want my condition to carry over day to day and be affected by everything."
- Pressure: `food, money, health, stamina, gear, morale` are threaded through six function signatures; adding one new stat means editing all of them.
- Smell: **state that travels together** — one expedition's data that must persist and mutate as a unit.
- Reuse: give the state one home.
- Mechanism: **object** — an `Expedition` owning the state. (This is the lone-stateful-thing case: there's *one* expedition, not N, and it still wants an object — because state must live somewhere and change coherently, not because it's a collection.)
- Withholding: *strongly.* Thread the loose variables first, then add "morale" and feel every signature break.

### Story 4: "As a player, I want a party whose members can each get sick or injured."
- Pressure: tracking each member's health as parallel lists (`health1, health2, health3`) repeats Story 3's mistake one level down.
- Smell: state that travels together, now per-member.
- Reuse: one member definition, many instances.
- Mechanism: **object, a list of `Member` records** — *not a hierarchy.* Members vary in **data** (their health), never in **behavior**; a `Medic`/`Navigator` subclass tree would be ceremony the base game never asks for. Homogeneous multiplicity → a list, full stop.
- Withholding: parallel lists first, then a fourth member.

### Story 5: "As a hiker, I want random events along the trail that change my situation."
- Pressure: a `bear / storm / dysentery / broken axle` chain of `if event == ...` grows without bound and buries each effect.
- Smell: variation on a theme.
- Reuse: shared shape ("roll, then change the expedition"), varied effect.
- Mechanism: **higher-order / data-driven — a table of events, each a record with a name, a trigger chance, and an effect function** applied to the `Expedition`. *Explicitly not an `Event` subclass per kind:* events carry almost no behavior beyond their effect, so a class hierarchy is ceremony; a data table + one applier function is the real reuse.
- Withholding: let the `if`-chain sprawl first, then collapse it into the table.

### Story 6: "As a player, I want to hike Georgia to Katahdin, making choices each leg."
- Pressure: nothing owns the sequence of leg → choices → day-loop → events → win/lose check.
- Smell: coordination.
- Reuse: orchestrate the parts.
- Mechanism: **object, composition** — a `Game` holding the `Expedition`, the `Trail` (a sequence of legs and towns — data, not subclasses), and the event table, driving the loop.
- Withholding: hand over the skeleton; they wire it from the abstractions they built.

## Functional-composition checkpoint
Rungs 1–2 are functional; rung 2 is genuine composition (`advance_day` delegating `miles_today` and `food_needed`). Real abstraction and reuse arrive before the first object. That's the shape.

## Design language to cultivate
Portable questions to reuse until they stick: *What idea are we naming? Where have we seen this shape? What breaks if we add a new stat? Does this earn its keep? Is this reuse across occurrences, state, variants, or steps?* Let students coin the trail's own terms — "leg," "resupply," "ford," "the daily grind" — and insist the names be precise.

## What is deliberately NOT abstracted
No inheritance tree anywhere. Events are data + an effect function, not `Event` subclasses. Party members are a list of records, not a `Medic`/`Navigator` hierarchy. Legs, towns, and terrain are data. A specialized-member hierarchy is a *possible* extension, but the base game exerts no pressure toward it, so the brief declines to add it — the correct restraint, and worth showing students as proof that variation existing is not the same as inheritance being warranted.

---

**Verdict on the dry run.** The skill did the thing you built the test to check: it hit variation *twice* (party members, events) and refused a tree both times, for two different reasons — homogeneous multiplicity → a list, and behavior-thin variation → a data table. It also exercised the broadened "state" row cleanly on the lone `Expedition` (single mutable thing, not a collection), which is the case the old four-signal cut would have fumbled. No blackjack pattern-matching leaked in.

Where a weaker model is still likely to slip: **rung 5.** "Variation on a theme" plus a list of event kinds is a strong pull toward an `Event` base class, and the current table row offers polymorphism as the object form of variation without saying *when it's overkill*. The skill catches this in prose ("no variation, no tree") but that rule guards against variation being *absent* — it doesn't guard against variation being *present but too thin for a class*, which is exactly rung 5. That distinction currently lives only in my head and in this example, not in the skill's instructions.

Want me to add one line to the diagnostic — something like "variation with little behavior beyond an effect → prefer a data table or higher-order function over a subclass" — so a small model reaches for the table on its own instead of needing the worked example to rescue it?