func minimumBoxes(apple []int, capacity []int) int {
    total := 0
    for _, num := range apple{
        total += num
    }

    slices.Sort(capacity)
    slices.Reverse(capacity)

    count := 0
    i := 0
    for total > 0{
        total -= capacity[i]
        count += 1
        i++
    }

    return count
}