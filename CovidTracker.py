from covid import Covid

covid = Covid()

country = input("Enter you country name : ")

try: 
    data = covid.get_status_by_country_name(country)

    print(f"Showing details of {country}")
    
    for key in data:
        print(f"{key} : {data[key]}")

except ValueError:
    print("Country not found, please check your input!")