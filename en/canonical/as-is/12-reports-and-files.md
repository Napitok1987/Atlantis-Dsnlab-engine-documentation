# Reports And Files

## Status

Mechanically complete.

## Purpose

This document describes the text interfaces of the original Atlantis DSNlab server:

- order files;
- command-line wrapper behavior;
- comments and quoted strings;
- reports;
- templates;
- parser command catalog.

## Main Text Interfaces

The game has two main text interfaces:

1. input order files;
2. output monthly reports.

Reports show the knowledge available to a faction, not the full internal server state.

## Command-Line Wrapper

The shipped `standard` binary has a service-level mismatch between usage text and real file behavior.

Canonical behavior:

- `check <orders> <check>` uses the paths passed on the command line;
- `new <gamefile> <playerfile>` still interactively asks for map size and writes fixed `game.out` and `players.out` in the current directory;
- `run <...>` ignores advertised file names and uses fixed files in the current directory: `game.in`, `players.in`, `orders.<factionnum>`, `report.<factionnum>`, `game.out`, and `players.out`.

## Order Files

A normal order file has:

```text
#atlantis <faction> [password]
unit <number>
...
#end
```

The file is not transactional. Parser errors do not automatically roll back already applied immediate state changes.

## Comments And Quoted Strings

`;` starts a comment to end of line.

Double quotes read a multiword token as one argument. This matters for passwords, names, descriptions, and spell names.

## `#atlantis`

`#atlantis` selects the faction and optionally validates a password.

NPC factions and city guard are not processed through this normal player path.

## `unit`

`unit <number>` selects the active unit context.

Many faction-level administrative orders are still syntactically submitted inside a selected `unit` block.

## `FORM`

`FORM` creates a unit immediately and temporarily moves parser context into that new unit until `END`.

## Templates

Lines starting with `@` are executed as orders and also saved into future order templates.

Template modes include:

- `off`
- `short`
- `long`
- `map`

Template regions do not necessarily match all monthly report regions, especially when remote visibility is involved.

## `SHOW`

Supported forms:

- `SHOW SKILL <skill> <level>`
- `SHOW ITEM <item>`

The server processes up to `101` SHOW-like requests. The `102nd` produces `Too many SHOW orders.`, and later ones are ignored.

## Report Structure

A normal report includes:

- faction heading and options;
- events and errors;
- battles;
- economy and faction status;
- region reports;
- object and unit lines;
- optional order template.

Reports are visibility-filtered.

## Region Reports

Region reports can include:

- terrain and settlement text;
- weather;
- wages;
- market;
- products;
- exits;
- visible gates;
- objects;
- visible units.

Advanced items and products can be hidden unless the faction has relevant local capability.

## Battle Reports

Battle reports include sides, participating units, round events, combat spells, losses, spoils, and outcome.

They use battle-visible unit summaries rather than ordinary monthly unit reports.

## Parser Catalog

The parser recognizes service lines, faction-level commands, immediate unit-state commands, queued early-phase commands, monthly orders, and magic orders.

The full Russian reference remains the detailed source for every parser branch; this English edition records the publication-level canonical behavior.
