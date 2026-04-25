# Items

## Status

Mechanically complete.

## Purpose

This document describes the item model of the original server.

## Item Categories

Items include:

- silver;
- food;
- people;
- weapons;
- armor;
- mounts;
- trade goods;
- advanced products;
- monsters;
- magical artifacts.

Each item has properties that can affect weight, combat, production, visibility, and special rules.

## Silver

Silver exists in several practical contexts:

- unclaimed faction silver;
- silver carried by units;
- population silver in regions;
- market silver;
- upkeep and wages.

Transfers between these contexts are handled by commands, economy phases, battle spoils, and maintenance.

## Food And Upkeep

Food and silver are used for maintenance.

`CONSUME` controls whether a unit prefers unit inventory, faction resources, or default behavior. DSNlab also accepts `CONSUME NONE`.

## People And Monsters

People and monsters are represented as item-like unit contents.

They affect:

- carrying capacity;
- combat readiness;
- upkeep;
- skill ownership;
- report output.

## Weapons And Armor

Weapons and armor determine combat attacks, defense, riding constraints, and battle-visible equipment.

Some items are only useful when paired with relevant skills.

## Advanced Items

Advanced items can be hidden from market and production reports unless the faction has the required recognition or local capability.

This behavior is report-facing and does not mean the item does not exist internally.

## Spoils

Battle spoils distribute captured items to surviving eligible units on the winning side.

Spoil settings affect what a unit is willing to take.

## Item Reports

`SHOW ITEM <item>` requests item description text for the next report.

Built-in item text can contain old wording or non-mechanical defects; code behavior remains canonical.
