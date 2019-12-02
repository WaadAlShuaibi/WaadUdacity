import time
import pandas as pd
import numpy as np
# This project written by Waad AlShuaibi
# Programming for data science
# For beginners 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs

    while True:
      city = input("\nSpcify a city to analyze? New York, Chicago or Washington?\n").lower()
      if city.lower() not in ('new york', 'chicago', 'washington'):
        print("Sorry, type a city from the following (New York, Chicago, Washignton). Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nSpecify a month to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?   \n").lower().capitalize()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        print("Sorry, type a month from the following (January, February, March, April, May, June or type all). Try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nSpecify a day to filter by? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.\n").lower().capitalize()
      if day not in ('Monday', 'Sunday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print("Sorry, type a day from the following(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type all). Try again.")
        continue
      else:
        break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # filter by the city
    df = pd.read_csv(CITY_DATA[city])

    # convert the start and end time from strings to dates, so we can extract the day

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extract the day and month into their seperate columns
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()


    # filter by month if applicable
    if month != 'All':
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':

       df = df[df['day'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:\n{} \n".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("Most common day:\n{} \n".format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:\n{} \n".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common start station:\n{} \n".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common end station:\n{} \n".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    popular_route = df['route'].mode()[0]
    print("Most frequent combination of start station and end station route:\n{} \n".format(popular_route))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print("Total travel time:\n{} \n".format(total))

    # TO DO: display mean travel time
    average = df['Trip Duration'].mean()
    print("Mean travel time:\n{} \n".format(average))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n{} \n".format(user_types))

    # TO DO: Display counts of gender
    if ('Gender' in list(df.columns)):
     user_genders = df['Gender'].value_counts()
     print("Counts of gender:\n{} \n".format(user_genders))
    else:
     print("No gender data available:\n{} \n")


    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in list(df.columns)):
        earlist_birth = df['Birth Year'].min()
        print("Earlist year of birth:\n{} \n".format(earlist_birth))

        recent_birth = df['Birth Year'].max()
        print("Recent year of birth:\n{} \n".format(recent_birth))

        popular_birth = df['Birth Year'].mode()[0]
        print("common year of birth:\n{} \n".format(popular_birth))
    else:
        print("No birth year data available:\n{} \n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():


    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        num_rows = 5
        row_initial= 0

        raw_data =  input('\nWould you like to see raw data? Enter yes or no.\n')
        while True:

            if raw_data.lower() == 'yes':
                print('\nShown rows from {} to {}:'.format(row_initial+1, num_rows))
                print('\n', df.iloc[row_initial : num_rows])

                num_rows += 5
                row_initial += 5

                raw_data =  input('\nWould you like to see raw data? Enter yes or no.\n')

            else:
                break

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
