from ssl import _PasswordType
from cryptography.fernet import Fernet 

def write_key () :
    key = Fernet.generate_key ()
    with open ('key.key', "rb")
    key = file.read ()
    file.close ()
    return key

key = load_key ()
fer  = Fernet (key)

def view () :
    with open ('passwords.txt', 'r') as f :
        for line in f.readlines () :
            data = line.rstrip ()
            user, pass = data.split (" | ")
            print ("User:", user, " | Password: ", fer.decrypt (pass.encode () ).decode () )
            
            
def add () :
    name = input ('Account Name:  ')
    pwd = input ("Password:  ")
    
    with open ('passwords.txt',  'a')  as f :
        f.write (name + "|" + fer.encrypt (pwd.encode () ).decode () + "\n")
        
while True :
    mode = input ("would you like to add a new password or view existing ones (view, add), press q to quit:  ")
    if mode == "q" :
        break
    
    if mode == "view" :
        view ()
    
    elif mode == "add" :
        add ()
        
    else :
        print ("Error!!")
        continue    
                            