
num_of_classses = int(input ('Total number of class: '))
attendence = int(input('Enter the number attend by the student: '))

per=(attendence/num_of_classses)*100
print('The attendence percentage is ',per, '%')

if per>=75:
    print('The student can attend the exam.')
else:
    print('The student cannot attend the exam.')