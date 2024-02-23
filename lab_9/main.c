#include <stdio.h>
#include <stdlib.h>

int *get_array_of_max_elements(int ** twod_array, int * length, int * elemets) {
    int * arr = (int * ) malloc( * length * sizeof(int));

    for (int i = 0; i < * length; ++i) {
        int max = * ( * (twod_array + i));

        for (int j = 0; j < * elemets; ++j) {
            int current_element = * ( * (twod_array + i) + j);

            if (current_element > max) {
                max = current_element;
            }
        }
        arr[i] = max;
    }

    return arr;
}

int *get_array_of_min_elements(int **twod_array, int *length, int *elements) {
    int *arr = (int *)malloc(*length * sizeof(int));

    for (int i = 0; i < *length; ++i) {
        int min = *(*twod_array + i);

        for (int j = 0; j < *elements; ++j) {
            int current_element = *(*(twod_array + i) + j);

            if (current_element < min) {
                min = current_element;
            }
        }

        arr[i] = min;
    }

    return arr;
}
int main() {
    puts("Komarnytskyi Nestor \nGrupa KNMS-11 \nZnakhodzhennia maksymalnoho ta minimalnoho dvomirnoho masivu(9 laboratorna robota)");

    int amount_of_arrays;
    int elements_length;

    puts("2d-array length: ");
    scanf("%d", & amount_of_arrays);

    puts("Arrays length: ");
    scanf("%d", & elements_length);

    int ** twod_array = (int ** ) malloc(amount_of_arrays * sizeof(int * ));

    for (int i = 0; i < amount_of_arrays; ++i) {
        twod_array[i] = (int * ) malloc(elements_length * sizeof(int));
    }

    for (int i = 0; i < amount_of_arrays; ++i) {
        for (int j = 0; j < elements_length; ++j) {
            printf("Set %d element of %d array\n", j, i);
            scanf("%d", ( * (twod_array + i) + j));
        }
    }

    int *max_array = get_array_of_max_elements(twod_array, & amount_of_arrays, & elements_length);

    int max = max_array[0]; 

    for (int i = 1; i < amount_of_arrays; ++i) {
        if (max_array[i] > max) {
            max = max_array[i]; 
        }
    }

    int *min_array = get_array_of_min_elements(twod_array, & amount_of_arrays, & elements_length);

    int min = min_array[0]; 

    for (int i = 1; i < amount_of_arrays; ++i) {
        if (min_array[i] < min) {
            min = min_array[i];
        }
    }

    printf("\nМаксимальне значення %d \nМінімальне значення %d\n", max, min);

    for (int i = 0; i < amount_of_arrays; ++i) {
        free(twod_array[i]);
    }

    free(twod_array);

    return 0;
}