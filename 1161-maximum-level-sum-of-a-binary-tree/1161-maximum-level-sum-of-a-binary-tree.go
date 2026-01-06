/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type temp struct {
    node *TreeNode
    level int
}

func maxLevelSum(root *TreeNode) int {
    gr := make(map[int]int)

    dfs := func(st *TreeNode)  {
        stack := []temp{{st, 1}}
        for len(stack) != 0{
            curr := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            gr[curr.level] += curr.node.Val

            if curr.node.Left != nil {
                stack = append(stack, temp{curr.node.Left, curr.level+1})
            }
            if curr.node.Right != nil {
                stack = append(stack, temp{curr.node.Right, curr.level+1})
            }
        }
    }

    dfs(root)
    ans := 0
    sc := int(math.Inf(-1))
    for level, val := range gr{
        if val > sc{
            ans = level
            sc = val
        }
    }
    return ans
}