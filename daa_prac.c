#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

// Swap utility
void swap(char *a, char *b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

// Compare function for qsort
int compare(const void *a, const void *b) {
    return (*(char *)a - *(char *)b);
}

// Function to check if a character can be swapped (to avoid duplicates)
bool shouldSwap(char str[], int start, int curr) {
    for (int i = start; i < curr; i++) {
        if (str[i] == str[curr])
            return false;
    }
    return true;
}

// Backtracking function to generate all unique permutations
void permute(char str[], int l, int r) {
    if (l == r) {
        printf("%s\n", str);
        return;
    }

    for (int i = l; i <= r; i++) {
        // Check if swapping str[l] and str[i] makes sense (no duplicate)
        if (shouldSwap(str, l, i)) {
            swap(&str[l], &str[i]);
            permute(str, l + 1, r);
            swap(&str[l], &str[i]); // backtrack
        }
    }
}

int main() {
    char str[100];
    printf("Enter the string: ");
    scanf("%s", str);

    int n = strlen(str);

    // Sort string to generate lexicographically sorted permutations
    qsort(str, n, sizeof(char), compare);

    printf("\nAll unique permutations in lexicographical order:\n");
    permute(str, 0, n - 1);

    return 0;
}
