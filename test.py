import requests

# Replace with your desired endpoint
url = 'https://jsonplaceholder.typicode.com/todos/1'
print(url_

# Send GET request
print("Sending Requests")
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Response: ", response.json())  # Print the JSON response if successful
else:
    print(f"Request failed with status code: {response.status_code}")
