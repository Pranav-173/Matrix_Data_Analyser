import numpy as np
import json

n = int(input("Enter the number of subjects: "))

def load_data():
    global marks
    try:
        with open("marks.json", "r") as f:
            data = json.load(f)
            if data:
                    temp_marks = np.array(data)
                    if temp_marks.shape[1] == n:
                        return temp_marks
                    else:
                        print(f"Invalid input")
    except:
        pass
    return np.empty((0, n))

marks = load_data()

def save_data():
    with open("marks.json", "w") as f:
        json.dump(marks.tolist(), f)

def show_data():
    print("\n----- Student Data -----")
    if marks.size == 0:
        print("No students found.")
    else:
        for i, x in enumerate(marks):
            print(f"Student {i+1}: {x}")
    print("------------------------")

def add_std():
    global marks
    try:
        user_input = input(f"Enter {n} marks (space separated): ")
        new_marks = list(map(int, user_input.split()))
        if len(new_marks) != n:
            print(f"Error: You must enter exactly {n} marks.")
            return
        if marks.size == 0:
            marks = np.array([new_marks])
        else:
            marks = np.vstack((marks, new_marks))
        save_data()
        print("Student Added !!")
    except:
        print("Invalid Input. Please enter numbers only.")

def clear_data():
    global marks
    marks = np.empty((0, n))
    save_data()
    print("Data Cleared.")

def analysis():
    if marks.size > 0:
        print("Student Averages:", np.mean(marks, axis=1))
    else: print("No data.")

def rank():
    if marks.shape[0] == 0:
        print("No data to rank.")
        return
    tot_marks = np.sum(marks, axis=1)
    ranks = np.argsort(tot_marks)[::-1]
    print("\n----- Ranks -----")
    for i, idx in enumerate(ranks):
        print(f"Rank {i+1}: Student {idx+1} (Total: {tot_marks[idx]})")
    print("----------------")

while True:
    print("\n***** Available Operations *****")
    print("1. Show Data\n2. Add student\n3. Clear Data\n4. Show Analysis\n5. Rankings\n6. Exit")
    print("*********************************")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1: show_data()
        elif choice == 2: add_std()
        elif choice == 3: clear_data()
        elif choice == 4: analysis()
        elif choice == 5:rank()
        elif choice == 6: 
            print("Exiting....")
            break
    except:
        print("Invalid Choice.")