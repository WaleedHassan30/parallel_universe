import Functions
import lang.messages as messages
import importlib
import time
import random
import os
importlib.reload(Functions)
importlib.reload(messages)
#################################################
class App:
    folder_back = ""
    path_parent = ""
    count_of_files = 0
    percentage = 0
    len_files = 0
    def __init__(self,user_set_new_dir):
        self.user_set_new_dir = user_set_new_dir

    def Remove_Duplicates_with(self,dir):
        for i in dir:
          if i == "\\":
            dir == i  
    
    def current_path(self):
        os.getcwd()
        print(f"now you are here: {self.user_set_new_dir}")
    def get_new_dir(self):
        os.chdir(f"{self.user_set_new_dir}")
        print(self.Remove_Duplicates_with(os.getcwd()))

    def get_list_of_folders(self):
        self.get_new_dir()
        #list_of_folders = list(os.listdir(os.getcwd()))
        for root, dirnames, filenames in os.walk('.'):
            list_of_folders = dirnames
            break
        folder_choose_number = (list(range(1,len(list_of_folders) +1)))
        global access_folder
        access_folder = {}
        
        for menu_num,folder in zip(folder_choose_number,list_of_folders):
                access_folder[folder] = menu_num
                print(f"to Access Folder Name | {folder} | press Enter number {menu_num}")
        print("to backward press enter 0")
    def get_specific_folder(self):
        #self.get_new_dir()
        self.get_list_of_folders()
        user_choose = (int(input("Enter Folder number for access it: ")))
        for folder_name , folder_number in access_folder.items():
            if user_choose == folder_number:
                user_set_new_dir = os.getcwd()+"\\"+folder_name
                self.user_set_new_dir = user_set_new_dir
                self.folder_back = folder_name
                os.chdir(self.user_set_new_dir)
        print(f"now you are here: {self.user_set_new_dir}")
    def backward(self):
        self.path_parent = os.path.dirname(os.getcwd())
        os.chdir(self.path_parent)
        print("changed dir | now you are here: " , os.getcwd())
    
    def show_files(self):
        global access_files
        access_files = {}
        list_of_files = list(os.listdir(os.getcwd()))
        self.len_files = len(list_of_files)
        file_choose_number = (list(range(1,len(list_of_files) +1)))
        for menu_num,file in zip(file_choose_number,list_of_files):
                access_files[file] = menu_num
                print(f"file Name | {file} ")
                self.len_files += 1
                time.sleep(0.5)
        print("Reading Done")

    def access_all_files(self):
        pass

    def delete_files(self):
        print("")

    def show(self):
        for key , value in messages.choose_Action_files.items():
            print(key)
    def Action_Menu(self):
        self.show()
        choose_num=input("press number: ")
        for key , value in messages.choose_Action_files.items():
            if value == choose_num:
                if value ==  "1":
                    temp = int(input(messages.percentage_delete))
                    if temp > 0 and temp <=100:
                        list_of_files = list(os.listdir(os.getcwd()))
                        file_choose_number = len(list_of_files)
                        self.percentage = round(file_choose_number * temp / 100)
                        print(f"you choose {temp}% from all files ({file_choose_number} files | we delete about {self.percentage} files )")
                        Confirm = input(messages.confirm_files_delete)
                        if Confirm.lower() == "y":
                            for i in range(self.percentage):
                                file_del = random.choice(list_of_files)
                                os.remove(os.getcwd()+"//"+file_del)
                                list_of_files.remove(file_del)
                                print(f"deleted file: {file_del}")
                                time.sleep(1)

                        else:
                            break
                    else:
                        print("you can select files from 1% to 100%")
                    break
                elif value == "2":
                    ##print("delete with starts m or n")
                    count = 0
                    first_letter = input("Enter what letter is at the beginning of the file name to deleting? ")
                    if len(first_letter) == 1:
                        Confirm = input(f"do you need to delete all files start with ({first_letter}) press y to start")
                        if Confirm.lower() == "y":
                            list_of_files = list(os.listdir(os.getcwd()))
                            for i in list_of_files:
                                file_del = i
                                if file_del[0] == first_letter.lower() or file_del[0] == first_letter.upper():
                                    os.remove(os.getcwd()+"//"+file_del)
                                    count +=1
                                    list_of_files.remove(file_del)
                                    print(f"deleted file: {file_del}")
                                    time.sleep(1)
                            print(f"Done | deleted all files start ({first_letter}) and count is | ({count}) files")   
                    else:
                        print("you can choose first letter only..... please try again")

                    break
                elif value == "3":
                    #print("To delete with last name starts specific letter press 3")
                    count = 0
                    last_letter = input("Type the start letter at the end of the name you want to delete? ...")
                    if len(last_letter) == 1:
                        Confirm = input(f"do you need to delete all files start with ({last_letter}) press y to start")
                        if Confirm.lower() == "y":
                            list_of_files = list(os.listdir(os.getcwd()))
                            for i in list_of_files:
                                file_del = i
                                if " " in file_del:
                                    l_file_name = file_del.split(" ")
                                    l_name = l_file_name[1]
                                    if l_name[0] == last_letter.lower() or l_name[0] == last_letter.upper():
                                            os.remove(os.getcwd()+"//"+file_del)
                                            count +=1
                                            list_of_files.remove(file_del)
                                            print(f"deleted file: {file_del}")
                                            time.sleep(1)
                            print(f"Done | deleted all files with last name start ({last_letter}) and count is | ({count}) files")   
                    else:
                        print("you can choose first letter only..... please try again")

                        
                elif value == "4":
                    #print("To convert files names to upper or lower press 4 ")
                    count = 0
                    list_of_files = list(os.listdir(os.getcwd()))
                    for i in list_of_files:
                        file_rename = i
                        if file_rename.isupper():
                            is_upper = True
                            print(f"the file  {file_rename}  already is upper .....")
                            time.sleep(1)
                        else:
                            is_upper = False
                            upper = file_rename.upper()
                            temp = file_rename
                            os.rename(file_rename,upper)
                            count +=1
                            list_of_files.remove(file_rename)
                            print(f"{temp} has been renamed to {upper} ..... ")
                            time.sleep(1)
                    print(f"Done | all files has been renamed to uppercase and count is | ({count}) files")   
                   
    def Main_Menu(self):
        print ("#############################################################################")
        print ("########                                                             ########")
        print ("########             Assignment Management Application               ########")
        print ("########                       27/02/2022                            ########")
        print ("######## ----------------------------------------------------------- ########")
        print ("########                                                             ########")
        print ("########                    Choose an option:                        ########")
        print ("#############################################################################")
        #######################################################################################
        self.Action_Menu()
        print ("######## ----------------------------------------------------------- ########")

