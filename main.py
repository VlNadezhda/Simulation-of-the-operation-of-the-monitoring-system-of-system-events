import datetime
from subprocess import Popen, PIPE

try:
    from subprocess import Popen, PIPE
    from time import sleep
except Exception as err:
    print(err)

file_launch = "C:/Users/Надежда/PycharmProjects/журнал/launch_process.txt"

class Journal:
    def CreateLogFile(self):
        return "journal" + str(datetime.date.today()) + ".txt"

    def __init__(self):
        self.filename = self.CreateLogFile()

    def PidRead(self):
        """ Чтение потокового ввода от subprocess.communicate() и запись в текстовый файл """
        for line in Popen('tasklist', stdout=PIPE).stdout.readlines():
            dline = line.decode('cp866', 'ignore')
            # print()
            if dline in open(self.filename).read():  # если строка существует, ...
                pass  # ... то пропустить, не записывать ...
            # if "ps -eo pid,start,args" in open(
            #         file_launch).read():  # не записывать в лог-файл нежелательную информацию (здесь - "ps -eo pid,start,args" )
            #     pass
            else:  # ... иначе ...
                with open(self.filename, "a+") as fl:  # ... если строка является уникальной, ...
                    fl.write(dline)


def main():
    jour = Journal()
    with open(file_launch, 'tw', encoding='utf-8') as f:                              # Очистить содержимое лог-файл, если он существует. Если не существует - создать пустой.
        pass
    while (True):
        sleep(10)                                                                     # Бесконечное исполнение скрипта. Частота (здесь - 10 сек) - по желанию пользователя.
        jour.PidRead()

if __name__ == "__main__":
    main()
