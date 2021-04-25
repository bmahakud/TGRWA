import random
import datetime
import qrcode
import qrcode as QR


from PIL import Image, ImageDraw, ImageFont
import os









image = Image.new('RGB', (1800, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28,  encoding="unic")





d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y\t ID CARD Generator\t  %I:%M:%S %p")
print (reg_format_date)



(x, y) = (50, 50)
company = "Trident Galaxy, Bhubaneswar"
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf", 80,  encoding="unic")
draw.text((x, y), company, fill=color, font=font)






(x, y) = (50, 600)
name = input('Enter Your Full Name: ')

color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 45,  encoding="unic")
draw.text((x, y), name, fill=color, font=font)






(x, y) = (500, 300)
gender = input('Enter Your Gender: ')

color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), 'Gender: '+gender, fill=color, font=font)





(x, y) = (500, 350)
dateofbirth = input('Enter Your Date Of Birth: ')

color = 'rgb(0, 0, 0)' # black color 


draw.text((x, y), 'DOB: '+dateofbirth, fill=color, font=font)

(x, y) = (500, 400)
mobileno = input('Enter Your Mobile Number: ')


color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), 'Mob No: '+mobileno, fill=color, font=font)

(x, y) = (500, 450)
flatnumber = input('Enter Your Flat No.: ')

color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), 'Flat No: '+flatnumber, fill=color, font=font)



(x, y) = (500, 500)
ExpiryDate = input('Enter Expiry date: ')
color = 'rgb(0, 0, 0)'
draw.text((x, y), 'Expiry: '+ ExpiryDate, fill=color, font=font)




block = input('Enter you block in Capitals: ')




(x, y) = (1400, 600)

id_no = input('Enter a new  ID No.: ')

idno = str('TG '+str(id_no))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 60,  encoding="unic")

draw.text((x, y), idno, fill=color, font=font)

image.save(name+'.png')

###########################################################
# CREATE WEB PAGE URL


PhotoName = input('Provide name of the photograph with extension')


img = Image.open(PhotoName)
img = img.resize((377, 377), Image.ANTIALIAS)

outputstoragepath = block+"/"+PhotoName

img.save(outputstoragepath)
img.save(PhotoName)






filename = idno.replace(" ","")+".html"




f = open(filename, "w")
f.write('<!DOCTYPE html>\n')
f.write('<html lang="en" dir="ltr">\n')
f.write('<head>')
f.write('<meta charset="utf-8">\n')
f.write('<title>Trident Galaxy ,Bhubaneswar </title>\n')
f.write('<h1>Resident Information, Trident Galaxy Bhubaneswar</h1>\n')

imagepathforhtml= '<img src="%s" alt="Avatar" width="200" height="250">\n'%(PhotoName)

f.write(imagepathforhtml)


residentName = "<h2> %s</h2>\n"%(name)

f.write(residentName)
f.write('<hr>\n')
f.write('   <ul>\n')


genderhtml = "<li>Gender: %s</li>\n"%(gender)

f.write(genderhtml)
dateofbirthhtml = "       <li>DOB: %s  </li>\n"%(dateofbirth)

f.write(dateofbirthhtml)

flatnumberhtml = "<li>Flat No: %s </li>\n"%(flatnumber)

f.write(flatnumberhtml)

f.write('       <li>Resident Type:   Owner</li>\n')


expiryhtml = "       <li>Card Expiry:  %s </li>\n"%(ExpiryDate)

f.write(expiryhtml)



f.write('   </ul>\n')
f.write('<hr>\n')
f.write('</head>\n')
f.write('</html>\n')

copy ="mv %s %s"%(filename, block)

os.system(copy)


copypic = "cp %s %s"%(PhotoName, block)
os.system(copypic)


gitadd ="git add %s/%s"%(block,filename)

print ("gitadd command: ",gitadd)
os.system(gitadd)




gitaddpic = "git add %s/%s"%(block,PhotoName)

os.system(gitaddpic)

gitcommit = "git commit -m '%s'"%(name)


print ("committing command : ", gitcommit)

os.system(gitcommit)

gitpush = "git push origin main"

os.system(gitpush)


URL = 'https://tgrwabbsr.github.io/Residents/%s/%s'%(block,filename)

img = qrcode.make(URL)   # this info. is added in QR code, also add other things

img.save("qrcode.png")





ID = Image.open(name+'.png')


tglogo = Image.open('TGLogo.png')







PPPhoto = Image.open(outputstoragepath)


QRCode = Image.open('qrcode.png')


green =Image.open('green.png')

#im = Image.open(str(idno)+'.bmp') #25x25


ID.paste(tglogo,(1500,0))

ID.paste(PPPhoto,(50,200))

ID.paste(QRCode,(1400,200))

ID.paste(green,(660,660))

#ID.save(name+'.png')

Padded_image = Image.new('RGB', (2300, 1400), (0, 0, 0))
padd_draw = ImageDraw.Draw(Padded_image)

outputIDpath = block+"/"+"IDcard_"+PhotoName

Padded_image.save(outputIDpath)





IDcard = Image.open(outputIDpath)
IDcard.paste(ID,(250,250))

IDcard.save(outputIDpath)

















