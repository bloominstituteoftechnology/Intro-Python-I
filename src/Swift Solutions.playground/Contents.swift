import UIKit

// 1.  Print "Hello, world!" to your terminal
print("Hello, World!")

// 2. Print out 2 to the 65536 power

print(pow(Double(2), Double(65536))) // Doesn't work.. Too large of a number.


// 3. Write a print statement that combines x + y into the integer value 12
let x = 5
let y = "7" // ?? 0 - since the string could be "Fish" and not a number.. So it returns an optional.
print(x + Int(y)!) // ! unwrapped optional.

//Write a print statement that combines x + y into the string value 57
print(String(x) + y)


