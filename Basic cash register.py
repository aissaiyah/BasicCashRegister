#Empty list to hold items
List = []
"""
#condition for my while loop to end
ringingUp = True
#Float input for item price
calPrice = float(input("How much for your first item or q to quit "))
#Takes input and adds to list
List.append(calPrice)
#while loop to add multiple items
while ringingUp == True:
    #try input take for q and float
    try:
        calPrice = float(input("How much for your next item or q to quit "))
        List.append(calPrice)
        #if enter q stop while loop
        if calPrice == str('q'):
            ringingUp = False
    #if fails stop while loop
    except:
        ringingUp = False
    #add last item to list
    
#Total amount fo the items
Total = 0
#Total is the sum of the list add the items together
Total = sum(List)
#print receipt 
print("Receipt:")
#for each item in list print the $ sign next to the value change to string to print together
for x in List:
    print("$" + str(x))
#print the total with the dollar sign
print("Total: " + "$" + str(Total))"""
