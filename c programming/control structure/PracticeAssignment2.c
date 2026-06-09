#include <stdio.h>
#include <string.h>

int main()
{
    int choice, qty, total = 0, points = 0;
    char promo[20];
    char again;

    do
    {
        printf("\n--- Smart Cafe Menu ---\n");
        printf("1. Coffee ($2)\n");
        printf("2. Tea ($1)\n");
        printf("3. Snacks ($3)\n");
        printf("Enter your choice : ");
        scanf("%d", &choice);

        printf("Enter quantity: ");
        scanf("%d", &qty);

        switch (choice)
        {
        case 1:
            printf("You ordered %d Coffee(s)\n", qty);
            total += 2 * qty;
            break;
        case 2:
            printf("You ordered %d Tea(s)\n", qty);
            total += 1 * qty;
            break;
        case 3:
            printf("You ordered %d Snack(s)\n", qty);
            total += 3 * qty;
            break;
        default:
            printf("Invalid choice!\n");
        }

        printf("Do you want to order more? (y/n): ");
        scanf(" %c", &again);

    } while (again == 'y' || again == 'Y');

    printf("\nEnter promo code (CAFE5 / FREEDRINK / WELCOME10): ");
    scanf("%s", promo);

    if (strcmp(promo, "CAFE5") == 0)
    {
        printf("Promo applied: $5 off!\n");
        total -= 5;
    }
    else if (strcmp(promo, "FREEDRINK") == 0)
    {
        printf("Promo applied: Free drink added!\n");
    }
    else if (strcmp(promo, "WELCOME10") == 0)
    {
        printf("Promo applied: 10%% off!\n");
        total = total - (total * 10 / 100);
    }
    else
    {
        printf("Invalid promo code.\n");
    }

    points = total / 5 * 2; // 2 points for every $5 spent

    printf("\n--- Order Summary ---\n");
    printf("Total Bill: $%d\n", total);
    printf("Loyalty Points Earned: %d\n", points);
    printf("Thank you for visiting Smart Cafe!\n");

    return 0;
}
