func maximumHappinessSum(happiness []int, k int) int64 {
    slices.Sort(happiness)
    slices.Reverse(happiness)
    var ans int64
    i := 0
    // c := 0
    for j := range k{
        if happiness[i] - j <= 0{
            break
        }
        ans += int64(happiness[i] - j)
        // c++
        i++
    }
    
    return ans
}