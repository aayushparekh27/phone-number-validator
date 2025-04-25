import requests

# Your API key from NumVerify
API_KEY = '95322bda9bc75bcc606cc857f02875c0'

def get_phone_info(phone_number, country_code):
    # API URL with URL parameters
    url = f'http://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}&country_code={country_code}&format=1'
    
    # Make the API request
    try:
        response = requests.get(url)
        
        # Check the response status code
        if response.status_code == 200:
            data = response.json()

            # Print the raw response for debugging
            # print("API Response:", data)

            # Check if the number is valid
            if data.get('valid', False):
                # Organize the output
                print("\nPhone Number Details:")
                print("----------------------------")
                print(f"Phone Number: {data.get('number')}")
                print(f"International Format: {data.get('international_format')}")
                print(f"Country: {data.get('country_name')}")
                print(f"Country Code: {data.get('country_code')}")
                print(f"Location: {data.get('location')}")
                print(f"Carrier: {data.get('carrier')}")
                print(f"Line Type: {data.get('line_type')}")
                print(f"Country Prefix: {data.get('country_prefix')}")
            else:
                print("\nInvalid phone number or unable to fetch details.")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Input phone number and country code
phone_number = input("Enter a phone number (without country code): ")
country_code = input("Enter the country code (e.g., IN for India): ")
get_phone_info(phone_number, country_code)
