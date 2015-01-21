import os
class ReplaceImages():
    
    def __init__(self):
        '''(ReplaceImages) -> NoneType
        '''
        
        self.file_names = []
         
    def original(self):
        '''(ReplaceImages) -> NoneType
        '''        
        folder1 = input('What is the folder containing the original images?:')
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
        folder2 = input('What is the folder of the new images?:')
        path2 = '/Users/pauloruberto/Desktop/' + folder2
        new_files = (os.listdir(path2))
        
        os.chdir(path2)
        
        for file in range(len(new_files)):
            if '.png' in new_files[file]:
                os.rename(new_files[file], self.file_names[file])        

if __name__ == '__main__':
    instance = ReplaceImages()
    instance.original()
    instance.new()
