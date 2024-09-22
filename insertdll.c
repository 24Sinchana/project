#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *prev;
    struct node *next;
};
struct node *head,*tail;

void create()
{
    struct node *newnode;
    head=0;
    int choice=1;
    while(choice)
    {
        newnode=(struct node*)malloc(sizeof(struct node));
        printf("Enter the data: ");
        scanf("%d",&newnode->data);
        newnode->prev=0;
        newnode->next=0;
        if(head==0){
            head=tail=newnode;
        }
        else{
            tail-> next=newnode;
            newnode->prev=tail;
            tail=newnode;
        }
        printf("Do you want to continue (0/1)? ");
        scanf("%d",&choice);
    }
}
    
void display(){
    struct node *temp;
    temp=head;
    while(temp!=0){
        printf("%d",temp->data);
        temp=temp->next;
        
    }
}
void insertatbeg(){
    struct node *newnode;
    newnode=(struct node *)malloc(sizeof(struct node));
    printf("\nEnter the data to be inserted at the begining:\n");
    scanf("%d",&newnode->data);
    newnode->prev=0;
    newnode->next=0;
    if(head==NULL){
       head=tail=newnode;
    }
    else{
        head->prev=newnode;
        newnode->next=head;
        head=newnode;
        }
}
void insertatend(){
    struct node *newnode;
    newnode=(struct node *)malloc(sizeof(struct node));
    printf("\nEnter the data to be inserted at the end:\n");
    scanf("%d",&newnode->data);
    newnode->prev=0;
    newnode->next=0;
    if(head==NULL){
        head=tail=newnode;
    }
    else{
        tail->next=newnode;
        newnode->prev=tail;
        tail=newnode;
        }
}
void insertatposition()
{
    int Pos ,i;
    printf("\nEnter the position: ");
    scanf("%d",&Pos);
    if(Pos<1)
    {
        printf("invalid position");
    }
    else if (Pos==1){
        insertatbeg();
    }
    else{
        struct node *newnode, *temp;
        temp=head;
        newnode=(struct node *)malloc(sizeof(struct node));
        printf("\nEnter the data: ");
        scanf("%d",&newnode->data);
        while(i<Pos-1)
        {
            temp=temp->next;
            i++;
        }
            newnode->prev=temp;
            newnode->next=temp->next;
            temp->next=newnode;
            newnode->next->prev=newnode;
        }
}
void insertafterposition()
{
    int Pos ,i;
    printf("\nEnter the position: ");
    scanf("%d",&Pos);
    if(Pos<1)
    {
        printf("invalid position");
    }
     
    else{
        struct node *newnode, *temp;
        temp=head;
        newnode=(struct node *)malloc(sizeof(struct node));
        printf("\nEnter the data: ");
        scanf("%d",&newnode->data);
        while(i<Pos)
        {
            temp=temp->next;
            i++;
        }
            newnode->prev=temp;
            newnode->next=temp->next;
            temp->next=newnode;
            newnode->next->prev=newnode;
        }
}

int main() {
    head = 0;
    create();
    display();
    printf("\nOriginal list:\n");
    display(head);
    insertatbeg();
    printf("\nInserted at the begining of the list:\n");
    display(head);
    insertatend();
    printf("\nInserted at the end of the list:\n");
    display(head);
    insertatposition();
    printf("\nInserted at the specific position of the list:\n");
    display(head);
    insertafterposition();
    printf("\nInserted after the specific position of the list:\n");
    display(head);
    return 0;
}