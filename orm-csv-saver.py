import os
#create a parent class CSV_Saver

def validator(id, name, price):
    if id.isdigit() and (not name.isdigit()) and price.isdigit():
        return True
    else:
        return False

class CSV_Saver:
    #static method for creating a file
    @staticmethod
    def create(file_name, col1, col2, col3):
        with open(file_name, 'w') as file:
            file.write(f"{col1},{col2},{col3}\n")
            print("File Created")
        
    #class method for reading a file
    @classmethod
    def read(cls):
        #read values from file
        found = False
        search = input("Enter Record ID or Name: ")
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip().split(",")[0] == search or line.strip().split(",")[1] == search:
                    print(line)
                    found = True
            if not found:
                print("Record not Found")

    #classmethod for updating existing records
    @classmethod
    def update(cls):
        found = False
        id = input("Enter Record ID to Update: ")
        updated_lines = []

        with open(cls.file_name, 'r') as file:
            for line in file:
                if line.strip().split(',')[0] == id:
                    try:
                        id, name, price = input(f"Enter Values (comma separated): ").split(',')
                    except ValueError:
                        print("Invalid Input")
                        return
                    if not validator(id, name, price):
                        print("Invalid Input")
                        return
                    else:
                        line = ','.join([id, name, price])
                updated_lines.append(line)
                    
        with open(cls.file_name, 'w') as file:
            for line in updated_lines:
                file.write(line)
            
        if updated_lines:
            print('Record Updated')
        else:
            print("Record not Found")
                
    #classmethod for deleting records
    @classmethod   
    def delete(cls):
        #delete records
        deleted = False
        id = input("Enter Record ID: ")
        remaining_lines = []
        with open(cls.file_name, 'r') as file:
            for line in file:
                if line.strip().split(',')[0] == id:
                    deleted = True
                else:
                    remaining_lines.append(line)

        with open(cls.file_name, 'w') as file:
            for line in remaining_lines:
                file.write(line)
        
        if deleted:
            print("Record Deleted")
        else:
            print("Record not Found")


#child class inherits csv_saver class
class CSV_Operation(CSV_Saver):

    def __init__(self, file_name, col1, col2, col3):
        CSV_Operation.file_name = file_name
        CSV_Operation.col1 = col1
        CSV_Operation.col2 = col2
        CSV_Operation.col3 = col3
        

    #classmethod for adding new records.
    @classmethod
    def write(cls):
        with open(cls.file_name, 'r') as file:
            next(file)
            try:
                id, name, price = input(f"Enter Values (comma separated): ").split(',')
            except ValueError:
                print("Invalid Input")
                return
        
            if not validator(id,name,price):
                print("Invalid Input")
                return

            for line in file:
                if int(line.strip().split(',')[0]) == int(id):
                    print("ID already exists. Cannot add value.")
                    return
                
        with open(cls.file_name, 'a') as file:   
            file.write(f"{id},{name},{price}\n") 
            print("Record Added")
            

#main
file_name =input("Enter file name: ")
if not os.path.exists(file_name):
    col1 = input("Enter Column1 Name: ")
    col2 = input("Enter Column2 Name: ")
    col3 = input("Enter Column3 Name: ")
    csv_op = CSV_Operation(file_name, col1, col2, col3)
    CSV_Operation.create(file_name, col1, col2, col3)
else:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        col1, col2, col3 = lines[0].split(',')
        csv_op = CSV_Operation(file_name, col1, col2, col3)

while True:
    print("Enter an Operation")
    print("1. Add Record\n2. Delete Record\n3. Update Record\n4. Read Records\n5. Exit")
    choice = int(input())
    if choice == 1:
        #write operation accesses the method from its own class
        CSV_Operation.write()
    elif choice == 2:
        #delete operation accesses the method from parent class
        CSV_Operation.delete()
    elif choice == 3:
        #update operation accesses the method from parent class
        CSV_Operation.update()
    elif choice == 4:
        #read operation accesses the method from parent classs
        CSV_Operation.read()
    elif choice == 5:
        #exit control
        exit(-1)
    else:
        print("Wrong Input")


