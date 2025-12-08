func countTriples(n int) int {
    ans := 0
    for i := 1; i <= n; i++{
        for j := 1; j <= n; j++{
            // for k := 1; k <= n; k++{
                k := int(math.Sqrt(float64((i*i) + (j*j))))
                if k <= n && k*k == (i*i) + (j*j){
                    ans += 1
                }
            // }
        }
    }    
    return ans
}