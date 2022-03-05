import datetime
from subprocess import Popen, PIPE
import  PySimpleGUI as sg
from PySimpleGUI import VerticalSeparator

try:
    from subprocess import Popen, PIPE
    from time import sleep
except Exception as err:
    print(err)


class Interface:
    def __init__(self):
        pass

    def DoWindow(self):
        sg.theme('Dark Blue 3')  # please make your windows colorful
        data = [['rocsptjach', 161, 570, 844, 745, 454],
                ['jwsqgvyatn', 380, 524, 697, 124, 911],
                ['egeflqdyvd', 813, 138, 834, 292, 625],
                ['vkrguwdoaw', 642, 607, 209, 688, 699],
                ['rygewgrzst', 670, 570, 499, 557, 518],
                ['stsfbznqtn', 419, 540, 638, 78, 325],
                ['szycvyypig', 786, 581, 489, 279, 264],
                ['rixofzlgil', 483, 243, 970, 664, 313],
                ['yzqrqhtwvt', 213, 887, 55, 119, 211],
                ['rurwvjivsy', 75, 110, 795, 484, 977],
                ['dimuvsdwan', 630, 840, 842, 822, 297],
                ['xnmcmlyyjh', 284, 936, 368, 183, 411],
                ['xogepbuatb', 309, 408, 181, 281, 219],
                ['zpiuwvnfcz', 770, 750, 652, 111, 440]]

        headings = ['column 1', 'column 10', 'column 2', 'column 3', 'column 4', 'column 5']
        col1 = sg.Column([[sg.Table(values=data, headings=headings, max_col_width=35,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=15,
                    tooltip='This is a table')]])
        col2 = sg.Column([[sg.Checkbox('chrom.exe')],[ sg.Checkbox('init')]])
        col3 = sg.Column([[sg.Checkbox('svchost.exe')],[sg.Checkbox('wps.exe ')]])
        # VerticalSeparator(pad=None)

        layout = [[col1,col2,col3]]
        self.window = sg.Window('Window that stays open', layout)
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            print(event, values)
        self.window.close()

class Journal:
    def CreateLogFile(self):
        return "journal" + str(datetime.date.today()) + ".txt"

    def CreateEventList(self):
        return "event" + str(datetime.date.today()) + ".txt"

    def __init__(self):
        self.filename = self.CreateLogFile()
        open(self.filename, 'w')
        self.eventList = self.CreateEventList()
        open(self.eventList, 'w')

    def PidRead(self):
        """ Чтение потокового ввода от subprocess.communicate() и запись в текстовый файл """
        for line in Popen('tasklist', stdout=PIPE).stdout.readlines():
            dline = line.decode('cp866', 'ignore')
            if dline in open(self.filename).read():  # если строка существует, ...
                pass  # ... то пропустить, не записывать ...
            # if mline in open(self.eventList).read():
                self.ShowData(dline)
                with open(self.filename, "a+") as fl:  # ... если строка является уникальной, ...
                    fl.write(dline)

    def ShowData(self,line):
        print(line)

def main():
    # jour = Journal()
    # while (True):
    #     sleep(10)                                                                     # Бесконечное исполнение скрипта. Частота (здесь - 10 сек) - по желанию пользователя.
    #     jour.PidRead()
    inter = Interface()
    inter.DoWindow()

if __name__ == "__main__":
    main()
