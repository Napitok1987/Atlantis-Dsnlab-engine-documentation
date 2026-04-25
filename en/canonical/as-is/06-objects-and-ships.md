# Objects And Ships

## Status

Mechanically complete.

## Purpose

This document describes objects, buildings, ships, ownership, entry, promotion, construction, and destruction.

## Objects

Objects are containers or structures inside regions.

They include:

- buildings;
- ships;
- shafts;
- lairs;
- dummy internal locations.

Objects can hold units and can affect movement, ownership, protection, visibility, and transport.

## Object Ownership

Object ownership is determined by unit ordering inside the object.

The effective owner is normally the first eligible unit in the object's unit list.

`PROMOTE` can move a unit to the front of the object list and therefore change effective ownership.

## Entry

`ENTER` checks whether a unit can enter an object.

The important attitude rule is asymmetric:

- entry depends on the owner's effective attitude toward the entering unit;
- it is not enough that the entering unit considers the owner friendly.

For occupied objects, ordinary `MOVE 1` can be refused while `ADVANCE 1` can trigger battle-before-entry behavior.

## Closed Objects

Some objects are closed to normal player units.

This can block ordinary entry while still allowing special server-side or object-specific behavior.

## Ships

Ships are objects used for sea movement.

They interact with:

- `SAIL`;
- carrying capacity;
- ship construction;
- ownership;
- ocean movement;
- leaving ships in ocean regions.

## Construction

`BUILD` can create unfinished structures immediately during parsing and then set a monthly build order.

This means later orders in the same file can see the new object context.

## Destruction

`DESTROY` allows eligible owners to destroy modifiable structures.

When an object is destroyed, units inside it are moved back to the outer region container. Ships at sea have additional restrictions.

## Naming Settlements

`NAME VILLAGE`, `NAME TOWN`, and `NAME CITY` use minimum building-tier checks in code.

The implementation accepts larger qualifying buildings, not only the exact building listed in older rules.
