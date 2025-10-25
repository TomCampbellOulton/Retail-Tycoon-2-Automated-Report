
# You need to create an email account on outlook for
# the program to utilize
sender = "SendersEmail@outlook.com"
# Senders email is required to allow your computer to
# sign in and send the email
sender_password = "SendersPassword"
# Your email here, password is NOT needed
recipient = "YourEmail@gmail.com"














#   Import Packages

# Provides break in between instructions to allow
# appropriate execution
import time

# Image Reading
# Screenshots screen
import pyscreenshot as ImageGrab
# Reads text from screenshot
import pytesseract
# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\your_username_here\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# Scrolling
# Import mouse controller for scrolling
from pynput.mouse import Controller
# Set up mouse
mouse = Controller()



# Set Global Variables
product = []
numberOfSales = []
salesOfProducts = {}
newProdcutRequest = []
validatedProducts = []






# Find validated Products
file = open("validatedProducts.txt", "r")
#                                               Removes any empty string
validatedProducts = file.read().replace(",","").replace("\n\n","\n").split("\n")
file.close()


# Variables for extra stats
timePlayed,cashEarned,cashSpent = str(),str(),str()
cashStolen,itemsStolen,customersServed = str(),int(),str()
robbersArrested,distanceDriven, totalItemsSold = str(),str(),int()


def data_validation(data):
    try:
        serperatedValues = data.split(': ')
        product = serperatedValues[0]
        numberOfSales =  int(str(serperatedValues[1]).replace(',', ''))
        dataValidated = True
    except:
        dataValidated = False

    if dataValidated:
        if product in validatedProducts:
            dataValidated = True
        # If the product is not recognised
        # a message is sent to user asking if
        # this is a new product
        else:
            dataValidated = False
            if product not in newProdcutRequest:
                newProdcutRequest.append(product)

        
    return dataValidated

def screenGrabNRead(x1,y1,x2,y2):
    # Screenshot Part Of Screen
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # Read Text from Image
    text = pytesseract.image_to_string(img)
    return text


def mainProgram(numberOfScrolls):
    # Scroll Down numberOfScrolls then Back Up
    sleepTime = 0
    direction = 'up'
    for j in range(1):
        if direction == 'up':


            # Screen Grab Extra DATA

            extraStats = screenGrabNRead(661, 346, 1120, 629)
            stats = extraStats.split('\n')
            for stat in stats:
                # Checks if a vowel is in stat or its removed
                
                if "o" in stat or "e" in stat or "i" in stat or "u" in stat:
                    print(stat)
                else:
                    stats.remove(stat)

            # Setting variables for statistics 
            timePlayed = stats[0]
            cashEarned = stats[1]
            cashSpent = stats[2]
            cashStolen = stats[3]
            itemsStolen = stats[4]
            customersServed = stats[5]
            robbersArrested = stats[6]
            distanceDriven = stats[7]
            direction = 'down'
            time.sleep(sleepTime)
        else:
            direction = 'up'

        # Range is the number of scrolls required to reach top
        # or bottom of list
        for i in range(numberOfScrolls):

            text = screenGrabNRead(690, 630, 1030, 824)
            print(text)
            
            # Seperate Values from Text
            seperatedLines = text.split('\n')



            for line in seperatedLines:
                if line == "":
                    pass
                else:
                    # Simple data validation
                    dataValidated = data_validation(line)
                    if dataValidated:
                        print("Seperated Line = %s"%(line))
                        # Splitting values at : to seperate name
                        # from the number of item sales
                        serperatedValues = line.split(': ')
                        
                        product = serperatedValues[0]
                        numberOfSales =  int(str(serperatedValues[1]).replace(',', ''))





                        # Save Values
                                             
                        salesOfProducts[product] = numberOfSales
                    else:
                        print("Invalid data provided :(")


            # Scroll down two steps
            if direction == 'up':
                mouse.scroll(0, 2)
            else:
                mouse.scroll(0, -2)

            time.sleep(sleepTime)
    return salesOfProducts,timePlayed,cashEarned,cashSpent,cashStolen,itemsStolen,customersServed,robbersArrested,distanceDriven

def writeFile(salesOfProducts):
    # Write to a CSV file
    file = open("RetailTycoon2Data.csv", "w")
    for item in salesOfProducts:
        product = item
        numOfSales = salesOfProducts[product]
        # Desired format = prodcut,numberOfSales
        desiredFormat = "%s,%s\n"%(product, str(numOfSales))
        # Writing the data to the csv
        file.write(desiredFormat)

    file.close()




def calculateTotalItemsSold(salesOfProducts):
    # Total Items Sold
    totalItemsSold = 0
    for item in salesOfProducts:
        totalItemsSold += int(salesOfProducts[item])
    print(salesOfProducts)
    print(totalItemsSold)
    return totalItemsSold


def sendMessageToUser(timePlayed,cashEarned,cashSpent,cashStolen,itemsStolen,customersServed,robbersArrested,distanceDriven,salesOfProducts, totalItemsSold):
    # Formatting 'salesOfProducts' to readable form
    messageDraft = "%s \n%s \n%s \n%s \n%s \n%s \n%s \n%s \nTotal Units Sold: %s \n\n\n"%(str(timePlayed),str(cashEarned),str(cashSpent),str(cashStolen),str(itemsStolen),str(customersServed),str(robbersArrested),str(distanceDriven), str(totalItemsSold))+ str(salesOfProducts).replace(",","\n").replace("{","").replace("}","").replace("'","")

    print("\n\n\n\n",messageDraft,"\n\n\n")

    return messageDraft


def sendEmail(sender,sender_password,recipient, messageDraft):

    print("About To send Email")

    # Send Email
    import smtplib
    import ssl
    port = 587  

    smtp_server = "smtp-mail.outlook.com"

    # Required format for sending email
    message = """
    %s
    """%(str(messageDraft))

    SSL_context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:

        server.starttls(context=SSL_context)

        server.login(sender, sender_password)

        server.sendmail(sender, recipient, message)

    print("Sent Email")

def validateNewProduct(item):
    # If the product is valid it will be added
    # to the list of valid products
    print( ("%s was added as a valid item.")%(item) )
    # and saved as valid
    file = open("validatedProducts.txt", "a")
    file.write("\n"+str(item))
    file.close()


def executeProgram():
    print("Executing...")
    salesOfProducts,timePlayed,cashEarned,cashSpent,cashStolen,itemsStolen,customersServed,robbersArrested,distanceDriven = mainProgram(numberOfScrolls=50)
    writeFile(salesOfProducts)
    totalItemsSold = calculateTotalItemsSold(salesOfProducts)
    messageDraft = sendMessageToUser(timePlayed,cashEarned,cashSpent,cashStolen,itemsStolen,customersServed,robbersArrested,distanceDriven,salesOfProducts,totalItemsSold)
    sendEmail(sender,sender_password,recipient, messageDraft)
    print("Complete :)")


executeProgram()

