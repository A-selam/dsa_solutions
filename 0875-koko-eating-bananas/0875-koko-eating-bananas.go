func minEatingSpeed(piles []int, h int) int {
    left := 1
    right := slices.Max(piles)
    ans := 0
    
    for left <= right {
        mid := int((left + right) / 2)

        total := 0
        for _, count := range piles{
            total += int(math.Ceil(float64(count) / float64(mid)))
        }

        if total <= h{
            ans = mid
            right = mid-1
        } else {
            left = mid+1
        }
    }

    return ans 
}