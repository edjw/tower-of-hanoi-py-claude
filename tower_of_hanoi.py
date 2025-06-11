#!/usr/bin/env python3
"""
Tower of Hanoi Visual Solver

A Python-based visual Tower of Hanoi solver that demonstrates the classic
recursive algorithm through an animated GUI interface using tkinter.

This application solves the Tower of Hanoi puzzle for 3-10 disks with
colour-blind accessible visual design and smooth animations.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
from typing import List, Optional, Tuple, Generator
from enum import Enum
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tower_of_hanoi.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class PegName(Enum):
    """Enumeration for the three pegs in Tower of Hanoi."""
    SOURCE = "A"
    AUXILIARY = "B" 
    DESTINATION = "C"


@dataclass
class Move:
    """Represents a single disk movement in the Tower of Hanoi solution."""
    disk_size: int
    from_peg: PegName
    to_peg: PegName
    
    def __str__(self) -> str:
        return f"Move disk {self.disk_size} from {self.from_peg.value} to {self.to_peg.value}"


class Disk:
    """Represents a disk in the Tower of Hanoi puzzle."""
    
    def __init__(self, size: int, colour: str):
        self.size = size
        self.colour = colour
        self.x = 0
        self.y = 0
        
    def __repr__(self) -> str:
        return f"Disk(size={self.size}, colour='{self.colour}')"


class Peg:
    """Represents a peg that holds disks in the Tower of Hanoi puzzle."""
    
    def __init__(self, name: PegName):
        self.name = name
        self.disks: List[Disk] = []
        
    def push(self, disk: Disk) -> None:
        """Add a disk to the top of this peg."""
        if self.disks and disk.size >= self.disks[-1].size:
            raise ValueError(f"Cannot place disk {disk.size} on smaller disk {self.disks[-1].size}")
        self.disks.append(disk)
        
    def pop(self) -> Optional[Disk]:
        """Remove and return the top disk from this peg."""
        return self.disks.pop() if self.disks else None
        
    def peek(self) -> Optional[Disk]:
        """Return the top disk without removing it."""
        return self.disks[-1] if self.disks else None
        
    def is_empty(self) -> bool:
        """Check if this peg has no disks."""
        return len(self.disks) == 0
        
    def size(self) -> int:
        """Return the number of disks on this peg."""
        return len(self.disks)
        
    def __repr__(self) -> str:
        return f"Peg({self.name.value}: {[d.size for d in self.disks]})"


class GameState:
    """Manages the current state of the Tower of Hanoi puzzle."""
    
    def __init__(self, num_disks: int):
        self.num_disks = num_disks
        self.total_moves = (2 ** num_disks) - 1
        self.current_move = 0
        
        # Create pegs
        self.pegs = {
            PegName.SOURCE: Peg(PegName.SOURCE),
            PegName.AUXILIARY: Peg(PegName.AUXILIARY), 
            PegName.DESTINATION: Peg(PegName.DESTINATION)
        }
        
        # Colour palette for colour-blind accessibility
        self.colours = [
            "#E8F4FD",  # Light blue
            "#4A90E2",  # Blue
            "#7ED321",  # Green
            "#F5A623",  # Orange
            "#D0021B",  # Red
            "#9013FE",  # Purple
            "#50E3C2",  # Teal
            "#B8E986",  # Light green
            "#F8E71C",  # Yellow
            "#BD10E0"   # Magenta
        ]
        
        # Initialize disks on source peg (largest at bottom)
        for i in range(num_disks, 0, -1):
            colour = self.colours[i - 1] if i <= len(self.colours) else "#CCCCCC"
            disk = Disk(i, colour)
            self.pegs[PegName.SOURCE].push(disk)
            
    def execute_move(self, move: Move) -> bool:
        """Execute a move and return True if successful."""
        from_peg = self.pegs[move.from_peg]
        to_peg = self.pegs[move.to_peg]
        
        if from_peg.is_empty():
            logger.warning(f"Attempted to move from empty peg {move.from_peg.value}")
            return False
            
        disk = from_peg.peek()
        if disk is None or disk.size != move.disk_size:
            logger.warning(f"Disk size mismatch: expected {move.disk_size}, found {disk.size if disk else None}")
            return False
            
        if not to_peg.is_empty() and to_peg.peek().size < disk.size:
            logger.warning(f"Invalid move: cannot place disk {disk.size} on smaller disk {to_peg.peek().size}")
            return False
            
        # Execute the move
        moved_disk = from_peg.pop()
        to_peg.push(moved_disk)
        self.current_move += 1
        
        logger.debug(f"Move {self.current_move}: {move}")
        return True
        
    def is_solved(self) -> bool:
        """Check if the puzzle is solved (all disks on destination peg)."""
        return (self.pegs[PegName.DESTINATION].size() == self.num_disks and
                self.pegs[PegName.SOURCE].is_empty() and
                self.pegs[PegName.AUXILIARY].is_empty())
                
    def reset(self) -> None:
        """Reset the puzzle to initial state."""
        # Clear all pegs
        for peg in self.pegs.values():
            peg.disks.clear()
            
        # Reinitialize disks on source peg
        for i in range(self.num_disks, 0, -1):
            colour = self.colours[i - 1] if i <= len(self.colours) else "#CCCCCC"
            disk = Disk(i, colour)
            self.pegs[PegName.SOURCE].push(disk)
            
        self.current_move = 0


def hanoi_solver(n: int, source: PegName, destination: PegName, auxiliary: PegName) -> Generator[Move, None, None]:
    """
    Generate the sequence of moves to solve Tower of Hanoi puzzle.
    
    This is the classic recursive algorithm:
    1. Move n-1 disks from source to auxiliary peg
    2. Move the largest disk from source to destination peg  
    3. Move n-1 disks from auxiliary to destination peg
    
    Args:
        n: Number of disks to move
        source: Starting peg
        destination: Target peg
        auxiliary: Helper peg
        
    Yields:
        Move objects representing each step in the solution
    """
    if n == 1:
        yield Move(1, source, destination)
    else:
        # Move n-1 disks to auxiliary peg
        yield from hanoi_solver(n - 1, source, auxiliary, destination)
        
        # Move the largest disk to destination
        yield Move(n, source, destination)
        
        # Move n-1 disks from auxiliary to destination
        yield from hanoi_solver(n - 1, auxiliary, destination, source)


class TowerOfHanoiGUI:
    """Main GUI application for the Tower of Hanoi visual solver."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tower of Hanoi Visual Solver")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Game state
        self.game_state: Optional[GameState] = None
        self.move_generator: Optional[Generator[Move, None, None]] = None
        self.is_solving = False
        self.is_paused = False
        self.animation_speed = 500  # milliseconds between moves
        self.current_move: Optional[Move] = None  # Track current move for highlighting
        
        # GUI components
        self.setup_gui()
        
        # Keyboard bindings
        self.root.bind('<space>', lambda e: self.toggle_pause())
        self.root.bind('<r>', lambda e: self.reset_puzzle())
        self.root.bind('<Return>', lambda e: self.start_solving())
        
        self.root.focus_set()  # Enable keyboard input
        
    def setup_gui(self) -> None:
        """Initialize the GUI components."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Control panel
        control_frame = ttk.LabelFrame(main_frame, text="Controls", padding="5")
        control_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Disk count selection
        ttk.Label(control_frame, text="Number of disks:").grid(row=0, column=0, padx=(0, 5))
        
        self.disk_count_var = tk.StringVar(value="3")
        disk_spinbox = ttk.Spinbox(control_frame, from_=3, to=10, width=5, 
                                  textvariable=self.disk_count_var)
        disk_spinbox.grid(row=0, column=1, padx=(0, 10))
        
        # Animation speed control
        ttk.Label(control_frame, text="Speed:").grid(row=0, column=2, padx=(10, 5))
        
        self.speed_var = tk.StringVar(value="Normal")
        speed_combo = ttk.Combobox(control_frame, textvariable=self.speed_var, width=8,
                                  values=["Slow", "Normal", "Fast"], state="readonly")
        speed_combo.grid(row=0, column=3, padx=(0, 10))
        speed_combo.bind('<<ComboboxSelected>>', self.update_animation_speed)
        
        # Control buttons
        self.start_button = ttk.Button(control_frame, text="Start", command=self.start_solving)
        self.start_button.grid(row=0, column=4, padx=5)
        
        self.pause_button = ttk.Button(control_frame, text="Pause", command=self.toggle_pause, state="disabled")
        self.pause_button.grid(row=0, column=5, padx=5)
        
        self.reset_button = ttk.Button(control_frame, text="Reset", command=self.reset_puzzle)
        self.reset_button.grid(row=0, column=6, padx=5)
        
        self.help_button = ttk.Button(control_frame, text="Help", command=self.show_help)
        self.help_button.grid(row=0, column=8, padx=5)
        
        # Status panel
        status_frame = ttk.LabelFrame(control_frame, text="Status", padding="5")
        status_frame.grid(row=0, column=9, padx=(20, 0), sticky=(tk.W, tk.E))
        control_frame.columnconfigure(9, weight=1)
        
        self.status_label = ttk.Label(status_frame, text="Ready to start")
        self.status_label.grid(row=0, column=0)
        
        # Canvas for drawing
        self.canvas = tk.Canvas(main_frame, bg="white", relief=tk.SUNKEN, borderwidth=2)
        self.canvas.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Initialize with 3 disks
        self.reset_puzzle()
        
    def start_solving(self) -> None:
        """Start solving the puzzle."""
        if self.is_solving and not self.is_paused:
            return
            
        if not self.is_solving:
            # Start new solution
            try:
                num_disks = int(self.disk_count_var.get())
                if not (3 <= num_disks <= 10):
                    messagebox.showerror("Invalid Input", "Number of disks must be between 3 and 10")
                    return
                    
                logger.info(f"Starting new puzzle with {num_disks} disks")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number")
                return
                
            self.game_state = GameState(num_disks)
            self.move_generator = hanoi_solver(num_disks, PegName.SOURCE, PegName.DESTINATION, PegName.AUXILIARY)
            self.is_solving = True
            self.is_paused = False
            
            # Update button states
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            
        elif self.is_paused:
            # Resume solving
            self.is_paused = False
            self.pause_button.config(text="Pause")
            
        self.draw_puzzle()
        self.next_move()
        
    def toggle_pause(self) -> None:
        """Toggle pause state."""
        if not self.is_solving:
            return
            
        self.is_paused = not self.is_paused
        self.pause_button.config(text="Resume" if self.is_paused else "Pause")
        
        if not self.is_paused:
            self.next_move()
            
    def update_animation_speed(self, event=None) -> None:
        """Update animation speed based on user selection."""
        speed_map = {
            "Slow": 1000,    # 1 second between moves
            "Normal": 500,   # 0.5 seconds between moves  
            "Fast": 100      # 0.1 seconds between moves
        }
        self.animation_speed = speed_map.get(self.speed_var.get(), 500)
            
    def show_help(self) -> None:
        """Display help dialog with usage instructions."""
        help_text = """Tower of Hanoi Visual Solver

OBJECTIVE:
Move all disks from the left peg (A) to the right peg (C) following these rules:
• Only move one disk at a time
• Only the top disk from a stack can be moved
• A larger disk cannot be placed on top of a smaller disk

CONTROLS:
• Number of disks: Select 3-10 disks for the puzzle
• Speed: Choose animation speed (Slow/Normal/Fast)
• Start: Begin solving the puzzle automatically
• Pause: Pause/resume the solving animation
• Reset: Return to initial state
• Help: Show this dialog

KEYBOARD SHORTCUTS:
• Space: Pause/resume solving
• R: Reset puzzle  
• Enter: Start solving

VISUAL CUES:
• Disks are colour-coded and sized for easy identification
• The currently moving disk is highlighted with a red border
• Move count shows progress towards completion

The algorithm uses 2^n - 1 moves for n disks (optimal solution)."""

        messagebox.showinfo("Help - Tower of Hanoi", help_text)
            
    def next_move(self) -> None:
        """Execute the next move in the solution."""
        if not self.is_solving or self.is_paused:
            return
            
        try:
            move = next(self.move_generator)
            self.current_move = move  # Store for highlighting
            success = self.game_state.execute_move(move)
            
            if success:
                self.draw_puzzle()
                self.update_status()
                
                if self.game_state.is_solved():
                    self.current_move = None
                    self.finish_solving()
                else:
                    # Schedule next move
                    self.root.after(self.animation_speed, self.next_move)
            else:
                messagebox.showerror("Error", f"Invalid move: {move}")
                self.current_move = None
                self.finish_solving()
                
        except StopIteration:
            self.current_move = None
            self.finish_solving()
            
    def finish_solving(self) -> None:
        """Finish the solving process."""
        self.is_solving = False
        self.is_paused = False
        
        # Update button states
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="Pause")
        
        if self.game_state and self.game_state.is_solved():
            logger.info(f"Puzzle solved in {self.game_state.current_move} moves!")
            self.status_label.config(text=f"Solved in {self.game_state.current_move} moves!")
        else:
            logger.info("Solving stopped by user")
            self.status_label.config(text="Solving stopped")
            
    def reset_puzzle(self) -> None:
        """Reset the puzzle to initial state."""
        self.is_solving = False
        self.is_paused = False
        self.current_move = None
        
        try:
            num_disks = int(self.disk_count_var.get())
            if not (3 <= num_disks <= 10):
                num_disks = 3
                self.disk_count_var.set("3")
        except ValueError:
            num_disks = 3
            self.disk_count_var.set("3")
            
        self.game_state = GameState(num_disks)
        logger.info(f"Puzzle reset with {num_disks} disks")
        
        # Update button states
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="Pause")
        
        self.draw_puzzle()
        self.update_status()
        
    def update_status(self) -> None:
        """Update the status display."""
        if self.game_state:
            remaining = self.game_state.total_moves - self.game_state.current_move
            self.status_label.config(
                text=f"Move {self.game_state.current_move}/{self.game_state.total_moves} "
                     f"({remaining} remaining)"
            )
        else:
            self.status_label.config(text="Ready to start")
            
    def draw_puzzle(self) -> None:
        """Draw the current puzzle state on the canvas."""
        if not self.game_state:
            return
            
        self.canvas.delete("all")
        
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            # Canvas not yet properly sized, schedule redraw
            self.root.after(100, self.draw_puzzle)
            return
            
        # Calculate dimensions
        peg_width = canvas_width // 3
        peg_height = canvas_height - 100
        base_y = canvas_height - 50
        
        max_disk_size = self.game_state.num_disks
        max_disk_width = peg_width * 0.8
        disk_height = min(peg_height // (max_disk_size + 2), 30)
        
        # Draw pegs and bases
        peg_names = [PegName.SOURCE, PegName.AUXILIARY, PegName.DESTINATION]
        peg_centers = []
        
        for i, peg_name in enumerate(peg_names):
            center_x = (i + 0.5) * peg_width
            peg_centers.append(center_x)
            
            # Draw base
            base_width = peg_width * 0.9
            self.canvas.create_rectangle(
                center_x - base_width/2, base_y - 10,
                center_x + base_width/2, base_y + 10,
                fill="#8B4513", outline="#654321", width=2
            )
            
            # Draw peg post
            post_width = 8
            self.canvas.create_rectangle(
                center_x - post_width/2, base_y - peg_height,
                center_x + post_width/2, base_y,
                fill="#A0522D", outline="#654321", width=2
            )
            
            # Draw peg label
            self.canvas.create_text(
                center_x, base_y + 30,
                text=peg_name.value, font=("Arial", 14, "bold")
            )
            
        # Draw disks
        for i, peg_name in enumerate(peg_names):
            peg = self.game_state.pegs[peg_name]
            center_x = peg_centers[i]
            
            for j, disk in enumerate(peg.disks):
                disk_width = (disk.size / max_disk_size) * max_disk_width
                disk_y = base_y - (j + 1) * disk_height
                
                # Check if this disk is currently moving
                is_moving = (self.current_move and 
                           disk.size == self.current_move.disk_size and
                           j == len(peg.disks) - 1 and  # Only highlight top disk
                           peg_name == self.current_move.from_peg)
                
                # Draw disk with shadow effect
                shadow_offset = 3
                self.canvas.create_rectangle(
                    center_x - disk_width/2 + shadow_offset,
                    disk_y - disk_height/2 + shadow_offset,
                    center_x + disk_width/2 + shadow_offset,
                    disk_y + disk_height/2 + shadow_offset,
                    fill="#000000", stipple="gray25", outline=""
                )
                
                # Draw main disk with highlighting if moving
                outline_colour = "#FF6B6B" if is_moving else "#333333"
                outline_width = 4 if is_moving else 2
                
                self.canvas.create_rectangle(
                    center_x - disk_width/2, disk_y - disk_height/2,
                    center_x + disk_width/2, disk_y + disk_height/2,
                    fill=disk.colour, outline=outline_colour, width=outline_width
                )
                
                # Add disk size label
                font_weight = "bold" if is_moving else "normal"
                self.canvas.create_text(
                    center_x, disk_y,
                    text=str(disk.size), font=("Arial", 10, font_weight)
                )
                
    def run(self) -> None:
        """Start the GUI event loop."""
        # Force initial canvas update
        self.root.update()
        self.draw_puzzle()
        self.root.mainloop()


def main() -> None:
    """Main entry point for the application."""
    app = TowerOfHanoiGUI()
    app.run()


if __name__ == "__main__":
    main()