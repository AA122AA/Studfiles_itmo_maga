// Пример из лекций Алексея Кладова
// https://www.youtube.com/watch?v=Oy_VYovfWyo&list=PLlb7e2G7aSpTfhiECYNI2EZ1uAluUqE_e

fn main() {
    let mut xs = vec![1, 2, 3];
    let x: &i32 = &xs[0];

    println!("x = {}", x);

    xs.push(4);

    println!("x = {}", x);
}
