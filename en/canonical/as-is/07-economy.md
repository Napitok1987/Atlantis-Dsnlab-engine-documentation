# Economy

## Status

Mechanically complete.

## Purpose

This document describes the original economic model: silver, population, markets, production, taxation, pillage, work, entertainment, and upkeep.

## Silver Flows

Silver exists as:

- faction unclaimed silver;
- unit-carried silver;
- population silver;
- market money;
- spoils;
- upkeep and wages.

Commands and turn phases move silver between these contexts.

## Starting Money

New faction starting money is code-confirmed as:

- `5020 + 50 * TurnNumber()`

This differs from older text that describes a fixed `5000`.

## Markets

Markets support:

- regional buying and selling;
- local `TRADE`;
- population-driven economy;
- starting-city special market setup.

Advanced market visibility can depend on whether the faction has relevant local items or capability.

## Local `TRADE`

Local `TRADE` is not a perfectly clean best-price auction.

The code searches for price extremes, but list handling means partial trades can be sensitive to order traversal. This server behavior is canonical.

## Production

Production depends on:

- region products;
- terrain;
- skills;
- tools and items;
- available targets;
- unit monthly orders.

Advanced products may be hidden from reports until the faction has an eligible local unit.

## Taxation

Taxation depends on:

- unit combat readiness;
- region economy;
- guards and limits;
- `AUTOTAX`.

`AUTOTAX` is not strictly permanent. The server can clear it when the unit is no longer capable of taxing.

## Pillage

`PILLAGE` is processed as a separate economic/combat-adjacent action.

It depends on unit eligibility and regional constraints.

## Work And Entertainment

`WORK` and `ENTERTAIN` are monthly orders that produce silver through different mechanics.

Entertainment availability is reported separately from ordinary products.

## Upkeep

Upkeep consumes silver and food according to unit state and consume settings.

Failure to maintain units can affect unit composition and survival.
