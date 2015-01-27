import os
print('-------------------------------------------------------')
folder2 = input('What is the folder containing the NEW images?:')

class RemoveDS_Store():
    
    def __init__(self):
        '''(ReplaceImages) -> NoneType
        '''
        
        self.file_names = []
        self.folder2 = ''
    
    def remove_ds(self):
        '''(ReplaceImages) -> NoneType
        '''
    
        #self.folder2 = input('What is the folder containing the NEW images?:')
        path2 = '/Users/pauloruberto/Desktop/' + folder2
        self.new_files = (os.listdir(path2))
    
        os.chdir(path2)
        
        for file in range(len(self.new_files)):
            if 'DS_Store' in self.new_files[file]:
                os.remove(self.new_files[file])
 
class ReplaceImages(RemoveDS_Store):
    def __init__(self):
        
        RemoveDS_Store.__init__(self)
        
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
                    
                            
    def new(self):
        '''(ReplaceImages) -> NoneType
        '''
        
        path2 = '/Users/pauloruberto/Desktop/' + folder2
        self.new_files = (os.listdir(path2))
        
        os.chdir(path2)
        
        for file in range(len(self.new_files)):
            if '.png' in self.new_files[file]:
                os.rename(self.new_files[file], self.file_names[file])  
                
        print('-------------------------------------------------------')
        print('Complete! {} images renamed.'.format(len(self.new_files)))

if __name__ == '__main__':
    
    instance1 = RemoveDS_Store()
    instance1.remove_ds()
    print('-------------------------------------------------------')
    print('Removed hidden .DS_Store file.')
    instance2 = ReplaceImages()
    instance2.original()
    instance2.new()
