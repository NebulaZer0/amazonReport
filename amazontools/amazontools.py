import os
from colorama import Fore
import pandas as pd


class amazonTools:
    def __init__(self, report):
        try:
            if os.path.isfile(report):
                amazonCSV = pd.read_csv(report)
                self.fileName = report[str(report).rfind('/') + 1:]
                self.totalRows = len(amazonCSV)
                self.startDate = str(amazonCSV.iloc[0][0])
                self.endDate = str(amazonCSV.iloc[self.totalRows - 1][0])

                startDateYear = int(self.startDate[self.startDate.rfind("/") + 1:])
                endDateYear = int(self.endDate[self.endDate.rfind("/") + 1:])
                self.totalYears = endDateYear - startDateYear

                self.orderPrices = amazonCSV['Item Total']

            else:
                raise FileExistsError

        except FileExistsError as Err:
            print(Fore.RED + "Error: File Not Found! Exiting...")
            exit(0)

    def totalSpent(self):
        total = 0

        for price in self.orderPrices:
            price = str(price).replace('$', '')
            price = float(price)
            total += price

        return round(total, 2)

    def averageSpent(self):
        return round(self.totalSpent() / self.totalYears, 2)

    def printFileInfo(self):
        print(Fore.LIGHTYELLOW_EX + f"File Information:"
                                    f"\n{Fore.LIGHTCYAN_EX + ' ' * 5}Name: {Fore.CYAN + self.fileName}"
                                    f"\n{Fore.LIGHTCYAN_EX + ' ' * 5}Start Date: {Fore.CYAN + self.startDate}"
                                    f"\n{Fore.LIGHTCYAN_EX + ' ' * 5}End Date: {Fore.CYAN + self.endDate}"
                                    f"\n{Fore.LIGHTCYAN_EX + ' ' * 5}Total Years: {Fore.CYAN + str(self.totalYears)}"
                                    f"\n{Fore.LIGHTCYAN_EX + ' ' * 5}Rows: {Fore.CYAN + str(self.totalRows)}\n")
