import time
import random
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ИМБА": "Что-то слишком крутое"
            }
while True:
    time.sleep(0.2)
    print("Выберите опцию:")
    time.sleep(0.2)
    print("1 - Добавить слово")
    time.sleep(0.2)
    print("2 - Просмотреть слова")
    time.sleep(0.2)
    print("3 - Рандомное слово")
    time.sleep(0.2)
    print("4 - Удалить")
    n = int(input())
    if n == 1:
        key=input("Введите слово: ")
        value=input("Введите объяснение: ")
        meme_dict[key] = value
    if n == 2:
        print(meme_dict)
    if n == 3:
        randkey = random.choice(meme_dict.keys())
        randval = meme_dict[randkey]
        print(randkey, " - ", randval)
    if n == 4:
        print("Введите название ключа: ")
        ke = input()
        del meme_dict[ke]
