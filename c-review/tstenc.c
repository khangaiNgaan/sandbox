#include <stdio.h>

int main()
{
    char plain[50];
    char cipher[50];
    gets(plain);
    for (int i = 0; i < 50; i++) {
        if ( plain[i] <= 'Z' && plain[i] >= 'A') {
            cipher[i] = 'Z' - plain[i] + 'A';
        } else if (plain[i] <= 'z' && plain[i] >= 'a') {
            cipher[i] = 'z' - plain[i] + 'a';
        } else {
            cipher[i] = plain[i];
        }
    }
    printf("%s\n", cipher);
    return 0;
}
