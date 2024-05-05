from exif import Image
import os


rootdir = r'automation\images'



# find files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path=os.path.join(subdir, file)
        print(path)

        # new time 
        new_time=file[:-4].split("-")
        
        # if the photo has a corect new time:
        if len(new_time)==4:

            with open(path, "r+b") as file:
                # get the file
                image=Image(file)

                # set the metadata
                image.datetime_original=f"{new_time[0]}:{new_time[1]}:{new_time[2]} 00:{new_time[3].zfill(2)}:00"

                # write it 
                with open(path, "wb") as file2:
                    file2.write(image.get_file())
        else:
            print(f"file: {path} isn't formated right ")

        

