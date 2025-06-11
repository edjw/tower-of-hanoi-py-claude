# Tower of Hanoi Visual Solver

A Python-based visual Tower of Hanoi solver that demonstrates the classic recursive algorithm through an animated GUI interface using tkinter.

## Features

- Visual solving of Tower of Hanoi puzzles with 3-10 disks
- Colour-blind accessible design with distinct colours and size differentiation
- Smooth animated transitions between moves with adjustable speed (Slow/Normal/Fast)
- Real-time move counting and progress tracking
- Visual feedback highlighting the currently moving disk
- Start, pause, and reset controls with built-in help system
- Keyboard shortcuts (Space to pause/resume, R to reset, Enter to start)
- Comprehensive logging for debugging and development

## Requirements

- Python 3.8 or higher
- tkinter (included with most Python installations)
- No external dependencies required

## Usage

```bash
python3 tower_of_hanoi.py
```

### Controls

- **Number of disks**: Select between 3-10 disks using the spinbox
- **Speed**: Choose animation speed (Slow/Normal/Fast)
- **Start**: Begin solving the puzzle
- **Pause/Resume**: Pause or resume the solving animation
- **Reset**: Reset the puzzle to initial state
- **Help**: Display comprehensive usage instructions

### Keyboard Shortcuts

- `Space`: Toggle pause/resume
- `R`: Reset puzzle
- `Enter`: Start solving

## Algorithm

The application implements the classic recursive Tower of Hanoi algorithm:

1. Move n-1 disks from source to auxiliary peg
2. Move the largest disk from source to destination peg
3. Move n-1 disks from auxiliary to destination peg

The solution always takes exactly 2^n - 1 moves for n disks.

## Testing

Run the algorithm test to verify correctness:

```bash
python3 test_algorithm.py
```

## Design Considerations

- **Accessibility**: Uses a colour-blind friendly palette with distinct colours
- **Performance**: Optimised for smooth animation up to 10 disks (1,023 moves)
- **User Experience**: Intuitive controls with visual feedback and built-in help system
- **Code Quality**: Single file implementation with comprehensive type hints and logging

## Educational Value

This solver demonstrates:

- Recursive algorithm implementation
- GUI programming with tkinter
- Object-oriented design principles
- Accessibility considerations in software design
- Performance optimisation for animations
