# Factions And Units

## Status

Mechanically complete.

## Purpose

This document describes faction state, unit state, limits, flags, and the core ownership model.

## Factions

A faction is the persistent player-side entity.

It stores:

- faction number;
- name and address;
- password;
- unclaimed silver;
- attitudes toward other factions;
- specialization limits;
- report options;
- known skill and item information;
- owned units.

NPC factions exist for guards and creatures. They are controlled by the server, not by normal player orders.

## Starting Faction State

The original server does not use a fixed `5000` silver start.

Canonical starting unclaimed silver is:

- `5020 + 50 * TurnNumber()`

This is a code-confirmed deviation from older text.

## Unit State

A unit stores:

- owner faction;
- location;
- name and description;
- men, monsters, and items;
- skills and experience;
- flags and reveal state;
- combat and movement state;
- pending monthly and immediate orders.

Units are the normal target of player orders.

## Unit Creation

Units can appear through:

- starting faction setup;
- `FORM`;
- recruiting;
- monster and guard generation;
- special world-generation logic.

`FORM` creates the new unit during parsing, not at the end of the turn. The new unit inherits important flags and location from the original unit.

## Specialization Limits

Factions have limits for special roles such as mages and leaders.

The server tracks these limits at faction level. Reports show current usage and limits, but the report is not a complete internal dump.

## Flags

Important unit flags include:

- `GUARD`
- `AVOID`
- `BEHIND`
- `HOLD`
- `NOAID`
- `REVEAL`
- `AUTOTAX`
- `SPOILS`
- `CONSUME`

Many flags are set immediately during parsing.

## Reveal State

Reveal state controls whether a unit exposes:

- no extra identity;
- unit identity;
- faction identity.

Visibility and reveal are described in more detail in [09-visibility-and-diplomacy.md](09-visibility-and-diplomacy.md).

## Ownership

Ownership affects:

- which orders are legal;
- which units are fully visible;
- who owns objects;
- who receives reports;
- who can promote units inside objects.

Object ownership is positional: the first eligible unit inside an object is the effective owner.

## Canonical Deviations

Important code-confirmed deviations include:

- starting money is `5020 + 50 * TurnNumber()`;
- `FORM` does not create a completely clean unit;
- some faction-level commands are syntactically submitted inside a `unit` block;
- NPC guard and creature factions exist as normal server-side factions.
