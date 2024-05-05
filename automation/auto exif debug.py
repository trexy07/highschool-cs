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
            print(new_time)
            with open(path, "r+b") as file:
                # get the file
                image=Image(file)
                print(image.datetime_original)
                # set the metadata
                image.datetime_original=f"{new_time[0]}:{new_time[1]}:{new_time[2]} 00:{new_time[3].zfill(2)}:00"
                print(image.datetime_original)
                # write it 
                with open(path, "wb") as file2:
                    file2.write(image.get_file())
        else:
            print(f"file: {path} isn't formated right ")


        


        # file=open(path, "rb")
        # images.append(Image(file))


# check for exif
# for index, image in enumerate(images):
#     if image.has_exif:
#         status = f"contains EXIF (version {image.exif_version}) information."
#     else:
#         status = "does not contain any EXIF information."
#     print(f"Image {index} {status}")



# exif properties
# image_members = []

# for image in images:
#     image_members.append(dir(image))

# for index, image_member_list in enumerate(image_members):
#     # print(f"Image {index} contains {len(image_member_list)} members:")
#     # print(f"{image_member_list}\n")


# add random date and time
# for index,image in enumerate(images):
#     # if index==5:
#         # continue

#     image.datetime_original=f"1963:12:1 00:{str(index).zfill(2)}:00"
#     print(f"""Image {index} @ 
#           {image.get('datetime_original', '')}""")



# write images back
# i=0
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         path=os.path.join(subdir, file)
#         print(path)

#         with open(path, "wb") as file:
#             file.write(images[i].get_file())
#         i+=1
#         # images.append(Image(file))





