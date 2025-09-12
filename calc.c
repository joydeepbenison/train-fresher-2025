#include <stdio.h>

int main() {
	char opr;
	double num1,num2,res;

	printf("Enter an operator (+,-,*,/): ");
	scanf("%c", &opr);

	printf("Enter two numbers: ");
	scanf("%lf %lf", &num1,&num2);

	switch(opr) {
		case '+':
			res = num1+num2;
			printf("Result = %.2lf\n",res);
			break;
		case '-':
			res=num1-num2;
			printf("Result = %.2lf\n",res);
			break;
		case '*':
			res=num1*num2;
			printf("Result = %.2lf\n",res);
			break;
		case '/':
			if(num2 != 0){
				res = num1/num2;
			} 
			else{
				printf("Error");
				return 1;
			}
			printf("Result = %.2lf\n", res);
			break;
		default:
			printf("Invalid");
	}
	return 0;
}

