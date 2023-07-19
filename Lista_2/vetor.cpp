#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    int num;
    while (std::cin >> num) {
        v.push_back(num);
    }

    std::vector<int> par;
    std::vector<int> impar;

    for (int i : v) {
        if (i % 2 == 0) {
            par.push_back(i);
        } else {
            impar.push_back(i);
        }

        if (par.size() == 5) {
            for (int j = 0; j < 5; j++) {
                std::cout << "par[" << j << "] = " << par[j] << std::endl;
            }
            par.clear();
        }

        if (impar.size() == 5) {
            for (int j = 0; j < 5; j++) {
                std::cout << "impar[" << j << "] = " << impar[j] << std::endl;
            }
            impar.clear();
        }
    }

    for (int i = 0; i < impar.size(); i++) {
        std::cout << "impar[" << i << "] = " << impar[i] << std::endl;
    }

    for (int i = 0; i < par.size(); i++) {
        std::cout << "par[" << i << "] = " << par[i] << std::endl;
    }

    return 0;
}
