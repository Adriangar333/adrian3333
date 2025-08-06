# Optimized Billiard Game

This repository contains a simple and optimized billiard simulation written in
Python. The game uses **pygame** for graphics but can also run a headless
simulation for testing purposes.

## Requirements

- Python 3.8+
- `pygame` (optional, for graphical gameplay)

## Usage

Run a quick physics simulation without graphics:

```bash
python billiard.py --simulate 60
```

If `pygame` is installed and a display is available, play the game:

```bash
python billiard.py
```
