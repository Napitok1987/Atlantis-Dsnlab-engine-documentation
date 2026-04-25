# Appendix Data Tables

## Статус

Заморожено (механически завершено)

## Назначение

Этот appendix не дублирует весь канонический корпус, а собирает быстрый индекс по главным таблицам данных оригинальной игры.

Если сущность уже полностью раскрыта в профильном документе, здесь остаётся:

- краткая сводка;
- список ключевых чисел;
- указание, где именно в каноническом комплекте лежит полное описание.

## Индекс Канонических Таблиц

### Skills

Основной документ:

- [03-skills.md](03-skills.md)

Связанные документы:

- [10-combat.md](10-combat.md)
- [11-magic.md](11-magic.md)

### Items

Основной документ:

- [04-items.md](04-items.md)

Связанные документы:

- [07-economy.md](07-economy.md)
- [10-combat.md](10-combat.md)
- [11-magic.md](11-magic.md)

### Terrain

Основной документ:

- [05-regions-and-terrain.md](05-regions-and-terrain.md)

Связанные документы:

- [08-movement.md](08-movement.md)
- [13-world-and-npc.md](13-world-and-npc.md)

### Objects и Ships

Основной документ:

- [06-objects-and-ships.md](06-objects-and-ships.md)

Связанные документы:

- [08-movement.md](08-movement.md)
- [10-combat.md](10-combat.md)
- [13-world-and-npc.md](13-world-and-npc.md)

### Reports и File Interface

Основной документ:

- [12-reports-and-files.md](12-reports-and-files.md)

## Game Constants

## Core Economy and Turn Constants

| Константа | Значение |
| --- | --- |
| `START_MONEY` | `5020` |
| стартовый безнал новой фракции | `5020 + 50 * TurnNumber()` |
| `WORK_FRACTION` | `5` |
| `ENTERTAIN_FRACTION` | `20` |
| `ENTERTAIN_INCOME` | `20` |
| `TAX_INCOME` | `50` |
| `TIMES_REWARD` | `50` |
| `MAINTENANCE_COST` | `10` |
| `LEADER_COST` | `20` |
| `STARVE_PERCENT` | `33` |
| `HEALS_PER_MAN` | `5` |

Полное поведение этих чисел описано в:

- [01-turn-processing.md](01-turn-processing.md)
- [07-economy.md](07-economy.md)

## Movement Constants

| Константа | Значение |
| --- | --- |
| `FOOT_SPEED` | `2` |
| `HORSE_SPEED` | `4` |
| `SHIP_SPEED` | `4` |
| `FLY_SPEED` | `6` |
| `MAX_SPEED` | `8` |
| `WAGON_CAPACITY` | `250` |

Полное применение:

- [08-movement.md](08-movement.md)

## Faction Limits

| Константа | Значение |
| --- | --- |
| `FACTION_POINTS` | `5` |
| `FACTION_LIMIT_TYPE` | `Faction Types` |

При `Faction Types` лимиты зависят от распределения War/Trade/Magic points.

Подробности:

- [02-factions-and-units.md](02-factions-and-units.md)

## NPC and World Constants

| Константа | Значение |
| --- | --- |
| `GUARD_REGEN` | `20%` |
| `CITY_GUARD` | `40` |
| `GUARD_MONEY` | `50` |
| `CITY_POP` | `4000` |
| `WMON_FREQUENCY` | `10` |
| `LAIR_FREQUENCY` | `10` |
| `MAX_AC_X` | `64` |
| `MAX_AC_Y` | `64` |

Подробности:

- [13-world-and-npc.md](13-world-and-npc.md)

## Magic Tables

## Passive Magic Summary

| Навык | Тип действия | Ключевой эффект |
| --- | --- | --- |
| `Summon Wind` | passive | бонус к ship/flying movement |
| `True Seeing` | passive | bonus к observation и распознавание иллюзий |
| `Mind Reading 3+` | passive | auto faction detection для видимых units |
| `Magical Healing` | passive | post-battle healing без herbs |
| `Phantasmal Entertainment` | passive | `Entertainment = 5 * level` |

Полное описание:

- [11-magic.md](11-magic.md)

## Combat Magic Summary

| Навык | Тип | Краткий эффект |
| --- | --- | --- |
| `Fire` | attack | energy spell attack |
| `Earthquake` | attack | бьёт только по units в buildings |
| `Force Shield` | defense | personal defensive bonus caster'а, а не полноценный army shield |
| `Energy Shield` | shield | army shield против energy attacks |
| `Spirit Shield` | shield | army shield против spirit attacks |
| `Summon Storm` | debuff | снижает `Combat` на `2` |
| `Summon Tornado` | attack | weather attack |
| `Call Lightning` | attack | weather + energy strike |
| `Clear Skies` | shield | weather shield в бою |
| `Create Aura of Fear` | debuff | снижает `Combat` на `2`, не действует на monsters |
| `Summon Black Wind` | attack | spirit damage, не бьёт undead/demons |
| `Banish Undead` | attack | действует только на undead family |
| `Banish Demons` | attack | действует только на demon family |
| `Dispel Illusions` | attack | уничтожает только иллюзии |

Полное описание:

- [10-combat.md](10-combat.md)
- [11-magic.md](11-magic.md)

## Artifact Creation Summary

| Spell | Cost | Выпуск |
| --- | --- | --- |
| `Construct_Portal` | `600` | chance-based |
| `Create_Ring_of_Invisibility` | `600` | chance-based |
| `Create_Cloak_of_Invulnerability` | `800` | chance-based |
| `Create_Staff_of_Fire` | `600` | chance-based |
| `Create_Staff_of_Lightning` | `1000` | chance-based |
| `Create_Amulet_of_True_Seeing` | `600` | chance-based |
| `Create_Runesword` | `800` | chance-based |
| `Create_Amulet_of_Protection` | `200` | `level` штук |
| `Create_Shieldstone` | `200` | `level` штук |
| `Create_Magic_Carpet` | `400` | `level` штук |

Полное описание:

- [11-magic.md](11-magic.md)

## World Tables

## Level Layout

| Уровень | Размер | Назначение |
| --- | --- | --- |
| `Nexus` | `1 x 1` | стартовый центральный уровень |
| `surface` | вводится при генерации | основной внешний мир |
| `underworld` | `surface / 2` по каждой оси | подземный мир |

## Standard World Generation Parameters

| Параметр | Значение |
| --- | --- |
| Surface ocean target | `40%` |
| Surface continent size seed | `10` |
| Shaft chance | `1/8` на underworld region |
| Initial wandering fill | `50%` |
| Initial lair fill | `50%` |

Полное описание:

- [13-world-and-npc.md](13-world-and-npc.md)

## Terrain Families by Level

| Уровень | Terrain |
| --- | --- |
| `surface` | `ocean`, `plain`, `forest`, `mountain`, `swamp`, `jungle`, `desert`, `tundra` |
| `underworld` | `ocean`, `cavern`, `underforest`, `tunnels` |
| `nexus` | `nexus` |

## NPC Spawn Model Summary

| Система | Initial Setup | Monthly Refill |
| --- | --- | --- |
| City Guards | `CreateCityMons()` | `AdjustCityMons()` |
| Wandering Monsters | `GrowWMons(50)` | `GrowWMons(10)` |
| Lair Monsters | `GrowLMons(50)` | `GrowLMons(10)` |

## Reporting Markers

| Маркер | Значение |
| --- | --- |
| `*` | собственный unit |
| `-` | чужой видимый unit |
| `+` | object line |
| `;` | comment line в template/report |
| `@` | сохранить строку orders в следующий template |

Полное описание:

- [12-reports-and-files.md](12-reports-and-files.md)

## Appendix Policy

Если в будущем понадобится "полная машинная таблица" по skills, items, monsters или terrain, её лучше добавлять сюда отдельными секциями, не раздувая основные narrative-документы.

Но на текущем этапе канонический комплект уже распределяет полные поведенческие описания по профильным документам, а этот appendix служит для быстрой навигации и сверки ключевых чисел.
