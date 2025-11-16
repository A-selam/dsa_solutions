func numSub(s string) int {
    left := 0
    ans := 0
    for right := range len(s){
        if s[right] == '0'{
            left = right + 1
        } else {
            ans += right - left + 1
        }
    }  
    return ans % int(math.Pow(10, 9) + 7)
}