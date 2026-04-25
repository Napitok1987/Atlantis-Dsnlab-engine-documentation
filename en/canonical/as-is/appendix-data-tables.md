# Appendix: Data Tables

## Status

Mechanically complete.

## Purpose

This appendix collects compact reference tables for the English publication edition.

The Russian corpus contains the full detailed data notes. This English appendix records the key canonical values and interpretation rules used by the `as-is` layer.

## Starting Money

| Value | Meaning |
|---|---|
| `5020 + 50 * TurnNumber()` | New faction unclaimed silver |

## Test Fixture

| Value | Meaning |
|---|---|
| `32x32` | Real generated `new` world snapshot used by runtime tests |
| `21` | Current mechanics regression test count |

## Important Commands

| Command | Canonical note |
|---|---|
| `FIND` | Accepted but mechanically disabled |
| `ROUTE` | DSNlab composite macro-order |
| `GIVE <target> ALL <item>` | DSNlab transfer form |
| `CONSUME NONE` | Accepted consume reset |
| `REVEAL NONE` | Accepted reveal reset |
| `NOSPOILS <flag>` | Legacy but still parsed |

## Important Report Markers

| Marker | Meaning |
|---|---|
| `*` | Own unit |
| `-` | Visible foreign unit |
| `+` | Object |
| `;` | Comment line in template or order file |
| `@` | Execute order and preserve it in next template |

## Known Code-Confirmed Deviations

| Area | Canonical behavior |
|---|---|
| `Mind Reading` | Full unit report at level `4+` |
| `Force Shield` | Personal defensive bonus remains meaningful; army-wide shield behavior is not effective as old text implies |
| `Clear Skies` | Economy effect applies in the same turn |
| `Construct Gate` | Silver is spent only on success |
| `Gate 0` | Can exist internally but is broken in several report and spell paths |
| Starting cities | Protected by strong guards, not by a separate absolute safe-region flag |

## Related Documents

- [00-overview.md](00-overview.md)
- [01-turn-processing.md](01-turn-processing.md)
- [11-magic.md](11-magic.md)
- [appendix-server-specific-deviations.md](appendix-server-specific-deviations.md)

## Full Reference Tables

- [../reference/skills.md](../reference/skills.md)
- [../reference/items.md](../reference/items.md)
- [../reference/spells.md](../reference/spells.md)
