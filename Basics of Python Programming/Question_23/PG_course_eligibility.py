x_percentage = float(input("Enter percentage in X examination: "))
xii_percentage = float(input("Enter percentage in XII examination: "))
graduation_percentage = float(input("Enter percentage in graduation: "))

change_stream = input("Did the student change the stream (yes/no)? ").lower()

if change_stream == "yes":
    graduation_percentage -= 5

if x_percentage > 80 and xii_percentage > 80 and graduation_percentage > 70:
    print("Congratulations! The student is eligible for the PG course.")
else:
    print("Sorry, the student is not eligible for the PG course.")
