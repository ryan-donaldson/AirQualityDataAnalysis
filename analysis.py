# Begin by importing
import pandas as pd
import matplotlib.pyplot as plt

'''Dataset used can be found here: https://www.kaggle.com/datasets/yakhyojon/air-quality-data/'''

questions = """
Questions about the air quality dataset:
    1. Which cities in the U.S. have the worst air quality (highest api)?
    2. Which 10 states have cities with the best air quality (lowest avg api)?
    3. Are all states represented at least once in the data?
    ***Note: Higher aqi means worse air quality. Some cities may have multiple data sites.***
"""
# Create a list of the states to help us answer one of the questions.
united_states = [ "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
 ]
def check_states(states_list):
    '''The purpose of this function is to determine if all states are represented in the dataset'''
    for state in united_states:
        if state not in states_list:
            return False
        else:
            return True

def main():
    '''This function runs the data analysis program.'''
    # Begin by telling the user what questions we're answering.
    print(questions)

    # Read in the file to be analyzed
    air_quality = pd.read_csv("c4_epa_air_quality.csv")

    # Get our first set of data to answer question 1
    cities_and_aqi = air_quality[["city_name","aqi"]]
    top_cities = cities_and_aqi.sort_values(by='aqi', ascending=False).head(5)

    # Answer question 1.
    print("Answer to question 1:")
    print("Top cities in the U.S. with the worst air quality:\n")
    print(f'{top_cities}\n')

    # Create a bar graph for question 1.
    plt.figure(figsize=(10, 6))
    plt.bar(top_cities["city_name"], top_cities["aqi"])

    # Add labels to the graph.
    plt.xlabel("City")
    plt.ylabel("AQI")
    plt.title("Top Cities with the Highest AQI")

    # Rotate the x-axis to make it readable
    plt.xticks(rotation=45)

    # Get the total aqi for each state
    state_aqi_total = air_quality.groupby("state_name")["aqi"].sum()

    # Get the city count for each state.
    state_city_count = air_quality.groupby("state_name")["city_name"].count()

    # Get the avg aqi for each state based on its cities.
    state_aqi_avg = (state_aqi_total / state_city_count).round(2)
    aqi_avg_sort = state_aqi_avg.sort_values().head(10)

    # Answer question 2.
    print("Answer to question 2:")
    print("Top 10 states with the best average air quality:\n")
    print(f'{aqi_avg_sort.head}\n')

    # Get data to answer question 3.
    states = []
    states_in_data = air_quality["state_name"]
    for state in states_in_data:
        states.append(state)

    # Determine if all states are represented and answer question 3.
    print("Answer to question 3:")
    print("Are all U.S. states represented at least once in the dataset?\n")
    if check_states(states):
        print("Yes, all states are represented.")
    elif not check_states(states):
        print("No, not all states are represented.")


    # Display the graph from question 1.
    plt.show()

if __name__ == "__main__":
    main()