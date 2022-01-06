
# The ride-hailing application 
### Introduction
##### 1. Overview
The application provides ride-hailing application for people in the South-East Asia. The application has two main kind of users which are Riders who find the taxis and Drivers who have car and provide taxi service.
##### 2. Estimate the number of users in app
- Rider: 
  - 100 millions riders in total
  - 20 millions active users per month
  - Each rider use the service 15 times per month
- Driver:
    - 2 millions drivers in total
    - 400,000 active driver per month
### System components
[![build](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Overview.png)](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Overview.png)
#### 1. Driver locations
[![driverLocation](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/driver%20location.png)](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/driver%20location.png)

- Driver's database

    | Column | Type |
    | ------ | ------ |
    | latitude | float |
    | longitude | float |
    | driverID | uuid |
- Throughput
    - 400,000 active drivers
    - Average shift: 6 hours
    - 150,000 drivers at every moment
    - Message requests for the driver's location every 5 seconds
    - 30,000 requests per second (60,000 requests per second on the peak)
#### 2. Storing locations
[![Storing locations](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Database%20for%20locator.png)](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Database%20for%20locator.png)

#### 3. Find the taxis around
[![Storing locations](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Taxi%20around.png)](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Taxi%20around.png)

- Rider perspective
    - Display 15 nearest driver at most
    - Refresh the driver location at every 5 seconds
- Throughput
    - 20 millions active Rider per day
    - Each user open app 3 times per day = 60 millions opens a day
    - Refresh every 5 second
    - Each seesion of a Rider is 3 minutes = 2.1 billions request per day = 8,700 requests per second
#### 4. Matching service
[![Storing locations](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Matching%20service.png)](https://github.com/BachQuang/SkyMavis_Test/blob/master/2.%20System%20design/Images/Matching%20service.png)

### Discussion
#### 1. Bottleneck
- Database sharding by city:
    - Some of the big cite (ex: Hanoi, Ho Chi Minh, Bangkok...) would have more user and driver than other cities. Therefore, the system in these places have more throughput and sometimes can cause delivery the requests slower.
- Too many of user in rush hour(5p.m to 7p.m). In rush hour the number of users is higher two or three times than causual day.
