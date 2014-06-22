from fabric.api import local

#prepare for deployment

def test():
    local("python test_tasks.py -v && python test_users.py -v")
    
def commit():
    message = raw_input("Enter a git command message:  ")
    local("git add . && git commit -am '{}'".format(message))
    
def push():
    local("git push origin master")
    
def prepare():
    test()
    commit()
    push()


    
