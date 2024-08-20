CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -pedantic -g
TARGET = main

all: $(TARGET)

$(TARGET): main.cpp dynamic_prog.h greedy_algh.h print_result.h
	$(CXX) $(CXXFLAGS) -o $(TARGET) main.cpp

valgrind: $(TARGET)
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all valgrind clean