// Пример из лекций Алексея Кладова
// https://www.youtube.com/watch?v=Oy_VYovfWyo&list=PLlb7e2G7aSpTfhiECYNI2EZ1uAluUqE_e

#include <iostream>
#include <vector>

int main() {
    std::vector<int> xs = {1, 2, 3};
    auto &x = xs[0];
    printf("x = %d\n", x);

    xs.push_back(4);

    printf("x = %d\n", x);

    return 0;
}
