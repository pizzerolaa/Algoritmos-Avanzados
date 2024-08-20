#ifndef STUDENT_H
#define STUDENT_H

#include <string>

struct student {
    int age;
    std::string name;

    bool operator<(const student& other) const {
        return age < other.age;
    }
};

#endif
