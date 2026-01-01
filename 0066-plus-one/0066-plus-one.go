func plusOne(digits []int) []int {
    slices.Reverse(digits)
    
    carry := 0
    if digits[0] == 9{
        digits[0] = 0
        carry = 1
    } else {
        digits[0]++
    }

    for i, val := range digits{
        if i == 0{
            continue
        } else {
            if val + carry == 10{
                digits[i] = 0
                carry = 1
            } else {
                digits[i] += carry
                carry = 0
            }
        }
    }
    if carry == 1{
        digits = append(digits, 1)
    }
    slices.Reverse(digits)
    return digits
}