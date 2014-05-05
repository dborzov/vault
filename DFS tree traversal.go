type Tree struct {
    Left, Right *Tree
    Value int
}

func Walk(t *tree.Tree) {
    if t.Left != nil {
        Walk(t.Left)
    }
    fmt.Println(t.Value)
    if t.Right != nil {
        Walk(t.Right)
    }
}

func main() {
    Walk(tree.New(1))
}