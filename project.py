from typing import List
import uuid
from colorama import Fore

class Todo:
    def __init__(self, sarlavha: str, tavsif: str = None, tugallangan: bool = None, id: uuid = None) -> None:
        self.sarlavha = sarlavha
        self.tavsif = tavsif
        self.tugallangan = tugallangan
        self.id = id or uuid.uuid4()
    
    def __repr__(self) -> str:
        return Fore.MAGENTA + f"""
    Sarlavha: {self.sarlavha}
    Tavsif: {self.tavsif}
    Tugallangan: {self.tugallangan}
    ID: {self.id}""" + Fore.RESET

class Application:
    def __init__(self, app_name: str, todo_list: List[Todo] = None) -> None:
        self.app_name = app_name
        self.todo_list = todo_list or []
    
    def menu(self):
        print("Todo qo'shish          -> (1)")
        print("Todo o'chirish         -> (2)")
        print("Todo yangilash         -> (3)")
        print("Todo ro'yxatni ko'rish -> (4)")
        print("Chiqish                -> (5)")
        return input("Kerakli bo'limni tanlang: ")
    
    def show_list(self):
        for index, todo in enumerate(self.todo_list, start = 1):
            print(index, todo)

    def add_todo(self):
        sarlavha = input("Sarlavha: ")
        tavsif = input("Tavsif: ")
        todo = Todo(sarlavha=sarlavha, tavsif=tavsif, tugallangan=True)
        self.todo_list.append(todo)
        print(Fore.GREEN + "Muvaffaqiyatli qo'shildi" + Fore.RESET)
    
    def delete_todo(self):
        try:
            self.show_list()
            index = int(input("Index kiriting: "))
            if index < 1 or index > len(self.todo_list):
                print(Fore.RED + "Ushbu indeks diapazondan tashqarida" + Fore.RESET)
            elif index == str:
                print(Fore.RED + "Faqat index bo'iycha murojat qiling:" + Fore.RESET)
            else:
                del self.todo_list[index - 1]
                print(index, Fore.GREEN + "chi index muvaffaqiyatli o'chirildi" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Faqat raqam bilan mirojat qiling!" + Fore.RESET)

    def update_todo(self):
        try:
            self.show_list()
            index = int(input("Index kiriting: "))
            if index < 1 or index > len(self.todo_list):
                print(Fore.RED + "Ushbu indeks diapazondan tashqarida" + Fore.RESET)
            else:
                sarlavha = input("Sarlavha: ")
                tavsif = input("Tavsif: ")
                tugallangan = input("Tugallangan: [True, False] ")
                todo = self.todo_list[index - 1]

                if len(sarlavha) > 0:
                    todo.sarlavha = sarlavha
                if len(tavsif) > 0:
                    todo.tavsif = tavsif
                if tugallangan in ['True', 'False']:
                    todo.tugallangan = tugallangan
                print(Fore.GREEN + "Muvaffaqiyatli yangilandi" + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Faqat raqam bilan mirojat qiling!" + Fore.RESET)
    
    def run(self):
        print(Fore.YELLOW + self.app_name + Fore.RESET, Fore.BLUE + "Boshlandi..." + Fore.RESET)
        while True:
            choice = self.menu()
            if choice == '1':
                self.add_todo()
            elif choice == '2':
                self.delete_todo()
            elif choice == '3':
                self.update_todo()
            elif choice == '4':
                self.show_list()
            elif choice == '5':
                break
            else:
                print(Fore.RED + "Noto'g'ri tanlov: [1,2,3,4,5]" + Fore.RESET)
        print(Fore.YELLOW + self.app_name + Fore.RESET, Fore.BLUE + "Chiqish..." + Fore.RESET)

if __name__ == '__main__':
    app = Application("Trello:")
    app.run()



print("Hello World")
