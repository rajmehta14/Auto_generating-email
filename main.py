import random
from datetime import datetime
import pandas
import smtplib

data = pandas.read_csv("birthdays.csv.numbers")

today = datetime.now()

today_tupple = (today.month, today.day)

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)
bithday_person = birthday_dict[today_tupple]

if today_tupple in birthday_dict:
    file_path = f"letters/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as file:
        content = file.read()
        c_name = content.replace("[NAME]", bithday_person["name"])
    e = "rajmehta2300@gmail.com"
    password = "pnzdbwmzqkqklzju"
    user_name = e.split('@')[0]

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=user_name, password=password)
    connection.sendmail(from_addr=e, to_addrs=bithday_person["email"], msg=f"Subject:Birthday Wish!!!\n\n{c_name}")
    connection.quit()
