import os

dupe = False
genres = ["Alt Rock", "Ambient", "Classical", "Country", "DeepHouse", "Drum and Bass", "EDM", "Hip Hop", "Indie", "Jazz", "Latin", "Piano", "Pop", "Reggae", "Soul", "Soundtrack", "Trance", "Trap", "World", "Worship"]
for i in genres:
    print(i)
    directory = 'C:/Users/sheza/Music/' + i #change this to rename in a certain directory

    genre = '#' + i
    doubleDash = False
    leaveAlone = False
    otherDash = False
    missing = False
    freestocktag = False
    os.chdir(directory)
    for f in os.listdir(directory):
        
    #reset dupe and double dash so it loops properly
        dupe = False

        doubleDash = False

        leaveAlone = False

        otherDash = False

        missing = False
        
        freestocktag = False
    #split the text on the extension
        file_name, file_ext = os.path.splitext(f)
        if file_name.count("free-stock") == 1:
            f_artist,f_extra = file_name.split('by')
            f_artist = f_artist.strip()
            f_extra = f_extra.strip()
            freestocktag = True
        print(file_name.count("-") == 3)
        if file_name.count("-") == 0:
       
            if file_name.count("Alternative_Punk Music [No Copyright _ Royalty Free]"):
                f_artist,f_extra = file_name.split('[No Copyright _ Royalty Free]')
                f_artist = f_artist.strip()
                f_extra = f_extra.strip()
                missing = True
            if file_name.count('by') == 1:
                
                f_artist,f_extra = file_name.split('by')
                f_artist = f_artist.strip()
                f_extra = f_extra.strip()
                
                missing = True
            if file_name.count( "by" ) >= 2:
                leaveAlone = True
                os.remove(f)
            else:
                
                os.remove(f)
                leaveAlone = True

        if file_name.count("-") == 2:
            f_artist,f_extra,f_lol = file_name.split('-')
            f_artist = f_artist.strip()
            f_extra = f_extra.strip()
            print(f_artist)
            print(f_extra)
            print(f_lol)
            if( f_artist == f_extra):
                doubleDash = True
            else:
                otherDash = True

        if file_name.count("#") == 2:
            f_genre,f_extra2,f_extra3 = file_name.split("#")
            f_genre = f_genre.strip()
            f_extra2 = f_extra2.strip()
            f_extra3 = f_extra3.strip()

            if(f_extra2 == f_extra3):
                leaveAlone = True
                f_genre = f_genre.rstrip("-")
                new_name = '{0}#{1}{2}'.format(f_genre,f_extra2, file_ext)
                new_name = new_name.rstrip("-")
                os.rename(f, new_name)

    #check if UTF viable



    #check if genre is already tagged, dont double tag
        if genre in file_name:

            dupe = True

        if missing == True:
            new_name = '{0}-{1}{2}'.format(f_artist,f_extra, file_ext)
            new_name = new_name.rstrip("-")
            print(f + "f")
            os.rename(f, new_name)
        if freestocktag == True:
            
            new_name = '{0}-{1}{2}'.format(f_artist,f_extra, file_ext)
            new_name = new_name.replace("_free-stock", "")
            new_name = new_name.rstrip("-")
            new_name = new_name.rstrip("_")
            os.rename(f, new_name)

        if dupe == False and doubleDash == False and leaveAlone == False and missing == False:


            new_name = '{0}{1}{2}'.format(file_name,genre, file_ext)
            new_name = new_name.rstrip("-")
            os.rename(f, new_name)
        
        if doubleDash ==True and leaveAlone == False:
            
            new_name = '{0}-{1}{2}{3}'.format(f_artist,f_lol,genre, file_ext)
            new_name = new_name.rstrip("-")

            os.rename(f, new_name)

        if otherDash ==True and leaveAlone == False:
            print( "artist shit " + f_artist)
            new_name = '{0}-{1}{2}{3}'.format(f_artist,f_extra,genre, file_ext)
            new_name = new_name.rstrip("-")
            print("artist shit 2" +f)
            try:
                os.rename(f, new_name)
            except Exception:
                pass


