func minimumDeleteSum(s1 string, s2 string) int {
    n := len(s1)
    m := len(s2)
    memo := make([][]int, n)    
    for i, _ := range s1{
        memo[i] = make([]int, m)
    }

    for i := range n{
        for j := range m{
            memo[i][j] = -1
        }
    }
    
    var dp func(i, j int) int 
    dp = func(i int, j int) int {
        if i == n {
            temp := 0
            for t := j; t < m; t++{
                temp += int(s2[t])
            }
            return temp
        }
        if j == m {
            temp := 0
            for t := i; t < n; t++{
                temp += int(s1[t])
            }
            return temp
        }

        if memo[i][j] != -1 {
            return memo[i][j]
        }

        if s1[i] == s2[j] {
            return dp(i+1, j+1)
        }

        cost1 := int(s1[i]) + dp(i+1, j)
        cost2 := int(s2[j]) + dp(i, j+1)

        memo[i][j] = min(cost1, cost2)
        return memo[i][j]
    }

    return dp(0, 0)
}
