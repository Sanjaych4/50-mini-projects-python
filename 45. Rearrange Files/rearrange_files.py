# Day 45: Rearrange Files

import os
import shutil


class RearrangeFile:
    def __init__(self):
        self.folder_path = os.getcwd()
        self.list_of_all_files = os.listdir(self.folder_path)

    def make_folder_and_return_name(self, foldername):
        if not os.path.exists(foldername):
            os.mkdir(foldername)
        else:
            i = 2
            while os.path.exists(foldername + str(i)):
                i += 1
            foldername = foldername + str(i)
            os.mkdir(foldername)
        return foldername

    def check_folder_existence(self):
        for filename in self.list_of_all_files:
            if filename.endswith('.pdf'):
                foldername = self.make_folder_and_return_name('pdfs')
                shutil.move(os.path.join(self.folder_path, filename), os.path.join(self.folder_path, foldername))
            elif filename.endswith('.jpg'):
                foldername = self.make_folder_and_return_name('jpgs')
                shutil.move(os.path.join(self.folder_path, filename), os.path.join(self.folder_path, foldername))

if __name__ == '__main__':
    re = RearrangeFile()
    re.check_folder_existence()
