# Справочник магии и заклинаний

## Статус

Заморожено (механически завершено)

## Источник

Магические записи `SkillDefs` из `DSNAtlantis-src/standard/rules.cpp`; обработка активных заклинаний сверяется с `DSNAtlantis-src/standard/spells.cpp`.

Всего магических навыков и spell-like записей: `59`.

Не каждая запись является активным `CAST`: foundation и passive навыки тоже входят в магическое дерево.

| # | Enum | Название | Код | Класс | Special | Зависимости |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | `S_FORCE` | force | `FORC` | foundation | `0` | - |
| 1 | `S_PATTERN` | pattern | `PATT` | foundation | `0` | - |
| 2 | `S_SPIRIT` | spirit | `SPIR` | foundation | `0` | - |
| 3 | `S_FIRE` | fire | `FIRE` | combat | `SPECIAL_FIREBALL` | force 1+ |
| 4 | `S_EARTHQUAKE` | earthquake | `EQUA` | combat | `SPECIAL_EARTHQUAKE` | force 1+; pattern 1+ |
| 5 | `S_FORCE_SHIELD` | force shield | `FSHI` | combat | `SPECIAL_FORCE_SHIELD` | force 1+ |
| 6 | `S_ENERGY_SHIELD` | energy shield | `ESHI` | combat | `SPECIAL_ENERGY_SHIELD` | force 1+ |
| 7 | `S_SPIRIT_SHIELD` | spirit shield | `SSHI` | combat | `SPECIAL_SPIRIT_SHIELD` | spirit 1+; force 1+ |
| 8 | `S_MAGICAL_HEALING` | magical healing | `MHEA` | passive | `0` | pattern 1+ |
| 9 | `S_GATE_LORE` | gate lore | `GATE` | cast | `0` | pattern 1+; spirit 1+ |
| 10 | `S_FARSIGHT` | farsight | `FARS` | cast | `0` | pattern 1+; spirit 1+ |
| 11 | `S_TELEPORTATION` | teleportation | `TELE` | cast | `0` | gate lore 1+; farsight 3+ |
| 12 | `S_PORTAL_LORE` | portal lore | `PORT` | cast | `0` | gate lore 3+; farsight 1+ |
| 13 | `S_MIND_READING` | mind reading | `MIND` | cast | `0` | pattern 1+ |
| 14 | `S_WEATHER_LORE` | weather lore | `WEAT` | passive | `0` | force 1+; pattern 1+ |
| 15 | `S_SUMMON_WIND` | summon wind | `SWIN` | passive | `0` | weather lore 1+ |
| 16 | `S_SUMMON_STORM` | summon storm | `SSTO` | combat | `SPECIAL_SUMMON_STORM` | weather lore 1+ |
| 17 | `S_SUMMON_TORNADO` | summon tornado | `STOR` | combat | `SPECIAL_TORNADO` | weather lore 3+ |
| 18 | `S_CALL_LIGHTNING` | call lightning | `CALL` | combat | `SPECIAL_LSTRIKE` | weather lore 5+ |
| 19 | `S_CLEAR_SKIES` | clear skies | `CLEA` | combat + cast | `SPECIAL_CLEAR_SKIES` | weather lore 1+ |
| 20 | `S_EARTH_LORE` | earth lore | `EART` | cast | `0` | pattern 1+ |
| 21 | `S_WOLF_LORE` | wolf lore | `WOLF` | cast | `0` | earth lore 1+ |
| 22 | `S_BIRD_LORE` | bird lore | `BIRD` | cast | `0` | earth lore 1+ |
| 23 | `S_DRAGON_LORE` | dragon lore | `DRAG` | cast | `0` | bird lore 3+ |
| 24 | `S_NECROMANCY` | necromancy | `NECR` | passive | `0` | force 1+; spirit 1+ |
| 25 | `S_SUMMON_SKELETONS` | summon skeletons | `SUSK` | cast | `0` | necromancy 1+ |
| 26 | `S_RAISE_UNDEAD` | raise undead | `RAIS` | cast | `0` | necromancy 3+ |
| 27 | `S_SUMMON_LICH` | summon lich | `SULI` | cast | `0` | necromancy 5+ |
| 28 | `S_CREATE_AURA_OF_FEAR` | create aura of fear | `FEAR` | combat | `SPECIAL_CAUSEFEAR` | necromancy 1+ |
| 29 | `S_SUMMON_BLACK_WIND` | summon black wind | `SBLA` | combat | `SPECIAL_BLACK_WIND` | necromancy 5+ |
| 30 | `S_BANISH_UNDEAD` | banish undead | `BUND` | combat | `SPECIAL_BANISH_UNDEAD` | necromancy 1+ |
| 31 | `S_DEMON_LORE` | demon lore | `DEMO` | passive | `0` | force 1+; spirit 1+ |
| 32 | `S_SUMMON_IMPS` | summon imps | `SUIM` | cast | `0` | demon lore 1+ |
| 33 | `S_SUMMON_DEMON` | summon demon | `SUDE` | cast | `0` | summon imps 3+ |
| 34 | `S_SUMMON_BALROG` | summon balrog | `SUBA` | cast | `0` | summon demon 3+ |
| 35 | `S_BANISH_DEMONS` | banish demons | `BDEM` | combat | `SPECIAL_BANISH_DEMONS` | demon lore 1+ |
| 36 | `S_ILLUSION` | illusion | `ILLU` | passive | `0` | force 1+; pattern 1+ |
| 37 | `S_PHANTASMAL_ENTERTAINMENT` | phantasmal entertainment | `PHEN` | passive | `0` | illusion 1+ |
| 38 | `S_CREATE_PHANTASMAL_BEASTS` | create phantasmal beasts | `PHBE` | cast | `0` | illusion 1+ |
| 39 | `S_CREATE_PHANTASMAL_UNDEAD` | create phantasmal undead | `PHUN` | cast | `0` | illusion 1+ |
| 40 | `S_CREATE_PHANTASMAL_DEMONS` | create phantasmal demons | `PHDE` | cast | `0` | illusion 1+ |
| 41 | `S_INVISIBILITY` | invisibility | `INVI` | cast | `0` | illusion 3+ |
| 42 | `S_TRUE_SEEING` | true seeing | `TRUE` | passive | `0` | illusion 3+ |
| 43 | `S_DISPEL_ILLUSIONS` | dispel illusions | `DISP` | combat | `SPECIAL_DISPEL_ILLUSIONS` | illusion 1+ |
| 44 | `S_ARTIFACT_LORE` | artifact lore | `ARTI` | passive | `0` | force 1+; pattern 1+; spirit 1+ |
| 45 | `S_CREATE_RING_OF_INVISIBILITY` | create ring of invisibility | `CRRI` | cast | `0` | artifact lore 3+; invisibility 3+ |
| 46 | `S_CREATE_CLOAK_OF_INVULNERABILITY` | create cloak of invulnerability | `CRCL` | cast | `0` | artifact lore 4+; force shield 3+ |
| 47 | `S_CREATE_STAFF_OF_FIRE` | create staff of fire | `CRSF` | cast | `0` | artifact lore 3+; fire 3+ |
| 48 | `S_CREATE_STAFF_OF_LIGHTNING` | create staff of lightning | `CRSL` | cast | `0` | artifact lore 5+; call lightning 3+ |
| 49 | `S_CREATE_AMULET_OF_TRUE_SEEING` | create amulet of true seeing | `CRTA` | cast | `0` | artifact lore 3+; true seeing 3+ |
| 50 | `S_CREATE_AMULET_OF_PROTECTION` | create amulet of protection | `CRPA` | cast | `0` | artifact lore 1+; spirit shield 3+ |
| 51 | `S_CREATE_RUNESWORD` | create runesword | `CRRU` | cast | `0` | artifact lore 4+; create aura of fear 3+ |
| 52 | `S_CREATE_SHIELDSTONE` | create shieldstone | `CRSH` | cast | `0` | artifact lore 3+; energy shield 3+ |
| 53 | `S_CREATE_MAGIC_CARPET` | create magic carpet | `CRMA` | cast | `0` | artifact lore 2+; weather lore 3+ |
| 54 | `S_ENGRAVE_RUNES_OF_WARDING` | engrave runes of warding | `ENGR` | cast | `0` | artifact lore 3+; energy shield 3+; spirit shield 3+ |
| 55 | `S_CONSTRUCT_GATE` | construct gate | `CGAT` | cast | `0` | artifact lore 3+; gate lore 3+ |
| 56 | `S_ENCHANT_SWORDS` | enchant swords | `ESWO` | cast | `0` | artifact lore 1+ |
| 57 | `S_ENCHANT_ARMOR` | enchant armor | `EARM` | cast | `0` | artifact lore 1+ |
| 58 | `S_CONSTRUCT_PORTAL` | construct portal | `CPOR` | cast | `0` | artifact lore 3+; portal lore 3+ |
