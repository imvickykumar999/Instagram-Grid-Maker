import os, image_slicer, getpass
from PIL import Image
from instabot import Bot

path1 = r"C:\Users\Vicky Kumar\Pictures\instagrid\photo\vicky.png"
path2 = r"C:\Users\Vicky Kumar\Pictures\instagrid\photo\cropped.png"
loc = r"C:\Users\Vicky Kumar\Pictures\instagrid\photo"
im = Image.open(path1)

if im.size[0] > im.size[1]:
    side = im.size[1]
else:
    side = im.size[0]

a = im.crop((im.size[0]/2-side/2, im.size[1]/2-side/2,
             im.size[0]/2+side/2, im.size[1]/2+side/2))
a.save(path2)

n = int(input('\nEnter n in (N x N) GRID : '))
grid = image_slicer.slice(path2, n*n)

bot = Bot()
passwd = getpass.getpass(prompt = 'Enter Your Password : ')
bot.login(username = "imvickykumar999", 
          password = passwd) 

cap = ['This grid image is uploaded using instabot library.',
      'I have tried to code a Insta Grid Maker software.',
      'Caption are appended in List.',
      'Hope you Liked Insta Grid Maker Software Idea.',
      'There is an .exe file of this Software, you should too run on your PC.',
      'Just enter userid and password and select Photo.',
      'It will automatically convert image into Central Crop Square.',
      'Split into (N*N) seperate image and Upload on insta as Grid.',
      '#insta_grid #python #automation']

for i in range(len(grid)):
    newpath = os.path.join(loc, str(grid[len(grid)-i-1]).split('- ')[1])[:-1]
    print(newpath)
    bot.upload_photo(newpath, caption = cap[i]) 