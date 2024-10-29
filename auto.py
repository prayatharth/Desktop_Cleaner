import os
import shutil

def move_and_arrange(desk_path, inp1, inp2):
    dst_path = os.path.join(desk_path, inp1)
    src_dst = os.chdir(desk_path)
    lst = os.listdir()
    for file in lst:
        if file.endswith(inp2):
            file_path = os.path.join(desk_path, file)
            if not os.path.exists(os.path.join(dst_path, file)):
                print(f"Moving {file} to {dst_path}")
                shutil.move(file_path, dst_path)
            else:
                print(f"File {file} already exists in {dst_path}")


def auto_arrange(desk_path):
    standard_folders = ['Documents', 'Images', 'Videos']
    for folder in standard_folders:
        folder_path = os.path.join(desk_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file in os.listdir(desk_path):
        file_path = os.path.join(desk_path, file)
        if os.path.isfile(file_path):
            category = get_file_category(file)

            if category:
                category_path = os.path.join(desk_path, category)
                count = 1
                new_file_path = os.path.join(category_path, file)

                while os.path.exists(new_file_path):
                    base_name, extension = os.path.splitext(file)
                    new_file_path = os.path.join(category_path, f"{base_name}_{count}{extension}")
                    count += 1

                print(f"Moving {file} to {new_file_path}")
                shutil.move(file_path, new_file_path)

    print('All files were sent to where should be')

def get_file_category(file_name):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
    document_extensions = ['.txt', '.docx', '.pdf', '.xlsx','.ppt','.pptx']

    ext = os.path.splitext(file_name)[1].lower()

    if ext in image_extensions:
        return 'Images'
    elif ext in video_extensions:
        return 'Videos'
    elif ext in document_extensions:
        return 'Documents'
    else:
        pass



while(1):
    choice=int(input('\nHey There ! Welcome to Desktop Cleaner \n\n Choose an option \n 1.Do you wish to Auto clean ? \n 2.Do you want to Custom Clean ? \n'))

    if choice == 1:
        desktop_path = r"C:\Users\praya\Desktop"
        auto_arrange(desktop_path)
        print('Thank You for using It ! ')
        break

    elif choice == 2:
        destination_folder = input('Enter the destination folder: ')
        file_format = input('Enter the file format: ')
        desktop_path = r"C:\Users\praya\Desktop"
        move_and_arrange(desktop_path, destination_folder, file_format)


    else:
        print('Thank You for using It ! ')
        break





