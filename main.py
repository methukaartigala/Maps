from flask import Flask, request, jsonify
import heapq

app = Flask(__name__)

def create_graph():
    # Define your school's graph as an adjacency list.
    # Each edge includes the destination node and a tuple representing (distance, directions).
    # Replace the example graph with your school's data.
    graph = {
        'Main Entrance': [('Library', (5, 'Walk straight down the main hallway.')), 
                          ('Cafeteria', (10, 'Take a right and walk along the cafeteria.'))],
        'Library': [('Main Entrance', (5, 'Walk straight towards the main entrance.')), 
                    ('Classroom1', (8, 'Turn left and walk to Classroom 1.'))],
        'Cafeteria': [('Main Entrance', (10, 'Turn left and walk down the main hallway.')), 
                      ('Classroom2', (6, 'Walk straight and take a left to Classroom 2.'))],
        'Classroom1': [('Library', (8, 'Turn right and head back to the library.'))],
        'Classroom2': [('Cafeteria', (6, 'Walk straight and head back to the cafeteria.'))]
        # Add more locations and connections as needed
    }
    return graph

def dijkstra(graph, source, destination):
    distances = {node: (float('inf'), '') for node in graph}
    distances[source] = (0, '')

    priority_queue = [(0, '', source)]

    while priority_queue:
        current_distance, current_directions, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node][0]:
            continue

        for neighbor, (distance, directions) in graph[current_node]:
            total_distance = current_distance + distance
            total_directions = current_directions + directions

            if total_distance < distances[neighbor][0]:
                distances[neighbor] = (total_distance, total_directions)
                heapq.heappush(priority_queue, (total_distance, total_directions, neighbor))

    return distances[destination]

@app.route('/shortest_path', methods=['POST'])
def shortest_path_endpoint():
    data = request.get_json()
    source_node = data.get('source_node')
    destination_node = data.get('destination_node')

    graph = create_graph()

    total_distance, total_directions = dijkstra(graph, source_node, destination_node)

    response = {
        'total_distance': total_distance,
        'textual_directions': total_directions
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
