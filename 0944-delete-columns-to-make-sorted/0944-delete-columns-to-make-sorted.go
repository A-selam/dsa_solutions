func minDeletionSize(strs []string) int {
    count := 0
    len_s := len(strs[0])
    n := len(strs)

    for j := 0; j < len_s; j++{
        prev := 'a'
        for i := 0; i < n; i++{
            if prev > rune(strs[i][j]){
                count++
                break
            }
            prev = rune(strs[i][j])
        }
    }
    return count 
}