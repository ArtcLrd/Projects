import working

msg = "NULL"

class Main:
    def __init__(self,url):
        x = url
        self.run_pred(x)
    def run_pred(self,x):
        global msg
        #x = "http://192.168.29.47/cam-hi.jpg"
        while(True):
            d = working.DETECT_WINDOW(x)
            #print(d.str_ret())
            msg = d
            if d == "Successfull":
                break
            else:
                continue
   