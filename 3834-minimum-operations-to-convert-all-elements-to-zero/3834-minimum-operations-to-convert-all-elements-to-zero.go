func minOperations(nums []int) int {
    ans := 0
    stack := []int{0}

    for _, num := range nums {
        for len(stack) > 0 && stack[len(stack)-1] > num {
            stack = stack[:len(stack)-1]
        } 
        if len(stack) == 0 || stack[len(stack)-1] < num {
            ans++
            stack = append(stack, num)
        }
    }

    return ans
}