#include "stack.h"
#include <stdio.h>
 
void StackInit(Stack *stk){
    stk->_size = 0; 
    stk->_top = -1; 
}
ElementType StackTop(Stack *stk){
    return stk->elements[stk->_top];
}
int StackEmpty(Stack *stk){
    return (stk->_top == -1); 
}
void StackPush(Stack *stk, ElementType element){
    stk->elements[stk->_size] = element; 
    stk->_size++; 
    stk->_top++; 
}
void StackPop(Stack *stk){
    if(StackEmpty(stk)){
        printf("Stack Empty\n"); 
        return; 
    }
    stk->_size--; 
    stk->_top--; 
}
