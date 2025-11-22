func minimumOperations(nums []int) int {
    ans := 0
    for _, num := range nums {
        temp := num % 3
        ans += min(temp, 3 - temp)
    }
    return ans
}