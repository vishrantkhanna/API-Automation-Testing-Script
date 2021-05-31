import requests
import json
import sys
import traceback

# Store JSON response in a file
def record_json_response(json_file):
     with open('api_json_response.json', 'w') as outfile:
          json.dump(json_file, outfile)


# Assessing JSON response
def assess_json_response(json_response):
     print(json_response)
     # Pasring JSON file
     for json_data in json_response:
          # Verifying status code returned by server in response
          if json_data == "code":
               if json_response[json_data] != 200:
                    print("Error, got " + str(json_response[json_data]) + " but expected 200")
               else:
                    print("'code': '200'")
          # Verifying status of request returned by the server
          if json_data == "status":
               if json_response[json_data] != "success":
                    print(("Error, got " + json_response[json_data] + " but expected success"))
               else:
                    print("'status': 'success'")

# Testing Headers

# Checks the satus code returned by server
def test_api_check_status_code():
    try:
        assert True
        response = requests.post(api_endpoint, json=data)
        assert response.status_code == 200

    except AssertionError:
         print("Expected stauts code 200, but got " + response.headers[response.status_code])


'''
# Checks the length of the response returned
def test_api_check_content_length():
    try:
        assert True
        response = requests.post(api_endpoint, json=data)
        assert response.headers['Content-Length'] == "<length of response returned>"

    except AssertionError:
         print("Expected Content-Length to be " + "<length of response returned>" + " but got " + response.headers['Content-Length'])
'''


# Checks what type for response is given by server; like JSON
def test_api_check_content_type_equals_json():
    try:
         response = requests.post(api_endpoint, json=data)
         assert response.headers['Content-Type'] == "application/json;charset=utf-8"
     
    except AssertionError:
         print("Expected Content-Type to be " + "application/json;charset=utf-8" + " but got " + response.headers['Content-Type'])


# End of Header tests

# API Endpoint
api_endpoint = input("Enter API Endpoint URI: ")
# api_endpoint = "<API enpoint URI>"

# Body of Post request
# Opens JSON file
f = open('config.txt', 'r')

# Reading JSON file as input
post_body = json.load(f)
json_file=[]

# Iterating through the JSON list
for data in post_body['details']:

    # Debug satement: used to check is json is being read correctly
    print("\t")
    print(data)

    # Testing Headers

    # Checks the satus code returned by server
    test_api_check_status_code()

    '''
    # Checks the length of the response returned
    test_api_check_content_length()
    '''

    # Checks what type for response is given by server; like JSON
    test_api_check_content_type_equals_json()


    # End of Header tests

    # Store JSON response in a file
    response = requests.post(api_endpoint, json=data)
    json_file.append(response.json())
    
    # Assessing JSON response 
    assess_json_response(response.json())

record_json_response(json_file)

# Closing file
f.close()
