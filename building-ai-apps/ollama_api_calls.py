import requests
import json
'''
# ------------------------ GENERATE API CALL ------------------------
# Define the URL and headers
url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

# Define the data payload
data = {
    "model": "llama3.2",
    "prompt": "Why is the sky blue?",
    "stream": False
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    try:
        data = response.json()  # Tries to parse the response as JSON
        print("Response Text:", data) #print the response
        print("Response Text:", data.get('response', 'No response field found')) #print content of response field
    except json.JSONDecodeError:
        print("Response is not valid JSON. Here's the raw content:")
        print(response.text)  # Print raw response if it fails to decode
        

# ------------------------ GENERATE API CALL --------------------------------

# ------------------------ Chat API CALL ------------------------
# Define the URL and headers
url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

# Define the data payload
data = {
  "model": "llama3.2",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ],
  "stream":False
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    try:
        data = response.json()  # Tries to parse the response as JSON
        print("Response Text:", data) #print the response
        print("Response Text:", data.get('response', 'No response field found')) #print content of response field
    except json.JSONDecodeError:
        print("Response is not valid JSON. Here's the raw content:")
        print(response.text)  # Print raw response if it fails to decode
        

# ------------------------ CHAT API CALL --------------------------------

'''

def ollama_api_call():
    options =[
        (0,"EXIT"),
        (1, "GENERATE"),
        (2, "CHAT")
    ]
    print("Please choose a number from the list below:")
    for number, text in options:
        print(f"{number}. {text}")
    while True:
        try:
            chosen_number = input("\nEnter the number corresponding to your choice (or 0 to exit): ")
            # Convert input to integer and check validity
            chosen_number = int(chosen_number)
            print(f"You chose: {chosen_number}")
               
            # If the user wants to exit
            if chosen_number == 0:
                print("Exiting the program.")
                exit(0)
            if chosen_number==1:
               
                url= 'http://localhost:11434/api/generate'
                data={
                        "model": "llama3.2",
                        "prompt": "Why is the sky blue?",
                        "stream":False
                    }
                break
            elif chosen_number==2:
                url= 'http://localhost:11434/api/chat'
                data={
                        "model": "llama3.2",
                        "messages": [
                            { "role": "user", "content": "why is the sky blue?" }
                        ],
                        "stream":False
                    }
                break
            else:
                print(f"Please choose a number between 1 and {len(options)}.")
        except ValueError:
            print("That's not a valid number! Please enter a valid number.")
   
    headers = {"Content-Type": "application/json"}



    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response
    if response.status_code == 200:
        try:
            data = response.json()  # Tries to parse the response as JSON
            print("Response Text:", data) #print the response
            if chosen_number==1:
                print("Response Text:", data.get('response', 'No response field found')) #print content of response field
            elif chosen_number==2:
                print("Response Text:", data['message']['content']) #print content of response field
            
        except json.JSONDecodeError:
            print("Response is not valid JSON. Here's the raw content:")
            print(response.text)  # Print raw response if it fails to decode
            


# ------------------------ FUNCTION CALL --------------------------------

ollama_api_call()

