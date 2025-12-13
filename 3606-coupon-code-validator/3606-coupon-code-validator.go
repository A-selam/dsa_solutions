func alnum(r rune) bool {
    return unicode.IsLetter(r) || unicode.IsDigit(r) || r == '_'
}
func validCode(code string) bool {
    if code == ""{
        return false
    }
    for _, r := range code{
        if !alnum(r){
            return false
        }
    }
    return true
}

func businessLineCheck(businessLine string) bool {
    valid := map[string]struct{}{
        "electronics": {},
        "grocery":     {},
        "pharmacy":    {},
        "restaurant":  {},
    }

    if _, exist := valid[businessLine]; !exist {
        return false
    }
    return true
}

func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
    // collection := make([]struct{businessLine string; code string}, len(code))
    var collection []struct{businessLine string; code string}
    for i := 0; i < len(code); i++{
        if isActive[i] && validCode(code[i]) && businessLineCheck(businessLine[i]){
            curr := struct{
                businessLine string
                code string
            } {businessLine: businessLine[i], code: code[i]}
            collection = append(collection, curr)
        }
    }
    sort.Slice(collection, func(i, j int) bool {
        if collection[i].businessLine != collection[j].businessLine {
            return collection[i].businessLine < collection[j].businessLine
        }
        return collection[i].code < collection[j].code
    })

    var ans []string 
    for _, el := range collection{
        ans = append(ans, el.code)
    }
    return ans
}