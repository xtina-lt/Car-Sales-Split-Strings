#######################################################
#                    DATA                             #
#######################################################
daily_sales = \
    """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""


#######################################################
#                 LETS GET CODING                     #
#######################################################
# 1) EVALUATE
# transactions stored? ","
# data w/i transaction stored? ";,;"

# 2) SPLIT
# List: replace; Strings: split, strip
replaced_string = daily_sales.replace(";,;", "*")
# so it doesn't get split
list = replaced_string.split(",")  # remove ,
new_list = []
for i in list:
    new_list.append(i.split("*"))  # remove *
clean_list = []
for i in new_list:  # outer list
    for j in i:  # each transaction
        clean_list.append(j.strip())  # remove whitespace
# print(clean_list)

# 3) SEPERATE CUSTOMER DATA
# loop through clean list range
# append into specified list
customers = []
sales = []
thread_sold = []
for i in range(0, len(clean_list), 4):
    customers.append(clean_list[i])
for i in range(1, len(clean_list), 4):
    sales.append(clean_list[i])
for i in range(2, len(clean_list), 4):
    thread_sold.append(clean_list[i])

# 4) CALCULATE TOTAL IN SALES
t = 0
for i in sales:
    t += float(i.strip("$"))
total_sales = round(t, 2)

# 5) TOTAL OF EACH THREAD
# Split threads to count each withought the &
threads_split = []
for i in threads_split:
    if "&" in i:
        threads_split.append(i.split("&"))
    else:
        threads_split.append(i)

# initiate total
red = 0
yellow = 0
green = 0
white = 0
black = 0
blue = 0
purple = 0

# iterate through thread
for i in thread_sold:
    if "red" in i:
        red += 1
    if "yellow" in i:
        yellow += 1
    if "green" in i:
        green += 1
    if "white" in i:
        white += 1
    if "black" in i:
        black += 1
    if "blue" in i:
        blue += 1
    if "purple" in i:
        purple += 1

# Total threads
total_threads = red + yellow + green + white + black + blue + purple


# 6) PRINT IT OUT
# Total Sales
print(f"The total of sales today was: {total_sales}")

# Message
if total_sales > 1200:
    print("Good Job! \nKeep it up SHARK!")
else:
    print("There's always tomarrow")

# Greeting
print(f'''
{total_threads} threads were sold:
Red: {red}
Yellow: {yellow}
Green: {green}
White: {white}
Black: {black}
Blue: {blue}
Purple: {purple}''')
print("\nThank you:")
for i in customers:
    print(i)



#######################################################
#               LETS SEE THE OUTPUT                   #
#######################################################
# The total of sales today was: 1498.74
# Good Job!
# Keep it up SHARK!

# 181 threads were sold:
# Red: 24
# Yellow: 34
# Green: 30
# White: 28
# Black: 26
# Blue: 22
# Purple: 17

# Thank you:
# Edith Mcbride
# Herbert Tran
# Paul Clarke
# Lucille Caldwell
# Eduardo George
# Danny Mclaughlin
# Stacy Vargas
# Shaun Brock
# Erick Harper
# Michelle Howell
# Carroll Boyd
# Teresa Carter
# Jacob Kennedy
# Craig Chambers
# Peggy Bell
# Kenneth Cunningham
# Marvin Morgan
# Marjorie Russell
# Israel Cummings
# June Doyle
# Jaime Buchanan
# Rhonda Farmer
# Darren Mckenzie
# Rufus Malone
# Hubert Miles
# Joseph Bridges
# Sergio Murphy
# Audrey Ferguson
# Edna Williams
# Randy Fleming
# Elisa Hart
# Ernesto Hunt
# Shannon Chavez
# Sammy Cain
# Steven Reeves
# Ruben Jones
# Essie Hansen
# Rene Hardy
# Lucy Snyder
# Dallas Obrien
# Stacey Payne
# Tanya Cox
# Melody Moran
# Louise Becker
# Ryan Webster
# Justin Blake
# Beverly Baldwin
# Dale Brady
# Guadalupe Potter
# Desiree Butler
# Sonja Barnett
# Angelica Garza
# Jamie Welch
# Rex Hudson
# Nadine Gibbs
# Hannah Pratt
# Gayle Richards
# Stanley Holland
# Anna Dean
# Terrance Saunders
# Brandi Zimmerman
# Guadalupe Freeman
# Irving Patterson
# Karl Ross
# Brandy Cortez
# Mamie Riley
# Mike Thornton
# Jamie Vaughn
# Noah Day
# Josephine Keller
# Tracey Wolfe
# Ignacio Parks
# Beatrice Newman
# Andre Norris
# Albert Lewis
# Javier Bailey
# Everett Lyons
# Abraham Maxwell
# Traci Craig
# Jeffrey Jenkins
# Merle Wilson
# Janis Franklin
# Leonard Guerrero
# Lana Sanchez
# Donna Ball
# Terrell Barber
# Jody Flores
# Daryl Herrera
# Miguel Mcguire
# Rogelio Gonzalez
# Lora Hammond
# Owen Ward
# Malcolm Morales
# Eric Mcdaniel
# Madeline Estrada
# Leticia Manning
# Mario Wallace
# Lewis Glover
# Gail Phelps
# Myrtle Morris