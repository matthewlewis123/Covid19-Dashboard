#This function converts minutes to seconds.
def minutes_to_seconds( minutes: str ) -> int:
      return int(minutes)*60

#This function converts hours to minutes
def hours_to_minutes( hours: str ) -> int:
      return int(hours)*60

#This function converts hours:minutes to seconds
def hhmm_to_seconds( hhmm: str ) -> int:
      if len(hhmm.split(':')) != 2:
          print('Incorrect format. Argument must be formatted as HH:MM')
          return None
      return minutes_to_seconds(hours_to_minutes(hhmm.split(':')[0])) + \
          minutes_to_seconds(hhmm.split(':')[1])

#This function converts hours:minutes:seconds to seconds
def hhmmss_to_seconds( hhmmss: str ) -> int:
      if len(hhmmss.split(':')) != 3:
          print('Incorrect format. Argument must be formatted as HH:MM:SS')
          return None
      return minutes_to_seconds(hours_to_minutes(hhmmss.split(':')[0])) + \
          minutes_to_seconds(hhmmss.split(':')[1]) + int(hhmmss.split(':')[2])


