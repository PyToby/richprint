# richprinted

> A drop-in, dependency-light replacement for Python's `print()` that adds smart type detection, color themes (to be added), and structured, readable output for terminals.

`richprinted` is designed to feel exactly like `print()` — until you need more. Pass it a list, a dict, or a primitive, and it figures out how to format it well. Need more control? Every formatter accepts a rich set of keyword arguments for filtering, sorting, truncating, and styling output.

---

## Features

- **Callable singleton** — use `rprint(...)` just like `print(...)`
- **Smart type detection** — lists, dicts, and primitives are each formatted appropriately
- **Highly configurable formatters** — filter keys, sort, truncate, recolor, and reshape output per call
- **Minimal dependencies** — built to stay lightweight and terminal-friendly
- **Composable internals** — formatting logic lives in pure functions, easy to extend or reuse

---

## Installation

```bash
pip install richprinted
```

---

## Quick Start

```python
from richprinted import rprint

# Works similarly to print() just makes it nicer
rprint("Hello, world!")

# Automatically detects and formats a list
rprint([1, 2, 3, "four", 5.0])

# Automatically detects and formats a dict
rprint({"name": "Toby", "role": "developer", "active": True})
```

---

## Usage

### Basic printing
 
```python
rprint("a plain string")
rprint(42)
rprint(True)
rprint(None)
```
 
`richprinted` detects the type of the value passed in and routes it to the appropriate formatter — no configuration needed for simple cases.
 
**Possible kwargs for primitive formatting:**
 
| kwarg      | description                                              |
|------------|-----------------------------------------------------------|
| `nullstr`  | Custom string to represent `None` values                  |
| `encoding` | Encoding to apply/validate against when displaying the value |
| `errors`   | Error handling mode for encoding issues (e.g. `"strict"`, `"ignore"`, `"replace"`) |
| `truncate` | Truncate long values to a maximum length                  |
| `prefix`   | String prepended before the formatted value                |
| `suffix`   | String appended after the formatted value                  |

### Formatting lists

```python
rprint([5, 3, 1, 4, 2], sort=True)
rprint(list(range(20)), maxlength=10)
```

| kwarg          | description                                              |
|----------------|-------------------------------------------------------------|
| `sorting`      | Sort the list before display                                |
| `encoding`     | Encoding to apply/validate against for string items         |
| `showonly`     | Restrict display to only specific items                     |
| `startat`      | Index to start numbering from (0 or 1 indexing)              |
| `errors`       | Error handling mode for encoding issues                      |
| `nullstr`      | Custom string to represent `None` values                    |
| `truncate`     | Truncate long individual items                               |
| `maxlength`    | Truncate output after N items, showing `... (X more)`        |
| `show_indices` | Display each item's index alongside its value                |
| `groupby`      | Group items by their type                                    |

### Formatting dictionaries

```python
rprint(
    {"id": 1, "name": "Toby", "password": "secret", "active": True},
    exclude=["password"],
    style="block",
)
```

| kwarg       | description                                              |
|-------------|-------------------------------------------------------------|
| `maxlength` | Truncate to N key-value pairs                                |
| `nullstr`   | Custom string to represent `None` values                    |
| `truncate`  | Truncate long values                                          |
| `sort`      | Sort entries by key                                           |
| `sort_by`   | Sort entries either by values or keys                          |
| `reverse`   | Reverse display order, used with sort                         |
| `showonly`  | Restrict display to only specific keys                        |
| `exclude`   | Blocklist specific keys from display                           |
| `style`     | Output format - either `"inline"` or `"block"`                |

### Utility methods

Beyond the callable interface, `richprinted` exposes utility methods for more structured output:

```python
rprint.table(data)       # Render tabular data
rprint.banner("Done!")   # Print a styled banner/header
rprint.inspect(obj)      # Inspect an object's attributes and structure
rprint.diff(old, new)    # Show a structured diff between two values
```
> **Note:** Utility methods are currently under active development. They have not been yet implemented into an official release.

---

## Project Structure

```
richprint/
├── .github/workflows
├── dist                     # Includes files to configure PyPI packaging
├── richprinted/
│   ├── __init__.py
│   ├── core.py              # _RichPrinted singleton + __call__ dispatch, detection and other
│   └── formatters/
│       ├── __init__.py
│       └── formatter.py     # format_list, format_primitive, format_dictionary, ...
├── README.md
├── LICENCE
└── pyproject.toml
```

---

## Roadmap

- [x] `format_list`
- [x] `format_primitive`
- [x] `format_dictionary`
- [x] PyPI release
- [ ] Color theme and styling system
- [ ] Utility methods


---

## Contributing

This project is currently a solo effort, but issues, suggestions, and feedback are welcome to improve this python package!

---

## License

MIT License - see `LICENSE` for details.
