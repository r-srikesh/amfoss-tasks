#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
int main(void)
{
    string text = get_string("Text:");
    int letter = 0;
    int words = 1;
    int sentences = 0;
    for (int i = 0; i < strlen(text) ; i++)
    {
        if((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letter++;
        }
        if(text[i] == ' ' )
        {
            words++;
        }
        if  (text[i] == '.' || text[i] == '!' ||  text[i] == '?' )
        {
            sentences++;
        }
    }
        
    
    float grade = 0.0588 * (100 * (float)letter / (float)words) - 0.296 * (100 * (float)sentences / (float)words) - 15.8;
    int gradex = round(grade);
    
    
        
        if (gradex > 1 && gradex < 16)
        {
            printf(" Grade %i\n",gradex);
        }
        else 
        {
            if (gradex >= 16)
            {
                printf("Grade 16+\n");
            }
            if (gradex <= 1)
            {
                printf("Before Grade 1\n");
            }
        }
}
