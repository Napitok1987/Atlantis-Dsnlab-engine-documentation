# Items Reference

## Status

Mechanically complete.

## Source

`ItemDefs` from `DSNAtlantis-src/standard/rules.cpp`; enum order from `DSNAtlantis-src/standard/rules.h`.

Total items: `131`.

`walk`, `ride`, `fly`, and `swim` show capacity or movement-channel contribution.

| # | Enum | Name | Plural | Code | Flags | Types | Production | Weight | Price | Combat | Index | Walk | Ride | Fly | Swim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `I_LEADERS` | leader | leaders | `LEAD` | - | MAN | - | `10` | `100` | `1` | `MAN_LEADER` | `15` | `0` | `0` | `0` |
| 1 | `I_VIKING` | viking | vikings | `VIKI` | - | MAN | - | `10` | `50` | `1` | `MAN_VIKING` | `15` | `0` | `0` | `0` |
| 2 | `I_BARBARIAN` | barbarian | barbarians | `BARB` | - | MAN | - | `10` | `50` | `1` | `MAN_BARBARIAN` | `15` | `0` | `0` | `0` |
| 3 | `I_PLAINSMAN` | plainsman | plainsmen | `PLAI` | - | MAN | - | `10` | `50` | `1` | `MAN_PLAINSMAN` | `15` | `0` | `0` | `0` |
| 4 | `I_ESKIMO` | eskimo | eskimos | `ESKI` | - | MAN | - | `10` | `50` | `1` | `MAN_ESKIMO` | `15` | `0` | `0` | `0` |
| 5 | `I_NOMAD` | nomad | nomads | `NOMA` | - | MAN | - | `10` | `50` | `1` | `MAN_NOMAD` | `15` | `0` | `0` | `0` |
| 6 | `I_TRIBESMAN` | tribesman | tribesmen | `TMAN` | - | MAN | - | `10` | `50` | `1` | `MAN_TRIBESMAN` | `15` | `0` | `0` | `0` |
| 7 | `I_DARKMAN` | darkman | darkmen | `DMAN` | - | MAN | - | `10` | `50` | `1` | `MAN_DARKMAN` | `15` | `0` | `0` | `0` |
| 8 | `I_WOODELF` | wood elf | wood elves | `WELF` | - | MAN | - | `10` | `50` | `1` | `MAN_WOODELF` | `15` | `0` | `0` | `0` |
| 9 | `I_SEAELF` | sea elf | sea elves | `SELF` | - | MAN | - | `10` | `50` | `1` | `MAN_SEAELF` | `15` | `0` | `0` | `0` |
| 10 | `I_HIGHELF` | high elf | high elves | `HELF` | - | MAN | - | `10` | `50` | `1` | `MAN_HIGHELF` | `15` | `0` | `0` | `0` |
| 11 | `I_TRIBALELF` | tribal elf | tribal elves | `TELF` | - | MAN | - | `10` | `50` | `1` | `MAN_TRIBALELF` | `15` | `0` | `0` | `0` |
| 12 | `I_ICEDWARF` | ice dwarf | ice dwarves | `IDWA` | - | MAN | - | `10` | `50` | `1` | `MAN_ICEDWARF` | `15` | `0` | `0` | `0` |
| 13 | `I_HILLDWARF` | hill dwarf | hill dwarves | `HDWA` | - | MAN | - | `10` | `50` | `1` | `MAN_HILLDWARF` | `15` | `0` | `0` | `0` |
| 14 | `I_UNDERDWARF` | under dwarf | under dwarves | `UDWA` | - | MAN | - | `10` | `50` | `1` | `MAN_UNDERDWARF` | `15` | `0` | `0` | `0` |
| 15 | `I_DESERTDWARF` | desert dwarf | desert dwarves | `DDWA` | - | MAN | - | `10` | `50` | `1` | `MAN_DESERTDWARF` | `15` | `0` | `0` | `0` |
| 16 | `I_ORC` | orc | orcs | `ORC` | - | MAN | - | `10` | `50` | `1` | `MAN_ORC` | `15` | `0` | `0` | `0` |
| 17 | `I_SILVER` | silver | silver | `SILV` | - | NORMAL | - | `0` | `1` | `0` | `0` | `0` | `0` | `0` | `0` |
| 18 | `I_GRAIN` | grain | grain | `GRAI` | - | NORMAL | `S_FARMING` / farming lvl `1` | `5` | `15` | `0` | `0` | `0` | `0` | `0` | `0` |
| 19 | `I_LIVESTOCK` | livestock | livestock | `LIVE` | - | NORMAL | `S_RANCHING` / ranching lvl `1` | `50` | `15` | `0` | `0` | `50` | `0` | `0` | `0` |
| 20 | `I_IRON` | iron | iron | `IRON` | - | NORMAL | `S_MINING` / mining lvl `1` | `5` | `30` | `0` | `0` | `0` | `0` | `0` | `0` |
| 21 | `I_WOOD` | wood | wood | `WOOD` | - | NORMAL | `S_LUMBERJACK` / lumberjack lvl `1` | `5` | `30` | `0` | `0` | `0` | `0` | `0` | `0` |
| 22 | `I_STONE` | stone | stone | `STON` | - | NORMAL | `S_QUARRYING` / quarrying lvl `1` | `50` | `30` | `0` | `0` | `0` | `0` | `0` | `0` |
| 23 | `I_FUR` | fur | furs | `FUR` | - | NORMAL | `S_HUNTING` / hunting lvl `1` | `1` | `30` | `0` | `0` | `0` | `0` | `0` | `0` |
| 24 | `I_FISH` | fish | fish | `FISH` | - | NORMAL | `S_FISHING` / fishing lvl `1` | `1` | `15` | `0` | `0` | `0` | `0` | `0` | `0` |
| 25 | `I_HERBS` | herb | herbs | `HERB` | - | NORMAL | `S_HERBLORE` / herb lore lvl `1` | `0` | `30` | `0` | `0` | `0` | `0` | `0` | `0` |
| 26 | `I_HORSE` | horse | horses | `HORS` | - | NORMAL, MOUNT | `S_HORSETRAINING` / horse training lvl `1` | `50` | `30` | `1` | `MOUNT_HORSE` | `70` | `70` | `0` | `0` |
| 27 | `I_SWORD` | sword | swords | `SWOR` | - | NORMAL, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `1`; input `I_IRON` / iron x`1` | `1` | `60` | `1` | `WEAPON_SWORD` | `0` | `0` | `0` | `0` |
| 28 | `I_CROSSBOW` | crossbow | crossbows | `XBOW` | - | NORMAL, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `1`; input `I_WOOD` / wood x`1` | `1` | `60` | `1` | `WEAPON_CROSSBOW` | `0` | `0` | `0` | `0` |
| 29 | `I_LONGBOW` | longbow | longbows | `LBOW` | - | NORMAL, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `1`; input `I_WOOD` / wood x`1` | `1` | `60` | `1` | `WEAPON_LONGBOW` | `0` | `0` | `0` | `0` |
| 30 | `I_CHAINARMOR` | chain armor | chain armor | `CARM` | - | NORMAL, ARMOR | `S_ARMORER` / armorer lvl `1`; input `I_IRON` / iron x`1` | `1` | `60` | `1` | `ARMOR_CHAINARMOR` | `0` | `0` | `0` | `0` |
| 31 | `I_PLATEARMOR` | plate armor | plate armor | `PARM` | - | NORMAL, ARMOR | `S_ARMORER` / armorer lvl `3`; input `I_IRON` / iron x`3` | `3` | `250` | `1` | `ARMOR_PLATEARMOR` | `0` | `0` | `0` | `0` |
| 32 | `I_WAGON` | wagon | wagons | `WAGO` | - | NORMAL | `S_CARPENTER` / carpenter lvl `1`; input `I_WOOD` / wood x`1` | `50` | `100` | `0` | `0` | `0` | `0` | `0` | `0` |
| 33 | `I_MITHRIL` | mithril | mithril | `MITH` | - | ADVANCED | `S_MINING` / mining lvl `3` | `10` | `100` | `0` | `0` | `0` | `0` | `0` | `0` |
| 34 | `I_IRONWOOD` | ironwood | ironwood | `IRWD` | - | ADVANCED | `S_LUMBERJACK` / lumberjack lvl `3` | `10` | `100` | `0` | `0` | `0` | `0` | `0` | `0` |
| 35 | `I_WHORSE` | winged horse | winged horses | `WING` | - | ADVANCED, MOUNT | `S_HORSETRAINING` / horse training lvl `5` | `50` | `100` | `1` | `MOUNT_WHORSE` | `70` | `70` | `70` | `0` |
| 36 | `I_FLOATER` | floater hide | floater hides | `FLOA` | - | ADVANCED | `S_HUNTING` / hunting lvl `3` | `1` | `100` | `0` | `0` | `0` | `0` | `0` | `0` |
| 37 | `I_ROOTSTONE` | rootstone | rootstone | `ROOT` | - | ADVANCED | `S_QUARRYING` / quarrying lvl `3` | `50` | `100` | `0` | `0` | `0` | `0` | `0` | `0` |
| 38 | `I_YEW` | yew | yew | `YEW` | - | ADVANCED | `S_LUMBERJACK` / lumberjack lvl `5` | `5` | `100` | `0` | `0` | `0` | `0` | `0` | `0` |
| 39 | `I_MSWORD` | mithril sword | mithril swords | `MSWO` | - | ADVANCED, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `3`; input `I_MITHRIL` / mithril x`1` | `1` | `200` | `1` | `WEAPON_MSWORD` | `0` | `0` | `0` | `0` |
| 40 | `I_MPLATE` | mithril armor | mithril armor | `MARM` | - | ADVANCED, ARMOR | `S_ARMORER` / armorer lvl `5`; input `I_MITHRIL` / mithril x`1` | `1` | `500` | `1` | `ARMOR_MARMOR` | `0` | `0` | `0` | `0` |
| 41 | `I_DOUBLEBOW` | double bow | double bows | `DBOW` | - | ADVANCED, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `5`; input `I_YEW` / yew x`1` | `1` | `200` | `1` | `WEAPON_DOUBLEBOW` | `0` | `0` | `0` | `0` |
| 42 | `I_IVORY` | ivory | ivory | `IVOR` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 43 | `I_PEARL` | pearls | pearls | `PEAR` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 44 | `I_JEWELRY` | jewelry | jewelry | `JEWE` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 45 | `I_FIGURINES` | figurines | figurines | `FIGU` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 46 | `I_TAROTCARDS` | tarot cards | tarot cards | `TARO` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 47 | `I_CAVIAR` | caviar | caviar | `CAVI` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 48 | `I_WINE` | wine | wine | `WINE` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 49 | `I_SPICES` | spices | spices | `SPIC` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 50 | `I_CHOCOLATE` | chocolate | chocolate | `CHOC` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 51 | `I_TRUFFLES` | truffles | truffles | `TRUF` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 52 | `I_VODKA` | vodka | vodka | `VODK` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 53 | `I_ROSES` | roses | roses | `ROSE` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 54 | `I_PERFUME` | perfume | perfume | `PERF` | - | TRADE | - | `1` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 55 | `I_SILK` | silk | silk | `SILK` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 56 | `I_VELVET` | velvet | velvet | `VELV` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 57 | `I_MINK` | mink | mink | `MINK` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 58 | `I_CASHMERE` | cashmere | cashmere | `CASH` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 59 | `I_COTTON` | cotton | cotton | `COTT` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 60 | `I_DYES` | dye | dye | `DYE` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 61 | `I_WOOL` | wool | wool | `WOOL` | - | TRADE | - | `5` | `60` | `0` | `0` | `0` | `0` | `0` | `0` |
| 62 | `I_LION` | lion | lions | `LION` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_LION` | `15` | `0` | `0` | `0` |
| 63 | `I_WOLF` | wolf | wolves | `WOLF` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_WOLF` | `15` | `15` | `0` | `0` |
| 64 | `I_GBEAR` | grizzly bear | grizzly bears | `GRIZ` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_GBEAR` | `60` | `0` | `0` | `0` |
| 65 | `I_CROCODILE` | crocodile | crocodiles | `CROC` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_CROCODILE` | `15` | `0` | `0` | `0` |
| 66 | `I_ANACONDA` | anaconda | anacondas | `ANAC` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_ANACONDA` | `60` | `0` | `0` | `0` |
| 67 | `I_SCORPION` | giant scorpion | giant scorpions | `SCOR` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_SCORPION` | `15` | `0` | `0` | `0` |
| 68 | `I_PBEAR` | polar bear | polar bears | `POLA` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_PBEAR` | `60` | `0` | `0` | `0` |
| 69 | `I_RAT` | giant rat | giant rats | `GRAT` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_GRAT` | `15` | `0` | `0` | `0` |
| 70 | `I_SPIDER` | giant spider | giant spiders | `GSPI` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_SPIDER` | `60` | `0` | `0` | `0` |
| 71 | `I_LIZARD` | giant lizard | giant lizards | `GLIZ` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_LIZARD` | `60` | `0` | `0` | `0` |
| 72 | `I_TRENT` | trent | trents | `TREN` | CANTGIVE | MONSTER | - | `250` | `50` | `1` | `MONSTER_TRENT` | `300` | `0` | `0` | `0` |
| 73 | `I_ROC` | roc | rocs | `ROC` | CANTGIVE | MONSTER | - | `250` | `50` | `1` | `MONSTER_ROC` | `300` | `300` | `300` | `0` |
| 74 | `I_BTHING` | bog thing | bog things | `BOGT` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_BTHING` | `60` | `0` | `0` | `0` |
| 75 | `I_KONG` | kong | kongs | `KONG` | CANTGIVE | MONSTER | - | `250` | `50` | `1` | `MONSTER_KONG` | `300` | `0` | `0` | `0` |
| 76 | `I_SPHINX` | sphinx | sphinxes | `SPHI` | CANTGIVE | MONSTER | - | `250` | `50` | `1` | `MONSTER_SPHINX` | `300` | `300` | `0` | `0` |
| 77 | `I_IWURM` | ice wurm | ice wurms | `ICEW` | CANTGIVE | MONSTER | - | `250` | `50` | `1` | `MONSTER_IWURM` | `300` | `0` | `0` | `0` |
| 78 | `I_DRAGON` | dragon | dragons | `DRAG` | CANTGIVE | MONSTER | - | `250` | `50` | `1` | `MONSTER_DRAGON` | `300` | `300` | `300` | `0` |
| 79 | `I_CENTAUR` | centaur | centaurs | `CENT` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_CENTAUR` | `60` | `60` | `0` | `0` |
| 80 | `I_KOBOLD` | kobold | kobolds | `KOBO` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_KOBOLD` | `15` | `0` | `0` | `0` |
| 81 | `I_OGRE` | ogre | ogres | `OGRE` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_OGRE` | `60` | `0` | `0` | `0` |
| 82 | `I_LMEN` | lizard man | lizard men | `LMAN` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_LMAN` | `15` | `0` | `0` | `0` |
| 83 | `I_WMEN` | wild man | wild men | `WMAN` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_WMAN` | `15` | `0` | `0` | `0` |
| 84 | `I_SANDLING` | sandling | sandlings | `SAND` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_SANDLING` | `15` | `0` | `0` | `0` |
| 85 | `I_YETI` | yeti | yeti | `YETI` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_YETI` | `60` | `0` | `0` | `0` |
| 86 | `I_GOBLIN` | goblin | goblins | `GOBL` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_GOBLIN` | `15` | `0` | `0` | `0` |
| 87 | `I_TROLL` | troll | trolls | `TROL` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_TROLL` | `60` | `0` | `0` | `0` |
| 88 | `I_ETTIN` | ettin | ettins | `ETTI` | CANTGIVE | MONSTER | - | `50` | `50` | `1` | `MONSTER_ETTIN` | `60` | `0` | `0` | `0` |
| 89 | `I_SKELETON` | skeleton | skeletons | `SKEL` | - | MONSTER | - | `10` | `50` | `1` | `MONSTER_SKELETON` | `15` | `0` | `0` | `0` |
| 90 | `I_UNDEAD` | undead | undead | `UNDE` | - | MONSTER | - | `10` | `50` | `1` | `MONSTER_UNDEAD` | `15` | `0` | `0` | `0` |
| 91 | `I_LICH` | lich | liches | `LICH` | - | MONSTER | - | `10` | `50` | `1` | `MONSTER_LICH` | `15` | `0` | `0` | `0` |
| 92 | `I_IMP` | imp | imps | `IMP` | - | MONSTER | - | `10` | `50` | `1` | `MONSTER_IMP` | `15` | `0` | `0` | `0` |
| 93 | `I_DEMON` | demon | demons | `DEMO` | - | MONSTER | - | `50` | `50` | `1` | `MONSTER_DEMON` | `60` | `60` | `0` | `0` |
| 94 | `I_BALROG` | balrog | balrogs | `BALR` | CANTGIVE | MONSTER | - | `250` | `50` | `1` | `MONSTER_BALROG` | `300` | `300` | `300` | `0` |
| 95 | `I_EAGLE` | eagle | eagles | `EAGL` | CANTGIVE | MONSTER | - | `10` | `50` | `1` | `MONSTER_EAGLE` | `15` | `15` | `15` | `0` |
| 96 | `I_AMULETOFI` | amulet of invulnerability | amulets of invulnerability | `XXXX` | - | MAGIC, BATTLE, SPECIAL | - | `0` | `1000000` | `1` | `BATTLE_AOFI` | `0` | `0` | `0` | `0` |
| 97 | `I_RINGOFI` | ring of invisibility | rings of invisibility | `RING` | - | MAGIC | - | `0` | `4000` | `1` | `0` | `0` | `0` | `0` | `0` |
| 98 | `I_CLOAKOFI` | cloak of invulnerability | cloaks of invulnerability | `CLOA` | - | MAGIC, ARMOR | - | `0` | `8000` | `1` | `ARMOR_CLOAKOFI` | `0` | `0` | `0` | `0` |
| 99 | `I_STAFFOFF` | staff of fire | staves of fire | `STAF` | - | MAGIC, BATTLE | - | `0` | `4000` | `1` | `BATTLE_STAFFOFF` | `0` | `0` | `0` | `0` |
| 100 | `I_STAFFOFL` | staff of lightning | staves of lightning | `STAL` | - | MAGIC, BATTLE | - | `0` | `16000` | `1` | `BATTLE_STAFFOFL` | `0` | `0` | `0` | `0` |
| 101 | `I_AMULETOFTS` | amulet of true seeing | amulets of true seeing | `AMTS` | - | MAGIC | - | `0` | `4000` | `0` | `0` | `0` | `0` | `0` | `0` |
| 102 | `I_AMULETOFP` | amulet of protection | amulets of protection | `AMPR` | - | MAGIC, BATTLE | - | `0` | `1000` | `1` | `BATTLE_AMULETOFP` | `0` | `0` | `0` | `0` |
| 103 | `I_RUNESWORD` | runesword | runeswords | `RUNE` | - | MAGIC, WEAPON, BATTLE | - | `1` | `8000` | `1` | `WEAPON_RUNESWORD` | `0` | `0` | `0` | `0` |
| 104 | `I_SHIELDSTONE` | shieldstone | shieldstones | `SHST` | - | MAGIC, BATTLE | - | `0` | `4000` | `1` | `BATTLE_SHIELDSTONE` | `0` | `0` | `0` | `0` |
| 105 | `I_MCARPET` | magic carpet | magic carpets | `CARP` | - | MAGIC | - | `0` | `2000` | `0` | `0` | `15` | `15` | `15` | `0` |
| 106 | `I_IWOLF` | wolf | wolves | `WOLF` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 107 | `I_IEAGLE` | eagle | eagles | `EAGL` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 108 | `I_IDRAGON` | dragon | dragons | `DRAG` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 109 | `I_ISKELETON` | skeleton | skeletons | `SKEL` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 110 | `I_IUNDEAD` | undead | undead | `UNDE` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 111 | `I_ILICH` | lich | liches | `LICH` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 112 | `I_IIMP` | imp | imps | `IMP` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 113 | `I_IDEMON` | demon | demons | `DEMO` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 114 | `I_IBALROG` | balrog | balrogs | `BALR` | CANTGIVE | MONSTER | - | `1` | `1` | `1` | `MONSTER_ILLUSION` | `1` | `1` | `1` | `0` |
| 115 | `I_PORTAL` | portal | portals | `PORT` | - | MAGIC, SPECIAL | - | `1` | `1000` | `0` | `0` | `0` | `0` | `0` | `0` |
| 116 | `I_PEASANT` | peasant | peasants | `PEAS` | - | MAN | - | `10` | `50` | `1` | `0` | `15` | `0` | `0` | `0` |
| 117 | `I_PICK` | pick | picks | `PICK` | - | NORMAL, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `1`; input `I_IRON` / iron x`1` | `1` | `60` | `1` | `WEAPON_PICK` | `0` | `0` | `0` | `0` |
| 118 | `I_SPEAR` | spear | spears | `SPEA` | - | NORMAL, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `1`; input `I_WOOD` / wood x`1` | `1` | `60` | `1` | `WEAPON_SPEAR` | `0` | `0` | `0` | `0` |
| 119 | `I_AXE` | axe | axes | `AXE` | - | NORMAL, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `1`; input `I_WOOD` / wood x`1` | `1` | `60` | `1` | `WEAPON_AXE` | `0` | `0` | `0` | `0` |
| 120 | `I_HAMMER` | hammer | hammers | `HAMM` | - | NORMAL, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `1`; input `I_IRON` / iron x`1` | `1` | `60` | `1` | `WEAPON_HAMMER` | `0` | `0` | `0` | `0` |
| 121 | `I_MCROSSBOW` | magic crossbow | magic crossbows | `MXBO` | - | ADVANCED, WEAPON | `S_WEAPONSMITH` / weaponsmith lvl `4`; input `I_IRONWOOD` / ironwood x`1` | `1` | `200` | `1` | `WEAPON_MCROSSBOW` | `0` | `0` | `0` | `0` |
| 122 | `I_MWAGON` | magic wagon | magic wagons | `MWAG` | - | ADVANCED | `S_CARPENTER` / carpenter lvl `3`; input `I_IRONWOOD` / ironwood x`1` | `50` | `200` | `1` | - | `250` | `250` | `0` | `0` |
| 123 | `I_GLIDER` | glider | gliders | `GLID` | - | ADVANCED | `S_CARPENTER` / carpenter lvl `5`; input `I_FLOATER` / floater hide x`2` | `5` | `400` | `1` | - | `0` | `0` | `15` | `0` |
| 124 | `I_NET` | net | nets | `NET` | - | NORMAL | `S_FISHING` / fishing lvl `1`; input `I_HERBS` / herb x`1` | `1` | `60` | `1` | - | `0` | `0` | `0` | `0` |
| 125 | `I_LASSO` | lasso | lassoes | `LASS` | - | NORMAL | `S_HERBLORE` / herb lore lvl `1`; input `I_HERBS` / herb x`1` | `1` | `60` | `1` | - | `0` | `0` | `0` | `0` |
| 126 | `I_BAG` | bag | bags | `BAG` | - | NORMAL | `S_HERBLORE` / herb lore lvl `1`; input `I_HERBS` / herb x`1` | `1` | `60` | `1` | - | `0` | `0` | `0` | `0` |
| 127 | `I_SPINNING` | spinning wheel | spinning wheels | `SPIN` | - | NORMAL | `S_CARPENTER` / carpenter lvl `1`; input `I_WOOD` / wood x`1` | `1` | `60` | `1` | - | `0` | `0` | `0` | `0` |
| 128 | `I_LEATHERARMOR` | leather armor | leather armor | `LARM` | - | NORMAL, ARMOR | `S_ARMORER` / armorer lvl `1`; input `I_FUR` / fur x`1` | `1` | `45` | `1` | `ARMOR_LEATHERARMOR` | `0` | `0` | `0` | `0` |
| 129 | `I_CLOTHARMOR` | cloth armor | cloth armor | `CLAR` | - | NORMAL, ARMOR | `S_ARMORER` / armorer lvl `1`; input `I_HERBS` / herb x`1` | `1` | `40` | `1` | `ARMOR_CLOTHARMOR` | `0` | `0` | `0` | `0` |
| 130 | `I_BOOTS` | boots of levitation | boots of levitation | `BOOT` | - | MAGIC | - | `0` | `1000` | `0` | `0` | `0` | `0` | `0` | `15` |
