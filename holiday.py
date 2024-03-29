# this program is called holiday.py
# the program ask one to enter the city name for their holiday,
# no. of days will spend in a hotel
# and the no. of days of renting a car
# using the above information, it would calculate the total cost of the holiday.


print('Hello, welcome to your best holiday calculator')

# The following is a city of list one should choose from
print("""
Choose from the options below the city you would love to visit:
1. nairobi
2. bali
3. bora bora
4. zanzibar
""")


while True:
    city_flight = input("Please enter the city of your choice: ").lower()

    if city_flight not in ['nairobi', 'bali', 'bora bora', 'zanzibar']:
        print('invalid choice. Please choose from the list given')
        continue
    else:
        break

num_nights = int(input("Please enter the number of nights you'll spend in a hotel: "))
rental_days = int(input("Please enter the number of days you'll rent a car: "))

# the function below calculate the hotel cost
def hotel_cost(x, y):
    z = x * y
    return(z)


total_cost = hotel_cost(x= num_nights, y = 60)

print(f'Your hotel charges would be: £{total_cost}.')

# the function below calculates the plane cost
def plane_cost(a = city_flight):
    price = 0
    if a == 'nairobi':
        price = 100
    elif a == 'bali':
        price = 80
    elif a == 'zanzibar':
        price = 120
    elif a == 'bora bora':
        price = 60
    else:
        print('Please choose from the options given!')

    return price


flight_cost = plane_cost()

print(f'Your flight would be: £{flight_cost}')

# The function below calculates the car rental cost
def car_rental(b,c):
    car_cost = b * c
    return(car_cost)


total_car_cost = car_rental(b= rental_days, c = 50 )
print(f'your car rental cost would be: £{total_car_cost}')

# This function calculates the total holiday cost
def holiday_cost(x,y,z):
    all_cost = x + y + z
    return(all_cost)


all_in_total = hotel_cost(x= num_nights, y = 60) + plane_cost() + car_rental(b= rental_days, c = 50 )

print(f'The total amount you will need for your holiday is:£{all_in_total}')






