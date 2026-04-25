# Regions And Terrain

## Status

Mechanically complete.

## Purpose

This document describes regions, terrain, settlements, gates, exits, Nexus, and starting cities.

## Regions

A region is the basic map cell.

It stores:

- coordinates and level;
- terrain;
- exits to neighboring regions;
- settlement data;
- population and economy;
- objects and units;
- gate data;
- weather and other state.

## Terrain

Terrain affects:

- movement;
- economy;
- products;
- population;
- settlement generation;
- monster behavior;
- report wording.

Terrain is a mechanical property, not only descriptive text.

## Exits

Regions connect through directional exits.

Movement orders use these exits. Missing or invalid exits prevent movement.

## Nexus

Nexus is the special starting hub.

It connects to starting cities and is protected by guard logic rather than by a separate absolute safe-region flag.

## Starting Cities

Some surface regions are transformed into starting cities.

Starting cities:

- connect to Nexus;
- receive special population and market setup;
- receive gates;
- receive strong city guards;
- are detected by code through current conditions such as `town->pop == 5000`, not by a permanent origin flag.

## Safe-Region Behavior

In this DSNlab version there is no separate hard-safe region immunity for Nexus or starting cities.

Their protection comes from:

- city guards;
- `GUARD` / `FORBID` logic;
- guard participation in relevant battles;
- very strong guard equipment and skills.

## Gates

Gates are numbered world links used by gate-related magic.

Important deviation:

- one gate can receive number `0`;
- several report and spell paths treat `gate 0` as false or nonexistent;
- this creates a partial `gate 0` bug that is canonical because it follows code.

## Reports

Region reports show only information visible to the faction.

Reports can include:

- terrain and settlement text;
- weather;
- exits;
- wages;
- markets;
- products;
- gates, if visible;
- objects and units.

Report visibility is not the same as full internal state.
