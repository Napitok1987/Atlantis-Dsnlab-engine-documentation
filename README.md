# Документация Atlantis DSNlab As-Is

Каноническая документация по текущему состоянию оригинальной игры Atlantis DSNlab.

Исторический код оригинального сервера используется для проверки как исходный репозиторий:

- [Labutin/DSNAtlantis](https://github.com/Labutin/DSNAtlantis)

## Статус

`as-is` слой заморожен как `Заморожено (механически завершено)`.

Это означает:

- основные игровые системы описаны в `canonical/as-is/`;
- незакрытых расхождений высокого и среднего приоритета не зафиксировано;
- тестовый слой оставлен только для исполняемых проверок игровых механик;
- архивные черновики удалены из публикуемого состава.

## Структура

- `canonical/` — каноническая документация.
- `canonical/as-is/` — замороженное описание оригинальной игры.
- `en/` — англоязычная публикационная версия документации.
- `tests/` — набор исполняемых регрессионных тестов для игровых механик.

## Тесты

Тесты проверяют только механики игры через уже собранный бинарь `standard`.

По умолчанию набор тестов ищет бинарь в `../DSNAtlantis-src/standard/standard`.
Другой путь можно задать через переменную окружения:

```bash
ATLANTIS_STANDARD_BINARY=/path/to/standard python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Обычный запуск из корня репозитория:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Лицензия

Материалы распространяются на условиях GNU General Public License v3.0 or later.

См. `LICENSE`.

# Atlantis DSNlab As-Is Documentation


Atlantis DSNlab As-Is Documentation
This directory contains the English publication edition of the Atlantis DSNlab as-is documentation.

The Russian corpus remains the primary detailed source. This English edition is a maintained parallel version intended for public reading, repository navigation, and future migration work.

Historical source code used for verification:

Labutin/DSNAtlantis
Status
The as-is layer is frozen as Mechanically complete.

This means:

the core game systems are described in canonical/as-is/;
no open high-priority or medium-priority source conflicts are known;
executable tests are limited to game mechanics;
archived drafts are not part of the publication set.
Structure
canonical/ - canonical English documentation.
canonical/as-is/ - frozen description of the original game.
tests/ - notes for the executable mechanics tests.
Tests
The tests validate game mechanics through a prebuilt standard server binary.

By default the test suite looks for the binary at ../DSNAtlantis-src/standard/standard. Another path can be provided through ATLANTIS_STANDARD_BINARY:

ATLANTIS_STANDARD_BINARY=/path/to/standard python3 -m unittest discover -s tests -p 'test_*.py' -v
Normal run from the repository root:

python3 -m unittest discover -s tests -p 'test_*.py' -v
License
The materials are distributed under the GNU General Public License v3.0 or later.

See ../LICENSE.
