# Atlantis As-Is Tests

## Purpose

This directory contains a lightweight regression test set for `as-is` game mechanics.

Historical source code baseline:

- [Labutin/DSNAtlantis](https://github.com/Labutin/DSNAtlantis)

The current test layer has one executable level:

- `test_runtime_server.py` runs a built `standard` binary through scenarios that change game state.

## Run

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Covered Areas

- new faction start and turn advancement;
- persistence across turns;
- movement, object entry, `MOVE`, `ADVANCE`, `GUARD`, and `FORBID`;
- object-entry battle and city guard behavior;
- battle spoils;
- basic magic paths for `Force Shield`, `Fire`, `Clear Skies`, and `Summon Storm`.

## Test Map

| Test | What it verifies |
|---|---|
| `test_run_can_process_a_real_new_game_snapshot_with_new_player` | the server accepts a real `new` world snapshot, creates a new faction, and writes the first report |
| `test_second_turn_persistence_overwrites_game_and_report_outputs` | the second turn uses `game.out` / `players.out` as the next inputs and persists state |
| `test_studying_force_turns_leader_into_mage_and_unlocks_magic_branch` | `study force` turns the leader into a mage and increases the faction-level `Mages` counter |
| `test_quoted_multiword_magic_skill_names_work_in_study_and_combat` | quoted multiword spell names work in study and combat orders |
| `test_clear_skies_cast_order_emits_runtime_event` | `cast CLEA` executes as a normal magic runtime event |
| `test_move_from_nexus_updates_region` | ordinary movement out of Nexus changes the unit region |
| `test_move_into_ocean_is_blocked_before_entry` | a non-swimming unit cannot enter ocean with ordinary `MOVE` |
| `test_route_move_can_enter_object_by_numeric_id` | `move north 1` enters an object by numeric id |
| `test_guard_requires_combat_ready_unit_at_runtime` | `GUARD` requires combat readiness at runtime |
| `test_move_is_blocked_by_guard_based_forbid` | a guarding unit's `FORBID` blocks ordinary `MOVE` |
| `test_advance_enters_guarded_region_and_triggers_battle` | `ADVANCE` enters a guarded region through battle |
| `test_region_advance_battle_reports_silver_spoils` | regional `ADVANCE` battle reports silver spoils |
| `test_advance_is_blocked_by_attackers_one_way_ally_attitude` | one-way attacker `Ally` attitude blocks breakthrough before entry |
| `test_move_is_refused_by_neutral_object_owner` | ordinary `MOVE 1` into an occupied object is refused by the owner |
| `test_advance_against_neutral_object_owner_triggers_battle_before_entry` | `ADVANCE 1` into an occupied object triggers battle before entry |
| `test_object_entry_battle_reports_silver_spoils` | object-entry battle reports silver spoils |
| `test_city_guard_joins_object_entry_battle_but_not_region_advance_battle` | city guard does not join ordinary regional `ADVANCE`, but joins object-entry battle |
| `test_force_shield_combat_spell_is_cast_in_runtime_battle` | `Force Shield` is actually cast in battle |
| `test_fire_combat_spell_emits_fireball_line_in_battle_log` | `FIRE` writes `shoots a Fireball` to the battle log |
| `test_clear_skies_combat_spell_is_cast_in_runtime_battle` | `Clear Skies` is actually cast as a combat spell |
| `test_summon_storm_combat_spell_emits_debuff_line_in_battle_log` | `Summon Storm` writes its debuff effect to the battle log |

## Notes

- By default the tests look for `../DSNAtlantis-src/standard/standard`.
- Another binary can be selected through `ATLANTIS_STANDARD_BINARY`.
- The tests use a real `32x32` `new` world fixture instead of regenerating the world for every case.
- Two-turn scenarios use real `orders.<faction>` files and validate persistence between turns.
- The test set intentionally excludes documentation source-contract checks, publication checks, and report-template-only checks.
