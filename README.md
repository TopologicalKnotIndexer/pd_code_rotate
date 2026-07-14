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

Python 3.10 or newer is required. Run tests with the two declared PD-code
dependencies available:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.

## Citation

If you use this repository in academic work, please cite it as:

```bibtex
@software{topologicalknotindexer_pd_code_rotate,
  author = {{GGN\_2015}},
  title = {{pd\_code\_rotate}},
  year = {2026},
  url = {https://github.com/TopologicalKnotIndexer/pd_code_rotate}
}
```
