import Foundation
// MARK: printing

// Print Hello World!
print("Hello World!")

// Print 2 to the 65536 power
print(pow(2.0, 65536.0)) //prints "inf"

// String interpolation
// let for constant, var for variable
let a = "A"
let b = 7
// Print "A:7"
print("\(a):\(b)")

// Print 5 + "7"
let x = 5
let y = "7"

// Int(y) could produce nil, so unwrap it then add
if let y = Int(y) {
    print("\(x + y)")
}

// MARK: Lists (arrays)

// Swift is type-safe so the variable x above can't be mutated to an array, it must remain an Integer value
var arrayX = [1, 2, 3]
var arrayY = [8, 9, 10]

// Change x so that it is [1, 2, 3, 4]
arrayX.append(4)
print(arrayX)

// Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
arrayX.append(contentsOf: arrayY)
print(arrayX)

// Change x so that it is [1, 2, 3, 4, 9, 10]

// remove value at 4, shifting elements
arrayX.remove(at: 4)
// -OR-
// $0 is anonymous placeholder - this will do nothing since all instances of 8 have already been removed
arrayX.removeAll(where: { $0 == 8 })
print(arrayX)

// Change x so that it is [1, 2, 3, 4, 9, 99, 10]
arrayX.insert(99, at: 5)
print(arrayX)

// Print the length of arrayX
print(arrayX.count)

// Print all values in arrayX multiplied by 1k
for num in arrayX {
    print(num*1000)
}

// MARK: Tuples

func dist(a: (Int, Int), b: (Int, Int)) -> Double {
    let x0 = a.0
    let y0 = a.1

    let x1 = b.0
    let y1 = b.1

    let val1 = (x1 - x0) * (x1 - x0)
    let val2 = (y1 - y0) * (y1 - y0)

    return sqrt(Double(val1) + Double(val2))
}

let tupleA = (2,7)
let tupleB = (-14,72)

print("The distance is: \(dist(a: tupleA, b: tupleB))")

// <T> is generic, it could be any type
func printTuple<T>(t:T) {
    // Mirror gives us the parts of an instance
    let mirror = Mirror(reflecting: t)
    // get the values
    let elements = mirror.children.map( { $0.value })
    print(elements)
}

let mixedTuple = ("A",7,6)

printTuple(t: mixedTuple)
