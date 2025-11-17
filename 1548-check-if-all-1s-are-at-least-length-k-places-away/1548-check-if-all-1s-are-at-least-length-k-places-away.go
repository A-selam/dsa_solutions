func kLengthApart(nums []int, k int) bool {
    left := -1
    for i := range len(nums){
        if nums[i] == 1 {
            if left != -1 {
                if i - left - 1 < k {
                    return false
                }
            }
            left = i
        }
    }
    return true
}