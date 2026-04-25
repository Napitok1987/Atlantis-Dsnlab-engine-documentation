# Тесты Atlantis As-Is

## Назначение

Этот каталог содержит лёгкий набор регрессионных тестов для проверки игровых механик `as-is`.

Исторический код оригинального сервера находится в исходном репозитории:

- [Labutin/DSNAtlantis](https://github.com/Labutin/DSNAtlantis)

Сейчас набор тестов состоит из одного исполняемого уровня:

- `test_runtime_server.py` проверяет собранный `standard` из исходного кода через исполняемые сценарии, где меняется состояние игры.

## Запуск

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Что покрыто

- старт новой фракции и переход хода;
- сохранение состояния между ходами;
- движение, вход в объекты, `MOVE` / `ADVANCE` / `GUARD` / `FORBID`;
- вход в объект через бой и поведение городской стражи;
- spoils в бою;
- базовые магические ветки `Force Shield`, `Fire`, `Clear Skies`, `Summon Storm`.

## Карта тестов

| Тест | Что проверяет |
|---|---|
| `test_run_can_process_a_real_new_game_snapshot_with_new_player` | сервер принимает реальный снимок `new`-мира, создаёт новую фракцию и пишет первый отчёт |
| `test_second_turn_persistence_overwrites_game_and_report_outputs` | второй ход использует `game.out` / `players.out` как новые входы и сохраняет состояние |
| `test_studying_force_turns_leader_into_mage_and_unlocks_magic_branch` | `study force` делает лидера магом и увеличивает фракционный счётчик `Mages` |
| `test_quoted_multiword_magic_skill_names_work_in_study_and_combat` | названия заклинаний из нескольких слов работают в кавычках |
| `test_clear_skies_cast_order_emits_runtime_event` | `cast CLEA` исполняется как событие обычной магии |
| `test_move_from_nexus_updates_region` | обычный выход из Nexus меняет регион отряда |
| `test_move_into_ocean_is_blocked_before_entry` | не-плавающий отряд не входит в океан обычным `MOVE` |
| `test_route_move_can_enter_object_by_numeric_id` | `move north 1` входит в объект по числовому id |
| `test_guard_requires_combat_ready_unit_at_runtime` | `GUARD` требует боеготовности при исполнении |
| `test_move_is_blocked_by_guard_based_forbid` | `FORBID` охраняющего отряда блокирует обычный `MOVE` |
| `test_advance_enters_guarded_region_and_triggers_battle` | `ADVANCE` входит в охраняемый регион через бой |
| `test_region_advance_battle_reports_silver_spoils` | региональный бой через `ADVANCE` пишет трофеи серебра |
| `test_advance_is_blocked_by_attackers_one_way_ally_attitude` | односторонний `Ally` у наступающего блокирует прорыв до входа |
| `test_move_is_refused_by_neutral_object_owner` | обычный `MOVE 1` в занятый объект получает отказ владельца |
| `test_advance_against_neutral_object_owner_triggers_battle_before_entry` | `ADVANCE 1` в занятый объект запускает бой до входа |
| `test_object_entry_battle_reports_silver_spoils` | бой при входе в объект пишет трофеи серебра |
| `test_city_guard_joins_object_entry_battle_but_not_region_advance_battle` | городская стража не входит в обычный региональный `ADVANCE`, но входит в бой при входе в объект |
| `test_force_shield_combat_spell_is_cast_in_runtime_battle` | `Force Shield` реально кастуется в бою |
| `test_fire_combat_spell_emits_fireball_line_in_battle_log` | `FIRE` пишет строку `shoots a Fireball` в боевом логе |
| `test_clear_skies_combat_spell_is_cast_in_runtime_battle` | `Clear Skies` реально кастуется как боевое заклинание |
| `test_summon_storm_combat_spell_emits_debuff_line_in_battle_log` | `Summon Storm` пишет боевой эффект ослабления |

## Заметки по исполняемым тестам

- набор исполняемых тестов по умолчанию ищет собранный бинарь в `../DSNAtlantis-src/standard/standard`; другой путь можно задать через `ATLANTIS_STANDARD_BINARY`;
- полноценный `run` проверяется на основе тестового снимка из реально сгенерированного `new`-мира `32x32`.
- есть отдельные двухходовые исполняемые тесты с настоящими `orders.<faction>` и проверкой сохранения состояния между ходами;
- базовый слой `movement/guard` тоже покрыт исполняемыми сценариями: выход из Nexus, блокировка входа в океан и ошибка `GUARD` при исполнении для отряда, не готового к бою.
- отдельно покрыт вход в объект по маршруту с числовым id через `move north 1`.
- отдельно покрыты варианты входа в занятый объект:
  - обычный `MOVE 1` получает `ENTER: Is refused entry.` уже на нейтральном владельце;
  - `ADVANCE 1` идёт через бой до входа и может сорваться, если атакующий обращён в бегство.
- есть контролируемый двухфракционный сценарий `MOVE` vs `ADVANCE` для запрета входа через охрану в негородском регионе.
- отдельно покрыт `ADVANCE`, учитывающий союзное отношение: односторонний `Ally` у наступающего действительно останавливает прорыв до входа.
- городская стража не автоприсоединяется к обычному региональному `ADVANCE`, но вмешивается в бой при входе в объект внутри города.
- в контролируемых боевых сценариях отдельно проверяются реальные строки `Spoils: ... silver [SILV].`.
- базовый магический путь исполнения тоже покрыт:
  - `study force` реально переводит лидерский отряд в мага и увеличивает счётчик `Mages`;
  - через `study FSHI` и `combat FSHI` подтверждён настоящий путь боевого заклинания;
  - в боевом логе печатается `casts Force Shield.`
  - названия заклинаний из нескольких слов в кавычках тоже реально работают в `study "force shield"` и `combat "force shield"`;
  - прямое атакующее боевое заклинание `FIRE` подтверждено строкой боевого лога `shoots a Fireball`.
  - цепочка погодной магии с несколькими зависимостями `force -> pattern -> WEAT -> CLEA` подтверждена и через `CAST`, и через `COMBAT`;
  - `cast CLEA` даёт событие при исполнении `Casts Clear Skies.`;
  - `combat CLEA` даёт строку боевого лога `casts Clear Skies.`
