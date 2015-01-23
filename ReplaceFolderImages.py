import os
class ReplaceImages():
    
    def __init__(self):
        '''(ReplaceImages) -> NoneType
        '''
        
        self.file_names = []
        self.folder2 = ''
         
    def original(self):
        '''(ReplaceImages) -> NoneType
        '''
        print('-------------------------------------------------------')
        folder1 = input('What is the folder containing the ORIGINAL images?:')
        path1 = '/Users/pauloruberto/Desktop/' + folder1
        original_files = (os.listdir(path1))
        self.file_names = []
        
        os.chdir(path1)
        
        for file in original_files:
                if '.png' in file:
                    self.file_names.append(file)
                    
    def remove_ds(self):
        '''(ReplaceImages) -> NoneType
        '''
    
        self.folder2 = input('What is the folder containing the NEW images?:')
        self.path2 = '/Users/pauloruberto/Desktop/' + self.folder2
        self.new_files = (os.listdir(self.path2))
    
        os.chdir(self.path2)
        
        for file in range(len(self.new_files)):
            if 'DS_Store' in self.new_files[file]:
                os.remove(self.new_files[file])        
                            
    def new(self):
        '''(ReplaceImages) -> NoneType
        '''
        
        self.folder2 = input('What is the folder containing the NEW images?:')
        self.path2 = '/Users/pauloruberto/Desktop/' + self.folder2
        self.new_files = (os.listdir(self.path2))        
        
        os.chdir(self.path2)
        
        for file in range(len(self.new_files)):
            if '.png' in self.new_files[file]:
                os.rename(self.new_files[file], self.file_names[file])  
                
        print('-------------------------------------------------------')
        print('Complete! {} images renamed.'.format(len(self.new_files)))

if __name__ == '__main__':
    instance1 = ReplaceImages()
    print('-------------------------------------------------------')
    print("This is to remove hidden .DS_Store files")
    instance1.remove_ds()
    print('-------------------------------------------------------')
    print(".DS_Store files removed!")
    instance2 = ReplaceImages()
    instance2.original()
    instance2.new()
