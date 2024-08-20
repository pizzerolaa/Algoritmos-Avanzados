#ifndef COMPBYAGE_H
#define COMPBYAGE_H
#include "student.h"

struct CompareByAge {
    bool operator()(const student& a, const student& b) const {
        return a.age < b.age;
    }
};

#endif