import  datetime
from background.models import Flight
from background.views import produce_flight_from_date_to_date

if __name__ == '__main__':
    flight_number = 'CN1234'
    flight = Flight.objects.get(flight_number=flight_number)
    xday=datetime.timedelta(days=10)
    next_day = datetime.date.today() + xday
    produce_flight_from_date_to_date(flight,datetime.date.today,next_day)