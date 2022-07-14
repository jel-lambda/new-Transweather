import os.path

file_path = r"/home/cvmlserver/Seohyeon/TransWeather/data/train/Amaro/gt"

files = os.listdir(file_path)

for name in files:
    src = os.path.join(file_path, name)
    new_name =  name.split('_')[0] + '_Amaro.jpg'
    dst = os.path.join(file_path, new_name)
    print("Amaro/input/"+ new_name)
    os.rename(src, dst)
