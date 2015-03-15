import os
import shutil

directory = '/Users/pauloruberto/Desktop/'
print('-------------------------------------------------------')
folder = input('What is the folder containing the ORIGINAL images?: ')
image = input('What is the name of the NEW image? (with extension): ')

class RemoveDS_Store():
    
    def __init__(self):
        '''(ReplaceImages) -> NoneType
        '''
        
        self.file_names = []
    
    def remove_ds(self):
        '''(ReplaceImages) -> NoneType
        '''
    
        path2 = directory + folder
        self.new_files = (os.listdir(path2))
    
        os.chdir(path2)
        
        for file in range(len(self.new_files)):
            if 'DS_Store' in self.new_files[file]:
                os.remove(self.new_files[file])
 
class ReplaceImages(RemoveDS_Store):
    def __init__(self):
        
        RemoveDS_Store.__init__(self)
        
    def rename_old_folder(self):
        
        original_name = directory + folder
        new_name = directory + folder + '-ORIGINAL'
        
        os.rename(original_name, new_name)
    
    
    def get_original_images(self):
        
        path = directory + folder + '-ORIGINAL'
        
        self.file_names = []
        
        os.chdir(path)
        
        # Iterate of each image, if it is a .png, add it to the list of files
        for file in (os.listdir(path)):
                if '.png' in file:
                    self.file_names.append(file)        
        
    def create_new_folder(self):
        
        new_folder = directory + folder
        os.makedirs(new_folder)
    
    def get_new_images(self):
        n = 'copy'
        
        path_name = directory + folder
        file_name = directory + image
        image_name_backup = directory + image
        
        for item in self.file_names:
            # copy the file
            shutil.copy(file_name, path_name)
            
            # rename the image to something else
            old_name = file_name
            new_name = file_name + n
            os.rename(old_name, new_name)
            
            # set the file name to the new name
            file_name = new_name
    
        # set the file name back to the original
        
        os.rename(file_name, image_name_backup)
        
    def rename_images(self):
        
        path_name = directory + folder
        self.new_files = (os.listdir(path_name))
        
        os.chdir(path_name)
        
        for file in range(len(self.new_files)):
            if '.png' in self.new_files[file]:
                os.rename(self.new_files[file], self.file_names[file])  
                
        print('-------------------------------------------------------')
        print('Complete! {} images have been created & named.'.format(len(self.new_files)))
        
    
if __name__ == '__main__':
    instance1 = RemoveDS_Store()
    instance1.remove_ds()
    instance2 = ReplaceImages()
    instance2.rename_old_folder()
    instance2.create_new_folder()
    instance2.get_original_images()
    instance2.get_new_images()
    instance2.rename_images()
