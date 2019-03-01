
from tkinter import *
import urllib.request, json
import webbrowser





def main():
    root = Tk()
    root.title('گنجور')

    first = StringVar()
    second = StringVar()
    poetName = StringVar()
    websiteAdd = StringVar()

    def callback(event):
        webbrowser.open_new((data['url']))

    def btncallback():
        try:
            with urllib.request.urlopen("http://c.ganjoor.net/beyt-json.php") as url:
                data = json.loads(url.read().decode())
                first.set(data['m1'])
                second.set(data['m2'])
                websiteAdd.set(data['url'])
                poetName.set(data['poet'])
                print(data)
        except:
            websiteAdd.set("اینترنت وصل نیست")

    #Label(root, text="Hello, world!").pack()

    Label(root, textvariable=first, anchor=CENTER, width=40, font=("B Nazanin", 16)).grid(column=1, row=0)
    Label(root, textvariable=second, anchor=CENTER, width=40, font=("B Nazanin", 16)).grid(column=0, row=0)
    b = Button(root, text="Next!", command=btncallback)
    b.grid(column=2, row=0)
    label3 = Label(root, textvariable=websiteAdd, anchor=CENTER, font=("Arial", 16),fg="blue", cursor="hand2")
    label3.grid(column=0, row=1)
    label3.bind("<Button-1>", callback)
    Label(root, textvariable=poetName, anchor=CENTER, font=("B Nazanin", 16)).grid(column=1, row=1)
    Label(root, text='شاعر:', anchor=CENTER, font=("B Nazanin", 16)).grid(column=2, row=1)


    try:
        with urllib.request.urlopen("http://c.ganjoor.net/beyt-json.php") as url:
            data = json.loads(url.read().decode())
            first.set(data['m1'])
            second.set(data['m2'])
            websiteAdd.set(data['url'])
            poetName.set(data['poet'])
            print(data)
    except:
        websiteAdd.set("اینترنت وصل نیست")



    root.mainloop()




if __name__ == "__main__": main()


