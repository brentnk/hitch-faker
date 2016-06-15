select *
from trips
where status = 'completed'
  and request_device = 'iphone' -- 'android'
  and request_at >= '2013-12-1 10:00:00'
  and request_at <= '2013-12-8 17:00:00';

select users.firstname, count(usersid) count_usersid, count(*) count_trips 
from users
join(
select * from trips where city_id = 8 and EXTRACT(month from request_at) = 10) sub
on users.usersid = sub.client_id
where not users.banned
group by users.usersid, users.firstname;


select * 
from users as rider
join trips on rider.usersid = trips.client_id 
  and trips.request_at >= '2013-9-10'
  and trips.request_at <= '2013-9-20'
  and trips.city_id = 8
join users as driver on trips.driver_id = driver.usersid
  and driver.banned
  and driver.creationtime >= '2013-9-01'
  and driver.creationtime <= '2013-9-10'
where not rider.banned;
