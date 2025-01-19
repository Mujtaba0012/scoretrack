student_scores = {}

print("student score tracker")
print("Options: 1.add 2.update 3.view 4.delete 5.exist")

while True:

    choice= input("\nenter your choice(1/2/3/4/5):")

    if choice == "1":

     name =input("enter studentname:")
     if name in student_scores:
      print(f"{name}already exists.")

     else:
       
       score = int(input("enter the student score:"))
       student_scores[name] = score
       print(f"Added{name}wih the score of {score}.")

    elif choice == "2":

     name = input("enter the student's name:")
     if name in student_scores:
       score = int(input(f"entere the new score for{name}:"))
       student_scores[name]= score
       print(f"Updated{name}with the new score of{score}.")
     else:
         print(f"{name}does not exist.")

    elif choice == "3":
     if student_scores:
       print("\nstudent scores:")
       for name, score in student_scores.items():
         print(f"{name}:{score}")
       else:
         print("\nNo student scores to display.")

    elif choice =="4":
     name = input ("enter the students name to delete:")
     if name in student_scores:
       del student_scores[name]
       print(f"deldeted {name}'s record.")
     else:
       print(f"{name}is not in the records.")

    elif choice == "5":
     print("Existing student score tracker.goodbye!")
     break

    else:
      print("invalid choce! please enter 1,2,3,4 or 5.")


