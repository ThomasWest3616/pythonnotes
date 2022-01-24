from datetime import datetime

datetime_str = '8 Mar 85'

def myFunction(): 
    datetime_object = datetime.strptime(datetime_str, '%d %b %y')
    newly_formatted_string = datetime_object.strftime("%d/%m/%Y")
    tuple2 = (newly_formatted_string.replace("/", "-"))
    print(tuple2)

myFunction()