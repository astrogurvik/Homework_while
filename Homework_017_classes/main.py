import datetime


class Project:
    def __init__(self, name, start, end, list_names, ):
        self.Name = name
        self.Start_date_time = start
        self.End_date = end
        self.List_prgrmers = list_names

    def __str__(self):
        return f'Project name: "{self.Name}"\n' \
                f'Date and time the project started: {self.Start_date_time:%F, %T}\n' \
                f'Project deadline date: {self.End_date}\n' \
                f'List of programmers working on the project:{self.List_prgrmers}\n'

    # def print_list(self, list_names):
    #     for i in list_names:
    #         print(i)

    def change_end(self, new_end_date):
        confirm = input('Do you want to change the Project deadline date? Enter "yes" or "no":\n')
        self.End_date = new_end_date if confirm == 'yes' else print('You refused')

    def add_prgrmer(self, new_prgrmer):
        confirm = input('Do you want to add a new programmer to the list of programmers '
                        'working on the project? Enter "yes" or "no":\n')
        self.List_prgrmers.append(new_prgrmer) if confirm == 'yes' else print('You refused')

    def remove_prgrmer(self, former_prgrmer, list_names):
        message = input('Do you want to remove a new programmer from the list of programmers '
                        'working on the project? Enter "yes" or "no":\n')
        if message == 'yes':
            if former_prgrmer in list_names:
                self.List_prgrmers.remove(former_prgrmer)
            else:
                print('There is no this programmer in the list of programmers')
        else:
            print('You refused')

Start_Project = datetime.datetime.now()
List_prgrmers = ['John', 'Bill', 'Kurt']
Project1 = Project('OnLineShop', Start_Project, '2024-02-12', List_prgrmers)
print(Project1)
# print(Project1.print_list(List_prgrmers))

# NameForAdd = input('Enter the name of the programmer '
#                    'you want to add from the list of programmers:\n')
# NameForRemove = input('Enter the name of the programmer '
#                       'you want to remove from the list of programmers:\n')

Project1.change_end('2025-05-01')
Project1.add_prgrmer('Klaus')
Project1.remove_prgrmer('Bill', List_prgrmers)
print(Project1)
# print(Project1.print_list(List_prgrmers))
print(List_prgrmers)