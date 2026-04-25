# Magic

## Status

Mechanically complete.

## Purpose

This document describes magic parsing, spell execution, combat spells, economy spells, visibility spells, and teleportation.

## Spell Orders

`CAST` creates a delayed spell order during parsing.

Depending on the spell, it can be queued as:

- normal current-turn magic;
- teleportation;
- gate jump;
- portal movement.

When the parser accepts a new spell order, previous `castorders` and `teleportorders` can be cleared.

## Mage Eligibility

The parser and immediate order processing reject non-mages or clearly invalid skills.

Studying magical foundations can turn a leader into a mage and increase the faction-level `Mages` counter.

## Spell Names

Quoted multiword spell names are accepted in tested cases, for example:

```text
study "force shield"
combat "force shield"
```

## Combat Spells

Combat spells are used through `COMBAT <spell>`.

Executable tests confirm runtime paths for:

- `Force Shield`
- `Fire`
- `Clear Skies`
- `Summon Storm`

Confirmed battle-log lines include:

```text
casts Force Shield.
shoots a Fireball
casts Clear Skies.
```

## `Force Shield`

Built-in text suggests a broad shield against bow attacks, but code behavior is narrower.

Canonical behavior:

- the general combat-shield effect does not protect the whole army from normal attacks;
- the meaningful effect is the caster's personal defensive bonus.

## `Clear Skies`

`Clear Skies` affects the economy in the same turn.

The spell sets state before post-turn product updates, so the production bonus applies immediately rather than only next turn.

## `Engrave Runes Of Warding`

After validation succeeds, the code applies runes without a separate success-chance roll.

This differs from older help text that describes a level-based chance.

## `Construct Gate`

The `1000 silver` cost is spent only on successful gate creation.

Failed attempts do not consume the silver.

## Gate Magic

Gate-related spells interact with numbered gates.

Important server edge case:

- `gate 0` can exist internally;
- several gate spell paths treat `0` as no gate;
- directed jump to `gate 0` is impossible because lookup returns no such gate.

## Portal Magic

`Portal Lore` moves listed units through the caster's portal logic.

The spell depends on caster eligibility, target existence, weight limits, and valid listed units.

## Built-In Text Defects

Several spell descriptions in built-in help contain text defects. They are documented as text defects, not as mechanics.
