import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # gets users input for city
    city = input('Choose city: chicago, new york city, washington \n').lower()
    cities = ['chicago', 'new york city', 'washington']
    while city not in cities:
       print('Wrong input. Please choose from the list of cities')
       city = ''
       city = input('Choose city: chicago, new york city, washington \n')

    # TO DO: get user input for month (all, january, february, ... , june)

    # gets users input for month
    month = input('Choose month \n').lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while month not in months and month != 'all':
       print('Wrong input. Please choose correct month')
       month= ''
       month = input('Choose month \n')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    # gets users input for day
    day = input('Choose day of week \n').lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days and day != 'all':
       print('Wrong input. Please choose correct day of week')
       day = ''
       day = input('Choose day of week \n')


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
    df = pd.read_csv(CITY_DATA[city])
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    # converts start time into date
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extracts month from start time
    df['month'] = df['Start Time'].dt.month
    #extracts day of week from start time
    df['week_day'] = df['Start Time'].dt.weekday_name

    # finds month in the month array and filters dataframe by month
    if month != 'all':
        month_num = months.index(month)+1
        df = df[df['month'] == month_num]

    #filters dataframe by day
    if day != 'all':
        df = df[df['week_day'] == day.title()]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    # finds the most common month
    if month == 'all':
        common_month = months[df['month'].mode()[0]-1].title()
        print('Most common month of travel: {}'.format(common_month))
    else:
        common_month = months[df['month'].mode()[0]-1].title()
        print('You have chosen a single month: {}'.format(common_month))

    # TO DO: display the most common day of week

    # finds the most common day of the week
    if day == 'all':
        common_day = df['week_day'].mode()[0]
        print('Most common day of travel: {}'.format(common_day))
    else:
        common_day = df['week_day'].mode()[0]
        print('You have chosen a single day: {}'.format(common_day))

    # TO DO: display the most common start hour

    # finds the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['start_hour'] = df['Start Time'].dt.hour
    common_hour = df['start_hour'].mode()[0]
    print('Most common hour of travel: {}'.format(common_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # finds most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most common start station: {}'.format(start_station))

    # TO DO: display most commonly used end station

     # finds most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most common end station: {}'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip

    # finds most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + '/' + df['End Station']
    freq_combination = df['Station Combination'].mode()[0]
    print ('Most frequent station combination: {}'.format(freq_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    #finds total travel time in hours
    total_travel_time = (df['Trip Duration'].sum())/3600
    print('Total travel time: {} hours'.format(total_travel_time))

    # TO DO: display mean travel time

     #finds mean travel time in minutes
    mean_travel_time = round((df['Trip Duration'].mean()) / 60,0)
    print('Mean travel time: {} min'. format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # finds count of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types: {}'. format(user_types))

    # TO DO: Display counts of gender

    # finds count of gender
    if city == 'washington':
        print('No gender data available')
    else:
        gender_types = df['Gender'].value_counts()
        print('Count of gender: {}'.format(gender_types))


    # TO DO: Display earliest, most recent, and most common year of birth

    # finds birth data
    if city == 'washington':
        print('No birth year data available')
    else:
        earliest_birth = df['Birth Year'].min()
        print('Earliest year of birth {}'.format(earliest_birth))
        recent_birth = df['Birth Year'].max()
        print('Most recent year of birth {}'.format(recent_birth))
        common_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth {}'.format(common_birth))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        #shows user raw data
        raw_data = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
        lower_row = 0
        upper_row = 5
        while raw_data == 'yes':
            print(df.iloc[lower_row:upper_row])
            lower_row += 5
            upper_row += 5
            raw_data = ''
            raw_data = input('\nWould you like to see next five rows of raw data? Enter yes or no.\n').lower()





        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
