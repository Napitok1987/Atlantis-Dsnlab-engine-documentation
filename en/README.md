# Atlantis DSNlab As-Is Documentation

This directory contains the English publication edition of the Atlantis DSNlab `as-is` documentation.

The Russian corpus remains the primary detailed source. This English edition is a maintained parallel version intended for public reading, repository navigation, and future migration work.

Historical source code used for verification:

- [Labutin/DSNAtlantis](https://github.com/Labutin/DSNAtlantis)

## Status

The `as-is` layer is frozen as `Mechanically complete`.

This means:

- the core game systems are described in `canonical/as-is/`;
- no open high-priority or medium-priority source conflicts are known;
- executable tests are limited to game mechanics;
- archived drafts are not part of the publication set.

## Structure

- `canonical/` - canonical English documentation.
- `canonical/as-is/` - frozen description of the original game.
- `tests/` - notes for the executable mechanics tests.

## Tests

The tests validate game mechanics through a prebuilt `standard` server binary.

By default the test suite looks for the binary at `../DSNAtlantis-src/standard/standard`.
Another path can be provided through `ATLANTIS_STANDARD_BINARY`:

```bash
ATLANTIS_STANDARD_BINARY=/path/to/standard python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Normal run from the repository root:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## License

The materials are distributed under the GNU General Public License v3.0 or later.

See `../LICENSE`.
