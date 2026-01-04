func repeatedNTimes(nums []int) int {
    n := len(nums)
    count := make(map[int]int)
    for _, num := range nums{
        count[num]++
    }

    for key, val := range count{
        if val == int(n/2){
            return key
        }
    }
    return 0
}