import requests 
import config
import smtplib, ssl
from email.mime.text import MIMEText


#Will add AWS integration to run script without the need for PC to be on


def find_geolocation():
    while True:
        city_name = 'New York'
        state_code = 'NY'
        country_code = 'USA'
        limit = 1

        api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={config.api_key}"
        response = requests.get(api_url)
        
        if response.status_code != 200:
            print("Valid")
        elif response.status_code == 200:
            data = response.json()
            break    

    return data

def find_current_city():
        
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={config.api_key}"

    response = requests.get(api_url)

    data = response.json()

    return data

def kelvin_to_farenheit():

    temp_min = find_current_city()['main']['temp_min']
    temp_max = find_current_city()['main']['temp_min']
    temp_avg = int(temp_max+temp_min)/2
    farenheit = int((temp_avg - 273.15) * 1.8 +32)
    
    if farenheit < 30:
        return(f"The average tempature for today is {farenheit} degrees Farenheit.\n It is fairly cold wear 3 layers")
    elif farenheit in range (30,50):
        return (f"The average tempature for today is {farenheit} degrees Farenheit.\n It is fairly cold wear 2 layers")
    elif farenheit in range (50,70):
        return (f"The average tempature for today is {farenheit} degrees Farenheit.\n It is fairly warm wear 1 layer")
    elif farenheit >70:
        return (f"The average tempature for today is {farenheit} degrees Farenheit.\n It is fairly warm, dress light")

def rain_calc():
     weather = find_current_city()['weather'][0]['main']
     weather_desc = find_current_city()['weather'][0]['description']
     if weather == "Rain":
        return f"RAIN ADVISORY!\nThe current weather will be {weather} with {weather_desc}\n PLEASE wear a jacket"
     else:
        return f"The current weather will be {weather} with {weather_desc}"


def send_email():
    message = f"""
    This is today's weather report:\n\n
    {kelvin_to_farenheit()}\n\n
    {rain_calc()}\n

    """

    message = MIMEText(message, "plain")
    message["Subject"] = "Daily Weather Report"
    message["From"] = config.sender_email

    port = 465
    sslcontext = ssl.create_default_context()
    connection = smtplib.SMTP_SSL(
        "smtp.gmail.com",
        port,
        context=sslcontext
    )

    connection.login(config.sender_email, config.password)
    connection.sendmail(config.sender_email, config.receiver_email, message.as_string())

    print("Succesful Email")


for i in find_geolocation():
        city_lat = (i['lat'])
        city_lon = (i['lon'])



send_email()






