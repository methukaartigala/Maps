import requests

url = "https://map-api.methukaartigala.repl.co/shortest_path"
data = {
    "source_node": "Main Entrance",
    "destination_node": "Classroom1"
}

response = requests.post(url, json=data)
if response.status_code == 200:
    result = response.json()
    print(f"Total distance: {result['total_distance']} meters")
    print("\nTextual directions:")
    print(result['textual_directions'])
else:
    print("Error:", response.text)
