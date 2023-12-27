import math


def knn(data, query, k):
    neighbor_distances_and_indices = []

    for index, example in enumerate(data):
        # Calculate the distance between the query example and the current example from the data.
        distance = euclidean_distance(example[:-1], query)

        # Add the distance and the index of the example to an ordered collection
        neighbor_distances_and_indices.append((distance, index))

    # Sort the ordered collection of distances and indices from smallest to largest by the distances
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)

    # Pick the first K entries from the sorted collection - we will pick 5
    result = sorted_neighbor_distances_and_indices[:k]
    return result


def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)
