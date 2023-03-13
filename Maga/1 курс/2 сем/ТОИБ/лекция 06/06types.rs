fn main() {
    // Ints 
    // Unsigned:    u8|u16|u32|u64|u128|usize
    // Signed:      i8|i16|i32|i64|i128|isize    
    let i:i8 = -1;
    let u:u32 = 0xdeadbeef;
    
    // Float
    let x = 2.0; // f64
    let y: f32 = 3.0; // f32

    // Booleans
    let t = true;
    let f: bool = false;
    
    // Characters
    let z1 = 'z';
    let z2 = 'ℤ';
    let cvd19 = '\u{1f637}';
    
    println!("{} {} {}", z1, z2, cvd19);
    println!("size of z1 in bytes: {}", std::mem::size_of_val(&z1));
    println!("size of z1 in bytes: {}", std::mem::size_of_val(&z2));
    println!("size of cvd19 in bytes: {}", std::mem::size_of_val(&cvd19));
}
