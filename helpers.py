from datetime import datetime, timedelta
import logtastic as logg
import random

def generate_times(time_string):
    print("..Generating times..")
    
    # Convert timestamp to date obj
    start_time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%f%z")
    logg.er("DEBUG", f'Got start time "{start_time}", Curr time: ""')
    
    # Get current timestamp, add timezone information to data object
    current_timestamp = datetime.now()
    format_string = "%Y-%m-%dT%H:%M:%S.%f"
    ct_string = current_timestamp.strftime(format_string)
    ct_string_with_tz = ct_string + "-0700"
    # print("CT as string with tz", ct_string_with_tz)
    current_timestamp_tz = datetime.strptime(ct_string_with_tz, "%Y-%m-%dT%H:%M:%S.%f%z")
    
    # print(f'Current datetime with tz: {current_timestamp_tz}')
    
    # Get random date between two timestamps
    diff = current_timestamp_tz - start_time
    int_delta = (diff.days * 24 * 60 * 60) + diff.seconds
    random_second = random.randrange(int_delta)
    randy = start_time + timedelta(seconds=random_second)
    # print("INT DELTA", int_delta, "RAND SECOND:", random_second, "RANDY:", randy)
    
    # return timestamp as datetime obj
    return randy
    

def get_timestamps(start_date, total_commits):
    print("..Getting timestamps..")
    timestamp_list = []
    for x in range(total_commits):
        timestamp_list.append(generate_times(start_date))
    
    def sort_by_datetime(dt):
        return dt
    
    # print("ORIG TIMESTAMP LIST", timestamp_list)
    # sorted_timestamps = timestamp_list.sort()
    sorted_timestamps = sorted(timestamp_list, key=sort_by_datetime)
    
    # CONVERT SORTED LIST TO STRINGS
    sorted_timestamps_as_str = []
    datetime_to_str_regex = "%Y-%m-%dT%H:%M:%S.%f%z"
    for x in sorted_timestamps:
        sorted_timestamps_as_str.append(x.strftime(datetime_to_str_regex))
    
    print("FORMATTED AS STR:", sorted_timestamps_as_str)
    
    return sorted_timestamps_as_str