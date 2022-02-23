var s string = "hello there"
var b byte = s[6]
var s2 string = s[:5] // sliced by byte

var a rune = 'x' // rune = 32 bit integer value (not type)
var s string = string(a)

// page 51