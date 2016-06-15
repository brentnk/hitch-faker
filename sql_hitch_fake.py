from faker import Faker
import random as r
import numpy as np
from datetime import date
import argparse

fk = Faker()

user_roles = 'client driver partner'.split()
trips_status = 'completed;cancelled_by_driver;cancelled_by_client'.split(';')
devices = 'android iphone sms mobile_web'.split()

def fake_it(n_users=10, n_trips=500):
    users = []

    def r_user(u_ct):
        user = {}
        user['userid'] = u_ct
        user['email']  = fk.email()
        user['firstname'] = fk.first_name().replace('\'', '\'\'')
        user['lastname']  = fk.last_name().replace('\'', '\'\'')
        user['banned'] = r.randint(0,10)
        user['role'] = np.random.choice(user_roles)
        user['creationtime'] = fk.date_time_between_dates(datetime_start=date(2013, 1, 1), datetime_end=date(2014,1,1))
        return user

    users = [r_user(a) for a in range(n_users)]

    client = [a for a in users if a['role'] == 'client']
    driver = [a for a in users if a['role'] == 'driver']
    partner= [a for a in users if a['role'] == 'partner']

    def r_trip(users, client, driver, partner, t_ct):
        trip = {}
        trip['id'] = t_ct
        trip['client_id'] = np.random.choice(client)['userid']
        trip['driver_id'] = np.random.choice(driver)['userid']
        trip['request_device'] = np.random.choice(devices)
        trip['status'] = np.random.choice(trips_status)
        trip['city_id'] = r.randint(0,10)
        trip['request_at'] = fk.date_time_between_dates(datetime_start=date(2013, 1, 1), datetime_end=date(2014,1, 1)) 
        return trip
    trips = [r_trip(users, client, driver, partner, a) for a in range(n_trips)]
        
    return users, trips

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate sql for user_trips dataset')
    parser.add_argument('--user-count', '-u', required=True, type=int, dest='user_count')
    parser.add_argument('--trip-count', '-t', required=True, type=int, dest='trip_count')

    args = parser.parse_args()
    print(args.user_count, args.trip_count)
    users , trips = fake_it(args.user_count, args.trip_count)

    user_del = 'delete from users;\n'
    user_ins = 'insert into users(usersid, email, firstname, lastname, banned, role, creationtime) values\n'
    user_str = ['''({0}, '{1}', '{2}', '{3}', {4}, '{5}', '{6}'),\n'''.format(u['userid'], u['email'], u['firstname'], u['lastname'], u['banned'] >= 8, u['role'], u['creationtime']) for u in users]
    user_str[-1] = user_str[-1][:-2]
    user_str.append(';\n')

    trip_del = 'delete from trips;\n'
    trip_ins = 'insert into trips(id, client_id, driver_id, request_device, status, city_id, request_at) values\n'
    trip_str = ['''({0}, {1}, {2}, '{3}', '{4}', {5}, '{6}'),\n'''.format(u['id'], u['client_id'], u['driver_id'], u['request_device'], u['status'], u['city_id'], u['request_at']) for u in trips]
    trip_str[-1] = trip_str[-1][:-2]
    trip_str.append(';\n')

    with open('./user_trip.data.sql', 'w+') as f:
        f.write(user_del)
        f.write(user_ins)
        f.writelines(user_str)

        f.write(trip_del)
        f.write(trip_ins)
        f.writelines(trip_str)

        f.flush()
        f.close()
