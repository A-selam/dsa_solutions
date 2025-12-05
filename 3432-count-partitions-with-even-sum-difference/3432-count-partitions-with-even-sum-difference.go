func sum(nums []int) int {
    sum := 0
    for _, num := range nums {
        sum += num
    }
    return sum
}
func countPartitions(nums []int) int {
    temp := nums[0]
    ans := 0
    sum := sum(nums)-nums[0]
    for i := 1; i < len(nums); i++{
        if int(math.Abs(float64(sum - temp))) % 2 == 0{
            ans += 1
        }
        temp += nums[i]
        sum -= nums[i]
    }
    return ans
}