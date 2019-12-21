from requests import get
import json
import sys

tmptype = ""
ecotype = ""
endarg = -1

def main(*arg):
    global endarg

    if sys.argv[-1] == "-f":
        tmptype = "f"
        ecotype = "fahrenheit"
    elif sys.argv[-1] == "-c":
        tmptype = "m"
        ecotype = "celcius"
    elif len(sys.argv[-1]) > 2:
        endarg = len(sys.argv)+1
        tmptype = "m"
        ecotype = "celcius"
    else:
        tmptype = "m"
        ecotype = "celcius"

    for i in (sys.argv[1:endarg]):

        city = i
        weather = get("http://api.weatherstack.com/current?access_key=a33b28c484453f67ce8fe059d25b0fa4&query="+city+"&units="+tmptype)
        data = weather.json()
        try:
            temp = data["current"]["temperature"]
        except:
            temp = data["success"]
            badcity = print("This is wrong, There's no city with name",i,"\nplease try again cities like madrid, dublin, london")
            return badcity
        end = print("temperature in ", city, " is ", temp, ecotype)
    return(end)


if __name__ == '__main__':
        main()






