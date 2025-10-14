func hasIncreasingSubarrays(nums []int, k int) bool {
    n := len(nums)
    arr := make([]int, n)
    arr[0] = 1

    for i:= 1; i < n; i++{
        if nums[i] > nums[i-1]{
            arr[i] += arr[i-1] + 1
        } else {
            arr[i] = 1
        }
        
        if i >= k && arr[i] >= k && arr[i-k] >= k{
            return true
        }
    }
    
    return false
}