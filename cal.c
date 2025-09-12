#include <stdio.h>

int main() 
{
    double num1, num2;
    char oper;

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &oper); 

    printf("Enter two numbers: ");
    scanf("%lf %lf", &num1, &num2);

    switch(oper) {
        case '+':
            printf("Result = %.2lf\n", num1 + num2);
            break;
        case '-':
            printf("Result = %.2lf\n", num1 - num2);
            break;
        case '*':
            printf("Resut = %.2lf\n", num1 * num2);
            break;
        case '/':
            if(num2 != 0)
                printf("Result = %.2lf\n", num1 / num2);
            else
                printf("Error: Division by zero is not allowed.\n");
            break;
        default:
            printf("Error: Invalid operator.\n");
    }

    return 0;
}

