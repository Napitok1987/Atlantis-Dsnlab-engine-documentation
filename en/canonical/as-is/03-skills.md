# Skills

## Status

Mechanically complete.

## Purpose

This document describes the skill model used by the original server.

## Skill Model

Skills define what a unit can do and how effective it is.

They affect:

- production;
- construction;
- combat;
- stealth and observation;
- riding and sailing;
- magic;
- entertainment and work-related actions;
- report visibility.

## Skill Levels

A unit's practical capability is determined by skill level.

The server stores training progress and derives levels from accumulated study. Faction-level knowledge can unlock report text for known skills.

## Study

`STUDY` is a monthly order.

It can:

- add study days to a skill;
- unlock new faction-level skill knowledge;
- contribute to mage status when studying magical foundations.

Study interacts with silver cost, prerequisites, and unit type.

## Teaching

`TEACH` allows one unit to teach another when the normal conditions are satisfied.

The details depend on location, unit eligibility, and the skill being taught.

## Skill Reports

`SHOW SKILL <skill> <level>` can request known skill text.

The parser checks the requested level against the faction-level known skill table. This table is not merely the current skill of a single unit.

## Magic Skills

Magic skills are normal skills with special consequences:

- they can make a leader count as a mage;
- they unlock spells;
- they interact with faction mage limits;
- they can create combat, economy, visibility, teleportation, or world effects.

Magic is covered in detail in [11-magic.md](11-magic.md).

## Combat Skills

Combat-related skills affect:

- attack and defense values;
- weapon use;
- riding;
- tactics;
- assassination and stealth interactions;
- battle report output.

Combat is covered in [10-combat.md](10-combat.md).

## Production Skills

Production skills gate:

- advanced products;
- buildings and ships;
- special items;
- market and report visibility for advanced goods.

Economy and production are covered in [07-economy.md](07-economy.md).

## Canonical Notes

- Skill text in built-in help can contain errors.
- Code-confirmed behavior wins over skill descriptions.
- Some skill descriptions are therefore treated as secondary text rather than mechanics.
