# Turn Processing And Orders

## Status

Mechanically complete.

## Purpose

This document describes how the original server reads order files and executes a turn.

## Order File Structure

A normal order file contains:

1. `#atlantis <faction> [password]`
2. one or more `unit <number>` blocks
3. orders for the selected unit
4. `#end`

The parser keeps a current faction and a current unit context. Commands outside a valid context usually produce errors, but they do not automatically stop the whole file.

## Non-Transactional Parsing

Order parsing is not transactional.

Important consequences:

- a normal line error does not roll back already applied changes;
- immediate flags such as `GUARD`, `AVOID`, `REVEAL`, and `AUTOTAX` can already be changed before a later error;
- `UNIT` clears pending orders and execution fields for the selected unit;
- `FORM` creates a unit immediately during parsing.

## Immediate State Changes

Some commands change state while the order file is being read:

- `FORM`
- `BUILD`
- `ENTER` and `LEAVE` markers
- `GUARD`
- `AVOID`
- `BEHIND`
- `HOLD`
- `NOAID`
- `REVEAL`
- `CONSUME`
- `SPOILS` and legacy `NOSPOILS`
- `AUTOTAX`
- `PASSWORD`, `ADDRESS`, `OPTION`

These are not merely compiled into a later queue.

## Boolean Parser Values

For boolean-style commands, DSNlab accepts more than `0` and `1`.

The same parser helper is used for commands such as:

- `GUARD`
- `BEHIND`
- `NOAID`
- `HOLD`
- `AUTOTAX`
- `AVOID`

Accepted true and false forms include the usual numeric and textual forms used by the original parser.

## Queued Orders

Some commands are stored for early phases:

- `FIND`
- `PROMOTE`
- `ATTACK`
- `STEAL`
- `ASSASSINATE`
- `GIVE`
- `SELL`
- `BUY`
- `TRADE`
- `FORGET`

Monthly orders replace the unit's current month-long action:

- `MOVE`
- `ADVANCE`
- `SAIL`
- `STUDY`
- `TEACH`
- `PRODUCE`
- `BUILD`
- `WORK`
- `ENTERTAIN`

`CAST` creates either a normal magic order or a teleportation/gate/portal order, depending on spell type.

## `ROUTE`

`ROUTE` is a DSNlab composite macro-order.

During parsing it can:

- create `GIVE` orders;
- compute a route;
- assign `MOVE` or `SAIL` as the monthly order.

It is therefore neither purely immediate nor purely monthly.

## Execution Phase Order

The canonical phase order is:

1. `FIND`
2. `ENTER` / `LEAVE`
3. `PROMOTE`
4. combat orders and automatic attacks
5. `STEAL` / `ASSASSINATE`
6. `GIVE`, `PAY`, and transfer
7. `DESTROY`
8. `PILLAGE`
9. `TAX`
10. `SELL`, `BUY`, and local `TRADE`
11. magic
12. movement, advance, and sailing
13. production, work, entertain, study, teach, and build
14. upkeep and post-turn world updates
15. report and save-file generation

The exact placement matters because earlier phases can change ownership, location, inventory, visibility, and combat eligibility before later phases run.

## DSNlab Extensions

The parser accepts several DSNlab-specific or legacy forms:

- `CONSUME NONE`
- `REVEAL NONE`
- `NOSPOILS <flag>`
- `ROUTE`
- `GIVE <target> ALL <item>`

These forms are canonical because they are accepted by the original server.
