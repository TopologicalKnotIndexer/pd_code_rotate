# pd-code-rotate

Rotate the local representation of every crossing while respecting component orientation.

## Installation

```bash
pip install pd-code-rotate
```

## Usage example

```python
from pd_code_rotate import rotate

pd = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]
print(rotate(pd))
```

## Algorithm

Predecessor/successor maps determine the direction of each strand. For crossing `[a,b,c,d]`, the implementation selects either `[b,a,d,c]` or `[d,c,b,a]` so the rotated crossing remains consistent with the canonical component direction. Arc incidences and crossing count are preserved.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Run examples and package checks before release. Python packages require Python 3.10 or newer. Build PyPI artifacts with:

```bash
poetry check
poetry build
```

## License

MIT. See `LICENSE`.
