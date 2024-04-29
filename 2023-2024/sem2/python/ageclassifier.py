def classify_age(age):
    if age <= 1:
        return "infant"
    elif age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    else:
        return "adult"

def main():
    while True:
        try:
            age = int(input("What is your current age?: "))
            if age < 0:
                print("Age cannot be negative.")
            else:
                age_category = classify_age(age)
                print("You are classified as a", age_category)
                break  
        except ValueError:
            print("Invalid input! Please enter a valid age (a whole number).")

if __name__ == "__main__":
    main()
