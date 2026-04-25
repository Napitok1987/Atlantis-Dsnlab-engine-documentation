# Appendix: Server-Specific Deviations

## Status

Mechanically complete.

## Purpose

This appendix indexes the main DSNlab deviations from old rules, built-in help, and expected clean Atlantis behavior.

It does not replace the topic documents. It points to areas where the canon intentionally follows code.

## Orders, Parser, And Runtime

### Order files are not transactional

Normal line errors do not roll back already applied immediate changes and usually do not abort the whole file.

### The parser accepts additional DSNlab forms

Canonical examples:

- `CONSUME NONE`
- `REVEAL NONE`
- legacy `NOSPOILS <flag>`
- server-specific `ROUTE`
- server-specific `GIVE <target> ALL <item>`

### `FIND` is syntactic but disabled

Runtime behavior returns:

```text
FIND: disabled
```

No faction address is returned.

### Interface limits are hardcoded

Canonical limits include:

- `SHOW` request limit;
- `Errors during turn` section limit.

## Economy, Diplomacy, And Combat

### Starting money is not fixed `5000`

Canonical formula:

```text
5020 + 50 * TurnNumber()
```

### `ENTER` checks owner attitude

Entry depends on the object owner's effective attitude toward the entering unit, not on symmetric friendliness.

### `GUARD` requires combat readiness

A unit must practically satisfy the combat-ready check to remain on active guard.

### `NOAID` works at side level

Aid from neighboring regions depends on the locally assembled battle side, not only on one initiating unit.

### Local `TRADE` is order-sensitive

Local trade is not a perfectly clean best-price auction in partial-fill cases.

## Magic

Canonical code-confirmed deviations:

- `Mind Reading` gives full report at level `4+`, not `5`;
- `Force Shield` is not a working army-wide shield against ordinary attacks;
- `Clear Skies` affects economy and weather state in the same turn;
- `Engrave Runes of Warding` has no separate failure roll after validation;
- `Construct Gate` spends `1000 silver` only on success.

## World Generation, Reports, And NPC

### Starting areas have no separate hard-safe flag

Nexus and starting cities are protected by city guards and related runtime logic, not by absolute region immunity.

### Starting-city status is heuristic

The code uses current state such as `town->pop == 5000`, not a stored origin flag.

### `Gate 0` is partially broken

A gate can receive number `0`, after which parts of visibility, detection, templates, and directed jumps treat it incorrectly.

### City guard restoration has special lookup behavior

`AdjustCityMons` first looks for any `U_GUARD`. If found, it adjusts that unit and does not continue to the fallback regeneration branch.

### Monster movement differs from spawn/refill checks

Wandering monster movement and monster spawn/refill use different guarded-region checks.

## Text Defects

Several built-in help defects are canonical only as text defects, not mechanics. Examples include misspellings and wrong spell names in help output.
