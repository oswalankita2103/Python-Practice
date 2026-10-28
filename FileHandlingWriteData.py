#----------------------WRITE DATA USING FILE HANDLING--------------------------------------

#file = open("C:\\Users\\ANKITA\\Desktop\\PythonProgram\\StudentData.txt","w")
#file.write("name:Ankita oswal\n")
#file.write("marks:90")
#file.close()
#print("Add Data successfully")

#---------------------------READ DATA---------------------------------------------------------

#file = open("C:\\Users\\ANKITA\\Desktop\\PythonProgram\\StudentData.txt","r")
#data = file.read()
#file.close()
#print(data)


#----------------------------APPEND DATA IN FILE----------------------------------------------

#file = open("C:\\Users\\ANKITA\\Desktop\\PythonProgram\\StudentData.txt","a")
#file.write("\nGrade:A")
#file.close()
#print("New data added")

#---------------------------Using with open-----------------------------------------------

#with open("C:\\Users\\ANKITA\\Desktop\\PythonProgram\\StudentData.txt","r") as file:
#    data = file.read()
#   print(data)

#-----------------------COPY DATA----------------------------------------------------------


try:
    with open("C:\\Users\\ANKITA\\Desktop\\PythonProgram\\StudentData.txt") as f2:
        with open("C:\\Users\\ANKITA\\Desktop\\PythonProgram\\Student.txt","w") as f3:
            for i in f2:
                f3.write(i)
except:
    print("file not available")

else:
    f2.close()
    print("file closed")                    
