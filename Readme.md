
Title: School Navigation Web Service using Dijkstra's Algorithm

Description:
This GitHub repository contains a Flask-based web service that provides navigation assistance within a school using Dijkstra's algorithm. The application enables users to find the shortest path and textual directions between different locations within the school.

The main components of this repository are as follows:

main.py: This file contains the implementation of the Flask web service. It defines the school's graph as an adjacency list and utilizes Dijkstra's algorithm to find the shortest path between two given locations within the school. The web service listens on the endpoint /shortest_path, where users can send a POST request with the source and destination nodes to receive the navigation information.

create_graph(): A helper function that defines the school's graph. Each edge in the graph includes the destination node and a tuple representing the distance and textual directions between the two nodes.

dijkstra(): A function that implements Dijkstra's algorithm to calculate the shortest distance and textual directions from a source node to a destination node within the school's graph.

Usage:
To use the web service, users can run the Flask application on their local machine or deploy it to a server. The web service listens on port 81 and accepts POST requests at the /shortest_path endpoint. Users can provide JSON data containing the source and destination nodes for which they need navigation assistance.

Dependencies:
The application requires Flask and heapq libraries. Ensure you have the necessary dependencies installed before running the web service.

Contributions:
Contributions to improve the algorithm's efficiency, add more locations and connections to the school's graph, or enhance the web service's functionality are welcome. Please fork the repository, make changes in a new branch, and submit a pull request to contribute to the project.

License:
The project is open-source and available under the MIT License. Feel free to use, modify, and distribute the code according to the terms mentioned in the license.

Enjoy navigating your school efficiently with the help of this Dijkstra-based navigation web service! If you have any feedback or suggestions, please don't hesitate to create an issue or reach out through the repository's contact information.
