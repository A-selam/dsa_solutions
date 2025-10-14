func nthUglyNumber(n int, a int, b int, c int) int {
    ab := lcm(a, b)
    ac := lcm(a, c)
    bc := lcm(b, c)
    abc := lcm(ab, c)

    left := 1
    right := n * min(a, b, c)

    for left < right {
        mid := (left + right) / 2

        count := mid/a + mid/b + mid/c - mid/ab - mid/ac - mid/bc + mid/abc
        if count < n{
            left = mid+1
        } else {
            right = mid
        }
    }

    return left
}

func gcd(a,b int) int {
    for b != 0{
        a, b = b, a%b
    }
    return a
}

func lcm(a, b int) int {
    return (a * b) / gcd(a, b)
}