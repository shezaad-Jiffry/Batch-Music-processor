
import os, csv
from mutagen.mp3 import MP3
f = open("C:/Users/sheza/Desktop/script/output.csv",'w',newline="")#csv save location
w=csv.writer(f)
i =  206
dupe = False
directory = 'C:/Users/sheza/Desktop/python script trst'#files to be renamed
os.chdir(directory)
for path, dirs, files in os.walk(directory):#files to be renamed
  files.sort()
 
  for filename in files:
        dupe = False
        print(filename)
        audio = MP3(path + "/" + filename)
        original = filename
        f_title, f_ext = os.path.splitext(filename)
        new_name = '{}{}'.format(str(i), f_ext)

        if filename.count("-") >= 2 or filename.count("#")  >= 2:
          dupe = True

        if "-" in f_title and dupe == False:
          f_artist,f_extra = f_title.split('-')
          f_extra = f_extra.strip()
          f_artist = f_artist.strip()
          
         

          try:
            f_extra2,f_genre = f_extra.split('#')
            w.writerow([f_extra2,'t',int(audio.info.length*1000),84,84,f_artist,f_genre])
            os.rename(original, new_name)
            i = i + 1
          except Exception:
            pass
        
          
          
          

        elif dupe == False:
          
    

          try:
            f_extra2,f_genre = f_extra.split('#')
            w.writerow([f_extra2,'t',int(audio.info.length*1000),84,84,f_artist,f_genre])
            os.rename(original, new_name)
            i = i + 1
          except Exception:
            pass
          
          
          



