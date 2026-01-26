func isValid(s string) bool {
    close := make(map[rune]rune)
    close[')'] = '('
    close[']'] = '['
    close['}'] = '{'

    stack := []rune{}
    for _, char := range s{
        if char == '(' || char == '[' || char == '{'{
            stack = append(stack, char)
        } else {
            if len(stack) == 0 {
                return false
            }
            if stack[len(stack)-1] != close[char]{
                return false
            } else {
                stack = stack[:len(stack)-1]
            }
        }
    }
    if len(stack) != 0{
        return false
    }
    return true
}