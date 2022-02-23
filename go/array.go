package main
import "fmt"


/*
Array in go is rarely used. Because:
* Size of array is treated as type [3]int != 4[int]
* Size of array can not be defined by var (since it must be known at compile-time)
*/
var x = [3]int
var x = [3]int{10,20,30}
var x = [6]]int{1,5:4} // {1,0,0,0,0,4} sparse array
var x = [...]int{10,20,30}

func main(){
	var x = [...]int{10,20,30}
	var y = [3]int{10,20,30}
	fmt.Println(x == y) // compare array
}


