# Atlantis DSNlab As-Is

## Status

Mechanically complete.

## Purpose

This document opens the canonical `as-is` set and gives a high-level map of the original game.

It defines:

- what Atlantis DSNlab is;
- the core entities and terms;
- the monthly turn cycle;
- the role of the other canonical documents;
- the main invariants of world state and reports.

## What Atlantis DSNlab Is

Atlantis DSNlab is a turn-based PBEM game about controlling a faction in a shared fantasy world.

The player does not control units in real time. Instead, the player:

- receives a monthly report;
- prepares a text order file;
- sends it for processing;
- receives the next report after the month is resolved.

Core gameplay is built around:

- exploration;
- economy and supply;
- skill development;
- magic;
- movement;
- diplomacy;
- combat.

## Core Entities

### Faction

A faction is the player's side in the world.

It has:

- a name;
- attitudes to other factions;
- specialization limits;
- unclaimed silver;
- owned units;
- its own world knowledge reflected in reports.

### Unit

A unit is the main controllable entity.

Units receive orders and store:

- people and monsters;
- items;
- skills;
- current location;
- behavior flags;
- monthly and immediate orders.

### Region

A region is the basic world cell.

It has:

- terrain;
- coordinates;
- neighbors;
- population;
- economy;
- objects;
- units;
- optional gates and special properties.

### Object

Objects are structures or containers located in a region.

They include:

- buildings;
- ships;
- lairs;
- shafts;
- dummy internal locations.

An object can hold units and can affect ownership, protection, transport, and visibility.

### Item

Items represent silver, food, weapons, armor, trade goods, mounts, monsters, and special artifacts.

Items are moved through production, trade, transfer, battle spoils, maintenance, and magic.

### Skill

Skills define what units can do and how well they do it.

They affect production, combat, stealth, magic, riding, sailing, construction, observation, and other systems.

## Monthly Cycle

The normal cycle is:

1. the server has a saved world state;
2. each faction receives a report for the previous month;
3. players submit order files;
4. the server parses orders;
5. the server executes the month in a fixed phase order;
6. new game state and reports are written.

The order parser is not purely declarative. Some orders change state immediately during parsing, while others are queued for later phases.

## Canonical Documents

- [01-turn-processing.md](01-turn-processing.md) - parsing and execution phases.
- [02-factions-and-units.md](02-factions-and-units.md) - faction and unit state.
- [03-skills.md](03-skills.md) - skills and learning.
- [04-items.md](04-items.md) - item model.
- [05-regions-and-terrain.md](05-regions-and-terrain.md) - regions, terrain, gates, and settlements.
- [06-objects-and-ships.md](06-objects-and-ships.md) - objects, ownership, ships, and buildings.
- [07-economy.md](07-economy.md) - economy, production, market, upkeep.
- [08-movement.md](08-movement.md) - movement, advance, sailing, guard, forbid.
- [09-visibility-and-diplomacy.md](09-visibility-and-diplomacy.md) - visibility, attitudes, reveal state.
- [10-combat.md](10-combat.md) - combat, assassination, spoils, aid.
- [11-magic.md](11-magic.md) - magic rules and spell-specific behavior.
- [12-reports-and-files.md](12-reports-and-files.md) - file formats, reports, templates, parser catalog.
- [13-world-and-npc.md](13-world-and-npc.md) - world generation, NPC factions, guards, monsters.

Appendices:

- [appendix-data-tables.md](appendix-data-tables.md)
- [appendix-server-specific-deviations.md](appendix-server-specific-deviations.md)

## Main Invariants

- Code-confirmed behavior wins over old prose.
- Reports show what a faction is allowed to know, not the full internal state.
- Order parsing can mutate state before the monthly phases begin.
- Some DSNlab behavior differs from old Atlantis expectations and is intentionally documented as server-specific.
