#include <stdio.h>
//Alekhya Code change
//changes in code

int main() {
    char operator;
    double num1, num2, res;

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator);

    printf("Enter two numbers: ");
    scanf("%lf %lf", &num1, &num2);
    switch (operator) {
        case '+':
            res = num1 + num2;
            printf("Res: %.2lf\n", res);
            break;
        case '-':
            res = num1 - num2;
            printf("Res: %.2lf\n", res);
            break;
        case '*':
            res = num1 * num2;
            printf("Res: %.2lf\n", res);           
            break;
        case '/':
            if (num2 != 0) {
                res = num1 / num2;
                printf("Res: %.2lf\n", res);
            } else {
                printf("Error\n");
            }
            break;
        default:
            printf("Invalid\n");
    }

    return 0;
}

