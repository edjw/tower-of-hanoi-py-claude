# Product Requirements Document: Tower of Hanoi Visual Solver

## 1. Introduction/Overview

**Feature:** A Python-based visual Tower of Hanoi solver that demonstrates the classic recursive algorithm through an animated GUI interface.

**Problem:** This project serves as a test case for Large Language Model (LLM) code generation capabilities. Research suggests LLMs struggle to solve Tower of Hanoi problems directly, but they may be capable of writing code that implements the solution algorithm.

**Goal:** Create a lightweight, maintainable Python application that visually solves the Tower of Hanoi puzzle with 3-10 disks, demonstrating both algorithmic problem-solving and accessible visual design.

## 2. Goals

- **Primary:** Demonstrate LLM capability to generate working Tower of Hanoi solving code
- **Secondary:** Create an educational tool that visually demonstrates the recursive algorithm
- **Tertiary:** Implement accessibility best practices for colour-blind users
- **Technical:** Showcase good Python coding practices in a single-file application

## 3. User Stories

**As a user, I want to:**

- Input the number of disks (3-10) via a GUI input field so that I can customise the puzzle complexity
- Watch the algorithm solve the puzzle step-by-step so that I can understand the recursive solution process
- See the current move count and remaining moves so that I can track progress towards completion
- Distinguish between different disk sizes through colour-blind accessible visual design so that the puzzle is usable regardless of colour vision
- Start, pause, and reset the solving animation so that I can control the learning experience

**As a developer, I want to:**

- Maintain the code easily in a single Python file so that deployment and distribution are straightforward
- Follow Python best practices so that the code is readable and maintainable
- Test LLM code generation capabilities on a classic computer science problem

## 4. Functional Requirements

### 4.1 Core Algorithm

- Implement recursive Tower of Hanoi solving algorithm for 3-peg configuration
- Calculate optimal solution path (2^n - 1 moves) for n disks
- Execute moves in correct sequence from source to destination peg

### 4.2 User Interface

- GUI input field for selecting number of disks (3-10)
- Three pegs displayed vertically with base platforms
- Disks rendered as different sizes (largest at bottom, smallest at top)
- Start/Pause/Reset control buttons
- Real-time display of current move count and total moves remaining

### 4.3 Visual Display

- Animated disk movement between pegs
- Colour-blind accessible colour scheme for disk differentiation
- Smooth transitions between moves
- Clear visual hierarchy (largest to smallest disks)

### 4.4 Performance

- Responsive animation for up to 10 disks (maximum 1,023 moves)
- Adjustable animation speed or step-through capability
- Efficient rendering without performance degradation

## 5. Non-Goals (Out of Scope)

- Multi-peg variants (4+ pegs) of Tower of Hanoi
- Manual puzzle-solving mode (user-controlled disk movement)
- Disk counts above 10 (to avoid excessive move counts)
- Web-based deployment or browser integration
- Save/load puzzle states
- Multiple solving algorithms or strategy comparisons
- Audio feedback or sound effects
- Networking or multi-user features

## 6. Technical Considerations

### 6.1 Python Libraries

- **GUI Framework:** tkinter (built into Python, lightweight, cross-platform)
- **Alternative:** pygame (if more advanced graphics needed)
- **No external dependencies preferred** for easy distribution

### 6.2 Architecture

- Single Python file structure for simplicity
- Separation of concerns: algorithm logic, GUI rendering, event handling
- Object-oriented design with classes for Disk, Peg, and Game state
- Type hints throughout for code clarity

### 6.3 Algorithm Implementation

- Recursive function for move calculation
- State management for tracking disk positions
- Move validation and execution system
- Animation queue for smooth visual transitions

## 7. Design Considerations

### 7.1 Accessibility

- **Colour-blind friendly palette:** Use colours that remain distinguishable with common colour vision deficiencies
- **Size differentiation:** Disks must be clearly distinguishable by size even without colour
- **High contrast:** Ensure adequate contrast ratios for visibility

### 7.2 User Experience

- **Intuitive controls:** Clear labelling and logical button placement
- **Visual feedback:** Immediate response to user actions
- **Error handling:** Graceful handling of invalid input values
- **Responsive design:** GUI adapts to different disk counts appropriately

### 7.3 Visual Design

- Clean, minimalist interface focusing on the puzzle
- Clear visual representation of the three pegs
- Smooth, natural-looking disk movement animations
- Consistent spacing and proportions

## 8. Success Metrics

### 8.1 Functional Success

- Algorithm correctly solves all disk configurations (3-10)
- Zero incorrect moves in solution sequence
- Accurate move counting and progress tracking

### 8.2 Code Quality Success

- Single Python file under 500 lines
- Comprehensive type hints and docstrings
- No external dependencies beyond Python standard library
- Code passes common Python linting tools (pylint, flake8)

### 8.3 User Experience Success

- Colour-blind users can distinguish all disks
- Application launches and runs without errors on macOS
- Intuitive operation requiring no documentation

### 8.4 Research Success

- Demonstrates LLM capability to generate working recursive algorithm code
- Code implements correct Tower of Hanoi solution logic
- Validates LLM understanding of classic computer science problems

## 9. Open Questions

- **Performance optimisation:** Should larger disk counts (8-10) have accelerated animation modes?
- **Error handling:** How should the application handle edge cases like system resource constraints?
- **Distribution:** Should the final application be packaged as an executable or remain as a Python script?
- **Testing strategy:** What level of automated testing is appropriate for a single-file educational tool?

---

**Document Version:** 1.0
**Created:** 06/11/2025
**Target Audience:** Development team familiar with Python, GUI applications, and recursive algorithms
