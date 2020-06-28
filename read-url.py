from urllib.request import urlopen
ulink=input("hello please enter your link:")
link=str(ulink)
textpage=urlopen(link)
print(str(textpage.read(),'utf-8'))