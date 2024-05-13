import pandas as pd

# data_frame =pd.read_csv('.learn/assets/pokemon_data.csv')

# print(data_frame)

# data = pd.Series([23,45,7,34,6,63,36,78,54,34])
# print(data)

# data = pd.date_range(start= '2021-05-01', end= '2021-05-12')

# print(data)

# my_series = pd.Series([2, 4, 6, 8, 10])

# print(my_series.apply(lambda x: x / 2))

# # Two-dimensional array of [name, age] values
# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]

# # Create the DataFrame and name the columns
# df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])

# # Print the DataFrame
# print(df)

# #Dict
# data = [
#     { 
#         "brand": "Toyota", 
#         "model": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "model": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porsche", 
#         "model": "Cayenne",
#         "color": "White"
#     },
#     {
#         "brand": "Tesla", 
#         "model": "Model S",
#         "color": "Red"
#     }
# ]

# # Create the DataFrame and name the columns
# df = pd.DataFrame(data)

# # Print the DataFrame
# print(df)

data_frame =pd.read_csv('.learn/assets/pokemon_data.csv')

# print(data_frame.iloc[133,6])

# print(data_frame.head(3))

# print(data_frame.tail(3))

print(data_frame['Name'][0:10],data_frame['Type 1'][0:10])