import os.path

file_path = r"/home/cvmlserver/Seohyeon/TransWeather/data/test/input"

files = os.listdir(file_path)

for name in files:
    src = os.path.join(file_path, name)
    new_name =  name.split('_')[0] + '_1977.jpg'
    dst = os.path.join(file_path, new_name)
    print("input/"+ new_name)
    os.rename(src, dst)
