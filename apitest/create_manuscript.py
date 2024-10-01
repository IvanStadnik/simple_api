import requests

endpoint = 'http://127.0.0.1:8000/api/v1/manuscripts/'
token = 'c721a55bccf3b7d669aaf8fb266c5efc880906b5'
headers = {
    'Authorization': f'Bearer {token}',
}

# Open the file in binary mode
files = {
    'file': open('./files/python_for_prof.pdf', 'rb'),
}
data = {
    'title': 'My First Manuscript',
    'category': '1',  # Replace with the appropriate category ID
}

response = requests.post(endpoint, headers=headers, files=files, data=data)


# Check the response
print(response.status_code)
print(response.json())
