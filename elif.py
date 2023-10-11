ram = int(input("Enter age of RAM : "))
shyam = int(input("Enter age of SHYAM : "))
jack = int(input("Enter age of JACK : "))

#if(ram > shyam and ram > jack):
#    print("RAM is eldest...")
#elif(shyam > ram and shyam > jack):
#    print("SHYAM is eldest...")
#else:
#    print("JACK is eldest...")

if(ram > shyam):
    if(ram > jack):
        print("RAM is eldest...")
    else:
        print("JACK is eldest...")
elif(shyam > jack):
    print("SHYAM is eldest")
else:
    print("JACK is eldest...")

    
 
