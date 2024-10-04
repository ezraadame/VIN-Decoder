import requests

def decode_vin(vin):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data.get('Results', [])
        
        make = None
        model = None
        year = None
        body_type = None
        engine_type = None
        trim = None

        for result in results:
            if result.get('Variable') == 'Make':
                make = result.get('Value', 'N/A')
            elif result.get('Variable') == 'Model':
                model = result.get('Value', 'N/A')
            elif result.get('Variable') == 'Model Year':
                year = result.get('Value', 'N/A')
            elif result.get('Variable') == 'Body Class':
                body_type = result.get('Value', 'N/A')
            elif result.get('Variable') == 'Engine Model':
                engine_type = result.get('Value', 'N/A')
            elif result.get('Variable') == 'Trim':
                trim = result.get('Value', 'N/A')

        print(f"Make: {make}")
        print(f"Model: {model}")
        print(f"Year: {year}")
        print(f"Body Type: {body_type}")
        print(f"Engine Type: {engine_type}")
        print(f"Trim: {trim}")
        


def main():
    vin = input("Enter a VIN to decode: ")
    decode_vin(vin)

if __name__ == "__main__":
    main()


