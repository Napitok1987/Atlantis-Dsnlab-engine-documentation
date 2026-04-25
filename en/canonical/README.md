# Canonical Documentation

This directory contains the English canonical documentation for Atlantis DSNlab.

The historical source code of the original server is used as the verification baseline:

- [Labutin/DSNAtlantis](https://github.com/Labutin/DSNAtlantis)

Rules for `as-is` documents:

- `as-is` documents must be readable without external context;
- they must not include design decisions for the future rewrite;
- they describe only the behavior of the original game;
- disputed behavior becomes canonical only after source-level verification;
- when sources disagree, the behavior confirmed by code is canonical.

Current status:

- the `as-is` document set is filled for all major systems;
- all `as-is` documents are frozen as `Mechanically complete`;
- no open high-priority or medium-priority conflicts are known;
- a mechanics-only executable regression test layer exists;
- further work should be outside the frozen `as-is` layer: publication and the normalized `to-be` layer.

Structure:

- `as-is/` - canonical description of the original game.
- `reference/` - full source-backed reference tables.

Key `as-is` documents:

- [00-overview.md](as-is/00-overview.md)
- [01-turn-processing.md](as-is/01-turn-processing.md)
- [02-factions-and-units.md](as-is/02-factions-and-units.md)
- [03-skills.md](as-is/03-skills.md)
- [04-items.md](as-is/04-items.md)
- [05-regions-and-terrain.md](as-is/05-regions-and-terrain.md)
- [06-objects-and-ships.md](as-is/06-objects-and-ships.md)
- [07-economy.md](as-is/07-economy.md)
- [08-movement.md](as-is/08-movement.md)
- [09-visibility-and-diplomacy.md](as-is/09-visibility-and-diplomacy.md)
- [10-combat.md](as-is/10-combat.md)
- [11-magic.md](as-is/11-magic.md)
- [12-reports-and-files.md](as-is/12-reports-and-files.md)
- [13-world-and-npc.md](as-is/13-world-and-npc.md)
- [appendix-data-tables.md](as-is/appendix-data-tables.md)
- [appendix-server-specific-deviations.md](as-is/appendix-server-specific-deviations.md)

Reference tables:

- [reference/README.md](reference/README.md)
- [reference/skills.md](reference/skills.md)
- [reference/items.md](reference/items.md)
- [reference/spells.md](reference/spells.md)
