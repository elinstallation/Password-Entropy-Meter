


# Password Entropy Meter

A simple desktop tool that calculates the Shannon entropy of a password and displays the result in a live-updating GUI built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

## Demo
https://github.com/user-attachments/assets/0261dda3-d715-4f10-bb5a-aef6bada0977

## Features

- Calculates entropy (bits per character) based on the character distribution of the entered password
- Live updates as you type — no need to press a button
- Color-coded strength indicator: **WEAK** (red), **MODERATE** (orange), **STRONG** (green)
- Progress bar that fills and changes color based on strength
- Displays password length and number of unique characters
- All output values are clamped to avoid negative numbers

## File Structure

```
.
├── main.py   # Entropy calculation logic
└── gui.py    # CustomTkinter GUI
```

## Requirements

- Python 3.8+
- [customtkinter](https://pypi.org/project/customtkinter/)

Install dependencies with:

```bash
pip install customtkinter
```

## Usage

Run the GUI:

```bash
python gui.py
```

Type a password into the entry field. The entropy score, strength label, progress bar, length, and unique character count will update automatically as you type.

## How Entropy is Calculated

The entropy calculation is based on **Shannon entropy**, which measures the average information content (in bits) per character, based on how often each character appears in the password.

For a password of length `n` with character frequencies `p₁, p₂, ..., pₖ`, the per-character entropy is:

```
H = -Σ (pᵢ × log₂(pᵢ))
```

A higher value means the characters in the password are more evenly distributed (less repetition), which generally indicates a less predictable password.

`calculate_entropy()` in `main.py` returns a dictionary with:

| Key                | Description                                      |
|--------------------|---------------------------------------------------|
| `length`           | Number of characters in the password              |
| `unique_chars`     | Number of distinct characters                     |
| `per_char_entropy` | Shannon entropy in bits per character             |
| `total_entropy`    | `per_char_entropy × length` (total information content) |

> **Note:** This metric reflects the randomness of the characters *within the password itself*, not a brute-force resistance estimate based on a full character set (e.g. lowercase/uppercase/digits/symbols). A password with a lot of repeated characters will score lower even if it's long.

## Customization

- **Strength thresholds**: edit the `get_strength()` function in `gui.py` to change the entropy cutoffs for WEAK/MODERATE/STRONG.
- **Progress bar scale**: the bar fills based on `entropy / 4.0`. Adjust the `4.0` divisor to change what counts as a "full" bar.
- **Colors**: change `COLOR_WEAK`, `COLOR_MODERATE`, and `COLOR_STRONG` at the top of `gui.py`.
- **Window size**: change `root.geometry("320x300")` in `gui.py` to resize the window (format is `"widthxheight"` in pixels).
