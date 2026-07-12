#include "functions.h"

char add(int a, int b) 
{
    return a+b;
}

char sub(int a, int b)
{
    return a-b;
}
/* Here the problem is the fact that the functions are given as char.
Since char is 8bits it can hold values of -127 up to +127. 
The function techically works, but with restricted size of CHAR.
When value is greater than 127 or less than -127 the function will give wrong value.
*/
