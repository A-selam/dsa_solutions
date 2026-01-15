func Max (a, b int) int {
    if a > b {
        return a
    } 
    return b
}
func Min (a, b int) int {
    if a < b {
        return a
    } 
    return b
}

func widest(bars []int) int {
    lon := 1
    curr := 1
    sort.Ints(bars)

    for i, val := range bars {
        if i == 0 {
            continue
        }
        if val == bars[i-1]+1{
            curr++
        } else {
            curr = 1
        }
        lon = Max(lon, curr)
    }

    return lon+1
}

func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
    mHor := widest(hBars)
    mVer := widest(vBars)

    side := Min(mHor, mVer)
    return side * side
}