import datetime
import pytz

dt = datetime.datetime(2023,3,24,12,30,45,tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC) #returns current local timezone of none
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
print(dt_now)

