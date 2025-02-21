#ifndef STUDENT_HEADER
#define STUDENT_HEADER
struct Student_t{
    int rollNo; 
    char name[50]; 
    int maths, physics, chemistry, cs; 
    int totalMarks; 
    float percentage; 
    char grade; 
}; 
typedef struct Student_t Student;  
#endif
