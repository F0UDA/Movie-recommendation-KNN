# Movie Recommendation System with K-Nearest Neighbors (KNN) Algorithm

This Python code implements a movie recommendation system using the K-Nearest Neighbors (KNN) algorithm. The system is designed with a graphical user interface (GUI) using the PyQt5 library. Below is an explanation of the logic behind the code.

## Overview

The recommendation system is based on the K-Nearest Neighbors algorithm, which suggests movies similar to a user's favorite movie. The GUI allows users to select a movie from a list, and upon clicking a button, the system recommends movies based on the features of the selected movie.

## Logic

1. **Loading Raw Data:**
   - The movie data is stored in a CSV file (`movies_list.csv`), including columns such as ID, title, and numerical features.

2. **Initializing the Presenter Class:**
   - The `Presenter` class is initialized with a reference to the GUI (`_view`), an empty list for raw data (`self.raw_data`), an empty list for movie titles (`self.movies_list`), and an empty list for recommended movies (`self.recommended`).

3. **Loading Raw Data:**
   - The `load_raw_data` method reads the movie data from the CSV file, excluding the header, and populates the `raw_data` list.

4. **Setting Movie List in the GUI:**
   - The `set_list` method extracts movie titles from the raw data and adds them to a list widget in the GUI.

5. **Button Click Event:**
   - When a button is clicked (`on_button_clicked` method), the system retrieves the title of the selected movie from the GUI.
   - It then gets the index of the selected movie in the list and prepares the raw data for the KNN algorithm.

6. **KNN Algorithm:**
   - The `prepare_data` method processes raw data by converting numerical features into a format suitable for the KNN algorithm.
   - The `get_recommended_movies` method runs the KNN algorithm (`knn` function) with the processed data and the selected movie's features.
   - The KNN algorithm returns a list of recommended movies.

7. **Displaying Recommendations:**
   - The recommended movie titles are saved in the `recommended` list using the `save_recommendation` method.
   - The `show_result` method displays the recommended movies in the GUI.

8. **Running the Application:**
   - The `run` method initializes the PyQt application, sets up the GUI, and launches the event loop.

## KNN Algorithm Logic

The K-Nearest Neighbors (KNN) algorithm is used to find movies similar to a user's favorite movie. The logic involves the following steps:

1. **Preparing Data:**
   - The `prepare_data` method processes raw data by converting numerical features of each movie into a format suitable for the KNN algorithm.

2. **Running KNN Algorithm:**
   - The `get_recommended_movies` method calls the `knn` function with the processed data and the features of the selected movie.
   - The `knn` function returns a list of indices representing the nearest neighbors.

3. **Displaying Recommendations:**
   - The indices of recommended movies are used to retrieve their titles from the `movies_list`.
   - The recommended movie titles are displayed in the GUI using the `show_result` method.
