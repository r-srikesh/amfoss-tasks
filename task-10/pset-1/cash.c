#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main()
{
    float dollar_owed;
    int cents_owed;
    int coins = 0;

    do
    {
        dollar_owed = get_float("Change Owed:");
    }
    while(dollar_owed <= 0);
    cents_owed = round(dollar_owed*100);

    while(cents_owed >= 25)
    {
    cents_owed = cents_owed - 25;
    coins++;
    }
    while(cents_owed >= 10)
    {
    cents_owed = cents_owed -10;
    coins++;
    }
    while(cents_owed >= 5)
    {
    cents_owed = cents_owed - 5;
    coins++;
    }
    while(cents_owed >= 1)
    {
    cents_owed--;
        coins++;
    }
    printf("%d\n",coins);
}