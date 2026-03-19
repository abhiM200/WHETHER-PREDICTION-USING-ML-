Weather Prediction Application
This is a simple weather prediction application built using Python and Tkinter. It allows users to enter information such as the date, precipitation, maximum temperature, minimum temperature, and wind speed. Based on these inputs, the application predicts the weather using a decision tree classifier.

How to Run
To run the application, follow these steps:

Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Clone this repository or download the main.py and calculation.py files to your local machine.

Open a terminal or command prompt and navigate to the directory where the files are located.

Install the required dependencies by running the following command:

pip install pandas numpy scikit-learn
Run the application by executing the following command:

python main.py
The application window will open, allowing you to enter the required information and click the "Predict" button to get the weather prediction.

How It Works
The application uses a decision tree classifier to predict the weather based on the input provided by the user. Here's a brief overview of how it works:

The user is prompted to enter the date, precipitation, maximum temperature, minimum temperature, and wind speed.

The application validates the input to ensure all fields are filled and numeric.

The input is processed and prepared for prediction. The calculation.py module is responsible for handling the input processing.

The application loads a dataset from a CSV file (dataset.csv) containing historical weather data. The dataset is used to train the decision tree classifier.

The dataset is preprocessed to handle outliers using the Interquartile Range (IQR) method and transform skewed distributions in the "precipitation" and "wind" columns.

The "weather" column in the dataset is label-encoded to convert categorical weather labels into numerical values.

The "date" column is converted to the datetime format and then to int64 format representing the timestamp of each date.

The input features are split into training and testing sets. The decision tree classifier is created and trained on the training data.

The user's input is processed and transformed using the same steps as during training.

The trained decision tree classifier is used to make predictions on the new input.

The predicted weather is displayed to the user.

The user can enter new inputs and click the "Predict" button to get updated weather predictions.

That's it! You can now use the weather prediction application to get weather forecasts based on the provided input.

Feel free to customize and enhance the application as needed. Enjoy predicting the weather!
