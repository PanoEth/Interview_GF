#include <stdio.h>
#include <string.h>

void setUsername(char username[])
{
    char name[8]; //Size restriction of 8 characters.
    strcpy(name, username);

    printf("User: %s.\n");
}

int main()
{
    setUsername("Alex");
    //Alex passes since its 4 chars
    setUsername("Alexander123"); 
    //Alexander123 dumps core, since its trying to write in unalocated memory. 

    return 0;
}
