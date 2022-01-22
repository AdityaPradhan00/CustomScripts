import datetime
import time
     
def check(day):
    print("\nEnter the number for the choices: ")
    for i in range(3):
        try:
            ch = int(input("1. Read\n2. Write:- "))
            exe(ch, day)
            break
        except ValueError as e:
            if i < 2:
                print("\nEnter the correct integer!")
            else:
                print("\nFool that was 3 tries, You're hopeless.")

def exe(ch, day):
    if ch == 1:
        re = open("records.txt" , "r")
        rea = re.read()
        print(rea)
        time.sleep(200)
        re.close
    elif ch == 2:
        d = datetime.date.today()
        for i in range(3):
            try:
                cal = int(input("Calories: "))
                try:
                    we = float(input("Weight: "))
                    wr =  open("records.txt", "a")
                    
                    wr.write("\n"  + str(d) + "\t" + day + "\tCalories(cal): " + str(cal) + "\t Weight(kg): " + str(we) +"\n" )
                    wr.close
                    break
                except ValueError as p:
                    if i < 2:
                        print("\nEnter the correct data!")
                    else:
                        print("\nFool that was 3 tries, You're hopeless.")
            except ValueError as e:
                if i < 2:
                    print("\nEnter the correct data!")
                else:
                    print("\nFool that was 3 tries, You're hopeless.")

    elif ch != 1 or 2:
        check(day)
        
if __name__ == "__main__":
    a = datetime.date.today()
    s = datetime.date.weekday(a)
    day = 0
    if s == 0:
        day = "Monday: "
    elif s == 1:
        day = "Tuesday: "
    elif s == 2:
        day = "Wednesday: "
    elif s == 3:
        day = "Thursday: "
    elif s == 4:
        day = "Friday: "
    elif s == 5:
        day = "Saturday: "
    elif s == 6:
        day = "Sunday: "
    check(day)
    