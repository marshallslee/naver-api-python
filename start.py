from geocode.geocode import get_latitude_and_longitude_by_address


def run():
    latitude, longitude = get_latitude_and_longitude_by_address()
    if latitude and longitude is not None:
        print("Latitude: {}, Longitude: {}".format(latitude, longitude))
    else:
        print("Cannot calculate latitude and longitude from the given address.")
    return


if __name__ == '__main__':
    run()
