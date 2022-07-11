import os.path

targerdir = r"/home/cvmlserver/Seohyeon/TransWeather/data/train/input"

files = os.listdir(targerdir)

for i in files:

    # if os.path.isdir(targerdir + r"\\" + i):
    #     print("folder : " +i)

    # else :
        print("input/" + i)
