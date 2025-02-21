#include <stdio.h>
#include "student.h"
#include "stack.h"

void readStudentDetails(int n, Student students[]); 
void calculateTotalAndAverage(int n, Student students[]); 
void displayStudentDetails(int n, Student students[]); 
void displayStudentDetailsUsingStack(int n, Student students[]); 
void createfile(int n, Student students[]);  
void manageStudents(); 

int main(){
    manageStudents(); 
    return 0; 
}

void manageStudents(){

    int numberOfStudents; 
    Student students[100]; 
    int choice; 
    do{
        printf("Choices:\n"); 
        printf("1-Read Students\n"); 
        printf("2-Display Students\n"); 
        printf("3-Display Students using Stack\n"); 
        printf("91-Exit\n");
        printf("Your Choice: "); 
        scanf("%d", &choice);
        
        switch(choice){
            case 1:{
                printf("Enter number of students: "); 
                scanf("%d", &numberOfStudents);
                
                readStudentDetails(numberOfStudents, students); 
                calculateTotalAndAverage(numberOfStudents, students); 
                createfile(numberOfStudents, students); 
            } break; 
            case 2: {
                displayStudentDetails(numberOfStudents, students); 
            } break; 
            case 3: {
                displayStudentDetailsUsingStack(numberOfStudents, students); 
            } break; 
            case 4:{
                printf("Thank you for using the App :)...\n"); 
            } break; 
        }
    }while(choice != 91); 
}


void readStudentDetails(int n, Student students[]){
    for(int i = 0 ; i < n ; i++){
        printf("Student %d details (id, name, maths marks, physics marks, chemistry marks, cs marks): ", i+1); 
        scanf("%d %s %d %d %d %d", &students[i].rollNo, students[i].name, &students[i].maths, &students[i].physics, &students[i].chemistry, 
        &students[i].cs); 
    } 
}


void calculateTotalAndAverage(int n, Student students[]){
    for(int i = 0 ; i < n ; i++)
    {
        students[i].totalMarks = 0; 
        students[i].totalMarks += (students[i].maths + students[i].physics + students[i].chemistry + students[i].cs); 
        students[i].percentage = (students[i].totalMarks / 400.0) * 100; 
        
        if (students[i].percentage >= 90)
        {
            students[i].grade = 'A'; 
        } else if (students[i].percentage >= 75 && students[i].percentage <= 89){
            students[i].grade = 'B'; 
        } else {
            students[i].grade = 'C'; 
        }
    }
} 

void displayStudentDetails(int n, Student students[]){
    printf("--------------------------------------------------------------------------------------\n"); 
    printf("Student Details:\n");
    printf("--------------------------------------------------------------------------------------\n"); 
    printf("|%5s|%-20s|%-8s|%10s|%10s|\n", "ID","Name", "Total Marks", "Percentage", "Grade");   
    for(int i = 0; i < n; i++) 
    { 
        printf("|%5d|%-20s|%-8d|%-10.2f|%-10c|\n", students[i].rollNo, 
        students[i].name, students[i].totalMarks, students[i].percentage, 
        students[i].grade); 
    }
    printf("--------------------------------------------------------------------------------------\n"); 
}
void createfile(int n, Student students[]) {
    FILE *file;
    file = fopen("student.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }
    for(int i = 0; i < n; i++) {
        fprintf(file, "%d %s %d %d %d %d\n", students[i].rollNo, students[i].name, students[i].maths, students[i].physics, students[i].chemistry, students[i].cs);
    }
    fclose(file);
}

void displayStudentDetailsUsingStack(int n, Student students[]){
    Stack stk;
    StackInit(&stk); 
    for(int i = 0 ; i < n ; i++){
        StackPush(&stk, students[i]); 
    }
    printf("Student Details displayed using Stack:\n");
    printf("--------------------------------------------------------------------------------------\n"); 
    printf("|%5s|%-20s|%-8s|%10s|%10s|\n", "ID","Name", "Total Marks", "Percentage", "Grade");   
    printf("--------------------------------------------------------------------------------------\n"); 
    while(!StackEmpty(&stk)){
        Student student = StackTop(&stk); 
        printf("|%5d|%-20s|%-8d|%-10.2f|%-10c|\n", student.rollNo, 
        student.name, student.totalMarks, student.percentage, 
        student.grade); 
        StackPop(&stk); 
    }
    printf("--------------------------------------------------------------------------------------\n"); 
}
