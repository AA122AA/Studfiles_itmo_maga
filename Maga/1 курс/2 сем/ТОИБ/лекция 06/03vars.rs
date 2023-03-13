fn main() {
    // Immutable by default
    let x = 0;
    println!("The value of x is: {}", x);
    x = 42;
    println!("The value of x is: {}", x);
    
//    // In the same scope (shadowing)
//    let x = 3.14;
//    println!("The value of x is: {}", x);
}
