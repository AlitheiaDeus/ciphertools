# Cipher Tools

A collection of cipher and cryptanalysis tools for educational exploration and puzzle solving.

---

## Subdirectories & Tools

### [ascii_morse/](./ascii_morse)
A high-performance algorithmic solver for **unspaced (continuous / "smooshed") Morse code**—the quintessential `r/morsecode` puzzle where dots and dashes are chained into a single unsegmented stream without spaces.

- Indexes words into a **Morse-Word Trie** with beam search and unigram log-probabilities.
- Prunes degenerate single-letter noise (`ETTTETEE`).
- Evaluates Standard, Inverted, Reversed, and Inverted-Reversed signal variants.
- Outputs ranked permutations directly to `.txt` files with optional LLM prompt wrappers.

See [ascii_morse/README.md](./ascii_morse/README.md) for full usage and CLI reference.

---

## Root Utilities
- `ciphers.py`: Classic ciphers (Caesar, Reverse, Atbash).
- `decodebox.py`: Character frequency analysis.
- `selector.py`: Cipher selection and parsing utilities.
