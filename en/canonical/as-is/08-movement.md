# Movement

## Status

Mechanically complete.

## Purpose

This document describes movement, advance, sailing, route handling, guards, and forbids.

## Movement Orders

Main movement-related commands:

- `MOVE`
- `ADVANCE`
- `SAIL`
- `ROUTE`

Movement is a monthly action unless created as part of a composite command such as `ROUTE`.

## `MOVE`

`MOVE` attempts ordinary movement through region exits or into objects.

It can be blocked by:

- invalid direction;
- terrain restrictions;
- ocean movement limits;
- object refusal;
- guard-based forbid.

## `ADVANCE`

`ADVANCE` is movement with attack intent.

It can:

- enter guarded regions by fighting;
- trigger battle before object entry;
- be stopped before entry if the attacker is defeated, routed, or blocked by attitude logic.

## Object Entry By Route

The server supports entering an object by numeric id in a route-like movement form, for example:

```text
move north 1
```

This is covered by executable tests.

## `SAIL`

`SAIL` moves ships and their contents.

It depends on:

- ship ownership;
- sailing capability;
- exits and ocean regions;
- carrying constraints.

## Guards And Forbid

`GUARD` and `FORBID` interact with movement.

Important canonical behavior:

- a unit must be combat-ready to remain on active guard;
- `GUARD` can fail at runtime for a non-combat-ready unit;
- guard-based forbid can block ordinary `MOVE`;
- `ADVANCE` can challenge forbid through combat;
- city guards have special behavior in cities and starting areas.

## Ally-Sensitive `ADVANCE`

`ADVANCE` is sensitive to attitudes.

An attacker's one-way `Ally` attitude can stop a breakthrough before entry in tested scenarios.

## Persistence

Movement changes region and object location and is persisted into the next saved game state.
