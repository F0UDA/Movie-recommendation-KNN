from PyQt5 import QtWidgets

from KNN import knn
import sys


class Presenter:


    # Constructor of the Presenter class

    def __init__(self, _view):
        self.raw_data = []
        self.view = _view
        self.load_raw_data()
        self.movies_list = []
        self.recommended = []


    # Method to load movie data from a CSV file
        
    def load_raw_data(self):
        path = "../Data/movies_list.csv"
        with open(path, 'r') as md:
            next(md)  # read the headings
            for line in md.readlines():
                data_row = line.strip().split(',')
                self.raw_data.append(data_row)


    # Method to extract movie titles from the raw data 
    # and add them to a list widget in the view
                
    def set_list(self):
        for a in self.raw_data:
            self.movies_list.append(a[1])
        self.view.listWidget.addItems(self.movies_list)


    # Method called when a button is clicked
        
    def on_button_clicked(self):
        selected_item = self.view.listWidget.currentItem().text()  # get title of selected movie
        index = self.movies_list.index(selected_item)              # get the index if this movie
        prepared_data = self.prepare_data()                        # process raw data for KNN
        result = self.get_recommended_movies(prepared_data, prepared_data[index])
        self.save_recommendation(result)
        self.show_result()


    # Method to prepare the raw data for the K-nearest neighbors algorithm 
    # by removing the ID and title of each movie
        
    def prepare_data(self):
        processed_data = []
        for row in self.raw_data:
            data_row = list(map(float, row[2:]))
            processed_data.append(data_row)
        return processed_data


    # Method to show the recommended movies in the view

    def show_result(self):
        i = 0
        for a in self.recommended:
            self.view.recom[i].setText(a)
            self.view.recom[i].show()
            i += 1


    # Method to run the K-nearest neighbors algorithm to get recommended movies
            
    def get_recommended_movies(self, data, fav_movie):
        recommended_movies = knn(data, fav_movie, k=5)
        return recommended_movies


    # Method to save the recommended movie titles to a local variable

    def save_recommendation(self, result):
        self.recommended = []
        for a in result:
            self.recommended.append(self.movies_list[a[1]])


    # Method to run the application
            
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.view.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.view.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())