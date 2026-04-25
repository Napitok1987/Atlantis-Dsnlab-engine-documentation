# Coverage Status

## Status

Mechanically complete.

## Purpose

This document records the state of the canonical Atlantis DSNlab corpus:

- which areas are covered at the `as-is` level;
- which disputed points are confirmed by code;
- which areas remain outside the mechanical core.

## Current Conclusion

The canonical `as-is` corpus is functionally complete.

This means:

- there are no known unresolved high-priority conflicts;
- there are no known unresolved medium-priority conflicts;
- the basic executable layer for mechanics and persistence is covered by regression tests;
- the remaining tail consists of secondary texts and built-in help defects that do not change the current canon.

## Test Status

The historical code used as the baseline is published in:

- [Labutin/DSNAtlantis](https://github.com/Labutin/DSNAtlantis)

The `as-is` layer keeps one verification layer:

- executable mechanics tests against a prebuilt `standard` binary using real `orders.<faction>` files.

Recorded state:

- `21` regression tests;
- last full run: `OK`;
- world generation is not repeated in every test; tests use a fixture created from a real `32x32` `new` world.

## Coverage By Layer

### Turn Pipeline And Orders Interface

Covered and aligned with code:

- orders parsing and service-level behavior;
- non-transactional order files;
- immediate state changes;
- report interface limits;
- legacy and extended parser forms.

Also confirmed by executable tests:

- new faction creation from a fixture snapshot;
- turn advancement, persistence, and unit age increase.

Main documents:

- [01-turn-processing.md](as-is/01-turn-processing.md)
- [12-reports-and-files.md](as-is/12-reports-and-files.md)

### Economy, Factions And Units

Covered and aligned with code:

- starting money;
- faction and mage limits;
- maintenance;
- taxation, pillage, and `AUTOTAX` nuances;
- basic unit and faction contracts.

Main documents:

- [02-factions-and-units.md](as-is/02-factions-and-units.md)
- [07-economy.md](as-is/07-economy.md)

### Regions, Objects, Movement And World Generation

Covered and aligned with code:

- terrain and settlements;
- ships and objects;
- `MOVE`, `ADVANCE`, `FORBID`, and `GUARD`;
- gates and the `gate 0` edge case;
- starting cities, guards, NPCs, and world generation.

Also confirmed by executable tests:

- movement from Nexus to a neighboring region;
- ocean-entry blocking for non-swimming units;
- route-based object entry by numeric id through `move north 1`;
- neutral-object refusal for ordinary `MOVE 1`;
- battle-before-entry behavior for `ADVANCE 1`;
- `GUARD` runtime error for a unit that is not combat-ready;
- controlled `MOVE` vs `ADVANCE` scenario against guard-based forbid;
- ally-sensitive `ADVANCE`.

Main documents:

- [05-regions-and-terrain.md](as-is/05-regions-and-terrain.md)
- [06-objects-and-ships.md](as-is/06-objects-and-ships.md)
- [08-movement.md](as-is/08-movement.md)
- [13-world-and-npc.md](as-is/13-world-and-npc.md)

### Visibility, Reports, Combat And Magic

Covered and aligned with code:

- visibility and reveal state;
- `Mind Reading` and report thresholds;
- battle report formatting;
- `NOAID` group behavior;
- battle-item and combat-spell contracts;
- `Force Shield`, `Clear Skies`, `Engrave Runes`, and `Construct Gate`.

Also confirmed by executable tests:

- city guards do not auto-join normal regional `ADVANCE`, but do join object-entry battle inside a city;
- real `Spoils: ... silver [SILV].` lines;
- `study force` makes the leader a mage and increases faction-level `Mages`;
- `Force Shield`, `Fire`, `Clear Skies`, and `Summon Storm` runtime spell paths.

Main documents:

- [09-visibility-and-diplomacy.md](as-is/09-visibility-and-diplomacy.md)
- [10-combat.md](as-is/10-combat.md)
- [11-magic.md](as-is/11-magic.md)
- [12-reports-and-files.md](as-is/12-reports-and-files.md)

## Canonical Server Deviations

Major differences between code, rules, and built-in help are indexed in:

- [appendix-server-specific-deviations.md](as-is/appendix-server-specific-deviations.md)

The appendix has two roles:

- show where canon intentionally follows code rather than old text;
- bridge the frozen `as-is` layer and the next normalized specification.

## Outside The Frozen As-Is Scope

The remaining low-risk tail does not change the canon:

- secondary textual materials;
- pure built-in help text defects that do not affect mechanics.

The mechanics-only executable tests intentionally exclude:

- source-contract documentation checks;
- publication checks;
- CLI and file-contract checks;
- report-format and `template`-only edge cases;
- heavier `combat/magic` integration scenarios beyond the already covered spell paths.

## Next Product Step

The next rational stage is:

1. treat `as-is` as mechanically closed;
2. use `appendix-server-specific-deviations.md` as the transition index;
3. start building the normalized `to-be` layer without repeating a full source audit.
