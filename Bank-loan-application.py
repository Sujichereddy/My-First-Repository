age = int(input("enter your age: "))
if (age >= 18):
     print("your age is ok continue: ")
     salary = float(input("enter your salary: "))
     if (salary >=40000):
        print("salary satisfied continue: ")
        cibil_score= int(input("enter your cibil score:   "))
        if (cibil_score>=720):
            print ("you are eligible for loan submit all the documents")
        else:
            print("you are not eligible due to cibil score:  ")
     else:
        print("salary requirement not satisfied")
        co_applicant = input("would you like to add co applicant(yes/no):  ").lower()   
        if(co_applicant == 'yes'):
            co_applicant_salary= float(input("enter your salary:  "))
            final_salary =  salary + co_applicant_salary
            if(final_salary >= 60000):
                print("your salary satisfied, continue")
                cibil_score = int(input("enter your cibil score: "))
                if(cibil_score >=720):
                    print("you are eligible for loan: submit the documents")
                else:
                    print("sorry you are not eligible for loan due to your cibil score: ")
            else:
                print("sorry your salary not satisfied: ")
        else:
            print("sorry, your loan not going to further process: ")
else:
   print("sorry you are not eligible due to age: ")                