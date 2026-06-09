#include <stdio.h>
#include <string.h>
#include <ctype.h>

void displayString(char str[])
{
    printf("You entered: %s\n", str);
}
void countVowelsConsonants(char str[])
{
    int vowels = 0, consonants = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        char ch = tolower(str[i]);
        if (ch >= 'a' && ch <= 'z')
        {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                vowels++;
            else
                consonants++;
        }
    }
    printf("Vowels: %d\n", vowels);
    printf("Consonants: %d\n", consonants);
}
void reverseString(char str[])
{
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++)
    {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
    printf("Reversed string: %s\n", str);
}
void toUpperCase(char str[])
{
    for (int i = 0; str[i] != '\0'; i++)
        str[i] = toupper(str[i]);
    printf("Uppercase: %s\n", str);
}
void toLowerCase(char str[])
{
    for (int i = 0; str[i] != '\0'; i++)
        str[i] = tolower(str[i]);
    printf("Lowercase: %s\n", str);
}
int main()
{
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';
    displayString(str);
    countVowelsConsonants(str);
    reverseString(str);
    toUpperCase(str);
    toLowerCase(str);
    return 0;
}
