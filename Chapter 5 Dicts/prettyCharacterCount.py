#Loop over each character in message and add count to dict
import pprint
message = 'It was a brigth cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) # setdefault() ensurs that the key is in count
    count[character] = count[character] + 1

pprint.pprint(count)

