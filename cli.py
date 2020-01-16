from requests import get
import click


@click.command()
@click.option('--token','token', prompt=True, type=str, help='please type in you api token.')
@click.option('--city','city',  help="Pick a city name ")
@click.option('--T','mode', default="m", help="choose tempurture mode celsius or fernhieght")


def main(token, city, mode):
    city_list = city.split(",")
    key = token

    if mode == "Fahrenheit" or mode == "fahrenheit" or mode == "f" or mode == "F":
        mode = "Fahrenheit"
        modetype = "f"
    else:
        mode = "Celsius" 
        modetype = "m"
    

    for x in city_list:
        weather = get("http://api.weatherstack.com/current?access_key="+key+"&query="+x+"&units="+modetype)
        data = weather.json()
        
        try:
            if data["error"]["code"] == 101:
                print("You have not supplied a valid API Access Key")
                break
        except:
            pass

        try:
            temperature = data["current"]["temperature"]
        except:
            temperature = data["success"]
            badcity = print("This is wrong, There's no city with name",x,"\nplease try again cities like madrid, dublin, london")
            print(badcity)
            continue

        print("temperature in ",x, "is", temperature, mode)
        
        
    

if __name__ == '__main__':
    main()
