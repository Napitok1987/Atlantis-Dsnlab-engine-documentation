# Visibility And Diplomacy

## Status

Mechanically complete.

## Purpose

This document describes what factions can see, how reveal state works, and how attitudes affect gameplay.

## Visibility Principle

Reports show faction knowledge, not full server truth.

A faction can see:

- its own units fully;
- visible foreign units partially;
- more details when observation, reveal, ownership, or magic allows it.

## Reveal State

Units can reveal:

- no extra identity;
- unit identity;
- faction identity.

DSNlab also accepts `REVEAL NONE`.

Invalid reveal arguments can behave as silent no-ops rather than normal parse errors.

## Attitudes

Factions have attitudes toward other factions.

Attitudes affect:

- object entry;
- combat participation;
- alliance-sensitive movement;
- aid behavior;
- some magic follower checks.

## Object Entry Attitude

`ENTER` checks the object owner's effective attitude toward the entering unit.

This is asymmetric and can be affected by visibility. The entering unit's own opinion of the owner is not the decisive check.

## `Mind Reading`

`Mind Reading` can expose more information about visible units.

The code-confirmed full report threshold is level `4+`, not level `5` as stated by older built-in text.

## `FARSIGHT`

Remote visibility can create region reports for regions where the faction has no physical unit.

Template generation does not necessarily mirror every remotely visible report region.

## `FIND`

`FIND` is syntactically accepted, but mechanically disabled.

At runtime it produces:

```text
FIND: disabled
```

It does not return faction addresses.
