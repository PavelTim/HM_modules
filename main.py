import emoji

import application.salary
import application.db.people as adp
import datetime


if __name__ == '__main__':
    print('now', datetime.datetime.now().date())
    print(application.salary.calculate_salary())

    print('today', datetime.datetime.today().date())
    print(adp.get_employees())
    # print(emoji.emojize(':thumbs_up:'))
    # print(emoji.emojize(':red_heart:'))