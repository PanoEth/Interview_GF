#include <stdio.h>
#include <string.h>

int main()
{
    char string[100];
    printf("Enter a word: ");
    scanf("%99s", string);
    int match=0;
    int size = strlen(string);
    
    for(int i=0; i < size/2; i++)
    {
        if(string[i] == string[size-1-i]) 
            match++;
    }
    if(match==size/2)
        printf("%s is a palindrome\n", string);
    else
        printf("%s is not a palindrome.\n", string);
    
    return 0;
}
/*    This example will fail even if input is a palindrom, but it has a uppercase letter
Example:
abba - passes
Abba - fails        */
