#include <stdio.h>
#include <stdlib.h>
int main()
{
int *arr = malloc(10*sizeof(int));
arr[0] = 100;
int *arr2 = malloc(10*sizeof(int));
arr2[0] = 200;
free(arr);

return 0;
}
