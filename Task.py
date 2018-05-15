import sys
import requests
import datetime
import calendar
import configparser
import os


class Task(object):
    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "zoho.conf")
        config.read(config_file_path)
        self.authtoken =config.get('zoho_parameters', 'authtoken')
        self.user_id = config.get('zoho_parameters', 'user_id')
        self.base_url = "https://projectsapi.zoho.com/restapi/"
        self.portal_id = "632377220"
        self.project_id = config.get('zoho_parameters', 'project_id')
        self.task_id = config.get('zoho_parameters', 'task_id')
        self.add_task_url = "{}portal/{}/projects/{}/tasks/{}/logs/"\
            .format(self.base_url, self.portal_id, self.project_id, self.task_id)

    def add_task(self, month, days_to_skip):
        today = datetime.date.today()
        year = today.year
        num_days = calendar.monthrange(year, month)[1]
        days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]

        for day in days:
            week_day = datetime.date.weekday(day)
            if week_day < 5 and (days_to_skip is None or day.day not in days_to_skip):
                params = {
                    "authtoken": self.authtoken,
                    "date": day.strftime('%m-%d-%Y'),
                    "owner": self.user_id,
                    "bill_status": "Billable",
                    "hours": 8,
                    "notes": "development"
                }
                response = requests.post(self.add_task_url, params=params)
                if response.status_code == 201:
                    print("8 hours added for date {}".format(day.strftime('%m-%d-%Y')))
                else:
                    print("Failed adding hours for {}. Error message: {}"
                          .format(day.strftime('%m-%d-%Y'), response.text))


if __name__ == "__main__":
    month = None
    days_to_skip = []
    try:
        for item in sys.argv:
            month = int(item) if month is None else month
            days_to_skip.append(int(item))
    except Exception as e:
        print("Enter valid parameters!\nYou need to enter: Month, Days To Skip\nExample 1: 5\nExample 2: 5 , 1, 2, 3")

    if month:
        task = Task()
        task.add_task(month, days_to_skip)
