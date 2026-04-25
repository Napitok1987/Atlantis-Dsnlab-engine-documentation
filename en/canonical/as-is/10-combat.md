# Combat

## Status

Mechanically complete.

## Purpose

This document describes battle initiation, participation, aid, city guards, assassination, spoils, and combat reporting.

## Battle Sources

Combat can be caused by:

- explicit `ATTACK`;
- automatic attacks;
- `ADVANCE`;
- object-entry battle;
- assassination;
- monster behavior;
- guard and forbid interactions.

## Participation

Battle sides are assembled from local units and sometimes supporting units.

Visibility, attitudes, `NOAID`, guards, and location affect who joins.

## `NOAID`

`NOAID` is not a purely individual isolation flag.

In code it works at the level of the locally assembled side:

- if all local participants on a side have `NOAID`, outside aid is blocked;
- if at least one local participant lacks `NOAID`, outside aid can be allowed.

## City Guards

City guards are real units, not invisible region shields.

Canonical behavior:

- Nexus and starting cities are protected by city guards and forbid/intervention logic;
- city guards do not automatically join ordinary regional `ADVANCE` in tested cases;
- they do join object-entry battle inside a city.

## `GUARD`

The server requires practical combat readiness for active guard.

If a unit cannot satisfy the combat-ready check, `GUARD` can fail at runtime with the server error:

```text
Must be combat ready to be on guard.
```

## Assassination

`ASSASSINATE` has a special battle path.

If successful, outside factions receive a reduced result rather than the full battle log.

## Spoils

Spoils go to surviving eligible units on the winning side.

Eligibility depends on:

- survival;
- item type;
- spoil settings;
- carrying and filter rules.

Executable tests confirm real lines such as:

```text
Spoils: ... silver [SILV].
```

## Legacy `NOSPOILS`

The DSNlab parser still accepts legacy `NOSPOILS <flag>`.

It is deprecated by text but mechanically recognized by the server.

## Reports

Battle reports include:

- sides;
- participating units;
- round events;
- combat spells;
- losses;
- spoils;
- final result.

Battle-visible unit lines are not identical to normal monthly unit report lines.
