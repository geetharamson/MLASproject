 # Machine Learning And Statistics Project -2020
 ### Author:- Geetha Karthikesan 
 ### g00376320@gmit.ie
    
 ## Project Instructions
In this project you must create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with predicted power values based on speed values sent as HTTP requests. Your submission must be in the form of a git repository containing, at a minimum, the following items:
1. Jupyter notebook that trains a model using the data set. In the notebook you should explain your model and give an analysis of its accuracy.
2. Python script that runs a web service based on the model, as above.
3. Dockerfile to build and run the web service in a container.

## How to download the repository
* Go to GitHub.
* Go to my repository: [:link:GitHub](https://github.com/geetharamson/MLASproject.git)
* Click the [`Code`](#code) button which is colored green.
* Click on HTTPS and copy the link that is shown.
* Open the command line on your machine, navigate to the directory where you would like to clone the repository down to.
* Enter the command: git clone followed by the URL of the repository.
* The repository will be cloned down to your current working directory.
* You will need to navigate to this folder location on the command line in order to run the program.
* Details on how to view my jupyter notebook are described in the next section below.

## How to run the jupyter notebook

+ On the command line navigate to the folder location where the repository has been downloaded and saved to using the cd change directory command.
+ Type jupyter notebook on the command line and press enter
+ After a short wait jupyter notebook will open in your web browser.
+ Open the **project.ipynb** notebook in the browser and the notebook containing the code and comments that I wrote for this assignment will be displayed.
+ If you want to run the code in any cell hold down the shift key and press enter and the command will run and the output wil be displayed in the next cell.
+ To change between edit and read mode at any time press the ESC key.
+ If you wish t run the entire notebook click Kernel in the toolbar at the top of the screen and then click Restart and run all. The notebook will refresh and all code cells will be executed from top to bottom.
+ When you have finished viewing the jupyter notebook close the web browser and return to the command line. Press Ctrl + C on the command line to kill the program.

       https://github.com/geetharamson/MLASproject/blob/main/Project.ipynb  is the direct link to my jupyternotebook.
______________________________________________________________
## Files in my repository
 
 :open_file_folder:Static    - contains the static page index.html
 
 :open_file_folder:Images    - contains all images needed for project.ipynb and graphs generated while predicting models.
 
 :open_file_folder:Models    - contains few models predicted (poly-reg.pkl (polynomial regression),
                                neural-network.h5 (sequential neural network)
 
         requirements.txt    - contains the packages to run flask 
             dockerfile      - contains the commandsd needed for dockerfile
             dataset.csv     - contains the dataset needed for this wind turbine project
                  df.csv     - contains the cleaned dataset
                  app.py     - has the python application to run in virtual environment
                  
   NB: add venv/ to your .gitignore file after downloading the code.      
 
 # Prerequiste:
- Anaconda distribution of Python
- Python Software Foundation
- Project Jupyter
- matplotlib: Python plotting library
- NumPy
- Seaborn
- SciPy
- Pandas
- Scikit-learn
- PIP
- TensorFlow
- Docker
- Flask

 ## Packages to be imported
    pip install numpy==1.19.3 (Got errors with newer version 1.19.4 with Tensorflow)
    pip install joblib (For importing scikit-learn learning models)
    pip install tensorflow

## Run Flask app from inside a virtual environment
     python -m venv venv
     .\venv\Scripts\activate.bat
     pip install -r requirements.txt
     pip install tensorflow
     pip install silence-tensorflow
     SET FLASK_APP=app
     SET FLASK_ENV=development
     flask run
  
 Runs on  http://127.0.0.1:5000/  in the web browser
 To stop flask running :  deactivate    

## To run the application via Docker from the command line:
  The first step is to build a Docker image - a read-only template that contains a set of instructions for creating a container that can run on the Docker platform. A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. Containers are dependent on images, and use them to construct a run-time environment and run an application. The commands required to build a Docker image are listed in the file Dockerfile in this repository.

    docker build -t model-server . to build a docker image called model-server.
    docker image ls to list images.
    docker run -d -p 5000:5000 model-server to create an instance of the image in a container.
Once the container is running, access the web service on your localhost at http://127.0.0.1:5000/ to get predictions of power output for input wind speeds.

    docker container ls to list containers by ID.
    docker kill ID to stop a container with given ID
    docker container ls -a to check that the container is really gone. If not do
    docker kill ID

### To host the Flask app on eu.pythonanywhere.com
   Trying to host :link:http://geetharamson.pythonanywhere.com/
 Still working on it to host.No luck yet.
 
 ## Output models
 ![polyregression](https://github.com/geetharamson/MLASproject/blob/main/Images/poly.png)
 ![neuralnetwork](https://github.com/geetharamson/MLASproject/blob/main/Images/Neuralnetwork.png)
 
# :memo: References

:one:[Anaconda distribution in python](https://www.anaconda.com/products/individual)

:two:[Python](https://www.python.org/)

:three:[Numpy](https://numpy.org/)

:four:[Scipy](https://www.scipy.org/)

:five:[Pandas](https://pandas.pydata.org/)

:six:[Tensorflow](https://www.tensorflow.org/)

:seven:[Docker](https://www.docker.com/resources/what-container)

:eight:[Matplotlib](https://matplotlib.org/)

:nine:[Seaborn](https://seaborn.pydata.org/)

:keycap_ten:[Flask](https://flask.palletsprojects.com/en/1.1.x/)

[Pip](https://pip.pypa.io/en/stable/)

[Jupyter Notebook](https://jupyter.org/documentation)

*Geetha Karthikesan*
:beginner:
