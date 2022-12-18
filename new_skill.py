import sqlite3
import os

db = sqlite3.connect("skills.db")
skill = db.execute(
    "create table if not exists skills (name text , progress integer , user_id insteger)")

cr = db.cursor()
usid = 2


def clear_screen():
    os.system("cls")


def commit_close():  # save and close connection
    db.commit()
    db.close()


def add_skill():  # adding skill function
    skillname = input("Please Advise Skill: ").strip()
    cr.execute(
        f"select name from skills where name=('{skillname}') and user_id=('{usid}')")
    result = cr.fetchone()
    if result is None:  # validate if there is skill with this name or not
        progress = input("Please Advise Progress: ")
        cr.execute(
            f"insert into skills (name,progress,user_id) values ('{skillname}','{progress}','{usid}')")
        os.system("cls")
        print(
            f"Skill {skillname} with progress {progress} % has been added successfully ")
        db.commit()
        loopback = input(
            "Would you like to add another skill or quit\n'a' for adding another skill.\n'M' for main page.\n'Q' for exist app.\nChoose action: ").strip().lower()
        if loopback == "a":
            add_skill()
        elif loopback == "m":
            start_app()
        elif loopback == "q":
            quite()
        else:
            print("wrong choosing and closing app")
            quite()

    else:
        asking = input(
            "Sorry but skill already exist.\n\nWould you like to update progress ?\n'U' => update\n'A' => Add another Skill\n'Q' => Exit ").strip().lower()
        if asking == "a":
            add_skill()
        elif asking == "u":
            progress = input("Please Advise Progress: ")
            cr.execute(
                f"update skills set progress='{progress}'where name='{skillname}' and user_id='{usid}'")
            print("Skill Progress updated.")
            commit_close()
        else:
            print("wrong choosing and closing app")
            quite()


def show_skill():
    cr.execute(f"select * from skills where user_id='{usid}'")
    show = cr.fetchall()
    for row in show:
        print(f"Skill => {row[0]} , Prgress => {row[1]} %")
    loopback2 = input(
        "'M' for main page.\n'Q' for exist app.\n Choose action: ").strip().lower()
    if loopback2 == "m":
        start_app()
    elif loopback2 == "q":
        quite()
    else:
        print("wrong choosing and closing app")
        quite()


def update_skill():
    skillname = input("Please Advise Skill: ").strip()
    cr.execute(
        f"select name from skills where name=('{skillname}') and user_id=('{usid}')")
    result = cr.fetchone()
    if result != None:  # validate if there is skill with this name or not
        progress = input("Please Advise Progress: ")
        cr.execute(
            f"update skills set progress='{progress}'where name='{skillname}' and user_id='{usid}'")
        print("Skill Progress updated.")
        db.commit()

        def loop1():
            loopback2 = input(
                "'M' for main page.\n'Q' for exist app.\n Choose action: ").strip().lower()
            if loopback2 == "m":
                os.system("cls")
                start_app()
            elif loopback2 == "q":
                quite()
            else:
                print("wrong choosing and closing app")
                quite()
        loop1()

    else:
        os.system("cls")
        print("Skill Not Found")
        update_skill()


def delete_skill():

    skillname = input("Please Advise Skill: ").strip()
    cr.execute(
        f"select name from skills where name=('{skillname}') and user_id=('{usid}')")
    result = cr.fetchone()
    if result != None:  # validate if there is skill with this name or not
        cr.execute(
            f"delete from skills where name='{skillname}' and '{usid}'")
        print("Skill Deleted")
        db.commit()

        def loop1():
            loopback2 = input(
                "'M' for main page.\n'Q' for exist app.\n Choose action: ").strip().lower()
            if loopback2 == "m":
                os.system("cls")
                start_app()
            elif loopback2 == "q":
                quite()
            else:
                print("wrong choosing and closing app")
                quite()
        loop1()

    else:
        clear_screen()
        print("Skill Not Found")
        delete_skill()


def quite():
    print("See You Soon (^_^)")
    commit_close()


def start_app():
    while True:  # looping to validate user input
        text_asking = input("""***Welcome to Skill Manager***
    Please advise your action :-
    "A" => Add Skill.
    "S" => Show Skills.
    "U" => Update Skill.
    "D" => Delete Skill.
    "Q" => Quite App.
    Choose Action :""").lower().strip()
        if text_asking in ("a", "s", "u", "d", "q"):
            break
        else:
            os.system("cls")
            print("Invalid input >> Please advise correct action \n\n")
            continue
    if text_asking == "a":
        add_skill()
    elif text_asking == "s":
        show_skill()
    elif text_asking == "u":
        update_skill()
    elif text_asking == "d":
        delete_skill()
    elif text_asking == "q":
        quite()


start_app()
