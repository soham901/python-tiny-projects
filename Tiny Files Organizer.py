import os
import shutil

if __name__ == '__main__':
    # Get the path to the folder from the user
    path = input("Enter the path to the folder : ")

    # change current directory to the path
    os.chdir(path)

    # get all the files not folders (Directories)
    files = [f for f in os.listdir(path) if os.path.isfile(f)]

    # check if there is not files then raise an error
    if not len(files):
        raise ValueError('All the files are aldready sorted or here is not files')

    # get all the extensions set (Non Duplicate) then converted it to list
    extensions = list(set(file.split('.')[-1] for file in files))
    
    print('\nHere is the all the extensions of your files :')
    for inx, extension in enumerate(extensions, start=1):
        print(f'{inx}. {extension}')
    
    # split user's choices by , and add it to the set (Non Duplicate)
    choices_of_extensions = set(input('\nEnter the id of extensions that you want to in a seperate folder (comma seperate) : ').split(','))

    # convert it to list and remove extra spaces
    choices_of_extensions = set(choice.strip() for choice in choices_of_extensions)

    # try to move the selected extension's files to the folders of extension
    try:
        for i in choices_of_extensions:
            extension = extensions[int(i)-1]
            folder = extension.title()
            # dont create another directory if its aldready exists
            if not os.path.exists(folder): os.mkdir(folder)
            # get only files which have the current extension
            t_files = [f for f in files if f.endswith(extension)]
            # finally move these files to their allocated folder
            for file in t_files:
                shutil.move(os.path.join(path, file), os.path.join(folder, file))
    
    # handle errors
    except Exception as e:
        print(e.with_traceback)
