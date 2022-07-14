import os.path

""" data 폴더 내 파일 이름을 바꿔주는 함수, 
    filter_name: 상위 폴더 이름대로 지정 """
def rename_files(file_path, filter_name):
    files = os.listdir(file_path)
    for name in files:
        src = os.path.join(file_path, name)
        new_name =  name.split('_')[0] + '_' + filter_name +'.jpg'
        dst = os.path.join(file_path, new_name)
        os.rename(src, dst)

def make_textfile(file_path, filter_name):
    f = open("/home/cvmlserver/Seohyeon/TransWeather/data/train/allfilter.txt", 'a')
    files = os.listdir(file_path)
    for name in files:
        f.write(filter_name + "/input/"+ name + '\n')
    f.close

def rename_and_textfile(file_path, filter_name):
    f = open("/home/cvmlserver/Seohyeon/TransWeather/data/train/allfilter.txt", 'a')
    files = os.listdir(file_path)
    for name in files:
        src = os.path.join(file_path, name)
        new_name =  name.split('_')[0] + '_' + filter_name +'.jpg'
        dst = os.path.join(file_path, new_name)
        f.write(filter_name + "/input/"+ new_name + '\n')
        os.rename(src, dst)
    f.close

def in_all_dir(dir_path,func):
    dir_list = os.listdir(dir_path)
    if func == 'rename_files':
        for directory in dir_list:
            if directory.split('.')[-1] != 'txt':
                file_path =  os.path.join(dir_path, directory + '/gt/')
                rename_files(file_path, directory)
    else:
        f = open("/home/cvmlserver/Seohyeon/TransWeather/data/train/allfilter.txt", 'w')
        f.close
        for directory in dir_list:
            if directory.split('.')[-1] != 'txt':
                file_path =  os.path.join(dir_path, directory + '/gt/')
                if func == "make_textfile":
                    make_textfile(file_path,directory)
                else:
                    rename_and_textfile(file_path, directory)

def main(): 
    dir_path = r"/home/cvmlserver/Seohyeon/TransWeather/data/train/"
    in_all_dir(dir_path, 'make_textfile')

if(__name__) == '__main__':
    main()
