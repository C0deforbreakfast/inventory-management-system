import csv
from display_message_gui import ShowMessage
from Info_table_gui import InfoTable

# git push -u origin master
class Product:
    def __init__(self, id: int, name: str, in_date: str, out_date: str) -> None:
        self.ID = id
        self.p_name = name
        self.in_date = in_date
        self.out_date = out_date
        

class Record:
    def __init__(self, product_id: int, quantity: int) -> None:
        self.p_id = product_id
        self.quantity = quantity


class Main:
    def __init__(self):
        self.products_file = "data/products.csv"
        self.storage_file = "data/storage.csv"

    def display_error(self, e):
        ShowMessage().run(e)
    
    def display_message(self, m):
        ShowMessage().run(m)

    def get_id(self, filename: str) -> int:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = [row for row in csv_reader] # Returns all the rows
            collumn = [row for row in rows[len(rows) - 1]] # Returns whole row
            if len(collumn) == 0:
                collumn = [row for row in rows[len(rows) - 2]] # Returns whole row
            ID = collumn[0]
            return int(ID)

    def create_product(self, name: str, in_date: str, out_date: str) -> None:
        product_id:int = self.get_id(self.products_file)
        # Created a product object
        offset = 1
        product_obj = Product(product_id + offset ,name, in_date, out_date)

        if (len(product_obj.p_name) == 0 or
            len(product_obj.in_date) == 0 or
            len(product_obj.out_date) == 0):
            e = "Please fill all the fields\n"
            self.display_error(e)
        else:
            m = "product added successfully!\n"
            with open(self.products_file, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([product_obj.ID, 
                                    product_obj.p_name, 
                                    product_obj.in_date,
                                    product_obj.out_date])
            offset += 1
            self.display_message(m)

    def is_added(self, id: int, filename: str) -> bool:
        with open(filename, 'r') as csv_file: # Opening the csv file
            csv_reader = csv.reader(csv_file) 
            rows = [row for row in csv_reader] # Iterating through the csv file
            for row in rows[1:len(rows):]:
                obj_id = row[0] # Id column 
                if id == obj_id:
                    return True
            return False

    def delete_product(self, id: int) -> None:
        updated_list = [] # For updating product list after deletion
        if self.is_added(id, self.products_file):
            m = "Product deleted successfully!\n"
            with open(self.products_file, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                rows = [row for row in csv_reader]
                for row in rows:
                    if len(row) != 0: # Only the rows that are not empty
                        if row[0] != str(id): # Compare with the given id
                            updated_list.append(row)
            with open(self.products_file, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(updated_list) # Update the csv file
            self.display_message(m)
        else:
            e = "The product doesn't exist!"
            self.display_error(e)

    def diplay_products(self) -> list:
        to_display = []
        with open(self.products_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = [row for row in csv_reader]
            for row in rows:
                if len(row) != (0 or 1):
                    info = row[:len(row):]
                    id = info[0]
                    name = info[1]
                    in_date = info[2]
                    out_date = info[3]
                    info_display = (id, name, in_date, out_date)
                    to_display.append(info_display)
        return to_display

    def get_product_info(self, id: int) -> tuple:
        # Getting information about products
        if self.is_added(id, self.products_file):
            with open(self.products_file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                rows = [row for row in csv_reader]
                for row in rows[1:len(rows):]:
                        obj_id = row[0]
                        if id == obj_id:
                            return row[1], row[2], row[3] # The name and in and out date of the product
                        
    def search_product_info(self, id: int) -> list:
        # Getting information about products
        if self.is_added(id, self.products_file):
            with open(self.products_file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                rows = [row for row in csv_reader]
                for row in rows[1:len(rows):]:
                        obj_id = row[0]
                        if id == obj_id:
                            e1 = list(("name", "store date", "discard date"))
                            e2 = list((row[1], row[2], row[3])) # The name and in and out date of the product
                            return [e1, e2]
        else:
            e = "No product with the given id!"
            self.display_error(e)

    def search_storage_info(self, id: int) -> tuple:
        # Getting information about storage
        if self.is_added(id, self.storage_file):
            with open(self.storage_file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                rows = [row for row in csv_reader]
                for row in rows[1:len(rows):]:
                    obj_id = row[0]
                    if id == obj_id:
                        e1 = list(("name", "store date", "discard date", "quantity"))
                        e2 = list((row[1], row[2], row[3], row[4])) # The name and in and out date and quantity of products in storage
                        return [e1, e2]
        else:
            e = "No record with the given id!"
            self.display_error(e)

    def create_record_in_storage(self, id: int, quantity: int):
        if self.is_added(id, self.products_file): # Checking wether the product exists or not
            m = "Product added successfully!\n"
            offset = 1
            record_id: int = self.get_id(self.storage_file) # Getting the last storage ID
            # Created a product object
            record_obj = Record(record_id + offset, quantity) # Creating a record object
            with open(self.storage_file, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                product_info = self.get_product_info(id)
                product_name = product_info[0]
                product_in_date = product_info[1]
                product_out_date = product_info[2]
                csv_writer.writerow([record_obj.p_id,  
                                    product_name,
                                    product_in_date,
                                    product_out_date, 
                                    record_obj.quantity]) # Writing on storage file
            offset += 1
            self.display_message(m)
        else:
            e = "No product with the given id exists!"
            self.display_error(e)

    def delete_record(self, id: int) -> None:
        updated_list = [] # For updating product list after deletion
        if self.is_added(id, self.storage_file):
            m = "Product deleted successfully!\n"
            with open(self.storage_file, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                rows = [row for row in csv_reader]
                for row in rows:
                    if len(row) != 0: # Only the rows that are not empty
                        if row[0] != str(id): # Compare with the given id
                            updated_list.append(row)
            with open(self.storage_file, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(updated_list) # Update the csv file
            self.display_message(m)
        else:
            e = "The product doesn't exist!"
            self.display_error(e)

    def display_storage(self) -> list:
        to_display = []
        with open(self.storage_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = [row for row in csv_reader]
            for row in rows:
                if len(row) != (0 or 1):
                    id, name, in_date, out_date, quantity = row[0], row[1], row[2], row[3], row[4]
                    info_display = (id, name, in_date, out_date, quantity)
                    to_display.append(info_display)
        return to_display
    
    def add_product(self, name: str, in_date: str, out_date: str) -> None:
        name: str = name
        in_date: str = in_date
        out_date: str = out_date
        self.create_product(name, in_date, out_date)

    def remove_product(self, id: str) -> None:
        id_del: str = id
        self.delete_product(id_del)

    def list_of_products(self) -> None:
        return self.diplay_products() 
    
    def add_product_to_storage(self, id: str, quantity: str) -> None:
        id_add: str = id
        quantity_add: str = quantity
        self.create_record_in_storage(id_add, quantity_add)

    def remove_product_from_storage(self, id: str) -> None:
        id: str = id
        self.delete_record(id)

    def storage(self) -> None:
        return self.display_storage()
    
    def search_products(self, id: int) -> None:
        list = self.search_product_info(id)
        if list != None:
            InfoTable().run(list)

    def search_storage(self, id: int) -> None:
        list = self.search_storage_info(id)
        if list != None:
            InfoTable().run(list)


if __name__ == '__main__':

    m = Main()
    
