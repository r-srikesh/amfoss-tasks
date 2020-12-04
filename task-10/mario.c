#include <cs50.h>
#include <stdio.h>
int main (void)
{
    int height;
    do
    {
        height = get_int("Height:");
    }
    while (height < 1 || height > 8);
    for (int rows = 1; rows<=height; rows++)
    {
        for (int k = 1; k <= height - rows;k++)
        {
            printf(" ");
        }
        for (int j = 1; j<=rows; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
