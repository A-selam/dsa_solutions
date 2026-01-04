func threeSum(nums []int) [][]int {
    n := len(nums)
    ans := [][]int{}
    slices.Sort(nums)

    twoSum := func(st int, target int) [][]int {
        left := st
        right := n-1
        lis := [][]int{}
        for left < right {
            if nums[left] + nums[right] == target{
                lis = append(lis, []int{nums[left], nums[right]})
                left++ 
                right--
                for left < right && nums[left] == nums[left-1]{
                    left++
                }
                for left < right && nums[right] == nums[right+1]{
                    right--
                }
            } else if nums[left] + nums[right] < target {
                left++
            } else {
                right--
            }
        }
        return lis
    }   

    for i, num := range nums{
        if i > 0 && nums[i] == nums[i-1]{
            continue
        }

        temp := twoSum(i+1, 0-num)
        if len(temp) != 0{
            for _, t := range temp{
                ans = append(ans, []int{num, t[0], t[1]})
            }
        }
    }

    return ans
}