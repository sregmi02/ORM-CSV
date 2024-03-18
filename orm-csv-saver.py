import os

class CSV_Saver:

    @staticmethod
    def create(file_name):
        #create a file if it doesn't exist
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                cols = input("Enter Column Names(column separated): ").split(',')
                for i in cols:
                    file.write(f"{i},")
                file.write("\n")
                print("File Created")
        else:
            print('File Found')


    def read(self):
        #read values from file
        f = open(self.file_name, 'r')
        print(f.read())

    def write(self):
        pass


    def update(self):
        pass
        
    def delete(self):
        #delete records
        deleted = False
        id = input("Enter Record ID: ")

        with open(self.file_name, 'r') as file:
            lines = file.readlines()

        with open(self.file_name, 'w') as file:
            for line in lines:
                if line.strip().split(',')[0] == id:
                    deleted = True
                    continue
                file.write(line)
            if not deleted:
                print("Record not found")
            else:
                print("Record Deleted")


class CSV_Operation(CSV_Saver):
    def __init__(self, file_name):
        self.file_name = file_name
        super().create(file_name)

    def write(self):
        #add records to a file
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            rows = input(f"Enter Values for {lines[0].split()} (comma separated): ").split(',')
            for line in file:
                if line.strip().split(',')[0] == rows[0].strip():
                    print("ID already exists. Cannot add value.")
                    return
        with open(self.file_name, 'a') as file:    
            for i in rows:
                file.write(f"{i},")
            file.write("\n")
            print("Record Added")

    def update(self):
        found = False
        id = input("Enter Record ID to Update: ")

        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().split(',')[0] == id:
                    found = True
        if found == True:
            row = input(f"Enter Values (comma separated): ").split(',')
            with open(self.file_name, 'w') as file:
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


file_name =input("Enter file name: ")
csv_op = CSV_Operation(file_name)
while True:
    print("Enter an Operation")
    print("1. Add Record\n2. Delete Record\n3. Update Record\n4. Read Records\n5. Exit")
    choice = int(input())
    if choice == 1:
        #write
        csv_op.write()
    elif choice == 2:
        #delete
        csv_op.delete()
    elif choice == 3:
        #update
        csv_op.update()
    elif choice == 4:
        #read
        csv_op.read()
    elif choice == 5:
        exit(-1)
    else:
        print("Wrong Input")


