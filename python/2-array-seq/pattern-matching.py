
# Handling incoming message that is encoded as BEEPER 440 3.
class Robot:
    def handle_command(self, message):
        match message:

            case ['BEEPER', frequency, times]: # match sequence with 3 items, starting in 'BEEPER'
                self.beep(times, frequency)
            
            case ['NECK', angle]: # match any 2 items
                self.rotate_neck(angle)

            case ['LED', ident, intensity]: # match 3 items starting in "LED"
                self.leds[ident].set_brightness(ident, intensity)

            # .... 

            case _:
                raise TypeError(message)


# Destructuring (more advaced form of unpacking)
"""
Unlike unpacking, patterns don't destructure iterables that are not sequences (like iterators)

In standard library, 
* list, memoryview, array.array, tuple, range, collections.deque are compatible with sequence pattern
"""
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

            # .... OR 

            case [name, _, _, (lat, lon) as coord]: # Use of as 

            # .... OR 

            # str(), float() is not constructor call HERE! 
            # In sequence pattern, these are just runtime type checker
            # It helps to match with the pattern! 
            case [str(name), _, _, (float(lat), float(lon))]:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

            # .... OR 

            # *_ takes any number of items without binding to variable
            case [str(name), *_, (float(lat), float(lon))]: 