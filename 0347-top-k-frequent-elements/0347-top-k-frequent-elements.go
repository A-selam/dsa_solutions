type pair struct {
    key int
    val int
}

func topKFrequent(nums []int, k int) []int {
    counted := make(map[int]int)
    for _, num := range nums{
        counted[num] += 1
    }   

    paired := []pair{} 
    for key, val := range counted {
        paired = append(paired, pair{key, val})
    }
    sort.Slice(paired, func(i, j int)bool {
        return paired[i].val > paired[j].val
    })

    ans := []int{}
    for i := 0; i < k; i++ {
        ans = append(ans, paired[i].key)
    }

    return ans
}