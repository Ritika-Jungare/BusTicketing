from datetime import datetime

# Sample data
bus_routes = {
    1: {
        'source': 'Nagpur',
        'destination': 'Mumbai',
        'departure_time': datetime(2023, 6, 5, 10, 0),
        'seats_available': 20,
        'fare': 100.0
    },
    2: {
        'source': 'Mumbai',
        'destination': 'Pune',
        'departure_time': datetime(2023, 6, 6, 9, 0),
        'seats_available': 15,
        'fare': 12.5
    },
    # Add more bus routes as needed
}

bookings = []

def display_available_routes():
    print("Available Bus Routes:")
    for route_id, route_info in bus_routes.items():
        if route_info['seats_available'] > 0:
            print(f"Route ID: {route_id}")
            print(f"Source: {route_info['source']}")
            print(f"Destination: {route_info['destination']}")
            print(f"Departure Time: {route_info['departure_time']}")
            print(f"Seats Available: {route_info['seats_available']}")
            print(f"Fare: {route_info['fare']}")
            print("-" * 30)

def book_bus(route_id, num_seats):
    if route_id in bus_routes:
        route = bus_routes[route_id]
        if route['seats_available'] >= num_seats:
            route['seats_available'] -= num_seats
            booking = {
                'route_id': route_id,
                'source': route['source'],
                'destination': route['destination'],
                'departure_time': route['departure_time'],
                'num_seats': num_seats,
                'total_fare': route['fare'] * num_seats
            }
            bookings.append(booking)
            print("Booking successful!")
            print(f"Booking ID: {len(bookings)}")
            print(f"Source: {route['source']}")
            print(f"Destination: {route['destination']}")
            print(f"Departure Time: {route['departure_time']}")
            print(f"Number of Seats: {num_seats}")
            print(f"Total Fare: {booking['total_fare']}")
        else:
            print("Not enough seats available on this route.")
    else:
        print("Invalid route ID.")

# Sample usage
display_available_routes()
book_bus(1, 2)