import os
#create a parent class CSV_Saver
class CSV_Saver:
    #static method for creating a file
    @staticmethod
    def create(file_name, col1, col2, col3):
        #create a file if it doesn't exist
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                file.write(f"{col1},{col2},{col3}\n")
                print("File Created")
        else:
            print('File Found')

    #class method for reading a file
    @classmethod
    def read(cls):
        #read values from file
        f = open(cls.file_name, 'r')
        print(f.read())

    #classmethod for updating existing records
    @classmethod
    def update(cls):
        found = False
        id = input("Enter Record ID to Update: ")

        with open(cls.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().split(',')[0] == id:
                    found = True
        if found:
            row = input(f"Enter Values (comma separated): ").split(',')
            with open(cls.file_name, 'w') as file:
                for line in lines:
                    if line.strip().split(',')[0] == id:
                        file.write(f"{id},")
                        for i in row:
                            file.write(f"{i},")
                        file.write("\n")
                    else:
                        file.write(line)
                print("Record Updated")
        else:
            print("Record Not Found")

    #classmethod for deleting records
    @classmethod   
    def delete(cls):
        #delete records
        deleted = False
        id = input("Enter Record ID: ")

        with open(cls.file_name, 'r') as file:
            lines = file.readlines()

        with open(cls.file_name, 'w') as file:
            for line in lines:
                if line.strip().split(',')[0] == id:
                    deleted = True
                    continue
                file.write(line)
            if not deleted:
                print("Record not found")
            else:
                print("Record Deleted")

#child class inherits csv_saver class
class CSV_Operation(CSV_Saver):

    def __init__(self, file_name, col1, col2, col3):
        CSV_Operation.file_name = file_name
        CSV_Operation.col1 = col1
        CSV_Operation.col2 = col2
        CSV_Operation.col3 = col3
        super().create(file_name, col1, col2, col3)

    #classmethod for adding new records.
    @classmethod
    def write(cls):
        with open(cls.file_name, 'r') as file:
            lines = file.readlines()
            rows = input(f"Enter Values for {lines[0].split()} (comma separated): ").split(',')
            for line in lines:
                if line.strip().split(',')[0] == rows[0].strip():
                    print("ID already exists. Cannot add value.")
                    return
        with open(cls.file_name, 'a') as file:    
            for i in rows:
                file.write(f"{i},")
            file.write("\n")
            print("Record Added")


#main
file_name =input("Enter file name: ")
csv_op = CSV_Operation(file_name, "ID", "Name", "Price")

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


