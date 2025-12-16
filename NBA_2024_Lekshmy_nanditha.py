import pandas as pd

# Function to calculate the player who scored highest by adding up the shot_type
def player_highest_score(df):
  player_id_dict = {}
  max_points = 0

# Replace the shot_type values with corresponding values
  df = df.replace('2PT Field Goal','2')
  df = df.replace('3PT Field Goal','3')

# Iterates the dataframe to find the player_id and shot_type of each player
  for index, row in df.iterrows():
    player_id = row['PLAYER_ID']
    shot_type = row['SHOT_TYPE']
    shot_made = row['SHOT_MADE']

# New player_ids and their shot_type values are added to the dictionary
    if (player_id not in player_id_dict) and (str(shot_made).upper() == 'TRUE'):
      player_id_dict[player_id] = int(shot_type)

# For the existing player_ids their shot_type values are added
    elif (player_id in player_id_dict) & (str(shot_made).upper() == 'TRUE') :
      player_id_dict[player_id] += int(shot_type)

# Iterates through the dictionary to identify the highest scorer
  for key, value in player_id_dict.items():
    if max_points < value:
      max_points = value
      player_id = key

  print(f"The player id who scored the maximum points is {player_id} and the player scored {max_points}")
  print("\n")

# Function to calculate the average shot distance in each zones
def average_shot_distance(df):
  shot_distance_calculation = {}
  zone_count = {}

# Iterates the dataframe to find the shot_distance, zone_name
  for index, row in df.iterrows():
    shot_distance = row['SHOT_DISTANCE']
    zone_name = row['ZONE_NAME']

# Adds the zone name if it is not added and increments the count by 1
    if zone_name not in shot_distance_calculation:
      shot_distance_calculation[zone_name] = shot_distance
      zone_count[zone_name] = 1

# Aggregrate the count of each shot_distance from each zone
    else:
      shot_distance_calculation[zone_name] += shot_distance
      zone_count[zone_name] += 1

# Calculates the average and displays it each for zone
  print("Average Shot distance for each zones")

  for key, value in shot_distance_calculation.items():
    print(f"{key}: {value/zone_count[key]:.2f}")

# Function to calculate the mode of shot distance
def mode_of_shot_distance(df):
  shot_distance_count = {}
  max = 0

# Iterates throught the dataframe to find the shot distance
  for index,row in df.iterrows():
    shot_distance = row["SHOT_DISTANCE"]

# Adds the shot distance in the dictionary else aggregate the count to find the frequency of each shot distance
    if shot_distance not in shot_distance_count:
      shot_distance_count[shot_distance] = 1
    else:
      shot_distance_count[shot_distance] += 1

  for key,value in shot_distance_count.items():

# Identifies the shot_distance that has the highest mode
    if max < value:
      max = value
      shot_distance_mode = key

  print("\n")
  print(f"The mode of the shot distance: {shot_distance_mode}")

def main():
  df = pd.read_csv('NBA_2024_Shots.csv')

# Calls three functions
  player_highest_score(df)
  average_shot_distance(df)
  mode_of_shot_distance(df)

main()