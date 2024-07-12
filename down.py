import requests
import text_extraction

class download_image:
    def __init__(self,x,p):
        url = x
        path = p
        download_image.dim(self,url,path)
    def dim(self,url,path):
        var=requests.get(url)
        #print(var.content)
        with open(path,'wb') as f:
            f.write(var.content)
        ret=text_extraction.image_mod(path)
        print(ret)