
void dfs(char** grid, int gridSize, int* gridColSize, int row, int col) {
    // Boundary check and if cell is water ('0'), return
    if (row < 0 || row >= gridSize || col < 0 || col >= gridColSize[row] || grid[row][col] == '0')
        return;

    grid[row][col] = '0';

    // Explore all 4 directions
    dfs(grid, gridSize, gridColSize, row + 1, col);
    dfs(grid, gridSize, gridColSize, row - 1, col);
    dfs(grid, gridSize, gridColSize, row, col + 1);
    dfs(grid, gridSize, gridColSize, row, col - 1);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int count = 0;

    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] == '1') {
                count++;
                dfs(grid, gridSize, gridColSize, i, j);
            }
        }
    }

    return count;
}
