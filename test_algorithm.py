#!/usr/bin/env python3
"""
Simple test to verify the Tower of Hanoi algorithm is working correctly.
"""

from tower_of_hanoi import hanoi_solver, PegName, GameState

def test_hanoi_algorithm():
    """Test the hanoi_solver algorithm for correctness."""
    
    for n in [3, 4, 5, 20]:  # Test with 3, 4, 5, and 20 disks
        print(f"\nTesting with {n} disks:")
        
        # Create game state
        game_state = GameState(n)
        
        # Generate solution moves
        moves = list(hanoi_solver(n, PegName.SOURCE, PegName.DESTINATION, PegName.AUXILIARY))
        
        print(f"Generated {len(moves)} moves")
        print(f"Expected {(2**n) - 1} moves")
        
        # Verify correct number of moves
        assert len(moves) == (2**n) - 1, f"Wrong number of moves for {n} disks"
        
        # Execute all moves
        for i, move in enumerate(moves):
            success = game_state.execute_move(move)
            if not success:
                print(f"Failed to execute move {i+1}: {move}")
                print(f"Game state: {game_state.pegs}")
                return False
        
        # Verify puzzle is solved
        if game_state.is_solved():
            print(f"✓ Successfully solved {n}-disk puzzle in {len(moves)} moves")
        else:
            print(f"✗ Failed to solve {n}-disk puzzle")
            print(f"Final state: {game_state.pegs}")
            return False
    
    print("\n✓ All tests passed!")
    return True

if __name__ == "__main__":
    test_hanoi_algorithm()