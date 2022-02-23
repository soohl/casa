/*
Unlike array, size of the slice is not defined as a type
*/
var x = []int{10, 20, 30} // [] is slice 
var x = [][]int // multidimensional

x == nil // nil != null. nil represents lack of value for some types

var x []int 
x = append(x,10) //append(slice, value)

x := make([]int, 5) // int slice with len of 5 and capacity of 5
// [0,0,0,0,0]
x := make([]int, 5,10) // int slice with len of 5 and capacity of 10

x := []int{1,2,3,4}
y := x[:2] // {1,2}
/*
Subslice sometime share memory with parent slice
Alterning child slice can alter parent slice. 
Therefore, do not append to subslice. 
Use full slice expression
*/ 
y = :=x[:2,2] // capacity specified = full slice expression

x := []int{1,2,3,4}
y := make([]int, 4) // int slice with len of 4 and capacity of 5
num := copy(y,x) // copy, no memory share. Return # of elements copied.


