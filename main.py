# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first_name = name1.lower()
second_name = name2.lower()

true_count = first_name.count("t") + first_name.count("r") + first_name.count("u") + first_name.count("e") + second_name.count("t")+second_name.count("r")+second_name.count("u")+second_name.count("e")

love_count = first_name.count("l")+ first_name.count("o")+first_name.count("v")+first_name.count("e") + second_name.count("l")+second_name.count("o")+second_name.count("v")+second_name.count("e")

score = int(f"{true_count}{love_count}")

if score <= 10 or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score is {score}.")

