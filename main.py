from datetime import date


    
    
print("========================")
print(" SMART EXPENSE TRACKER  ")
print("========================")

Add_Expense=[]
choice=0
while(choice!=5):
    print("1.Add Expense:")
    print("2.View Expense:")
    print("3.Expense Summary:")
    print("4.Delete Expense:")
    print("5.Exist")

#Enter user's choice
    choice=int(input("enter your choice (From 1 to 5):"))

    if (choice==1):
        print("Add Expense")
        
        user_input=""
        while (user_input !="no" and user_input !="n"):
            amt=float(input("Enter your amount:"))
            cate=input("enter category:")
            des=input("enter description:")
            Today_date=str(date.today())
            Expense={"Amount:":amt,
                    "Category:":cate,
                    "Description:":des,
                    "Date:":Today_date}
            Add_Expense.append(Expense)
            user_input=input ("Type 'no' to stop adding more expenses and 'yes' to continue:").lower()
        print(Add_Expense)
        print("Expense added succesfully")    
        
    
    
    elif choice==2:
        print("============")
        print("View Expense")
        print("=============")
        for number,expense in enumerate (Add_Expense,start=1):
            print(f"{number}. {expense['Amount']} |{expense['Category']} |{expense['Description']} |{expense['Date']}")
            
        
    elif choice==3:
        print("Expense Summary")
        
    elif choice==4:
        print("Delete Expense")
    elif choice==5:
        print("Thank you for choosing Smart Expense Tracker") 
    else:
        print("Enter a valid choice from 1 to 5")

                       






