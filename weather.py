from requests import get
import sys

readcode = open("key.txt", "r")
key = readcode.read()
tmptype = ""
ecotype = ""
endarg = -1
cities = ""

def chktempurature(cities):
    global endarg
    global key

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

    for i in cities:

        city = i
        weather = get("http://api.weatherstack.com/current?access_key="+key+"&query="+city+"&units="+tmptype)
        data = weather.json()
        try:
            temp = data["current"]["temperature"]
        except:
            temp = data["success"]
            badcity = print("This is wrong, There's no city with name",i,"\nplease try again cities like madrid, dublin, london")
            return badcity
        end = print("temperature in ", city, " is ", temp, ecotype)
    return(end)

def main(*arg):
    global cities
    if len(sys.argv[-1]) > 2:
        arglist = str(sys.argv[1:])
    else:
        len(sys.argv[-1]) < 2
        arglist = str(sys.argv[1:-1])

    cities = arglist.replace(",", " ").replace("'", " ").strip("'[] ").split()
    chktempurature(cities)


if __name__ == '__main__':
        main()






