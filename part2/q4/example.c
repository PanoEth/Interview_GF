#include <stdio.h>

float calculateVersion1(float a, float b, float c);
float calculateVersion2(float a, float b, float c);

int main() 
{
    float a, b, c;
    printf("Enter number a: ");
        scanf("%f", &a);
    printf("Enter number b: ");
        scanf("%f", &b);
    printf("Enter number c: ");
        scanf("%f", &c);
    
    printf("Version 1 calculation of your inputs: %f\n",calculateVersion1(a, b, c));
    printf("Version 2 calculation of your inputs: %f\n",calculateVersion2(a, b, c));

    return 0;
}

float calculateVersion1(float a, float b, float c)
{
    return a+b*c;
}

float calculateVersion2(float a, float b, float c)
{
    return a*b+c;
}
