class item:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}"

class CRUD:
    def __init__(self):
        self.items = {}
        self.next_id = 1

    def Create(self, name, description, price):
        try:
            if price < 0:
                raise ValueError("Price cannot be zero or negative.")
            if not name or not description:
                raise ValueError("Name and description cannot be empty.")
            if not isinstance(price, (int, float)):
                raise ValueError("Price must be a number.")
            if not isinstance(name, str) or not isinstance(description, str):
                raise ValueError("Name and description must be strings.")
        except ValueError as e:
            print(f"Error: {e}")
            return None
        
        new_item = item(self.next_id, name, description, price)
        self.items[self.next_id] = new_item
        self.next_id += 1
        print("Item created successfully.")
        
    def Read(self):
        if not self.items:
            print("No items found.")
            return
        for item in self.items.values():
            print(item)
            
    def Update(self, id, name, description, price):
        if id not in self.items:
            print("Item not found.")
            return
        item = self.items[id]
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            if price < 0:
                print("Price cannot be zero or negative.")
                return
            item.price = price
        
        print("Item updated successfully.")
    
    def Delete(self, id):
        if id not in self.items:
            print("Item not found.")
            return
        del self.items[id]
        print("Item deleted successfully.")
    
crud = CRUD()

while True:
    print("\nMenu:")
    print("[C] - Create Item")
    print("[R] - Read Items")
    print("[U] - Update Item")
    print("[D] - Delete Item")
    print("[Q] - Quit")
    
    choice = input("Enter your choice: ").upper()
    
    if choice == "C":
        name = input("Enter item name: ")
        description = input("Enter item description: ")
        try:
            price = float(input("Enter item price: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue
        crud.Create(name, description, price)
        
    elif choice == "R":
        crud.Read()
        
    elif choice == "U":
        try:
            id = int(input("Enter item ID to update: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            continue
        name = input("Enter new item name (leave blank to keep current): ")
        description = input("Enter new item description (leave blank to keep current): ")
        try:
            price_input = input("Enter new item price (leave blank to keep current): ")
            price = float(price_input) if price_input else None
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue
        crud.Update(id, name, description, price)
        
    elif choice == "D":
        try:
            id = int(input("Enter item ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            continue
        crud.Delete(id)
        
    elif choice == "Q":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")