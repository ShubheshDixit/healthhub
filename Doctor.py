import requests, json, os 

API_KEY = 'AIzaSyCGs4xRzHVjmtm1DHtu0u1ejMa1nirVWGc' 

LNG = 28.4843902 
LAT = 77.5135804 

keyword = input('Enter the Doctor type :- ')

filename = keyword+'.json'

# url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LNG}%2C{LAT}&radius=5000&type=doctors&keyword={keyword}&key={API_KEY}" 

payload={} 
headers = {} 
os.chdir(os.getcwd()) 
# response = requests.request("GET", url, headers=headers, data=payload) 

# print(response.text) 

with open(filename, 'r') as f: 
    data = json.load(f) 

# data = json.loads(response.text) 

# with open(filename, 'w') as f: 
#     json.dump(data, f, indent=4) 

#  print(data) 
for index, item in enumerate(data['results']): 
    
    lng = item['geometry']['location']['lng'] 
    lat = item['geometry']['location']['lat'] 
    name = item['name'] 
    rating = item['rating'] 
    try: 
        open_now = item["opening_hours"]["open_now"] 
    except Exception as e: 
        open_now = False 
    print(index+1) 
    print(lng) 
    print(lat) 
    print(name) 
    print(rating) 
    print(open_now) 
    print() 

