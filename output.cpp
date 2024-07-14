#include <iostream>

int main() {
    int  filas;

    std::cout << "Introduce el número de filas: ";
    std::cin >> filas;

    for (variable entera i = 1; i <= filas; ++i ) {
        for (variable entera j = 1; j <= i; ++j ) {
            std::cout << "*";
        }

        std::cout << "\n";
    }

    return 0;
}