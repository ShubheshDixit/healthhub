import requests, json, os 

API_KEY = 'Api Key' 

LNG = 28.4843902 
LAT = 77.5135804 

def doctors_nearby(keyword: str):
    

    filename = 'utils/json_files/'+keyword+'.json'

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LNG}%2C{LAT}&radius=5000&type=doctors&keyword={keyword}&key={API_KEY}" 

    payload={} 
    headers = {} 
    print(os.getcwd())
    os.chdir(os.getcwd()) 
    # return os.getcwd()
    
    response = requests.request("GET", url, headers=headers, data=payload) 

    # print(response.text) 

    # with open(filename, 'r') as f: 
    #     data = json.load(f) 

    data = json.loads(response.text) 

    # with open(filename, 'w') as f: 
    #     json.dump(data, f, indent=4) 

    #  print(data) 
    response = {}
    results = []
    for index, item in enumerate(data['results']): 
        
        lng = item['geometry']['location']['lng'] 
        lat = item['geometry']['location']['lat'] 
        name = item['name'] 
        rating = item['rating'] 
        try: 
            open_now = item["opening_hours"]["open_now"] 
        except Exception as e: 
            open_now = False 
        # print(index+1) 
        # print(lng) 
        # print(lat) 
        # print(name) 
        # print(rating) 
        # print(open_now) 
        # print() 
        
        output = {}
        output['name']=name
        output['rating']=rating
        output['open_now']=open_now
        output['location']={'lat':lat, 'lng':lng}
        results.append(output)
        
    return {'results' : results}   
        


# doctors_nearby('dermatologists')
