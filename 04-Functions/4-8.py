##Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23) and the number of minutes (0..59), 
# returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time).

#Then write a program that tests whether the function works correctly.


#time_string(15, 38, '24') returns '15:38'
#time_string(8, 3, '24') returns '08:03'
#time_string(0, 5 '24') returns '00:05'
#time_string(11, 15, '12') returns '11:15am'
#time_string(0, 7, '12') returns '12:07am'
#time_string(7, 30, '12') returns '7:30am'
#time_string(12, 46, '12') returns '12:46pm'
#time_string(13, 10, '12') returns '1:10pm'
#time_string(19, 02, '12') returns '7:02pm'

def time_string(hours, minutes, time_format):
    
    if 0 <= hours <= 23 and 0<= minutes <= 59:
        if time_format == 12:
            if hours <= 11:
                syntax = 'am'
                hours_12 = hours
                if minutes <10:
                    minutes = f'0{minutes}'
                else:
                    minutes = minutes
                time = f'{hours_12}:{minutes}{syntax}'
            elif hours == 12:
                syntax = 'pm'
                hours = hours
                if minutes <10:
                    minutes = f'0{minutes}'
                else:
                    minutes = minutes
                time = f'{hours}:{minutes}{syntax}'
            elif hours == 24:
                syntax = 'am'
                hours_12 = 00
                if minutes <10:
                    minutes = f'0{minutes}'
                else:
                    minutes = minutes
                time = f'{hours_12}:{minutes}{syntax}'
            else:
                syntax = 'pm'
                hours_12 = hours - 12
                if minutes <10:
                    minutes = f'0{minutes}'
                else:
                    minutes = minutes
                time = f'{hours_12}:{minutes}{syntax}'
        if time_format == 24:
            hours = hours
            if minutes <10:
                    minutes = f'0{minutes}'
            else:
                    minutes = minutes
            time = f'{hours}:{minutes}'
    return time


result = time_string(19,2,12)
final = print(f'your time is {result}')