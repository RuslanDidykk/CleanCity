import csv

from managers.Generator import Generator


def saveCSV(list_data):
    time = Generator().generate_timestamp()
    print(str(time))
    with open('../../../../'+'raport: '+time +'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for item in list_data:
            writer.writerow((
                item.klient_nazwa,
                item.ulica,
                item.pracownik,
                item.pojazd,
                item.date,
                item.sprzet,
                item.sprzet_ilosc
            ))