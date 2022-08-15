import requests
import time
import random
# ______________________________________________________________________________________________________________________

images = ["davy.png", "heart.png", "pirate.gif", "davy3.jpg", "davy4.jpg", "davy2.jpg", "davy5.jpg"]

# ______________________________________________________________________________________________________________________


def command():
    print("Welcome Captain!")
    while True:
        if input("do u want to add ships? y/n (dc chat url): ") == "y":
            ship = input("which ship do you want to sink?: ")
            with open("urls.txt", "a") as sh:
                sh.write("\n"+ship)
            continue
        break
    print("\n Attack lazy pigs!!!!")


# ______________________________________________________________________________________________________________________


def attack_the_traitors():

    def reload():
        with open("urls.txt", "r") as u:    urls = u.readlines()

        with open("szöveg.txt", "r") as s:    massages = s.readlines()

        random_massage = massages[random.randint(0, len(massages) - 1)]
        random_image = images[random.randint(0, len(images) - 1)]
        return random_massage, random_image, urls

    for i in range(100):

        payload = {
            "content": reload()[0]
        }

        header = {
            "authorization": "NDMyOTIxODA3Mzc3NTMwODgw.GtZKgk.HHJUf9BU5HmqYH3FS4rPLW-QgEH6gmlYwX6hFE"
        }

        for u in range(len(reload()[2])):
            requests.post(reload()[2][u-1], data=payload, headers=header)

            image_file_descriptor = open(f".\pic\{reload()[1]}", 'rb')

            files = {'media': image_file_descriptor}

            requests.post(reload()[2][u-1], files=files, headers=header)

            image_file_descriptor.close()

            time.sleep(2)


# ______________________________________________________________________________________________________________________


command()
attack_the_traitors()


# ______________________________________________________________________________________________________________________

