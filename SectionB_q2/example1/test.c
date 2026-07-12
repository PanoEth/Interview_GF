#include <stdio.h>
#include "functions.h"

int main()
{
    int result = add(100,100); // works untill value: -127<value<+127
    int result2 = sub(1000, 10);

    if(result == 200)
        printf("Test add passed.\n");
    else
        printf("Test add failed, got: %d.\n", result);

    if(result2 == 990)
        printf("Test sub passed.\n");
    else
        printf("Test sub failed, got: %d.\n", result2);

    return 0;
}
