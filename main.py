import matplotlib.pyplot as plt
import numpy as np

#Read From File Function, each file will contain data of excl that data; eg screen data will contain only data abt screen resoltions
#for this reasson im setting it up as a def to be re-used

#Going to save the read contents into a global array to be manipulated into useful information
def read_file(file_name,dir):
    global data_ #global so it can be accessed after function is ran
    data_=[]
    try:
        with open(file_name) as f:#opens the file
                for line in f:
                    #print(line)
                    #line= line.strip("\n")#strips as next line is detected when retriving
                    data_.append(line)
    except:#error code
        print("There was an error with opening the file(Directory  or filename #defualt ver)")# added ver so its easier to debug

#-----------------------------Main-----------------------------------------------------------

#-----------------------------Main-----------------------------------------------------------


#---------------------------------------------Time spent(avg,largest and smallest)
read_file("time_data.txt",1)
#Sorts the list from smallest to largest
#data_=[1,5,8,4,6]#testing purposes
data_.sort()
#retrives the largest& by seeing what the len is( as the largest will be last position and smallest will be 0)
#print(data_)#testing purposes
length=len(data_)
length=length-1
leng=int(length)
#print(length)#testing purposes
largest=data_[length]
smallest=data_[0]

#avrage
total=0
for num in data_:
    total=total+int(num)
avg=total/int(length)
#print(total)#testing purposes
#print(avg)#testing purposes
#outputs the results
print(f"The highest time a user has spent is:{largest}seconds\n")
print(f"The quickest time a user has spent is:{smallest}seconds\n")
print(f"The Avrage time a user has spent is:{avg} seconds")


#----------------------------------Histogram(screen res)---------------------------
read_file("screen_data.txt",1)

plt.hist(data_)#plots the graph
plt.show()

#Pie Chart(browser used)

""" 
Solution:with it being in an array i could filter through the list making a counter for each COMMON browser agent       
"""
#counters for each browser agent

#with browsers having a naming standards like Chrome 93, safari 14, edge 44 etc im going to apply the .strip to within the retrive data so its
# more effective and easier to work with the data without affecting  the functionality of the other 2 sections ( time and histograph)

def read_file_brow_ver(file_name,dir):
    global data_ #global so it can be accessed after function is ran
    data_=[]
    try:
        with open(file_name) as f:#opens the file
                for line in f:
                    #print(line)
                    line=line.strip("\n")#without it doesnt work (most likely due to google\n == google)
                    line= line.replace(" ","")#strips spaces so its just "chrome80, edge44 , safari14 etc
                    line=line.replace("1","")
                    line=line.replace("2","")
                    line=line.replace("3","")
                    line=line.replace("4","")
                    line=line.replace("5","")#Was unsure how to store mutiple flters inside of one comand so ultiple wil have to do
                    line=line.replace("6","")#ethier way it works
                    line=line.replace("7","")
                    line=line.replace("8","")
                    line=line.replace("9","")
                    line=line.replace("0","")
                    line=str(line)
                    #print(line)
                    data_.append(line)
    except:#error code
        print("There was an error with opening the file(Directory  or filename #browser ver)")#added ver so its easier to debug



#counters for each browser agent
read_file_brow_ver("browser_data.txt",1)# replaces current data_ array with
google_c=0
firefox_c=0
m_edge_c=0
safari_c=0
explorer_c=0
other=0
data_percentages = []#percenages
google_p=0
firefox_p=0
m_edge_p=0
safari_p=0
explorer_p=0
other_p=0
#cycles through the data within the list "data_" and sees if its google, if it is adds one to counter , if its edge it will add to tht counter and so on
for data in data_:
    print(data)
    if data == "Chrome":
        google_c=google_c+1
    if data =="Safari":
        safari_c=safari_c+1
    if data =="Firefox":
        firefox_c=firefox_c+1
    if data=="Edge":
        m_edge_c=m_edge_c+1
    if data=="Internet Explorer":
        explorer_c=explorer_c+1
    else:
        other=other=1
print(f"the count of google is: {google_c}")


#Now we have the ammount of each one in simple numbers we turn it into a % to be worked with by piechart
total=google_c+firefox_c+m_edge_c+other+safari_c+explorer_c
try:
    google_p=total/google_c
except:
    pass
finally:
    google_p=google_p*10
    data_percentages.append(google_p)

try:
    safari_p=total/safari_c
except:
    pass
finally:
    safari_p=safari_p*10
    data_percentages.append(safari_p)

try:
    firefox_p=total/firefox_c
except:
    pass
finally:
    firefox_p=firefox_p*10
    data_percentages.append(firefox_p)

try:
    m_edge_p=total/m_edge_c
except:
    pass
finally:
    m_edge_p=m_edge_c*10
    data_percentages.append(m_edge_p)

try:
    other_p=total/other
except:
    pass
finally:
    other_p=other_p*10
    data_percentages.append(other_p)

try:
    explorer_p=total/explorer_c
except:
    pass
finally:
    #explorer_p=explorer_p*10
    data_percentages.append(explorer_p)

print(data_percentages)


"""
#it starts on the east side and works clockwise
mylabels = ["Google", "Safari", "Firefox", "Edge","Other","Internet Exp"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["Blue", "Red", "#FF00FF", "#4CAF50"]
plt.pie(data_percentages, labels = mylabels, explode = myexplode,colors=mycolors)
plt.show()
"""


