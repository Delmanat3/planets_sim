import sys
import clipboard
import json


# data=clipboard.paste()
# clipboard.copy("cunt")
def saver(filepath,data):
    with open(filepath,"r+")as f:
        righter=json.load(f)
        righter["copper"].append(data)
        f.seek(0)
        json.dump(righter, f, indent = 4)

def loader(filepath):
    with open(filepath,"r"):
        data=json.load(filepath)
        print(data)
        return data

input("press enter to start")

def clippy():
    print("enter p to past c to copy or q to quit")
    while True:
        
  
        op= input()
        if op=="c":
            key=input("enter a key: ")
            data=input("enter a value: ")
            item={key:data}
            saver("clipboard.json",item)
            clipboard.copy(data)
            continue

        elif op=="p":
            # key=input("enter key of data you want: ")
            # v= loader("clipboard.json")
            # print(v)
            vv=clipboard.paste()
            print(vv)
            continue

        elif op=="q":
            print("fucktard")
            break
        else:
            print("enter c to copy p to paste or q to quit")
        

clippy()
