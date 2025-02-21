#include "Student.h"
#ifndef STACK_HEADER
#define STACK_HEADER
#define TOTAL_SIZE 1000

typedef Student ElementType; 

typedef struct{
    ElementType elements[TOTAL_SIZE]; 
    int _size; 

    int _top; 
} Stack; 

void StackInit(Stack *stk); 
ElementType StackTop(Stack *stk); 
int StackEmpty(Stack *stk); 
void StackPush(Stack *stk, ElementType element); 
void StackPop(Stack *stk); 
#endif
