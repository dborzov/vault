import datetime
datetime.datetime.strptime(self.args['from_date'], "%Y-%m-%d")
datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

# tomorrow
datetime.datetime.now() + datetime.timedelta(days=1)