__author__ = 'James Cunningham, Adriana Jergusova'


import Pair_project_7_James_C
import random as r
import pytest

# Test case for the is_satisfied function
def test_is_satisfied():
    grid = [
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ]

    # Test for a red square (0) surrounded by blue squares (1)
    satisfied, satisfaction = Pair_project_7_James_C.is_satisfied(0, 0, 0, grid)
    assert satisfied == False  # It should not be satisfied (not enough red neighbors)
    assert satisfaction == (1/3)  # No matching neighbors, so satisfaction is 0%

    # Test for a blue square (1) surrounded by a mix of colors
    satisfied, satisfaction = Pair_project_7_James_C.is_satisfied(1, 0, 1, grid)
    assert satisfied == False  
    assert satisfaction == .5  #neighbors match (satisfaction = .5)

    # Test for an empty square (2) surrounded by other empty squares
    satisfied, satisfaction = Pair_project_7_James_C.is_satisfied(2, 2, 2, grid)
    assert satisfied == False  
    assert satisfaction == 0  

# Test case for grid initialization (testing grid creation with valid values)
def test_initialize_grid():
    grid = Pair_project_7_James_C.initialize_grid(5, 5, 40, 40, 20)
    
    # Check that the grid is of the expected size
    assert len(grid) == 5  # Rows
    assert len(grid[0]) == 5  # Columns
    
    # Check if the grid contains valid values (0 = red, 1 = blue, 2 = empty)
    valid_values = {0, 1, 2}
    for row in grid:
        for cell in row:
            assert cell in valid_values  # All cells must be either 0, 1, or 2

# Test edge case where grid has only empty spaces (2)
def test_empty_grid_satisfaction():
    grid = [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
    ]
    
    # Test for an empty grid (all cells are 2)
    satisfied, satisfaction = Pair_project_7_James_C.is_satisfied(1, 1, 2, grid)  # Center cell, which is empty
    assert satisfied == True  # Should be satisfied (no neighbors to compare)
    assert satisfaction == 100  # No neighbors to compare, 100% satisfaction

if __name__ == "__main__":
    pytest.main()
