#include "student.h"
#include "compareByAge.h"
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<student> students;
    int age;
    string name;

    while (cin >> age >> name) {
        students.push_back({age, name});
    }

    sort(students.begin(), students.end());
    cout << "Ordenado por edad (sobrecarga del operador <):\n";
    for (const auto& s : students) {
        cout << s.name << ": " << s.age << '\n';
    }

    sort(students.begin(), students.end(), CompareByAge());
    cout << "\nOrdenado por edad (function object):\n";
    for (const auto& s : students) {
        cout << s.name << ": " << s.age << '\n';
    }

    sort(students.begin(), students.end(), [](const student& a, const student& b) {
        return a.age < b.age;
    });
    cout << "\nOrdenado por edad (lambda):\n";
    for (const auto& s : students) {
        cout << s.name << ": " << s.age << '\n';
    }

    return 0;
}
