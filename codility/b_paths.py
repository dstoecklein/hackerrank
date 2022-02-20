import os

def pathify(foo, bar):
    print(os.path.join(foo, bar))

if __name__=="__main__":
    pathify("/home/user/", ".bashrc")