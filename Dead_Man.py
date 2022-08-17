import requests
import time
import random
import os
import shutil
# ______________________________________________________________________________________________________________________


# ______________________________________________________________________________________________________________________

def load():
    with open(r".\txts\pirates\pirates.txt") as pir: pirates = pir.readlines()
    if len(pirates) >= 1:
        for pirate in pirates:
            pirate_dat = pirate.split(",")
            pirate_dat_name = pirate_dat[1].split("_")[0].lower()
            pirate_dat[1] = Pirates(int(pirate_dat[0]), pirate_dat_name)
    else:
        return None

# ______________________________________________________________________________________________________________________


class Pirates:
    Team = []

    def __init__(self, shots, name):
        self.shots = shots
        self.name = name
        # self.song = song
        with open(fr".\txts\{self.name.strip()}.txt", "r") as cap: self.text = cap.readlines()
        self.images = [image for image in os.listdir(f".\pic\{self.name.strip()}")]

        Pirates.Team.append(self)


# ______________________________________________________________________________________________________________________


Davy_Jones = Pirates(50, "davy")


# ______________________________________________________________________________________________________________________
def commands():

    def create_captain():
        def is_it_okay():
            while True:
                stats = input("shots and name (example: 10,Morris_Shmebiulack): ")
                stat_pir = stats.split(",")
                if len(stat_pir) == 2 and "_" in stat_pir[1]:
                    return stat_pir
                else:
                    print("is this like in the example")
                    continue

# ______________________________________________________________________________________________________________________

        stat_dat = is_it_okay()
        pirate_dat_name = stat_dat[1].split("_")[0].lower()
        os.mkdir(fr".\pic\{pirate_dat_name}"); os.mkdir(fr".\song\{pirate_dat_name}")
        with open(fr".\txts\{pirate_dat_name}.txt", "w") as dn: dn.write(" ");
        print("Pirate datas are ready (in pic, txts, and song u can costumize them)")
        stat_dat[1] = Pirates(int(stat_dat[0]), pirate_dat_name)
        with open(r".\txts\pirates\pirates.txt", "a") as pi: pi.write(f"{stat_dat[0]},{pirate_dat_name}\n")

# ______________________________________________________________________________________________________________________

    def choose_captain():
        while True:
            [print(pirate.name) for pirate in Pirates.Team]
            ch_pirate = input("ki legyen a kapitány: ")
            ch_pirate = [pirate for pirate in Pirates.Team if pirate.name == ch_pirate]
            if len(ch_pirate) == 1:return ch_pirate
            else: continue
# ______________________________________________________________________________________________________________________

    def attack_the_traitors(pirate):

# ______________________________________________________________________________________________________________________

        def reload():
            with open(r".\txts\urls.txt", "r") as u:    urls = u.readlines()

            with open(r".\txts\aut.txt", "r") as au: aut = au.readline()

            random_massage = pirate.text[random.randint(0, len(pirate.text) - 1)]
            random_image = pirate.images[random.randint(0, len(pirate.images) - 1)]
            return random_massage, random_image, urls, aut

        for i in range(pirate.shots):

            payload = {
                "content": reload()[0]
            }

            header = {
                "authorization": reload()[3]
            }

            for u in range(len(reload()[2])):
                requests.post(reload()[2][u - 1], data=payload, headers=header)

                image_file_descriptor = open(f".\pic\{pirate.name}\{reload()[1]}", 'rb')

                files = {'media': image_file_descriptor}

                requests.post(reload()[2][u - 1], files=files, headers=header)

                image_file_descriptor.close()

                time.sleep(2)


# ______________________________________________________________________________________________________________________


    def welcome_captain():
        ask = input("choose or make captain? c/m: ")
        if ask == "c":
            pass
        else:
            create_captain()

        captain = choose_captain()[0]
        print(f"Welcome Captain {captain.name.upper()}!")
        while True:
            if input("do u want to add ships? y/n (dc chat url): ") == "y":
                ship = input("which ship do you want to sink?: ")
                with open(r".\txts\urls.txt", "a") as sh:
                    sh.write("\n"+ship)
                continue
            break
        print("\n Attack lazy pigs!!!!")
        attack_the_traitors(captain)

    welcome_captain()


# ______________________________________________________________________________________________________________________


load()
commands()


# ______________________________________________________________________________________________________________________