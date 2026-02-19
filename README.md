# NBA Shot Analysis – Data Exploration

Author - Nanditha Lekshmy

Description: Exploratory analysis of NBA shot data to evaluate player scoring performance and shooting distance patterns across court zones.
## Project Overview

This project analyzes NBA shot-level data to understand scoring contributions and shooting characteristics across different court areas. The dataset includes player identifiers, shot types, shot distances, shot outcomes, and zone information.

* The project addresses the following research questions:

* Which player scored the highest total points based on made shots?

* What is the average shot distance in each court zone?

* What is the most common (mode) shot distance?

The analysis demonstrates programming and data analytics skills, including data cleaning and preparation, exploratory data analysis (EDA) without relying on major built-in analytical functions. Results are printed directly to the console.

## Data

Source: NBA_2024_Shots.csv (Kaggle dataset)
Kaggle: https://www.kaggle.com/datasets/mexwell/nba-shots?select=NBA_2024_Shots.csv

Description:
The dataset contains shot-level records from NBA games, including:

* PLAYER_ID – Unique identifier for each player

* SHOT_TYPE – Type of shot (2PT Field Goal or 3PT Field Goal)

* SHOT_MADE – Whether the shot was successful (True/False)

* SHOT_DISTANCE – Distance of the shot attempt

* ZONE_NAME – Court zone where the shot was taken

This dataset is suitable for practicing sports analytics, and aggregation logic using Python.
## Program Functionality

The program:

* Imports NBA shot data from CSV using Pandas

* Converts shot types (2PT/3PT) into numeric scoring values

* Calculates total points scored per player using made shots only

*  Computes average shot distance for each court zone

* Determines the mode of shot distance across all attempts

* Prints all results to the console
## Dependencies

* Python 3.x

* pandas

