import sklearn.linear_model as lin
import pandas as pd

def linear_regression(data,text):

    # Load a dataset.
    text = text
    powerproduction = data
    def f(speed, p):
        return p[0] + speed * p[1]

    def predict_power_output(speed):
        return round(f(speed, p),2)

    speed = powerproduction["speed"].to_numpy()
    y = powerproduction["power"].to_numpy()

    speed = speed.reshape(-1, 1)

    model = lin.LinearRegression()
    model.fit(speed, y)
    #r = model.score(speed, y)
    p = [model.intercept_, model.coef_[0]]

    return(predict_power_output(float(text)))

# Load a dataset.
df = pd.read_csv('dataset.csv')

# We are removing the non zero values
cleansed_data = df.loc[df['power'] > 0 ]

# filtering between values see https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates



# If a user types wind speeds lower than 0.275 or equal higher than 24.499, it will be handled with an if statement and return 0

def receive_text(text):
    text = text
    if text <= 0.2:
        return 0

    if text >= 24.4:
        return 0


    #if a user inputs a wind speed between 0 - 5 mph, they will get a linear prediction from wind speed data betwween 0 and 5 mph.

    if text > 0.2 and text <= 5:
        value_one = cleansed_data.loc[(cleansed_data['speed'] > 0.2) & (cleansed_data['speed']<= 5)]
        return linear_regression(value_one,text)


    #if a user inputs a wind speed between 5 - 10 mph, they will get a linear prediction from wind speed data betwween 5 and 10 mph.

    if text > 5 and text <= 10:
        value_two = cleansed_data.loc[(cleansed_data['speed'] > 5) & (cleansed_data['speed']<= 10)]
        return linear_regression(value_two,text)


    #if a user inputs a wind speed between 10 - 15 mph, they will get a linear prediction from wind speed data betwween 10 and 15 mph.
        
    if text > 10 and text <= 15:
        value_three = cleansed_data.loc[(cleansed_data['speed'] > 10) & (cleansed_data['speed']<= 15)]
        return linear_regression(value_three,text)

    #if a user inputs a wind speed between 15 - 20 mph, they will get a linear prediction from wind speed data betwween 15 and 20 mph.

    if text > 15 and text <= 20:
        value_four = cleansed_data.loc[(cleansed_data['speed'] > 15) & (cleansed_data['speed']<= 20)]
        return linear_regression(value_four,text)

        #if a user inputs a wind speed between 20 - 25 mph, they will get a linear prediction from wind speed data betwween 20 and 25 mph.

    if text > 20 and text <= 24.4:
        value_five = cleansed_data.loc[(cleansed_data['speed'] > 20) & (cleansed_data['speed']<= 24.498)]
        return linear_regression(value_five,text)