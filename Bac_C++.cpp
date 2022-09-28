#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <algorithm>
#include <random>
using namespace std;

template<typename T, size_t n>
void print_array(T const(& arr)[n])
{
    for (size_t i = 0; i < n; i++) {
        std::cout << arr[i] << ' ';
    }
}

// Function to insert x in arr at position pos
int* insertX(int n, int arr[],
            int x, int pos)
{
    int i;
 
    // increase the size by 1
    n++;
 
    // shift elements forward
    for (i = n; i >= pos; i--)
        arr[i] = arr[i - 1];
 
    // insert x at pos
    arr[pos - 1] = x;
 
    return arr;
}


int main(void)
{
//    build a baccarat deck
    int deck_array[] = {
        //deck-1
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        //deck-2
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        //deck-3
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        //deck-4
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        //deck-5
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        //deck-6
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        //deck-7
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        //deck-8
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
        };


    // Shuffle the decks
    auto rng = std::default_random_engine {};
    std::shuffle(std::begin(deck_array), std::end(deck_array), rng);

    // get the red card at random cut
    std::random_device seed;
    std::mt19937 gen{seed()}; // seed the generator
    std::uniform_int_distribution dist{280, 320}; // set min and max
    int guess = dist(gen); // generate number
    int rend = guess;
    // std::cout << "Computer guess: " << rend << '\n';
    int cp[290];
    int deck_ready[290];

    // insert the red card into deck
    print_array(deck_array);
    std::cout << "Computer guess: " << cp << '\n';
    memcpy(deck_ready, deck_array + 1, rend);
    
    print_array(deck_ready);

    // int x, pos,
    // i give up C++


    // return 0;
}

