# Import Modules
import csv

# Open dataset .csv and store each row as an object in array
try:
  with open("owid-covid-data.csv", 'r') as dataset:
    # Array to hold all rows as objects as elements
    data_array = [] 

    reader = csv.DictReader(dataset)
    for line in reader:
      data_array.append(dict(line))
except FileNotFoundError:
  print("Dataset is missing. Check your working directory.")


# Take informal metric command and return formal column name for query
def translate_metric(metric):
    # Defined commands informal:formal values
    metric_commands = {"deaths": "total_deaths", "cases": "total_cases", "positivity": "positivity_rate", "new": "new_cases"}

    return metric_commands.get(metric)

# Format and prepare user input country value for validation and query
def format_country(country_input):
  if len(country_input) == 3:
    return country_input.upper()
  else:
    return country_input.title()

# Check to see if formatted input exists in dataset (country or metric)
def validate_input(input_to_check, input_type):
  if len(input_to_check) >= 3:
    for data_object in data_array:
      for key, val in data_object.items():
        if val == input_to_check or key == input_to_check:
          print(input_type, input_to_check)
          return True
  elif len(input_to_check) < 3:
    print("Enter at least three characters.")

# ---------------------------------------------
# Begin collection of input gathering functions
# TODO: Replace with single function?
def get_country():
  while True:
    input_country = format_country(input("Country (ex: Honduras or HND, United States or USA): ").strip().lower())
      
    if validate_input(input_country, "Country:"):
      return input_country
    else:
      print("Sorry,", input_country, "was not found. Please try again.")
      continue

def get_timeframe():
  while True:
    input_timeframe = input("Timeframe (week, month, alltime)): ").strip().lower()
    
    # TODO: Allow for custom timeframe (ex: Februrary 2020 - September 2020)
    if input_timeframe == "week" or input_timeframe == "month" or input_timeframe == "alltime":
      return input_timeframe
    else:
      print("You have selected an invalid timeframe, please try again.")
      continue

def get_metric():
  while True:
    input_metric = input("Metric (deaths, cases, postivity or 'list' to see more options): ").strip().lower()

    try:
      # Check if user requested to see available metrics
      if input_metric == "list":
        print("--- Available Metrics --")
        print("cases - total case count per day")
        print("deaths - total death count per day")
        print("new - new cases per day")
        print("positivity - daily postitivity rate")
      else:
        # Call translate_metric and get formal column title from informal command
        input_metric = translate_metric(input_metric)
        
        # Ensure metric exists in dataset
        if validate_input(input_metric, "Metric:"):
          return input_metric
        else:
          continue
    except:
      print("Your chosen metric does not appear in the dataset, please try again. Alternatively, type 'list' to see a list of available metrics.")
    
# End collection of input gathering functions
# -----------------------------------------

def general_error():
  print("Sorry, I didn't understand that command. Please try again.")

def build_query():
  # Gets user input for country, data and timeframe parameters
  print("Please enter the country, metric and timeframe for your query.")
  
  # DEBUG remove before prod
  # print(data_array[0])
  # ###########################
  search_country = get_country()
  search_timeframe = get_timeframe()
  search_metric = get_metric()

  print("You have selected the following parameters:", "\nCountry:", search_country, "\nTimeframe:", search_timeframe, "\nMetric:", search_metric)


def main():
  print("COVID-19 Stats")
  print("----------------------------")
  # TODO: Take response and pass it to search/query function
  # Get inputs and build query 
  build_query()


if __name__ == '__main__':
  main()
