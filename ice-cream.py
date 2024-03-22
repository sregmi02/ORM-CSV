import csv
from prettytable import PrettyTable
class IceCreamShop:
    @staticmethod
    def create_menu():
        fields_ic = ['Flavor','Price']
        rows_ic = [
            ['Chocolate','200'],
            ['Vanilla','190'],
            ['Strawberry','200']
        ]
        with open('ice-cream-menu.csv', 'w', newline = '') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(fields_ic)
            csvwriter.writerows(rows_ic)
        
        fields_c = ['Type', 'Price']
        rows_c = [
            ['Waffle', '50'],
            ['Sugar', '20']
        ]
        with open('cone-menu.csv', 'w', newline = '') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(fields_c)
            csvwriter.writerows(rows_c)
        

    @staticmethod
    def read_menu():
        print("Ice-Creams: ")
        with open('ice-cream-menu.csv','r') as file:
            csvreader = csv.reader(file)
            table = PrettyTable(next(csvreader))
            for row in csvreader:
                table.add_row(row)
            print(table)


        print("Cones: ")
        with open('cone-menu.csv','r') as file:
            csvreader = csv.reader(file)
            table = PrettyTable(next(csvreader))
            for row in csvreader:
                table.add_row(row)
            
            print(table)

    @staticmethod
    def is_available(flavor, cone):
        flavor_found = False
        cone_found = False
        with open ('ice-cream-menu.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if flavor in row:
                    flavor_found = True
        
        with open ('cone-menu.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if cone in row:
                    cone_found = True
        
        return flavor_found, cone_found

    @staticmethod
    def billing(flavor, scoop, cone):
        price = 0
        with open ('ice-cream-menu.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if flavor in row:
                    price = int(row[1])*scoop
        with open ('cone-menu.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if cone in row:
                    price = price + int(row[1])*scoop
               
                    
        table = PrettyTable(['Flavor', 'Cone', 'Scoops', 'Price'])
        table.add_row([flavor, cone, scoop, price])
        print(table)

        
IceCreamShop.create_menu()
print("Menu: ")
IceCreamShop.read_menu()

while(True):
    flavor = input("Enter Flavor: ")
    scoops = int(input("Enter Number of Scoops: "))
    if (scoops>0):
        cone = input("Enter Cone Type: ")

        flavor_found, cone_found = IceCreamShop.is_available(flavor, cone)
        
        if flavor_found and cone_found:
            print("Calculating Price....")
            IceCreamShop.billing(flavor, scoops, cone)
        else:
            print("Item not Found")
    else:
        print("Number of Scoops cannot be less than zero")

    next_order = input("Order More? (Y/N): ")
    if next_order != 'Y':
        exit(-1)



    



