func isOneBitCharacter(bits []int) bool {
    stack := []int{}
    for i := range len(bits)-1{
        if len(stack) == 0{
            if bits[i] == 1{
                stack = append(stack, 1)
            }
        } else {
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}