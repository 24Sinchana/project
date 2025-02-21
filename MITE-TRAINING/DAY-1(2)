#include <stdio.h>
#include <stdlib.h>
#define MAX_CUSTOMER 100

struct customer
{
    char name[100];
    int id;
    int units;
};

int main()
{
    struct customer custo[MAX_CUSTOMER];
    int n;
    float base_bill, total_bill,surcharge;
    int fixed_charge = 100;

    printf("Enter the number of customers: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("Enter customer name: ");
        scanf("%s", custo[i].name);

        printf("Enter id: ");
        scanf("%d", &custo[i].id);

        printf("Enter total units consumed: ");
        scanf("%d", &custo[i].units);

        if (custo[i].units <= 100)
        {
            base_bill = custo[i].units * 5;
        }
        else if (custo[i].units >= 101 && custo[i].units <= 300)
        {
            base_bill =100*5+(custo[i].units-100) * 7;
        }
        else
        {
            base_bill = 100*5+200*7+(custo[i].units-300) * 10;
        }

        total_bill = base_bill + fixed_charge;

        printf("Base bill: %.2f\nTotal bill: %.2f\n", base_bill, total_bill);
        if(total_bill>1000)
        {
            surcharge=total_bill * 0.05;
            printf("Surcharge:%.2f",surcharge);
        }
    }

    return 0;
}
