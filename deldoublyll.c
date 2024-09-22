#include <stdio.h>
#include <stdlib.h>
struct node {
    int data;
    struct node *prev;
    struct node *next;
   
};
struct node *head, *tail;
void create() 
{   
    struct node *newnode;
    head=0;
    struct node *temp;
    int choice = 1;
    while (choice)
    {
        newnode= (struct node *)malloc(sizeof(struct node));
        printf("Enter the data: ");
        scanf("%d", &newnode->data);
        newnode->prev = 0;
        newnode->next = 0;
        if (head == 0){
            head = tail = newnode;
        }
        else{
            tail->next = newnode;
            newnode->prev = tail;
            tail = newnode;
        }
        printf("Do you want to continue (0/1)? ");
    scanf("%d", &choice);
    }

}
void display() {
    struct node *temp;
    temp = head;
    while (temp != 0) {
        printf("%d ", temp->data);
        temp = temp->next; 

    }
}
void delfrombeg()
{
    struct node *temp;
    if(head==0)
    {
        printf("list is empty");
    }
    else
    {
        temp=head;
        head=temp->next;
        head->prev=0;
        free(temp);

    }
}
void delfromend()
{
    struct node *temp;
    if(tail==0)
    {
        printf("list is empty");
    }
    else{
        temp=tail;
        temp->prev->next=0;
        tail=tail->prev;
        free(temp);

    }
}
void delfrompos()
{
    int pos,i=1;
    struct node *temp;
    temp=head;
    printf("\nEnter the position:\n");
    scanf("%d",&pos);
    while(i<pos){
        temp=temp->next;
        i++;
    }
    temp->prev->next=temp->next;
    temp->next->prev=temp->prev;
    free(temp);

}
int main() {
    head = 0;
    create();
    display();
    printf("\nOriginal list:\n");
    display(head);
    delfrombeg();
    printf("\nDeleted from the begining  list:\n");
    display(head);
    delfromend();
    printf("\nDelete from the end list:\n");
    display(tail);
    delfrompos();
    printf("\nDelete from the position list:\n");
    display(head);
    return 0;
}