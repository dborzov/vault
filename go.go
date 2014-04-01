i :=3
p= &i   // pointer to i, p would be of type *int
var p *string = &s // would assign the address of the s object to p
fmt.Printf(*p) // get pointer value