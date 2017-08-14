class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # The approach is to traverse 'grid' from top-to-bottom and left-to-right.
        # If we find 1, we increment 'island' variable by 1, and
        # check if one cell right (if any) is 1, and 
        # check if one cell below (if any) is 1.
        # If we find a 1 in a cell, we increment 'neighbour' variable by 1.
        # Then, we multiply 4 to 'island' and 2 to 'neighbour'.
        # Finally, we return difference of island*4 and neighbour*2.
         
        island = 0
        neighbour = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    island += 1
                
                    if (i != len(grid)-1 and grid[i+1][j] == 1):
                        neighbour += 1
                    if (j != len(grid[i])-1 and grid[i][j+1] == 1):
                        neighbour += 1
        
        print island
        print neighbour
        return 4*island - 2*neighbour
        