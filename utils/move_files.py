import os.path
import shutil

""" data 폴더 내 파일 이동 함수, 
    filter_name: 상위 폴더 이름대로 지정 """

def move_file(path_before, path_after, filter_name):
    filelist = os.listdir(path_before)
    for file in filelist:
        # temp_list = file.split("_")
        # from train to test
        # if temp_list[0] == '0':
        #     shutil.move(path_before+file, path_after+"/allfilter/gt/"+file)
        # from test to train
        # shutil.move(path_before+file, path_after+filter_name+"/input/"+file)
        # from test to train gt
        shutil.move(path_before+file, path_after+filter_name+"/gt/"+file)

def in_all_dir(dir_path, target_path):
    dir_list = os.listdir(dir_path)
    for directory in dir_list:
        if directory.split('.')[-1] != 'txt' and directory !='rain' and directory !='allfilter':
            file_path =  os.path.join(dir_path, directory + '/gt/')
            move_file(file_path, target_path, directory)

def main(): 
    dir_path = r"/home/cvmlserver/Seohyeon/TransWeather/data/test/"
    target_path = r"/home/cvmlserver/Seohyeon/TransWeather/data/train/"
    in_all_dir(dir_path, target_path)

if(__name__) == '__main__':
    main()
