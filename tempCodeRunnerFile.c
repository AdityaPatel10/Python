#include <stdio.h>
int main ()   {
    int n;
    printf ("Enter an number : ");
    scanf ("%d", &n);
    if (n >0)
    printf ("%d is an natural number.", n);
    else
    printf ("%d is not an natural number.", n);
    return 0;
}