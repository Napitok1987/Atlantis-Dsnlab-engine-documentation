# World Generation And NPC

## Status

Mechanically complete.

## Purpose

This document describes world generation, Nexus, starting cities, gates, shafts, NPC factions, city guards, and monsters.

## World Generation

World generation creates:

- map levels;
- terrain;
- settlements;
- exits;
- Nexus;
- starting cities;
- gates;
- shafts;
- NPC factions;
- guards and monsters.

## Nexus

Nexus is created as the starting hub and connected to surface starting cities.

It is protected by city guard logic rather than by a separate absolute safe-region flag.

## Starting Cities

Starting cities are selected surface regions connected to Nexus.

They receive:

- population `5000`;
- special market setup;
- gates;
- strong guards.

The server recognizes starting-city status by current conditions such as `town->pop == 5000`, not by a permanent origin flag.

## Markets

Starting cities have a special starting-store-like market.

They sell most normal items in effectively unlimited quantity, except silver and food, and support key starting purchases.

## Gates

Gates are placed in starting cities and selected regions.

After gate placeholders are placed, gates receive random unique numbers. One gate can effectively become `0`, creating the canonical `gate 0` issue.

## Shafts

Shafts connect underground and surface regions through paired objects.

Generation skips invalid ocean cases.

## NPC Factions

Two important NPC factions are created:

1. `The Guardsmen`
2. `Creatures`

The first is used for city guards. The second is used for wandering monsters and lair monsters.

## City Guards

City guards are normal server-side units:

- faction: `The Guardsmen`;
- type: `U_GUARD`;
- guard state: `GUARD_GUARD`;
- holding state;
- generated money and equipment.

Nexus and starting-city guards use a special stronger setup with high effective skill, mithril swords, amulets of invulnerability, high observation, and `BEHIND`.

## Guard Restoration

After the turn, `AdjustCityMons` restores or creates city guard groups.

Important behavior:

- if any `U_GUARD` is present, the server adjusts that unit and stops processing that region;
- only if no city guard unit and no active regional guard exists can a new guard group be regenerated.

## Guarded Regions

A region is guarded if it has at least one unit with `guard == GUARD_GUARD`.

This is a runtime condition, not a stored protected-region flag.

## Monsters

The creature faction controls:

- wandering monsters;
- lair monsters.

Monster movement and monster creation/refill use different guarded-region checks, so they do not have identical behavior.
