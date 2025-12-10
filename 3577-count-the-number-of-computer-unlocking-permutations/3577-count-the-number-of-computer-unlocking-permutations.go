func count(comp []int, target int) bool{
    count := 1
    for _, val := range comp{
        if val == target{
            count -= 1
        }
    }
    return count == 0
}

func factorials(MOD int) []int{
    factorial := make([]int, int(math.Pow(10, 5)+2))
    factorial[1] = 1
    factorial[2] = 2
    for i := 2; i <= int(math.Pow(10, 5))+1; i++{
        factorial[i] = (factorial[i-1] * i) % MOD
    }

    return factorial
}

func countPermutations(complexity []int) int {
    MOD := int(math.Pow(float64(10), 9)) + 7
    factorial := factorials(MOD)

    first := complexity[0]
    if slices.Min(complexity) != first{
        return 0
    }
    if !count(complexity, first){
        return 0
    }

    return factorial[len(complexity)-1]
}