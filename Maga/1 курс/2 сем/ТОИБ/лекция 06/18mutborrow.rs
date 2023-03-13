fn main() {
    let s = String::from("Goodbye");

    change(&s);
    
    println!("{}", s);
}

fn change(some_string: &String) {
    some_string.push_str(", cruel world!");
}
