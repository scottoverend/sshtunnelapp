# need to set up function so the ssh tunnel is running 24/7 on computer. it needs to be quantum proof.
# note. each browser has to be configured
# aim of the project is to set up a permanent quantum safe tunnel that can be set-up remotely via 
# add time limits as well 
# make a little gui interface for the application
# provide a small bit of instructbns

import subprocess
import time

def tunnelFunction():
    print("Creating tunnel.....")
    command = "ssh -D 9000 kali@10.0.2.15"
    subprocess.Popen(command, shell=True)
    print("Tunnel created")

if __name__ == '__main__':

    print("This is an ssh tunnelling programme")
#enter a 1 second delay here


    print("Press '1' to set up tunnelling with the 'Kali' VM")

    n = input()

    if n=="1":
            #try:
                #while True:
        print("initializing the function")
        tunnelFunction()
            #except:
                #print("function called")
               
    else:
        print("closing programme")
       
    

  

