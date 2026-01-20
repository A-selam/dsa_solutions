func minBitwiseArray(nums []int) []int {
    ans := []int{}
    for _, num := range nums{
        ans = append(ans, ansI(num))
    }

    return ans
}

func ansI(num int) int {
    temp := -1
    for can := num-1; can >= 0; can-- {
        if (can | (can+1)) == num{
            temp = can
        }
    }
    return temp
}