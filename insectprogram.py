import InsectClass as i

housefly = i.Insect(2,4)
mosquito = i.Insect(6,8)

housefly.flight_length()
mosquito.flight_length()

print("The length of the Housefly's flight is", housefly.get_flight(), 'miles.')
print("The length of the Mosquito's flight is", mosquito.get_flight(), 'miles.')

