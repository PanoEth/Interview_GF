#include <stdio.h>
#include <ctype.h>
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
        if(tolower(string[i])== tolower(string[size-1-i])) 
            match++;
    }
    if(match==size/2)
        printf("%s is a palindrome\n", string);
    else
        printf("%s is not a palindrome.\n", string);
    
    return 0;
}
/*  Since this version has tolower() when comparing it:
    Changes uppercase into lowercase, meaning the IF statement will pass
    even when it compares A to a.
    Now both abba and Abba (abBa or aBbA) will pass.    */