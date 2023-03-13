fn main() {
    // Try it with or without -O
    let mut x:u8 = 255;    
    x += 1;    
    println!("x = {}", x);
    
//    let mut y:u8 = 254;
//    println!("wrapping y = {}", y.wrapping_add(1));
//    println!("checked y = {:?}", y.checked_add(1));
//    println!("overflowing y = {:?}", y.overflowing_add(1));
//    println!("saturating y = {}", y.saturating_add(1));
}
