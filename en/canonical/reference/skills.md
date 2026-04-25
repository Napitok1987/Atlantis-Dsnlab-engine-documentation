# Skills Reference

## Status

Mechanically complete.

## Source

`SkillDefs` from `DSNAtlantis-src/standard/rules.cpp`; enum order from `DSNAtlantis-src/standard/rules.h`.

Total skills: `83`.

| # | Enum | Name | Code | Cost | Flags | Special | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `S_MINING` | mining | `MINI` | `10` | - | `0` | - |
| 1 | `S_LUMBERJACK` | lumberjack | `LUMB` | `10` | - | `0` | - |
| 2 | `S_QUARRYING` | quarrying | `QUAR` | `10` | - | `0` | - |
| 3 | `S_HUNTING` | hunting | `HUNT` | `10` | - | `0` | - |
| 4 | `S_FISHING` | fishing | `FISH` | `10` | - | `0` | - |
| 5 | `S_HERBLORE` | herb lore | `HERB` | `10` | - | `0` | - |
| 6 | `S_HORSETRAINING` | horse training | `HORS` | `10` | - | `0` | - |
| 7 | `S_WEAPONSMITH` | weaponsmith | `WEAP` | `10` | - | `0` | - |
| 8 | `S_ARMORER` | armorer | `ARMO` | `10` | - | `0` | - |
| 9 | `S_CARPENTER` | carpenter | `CARP` | `10` | - | `0` | - |
| 10 | `S_BUILDING` | building | `BUIL` | `10` | - | `0` | - |
| 11 | `S_SHIPBUILDING` | shipbuilding | `SHIP` | `10` | - | `0` | - |
| 12 | `S_ENTERTAINMENT` | entertainment | `ENTE` | `10` | - | `0` | - |
| 13 | `S_TACTICS` | tactics | `TACT` | `200` | - | `0` | - |
| 14 | `S_COMBAT` | combat | `COMB` | `10` | - | `0` | - |
| 15 | `S_RIDING` | riding | `RIDI` | `10` | - | `0` | - |
| 16 | `S_CROSSBOW` | crossbow | `XBOW` | `10` | - | `0` | - |
| 17 | `S_LONGBOW` | longbow | `LBOW` | `10` | - | `0` | - |
| 18 | `S_STEALTH` | stealth | `STEA` | `50` | - | `0` | - |
| 19 | `S_OBSERVATION` | observation | `OBSE` | `50` | - | `0` | - |
| 20 | `S_HEALING` | healing | `HEAL` | `10` | - | `0` | - |
| 21 | `S_SAILING` | sailing | `SAIL` | `10` | - | `0` | - |
| 22 | `S_FARMING` | farming | `FARM` | `10` | - | `0` | - |
| 23 | `S_RANCHING` | ranching | `RANC` | `10` | - | `0` | - |
| 24 | `S_FORCE` | force | `FORC` | `100` | MAGIC, FOUNDATION | `0` | - |
| 25 | `S_PATTERN` | pattern | `PATT` | `100` | MAGIC, FOUNDATION | `0` | - |
| 26 | `S_SPIRIT` | spirit | `SPIR` | `100` | MAGIC, FOUNDATION | `0` | - |
| 27 | `S_FIRE` | fire | `FIRE` | `100` | MAGIC, COMBAT | `SPECIAL_FIREBALL` | force 1+ |
| 28 | `S_EARTHQUAKE` | earthquake | `EQUA` | `100` | MAGIC, COMBAT | `SPECIAL_EARTHQUAKE` | force 1+; pattern 1+ |
| 29 | `S_FORCE_SHIELD` | force shield | `FSHI` | `100` | MAGIC, COMBAT | `SPECIAL_FORCE_SHIELD` | force 1+ |
| 30 | `S_ENERGY_SHIELD` | energy shield | `ESHI` | `100` | MAGIC, COMBAT | `SPECIAL_ENERGY_SHIELD` | force 1+ |
| 31 | `S_SPIRIT_SHIELD` | spirit shield | `SSHI` | `100` | MAGIC, COMBAT | `SPECIAL_SPIRIT_SHIELD` | spirit 1+; force 1+ |
| 32 | `S_MAGICAL_HEALING` | magical healing | `MHEA` | `100` | MAGIC | `0` | pattern 1+ |
| 33 | `S_GATE_LORE` | gate lore | `GATE` | `100` | MAGIC, CAST | `0` | pattern 1+; spirit 1+ |
| 34 | `S_FARSIGHT` | farsight | `FARS` | `100` | MAGIC, CAST | `0` | pattern 1+; spirit 1+ |
| 35 | `S_TELEPORTATION` | teleportation | `TELE` | `100` | MAGIC, CAST | `0` | gate lore 1+; farsight 3+ |
| 36 | `S_PORTAL_LORE` | portal lore | `PORT` | `100` | MAGIC, CAST | `0` | gate lore 3+; farsight 1+ |
| 37 | `S_MIND_READING` | mind reading | `MIND` | `100` | MAGIC, CAST | `0` | pattern 1+ |
| 38 | `S_WEATHER_LORE` | weather lore | `WEAT` | `100` | MAGIC | `0` | force 1+; pattern 1+ |
| 39 | `S_SUMMON_WIND` | summon wind | `SWIN` | `100` | MAGIC | `0` | weather lore 1+ |
| 40 | `S_SUMMON_STORM` | summon storm | `SSTO` | `100` | MAGIC, COMBAT | `SPECIAL_SUMMON_STORM` | weather lore 1+ |
| 41 | `S_SUMMON_TORNADO` | summon tornado | `STOR` | `100` | MAGIC, COMBAT | `SPECIAL_TORNADO` | weather lore 3+ |
| 42 | `S_CALL_LIGHTNING` | call lightning | `CALL` | `100` | MAGIC, COMBAT | `SPECIAL_LSTRIKE` | weather lore 5+ |
| 43 | `S_CLEAR_SKIES` | clear skies | `CLEA` | `100` | MAGIC, COMBAT, CAST | `SPECIAL_CLEAR_SKIES` | weather lore 1+ |
| 44 | `S_EARTH_LORE` | earth lore | `EART` | `100` | MAGIC, CAST | `0` | pattern 1+ |
| 45 | `S_WOLF_LORE` | wolf lore | `WOLF` | `100` | MAGIC, CAST | `0` | earth lore 1+ |
| 46 | `S_BIRD_LORE` | bird lore | `BIRD` | `100` | MAGIC, CAST | `0` | earth lore 1+ |
| 47 | `S_DRAGON_LORE` | dragon lore | `DRAG` | `100` | MAGIC, CAST | `0` | bird lore 3+ |
| 48 | `S_NECROMANCY` | necromancy | `NECR` | `100` | MAGIC | `0` | force 1+; spirit 1+ |
| 49 | `S_SUMMON_SKELETONS` | summon skeletons | `SUSK` | `100` | MAGIC, CAST | `0` | necromancy 1+ |
| 50 | `S_RAISE_UNDEAD` | raise undead | `RAIS` | `100` | MAGIC, CAST | `0` | necromancy 3+ |
| 51 | `S_SUMMON_LICH` | summon lich | `SULI` | `100` | MAGIC, CAST | `0` | necromancy 5+ |
| 52 | `S_CREATE_AURA_OF_FEAR` | create aura of fear | `FEAR` | `100` | MAGIC, COMBAT | `SPECIAL_CAUSEFEAR` | necromancy 1+ |
| 53 | `S_SUMMON_BLACK_WIND` | summon black wind | `SBLA` | `100` | MAGIC, COMBAT | `SPECIAL_BLACK_WIND` | necromancy 5+ |
| 54 | `S_BANISH_UNDEAD` | banish undead | `BUND` | `100` | MAGIC, COMBAT | `SPECIAL_BANISH_UNDEAD` | necromancy 1+ |
| 55 | `S_DEMON_LORE` | demon lore | `DEMO` | `100` | MAGIC | `0` | force 1+; spirit 1+ |
| 56 | `S_SUMMON_IMPS` | summon imps | `SUIM` | `100` | MAGIC, CAST | `0` | demon lore 1+ |
| 57 | `S_SUMMON_DEMON` | summon demon | `SUDE` | `100` | MAGIC, CAST | `0` | summon imps 3+ |
| 58 | `S_SUMMON_BALROG` | summon balrog | `SUBA` | `100` | MAGIC, CAST | `0` | summon demon 3+ |
| 59 | `S_BANISH_DEMONS` | banish demons | `BDEM` | `100` | MAGIC, COMBAT | `SPECIAL_BANISH_DEMONS` | demon lore 1+ |
| 60 | `S_ILLUSION` | illusion | `ILLU` | `100` | MAGIC | `0` | force 1+; pattern 1+ |
| 61 | `S_PHANTASMAL_ENTERTAINMENT` | phantasmal entertainment | `PHEN` | `100` | MAGIC | `0` | illusion 1+ |
| 62 | `S_CREATE_PHANTASMAL_BEASTS` | create phantasmal beasts | `PHBE` | `100` | MAGIC, CAST | `0` | illusion 1+ |
| 63 | `S_CREATE_PHANTASMAL_UNDEAD` | create phantasmal undead | `PHUN` | `100` | MAGIC, CAST | `0` | illusion 1+ |
| 64 | `S_CREATE_PHANTASMAL_DEMONS` | create phantasmal demons | `PHDE` | `100` | MAGIC, CAST | `0` | illusion 1+ |
| 65 | `S_INVISIBILITY` | invisibility | `INVI` | `100` | MAGIC, CAST | `0` | illusion 3+ |
| 66 | `S_TRUE_SEEING` | true seeing | `TRUE` | `100` | MAGIC | `0` | illusion 3+ |
| 67 | `S_DISPEL_ILLUSIONS` | dispel illusions | `DISP` | `100` | MAGIC, COMBAT | `SPECIAL_DISPEL_ILLUSIONS` | illusion 1+ |
| 68 | `S_ARTIFACT_LORE` | artifact lore | `ARTI` | `100` | MAGIC | `0` | force 1+; pattern 1+; spirit 1+ |
| 69 | `S_CREATE_RING_OF_INVISIBILITY` | create ring of invisibility | `CRRI` | `100` | MAGIC, CAST | `0` | artifact lore 3+; invisibility 3+ |
| 70 | `S_CREATE_CLOAK_OF_INVULNERABILITY` | create cloak of invulnerability | `CRCL` | `100` | MAGIC, CAST | `0` | artifact lore 4+; force shield 3+ |
| 71 | `S_CREATE_STAFF_OF_FIRE` | create staff of fire | `CRSF` | `100` | MAGIC, CAST | `0` | artifact lore 3+; fire 3+ |
| 72 | `S_CREATE_STAFF_OF_LIGHTNING` | create staff of lightning | `CRSL` | `100` | MAGIC, CAST | `0` | artifact lore 5+; call lightning 3+ |
| 73 | `S_CREATE_AMULET_OF_TRUE_SEEING` | create amulet of true seeing | `CRTA` | `100` | MAGIC, CAST | `0` | artifact lore 3+; true seeing 3+ |
| 74 | `S_CREATE_AMULET_OF_PROTECTION` | create amulet of protection | `CRPA` | `100` | MAGIC, CAST | `0` | artifact lore 1+; spirit shield 3+ |
| 75 | `S_CREATE_RUNESWORD` | create runesword | `CRRU` | `100` | MAGIC, CAST | `0` | artifact lore 4+; create aura of fear 3+ |
| 76 | `S_CREATE_SHIELDSTONE` | create shieldstone | `CRSH` | `100` | MAGIC, CAST | `0` | artifact lore 3+; energy shield 3+ |
| 77 | `S_CREATE_MAGIC_CARPET` | create magic carpet | `CRMA` | `100` | MAGIC, CAST | `0` | artifact lore 2+; weather lore 3+ |
| 78 | `S_ENGRAVE_RUNES_OF_WARDING` | engrave runes of warding | `ENGR` | `100` | MAGIC, CAST | `0` | artifact lore 3+; energy shield 3+; spirit shield 3+ |
| 79 | `S_CONSTRUCT_GATE` | construct gate | `CGAT` | `100` | MAGIC, CAST | `0` | artifact lore 3+; gate lore 3+ |
| 80 | `S_ENCHANT_SWORDS` | enchant swords | `ESWO` | `100` | MAGIC, CAST | `0` | artifact lore 1+ |
| 81 | `S_ENCHANT_ARMOR` | enchant armor | `EARM` | `100` | MAGIC, CAST | `0` | artifact lore 1+ |
| 82 | `S_CONSTRUCT_PORTAL` | construct portal | `CPOR` | `100` | MAGIC, CAST | `0` | artifact lore 3+; portal lore 3+ |
