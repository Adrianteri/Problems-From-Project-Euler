package main 

import (
    "google.golang.org/api/iterator"
    "fmt"
    "math/big"
)


func expBy2(base, power *big.Int) {
	result := big.NewInt(1)
	zero := big.NewInt(0)
	
	for power != zero {
		if modBy2(power) != zero {
			mutiply(result, base)
		}
		power = divideBy2(power)
		base = mutiply(base, base)
	}
}

func modBy2( x *big.Int) *big.Int{
	return big.NewInt(0).Mod(x, big.NewInt(2))
}

func mutiply(x, y *big.Int) *big.Int {
	return big.NewInt(0).Mul(x,y)	
}

func divideBy2(x *big.Int) *big.Int {
	return big.NewInt(0).Div(x, big.NewInt(2))
}


func main() {
	var counter := 
	for i := range []{
		fmt.Println(i)

	}


}