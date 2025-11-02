#include <stdio.h>

void insertionSort(int arr[], int n, const char *name) {
    int comparisons = 0, shifts = 0;

    printf("\nInsertion Sort on array %s:\n", name);
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            comparisons++;
            arr[j + 1] = arr[j];
            j--;
            shifts++;
        }
        if (j >= 0) comparisons++; // One last failed comparison
        arr[j + 1] = key;
        shifts++;
    }

    printf("Sorted Array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\nComparisons: %d, Shifts: %d\n", comparisons, shifts);
}

void selectionSort(int arr[], int n, const char *name) {
    int comparisons = 0, swaps = 0;

    printf("\nSelection Sort on array %s:\n", name);
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comparisons++;
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        if (minIdx != i) {
            // Swap elements
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
            swaps++;
        }
    }

    printf("Sorted Array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\nComparisons: %d, Swaps: %d\n", comparisons, swaps);
}

void copyArray(int src[], int dest[], int n) {
    for (int i = 0; i < n; i++)
        dest[i] = src[i];
}

int main() {
    int n = 6;
    int U[6], V[6], W[6];
    int X[6] = {1, 1, 1, 1, 1, 1};

    printf("Enter 6 elements for array U (Sorted): ");
    for (int i = 0; i < n; i++) scanf("%d", &U[i]);

    printf("Enter 6 elements for array V (Reverse Sorted): ");
    for (int i = 0; i < n; i++) scanf("%d", &V[i]);

    printf("Enter 6 elements for array W (Random Order): ");
    for (int i = 0; i < n; i++) scanf("%d", &W[i]);

    // Temp arrays so original arrays remain unchanged for second sort
    int temp[6];

    // Insertion Sort
    copyArray(U, temp, n);
    insertionSort(temp, n, "U");

    copyArray(V, temp, n);
    insertionSort(temp, n, "V");

    copyArray(W, temp, n);
    insertionSort(temp, n, "W");

    copyArray(X, temp, n);
    insertionSort(temp, n, "X");

    // Selection Sort
    copyArray(U, temp, n);
    selectionSort(temp, n, "U");

    copyArray(V, temp, n);
    selectionSort(temp, n, "V");

    copyArray(W, temp, n);
    selectionSort(temp, n, "W");

    copyArray(X, temp, n);
    selectionSort(temp, n, "X");

    return 0;
}
