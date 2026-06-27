#include <stdio.h>
#include <string.h>

int main()
{
    char str_a[10];
    char str_b[10];
    scanf("%s", str_a);
    scanf("%s", str_b);
    printf("%d\n", strcmp(str_a, str_b));
    return 0;
}
