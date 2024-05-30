# College NIRF Rank Predictor using ML

This project is an end-to-end machine learning solution that predicts the NIRF rank of a college based on various parameters such as Teaching, Learning and Resources (TLR) score, Research and Professional Practice (RPC) score, Graduation Outcomes (GO) score, Outreach and Inclusivity (OI) score, Perception score, and Peer Perception score.

I used a 2020 NIRF ranking dataset from Kaggle and implemented the project using Flask to create a simple API service that anyone can use to make predictions. The model achieved a score of 93% and a root mean square error of 15.47, which demonstrates its accuracy in predicting college NIRF rankings.

## Getting Started

### Folder Structure 

`dataset` folder contains the engineering.csv dataset used in the project.

`College_rank_predictor.ipynb` notebook that was used to develop and train the model.

`app.py` is the Flask application file that defines the API endpoints and loads the saved model.

`college_rank_predictor.pkl` is the serialized machine learning model that is used for prediction.

`README.md` is the project documentation file.

`requirements.txt` lists the Python dependencies required to run the project.

`templates` folder contains the HTML templates for the web application.

`static` folder contains the images.



### Prerequisites

To run the project, you must have the following installed on your system:

* Python 3.6+
* Flask
* Pandas
* Scikit-learn

You can install the required packages using the following command:
pip install -r requirements.txt

## How to Use
To get started with this project, follow these steps:
* Clone this repository
* Install the required dependencies using pip: pip install -r requirements.txt
* Start the Flask server: python app.py
* Send a POST request to the /predict endpoint with a JSON payload containing the values for TLR score, RPC score, GO score, OI score, Perception score, and Peer * Perception score.

### Required parameters
The required parameters are:

* `tlr` - Teaching, Learning and Resources score 
* `rpc` - Research and Professional Practice score 
* `go` - Graduation Outcomes score 
* `oi` - Outreach and Inclusivity score 
* `perception` - Perception score 
* `peer_perception` - Peer Perception score 
## Results
The model achieved a score of 93% and a root mean square error of 15.47, which demonstrates its accuracy in predicting college NIRF rankings.

