import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC) #returns current local timezone of none
print(dt_utcnow)

dt_now = datetime.datetime.now()
dt_east = dt_now.astimezone(pytz.timezone('US/Eastern'))
centaral_tx = pytz.timezone('US/Central')

dt_now = centaral_tx.localize(dt_now)
print(dt_now)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)


