func anagramCheck(word1 string, word2 string) bool {
        freq := make([]int, 26)
        for _, r := range word1{
            freq[int(r)-97] += 1
        }
        for _, r := range word2{
            freq[int(r)-97] -= 1
        }
        for _, f := range freq{
            if f != 0 {
                return false
            }
        }
        return true
    }

func removeAnagrams(words []string) []string {
    n := len(words)
    ans := []string{words[0]}

    for i := 1; i < n; i++ {
        if anagramCheck(words[i], words[i-1]) {
            continue
        }
        ans = append(ans, words[i])
    }
    
    return ans
}