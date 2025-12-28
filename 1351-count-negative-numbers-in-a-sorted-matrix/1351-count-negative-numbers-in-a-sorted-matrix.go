func countNegatives(grid [][]int) int {
    cnt := 0
    n := len(grid)
    m := len(grid[0])
    for i := range n{
        for j := range m{
            if grid[i][j] < 0{
                cnt++
            }
        }
    }
    return cnt
}