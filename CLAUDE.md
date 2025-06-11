# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Tower of Hanoi Visual Solver - A Python-based educational application that visually demonstrates the classic recursive Tower of Hanoi algorithm through an animated tkinter GUI interface. This project serves as a test case for LLM code generation capabilities on classic computer science problems.

## Architecture

**Single-file Application Design:**

- `tower_of_hanoi.py` - Complete application with all functionality (algorithm, GUI, animation)
- Object-oriented design with clear separation: algorithm logic, state management, GUI rendering
- Type hints throughout using Python 3.8+ typing features
- British English throughout codebase (colour, optimise, centre)

**Core Components:**

- `hanoi_solver()` - Recursive algorithm generator yielding Move objects
- `GameState` - Manages puzzle state, move validation, and progress tracking
- `TowerOfHanoiGUI` - Main application class handling tkinter interface and animation
- `Disk`, `Peg`, `Move` classes - Data structures with clear responsibilities

## Common Development Commands

**Run the application:**

```bash
python3 tower_of_hanoi.py
```

**Run algorithm tests:**

```bash
python3 test_algorithm.py
```

## Code Conventions

- **Dependencies:** Standard library only (tkinter for GUI, no external packages)
- **Code Style:** PEP 8 compliant, comprehensive docstrings for educational value
- **Type Safety:** Full type annotations using typing module
- **Architecture Pattern:** Model-View-Controller separation within single file
- **Target:** Under 600 lines total (expanded from original 500 due to added features)
- **Logging:** Built-in logging system for debugging and development tracking

## Key Implementation Details

**Algorithm Implementation:**

- Classic recursive Tower of Hanoi using generator pattern for move sequences
- Move validation ensures puzzle rules are maintained throughout execution
- State management tracks disk positions and validates legal moves

**Animation System:**

- Uses `tkinter.after()` for non-blocking smooth animations
- Colour-blind accessible palette with size-based disk differentiation
- Canvas-based custom drawing for pegs, bases, and animated disk movements

**GUI Features:**

- Disk count selection (3-10 disks) with input validation
- Animation speed control (Slow/Normal/Fast) with real-time adjustment
- Start/Pause/Resume/Reset controls with proper state management
- Built-in help system with comprehensive usage instructions
- Real-time move counting and progress display
- Visual feedback highlighting currently moving disk with red border
- Keyboard shortcuts (Space: pause/resume, R: reset, Enter: start)

## Testing Strategy

- `test_algorithm.py` validates algorithm correctness for 3, 4, 5, and 20 disk configurations
- Tests verify exact move count (2^n - 1) and successful puzzle completion
- Manual GUI testing for animation smoothness and user experience

## Performance Considerations

- Optimised for smooth animation up to 10 disks (1,023 moves maximum)
- Efficient canvas redrawing with proper dimension calculations
- Animation speed configurable via GUI controls (Slow: 1000ms, Normal: 500ms, Fast: 100ms)

## Accessibility Requirements

- Colour-blind friendly palette using distinct, accessible colours
- Size-based disk differentiation as primary visual cue
- High contrast design for visibility
- Keyboard accessibility for all main functions
