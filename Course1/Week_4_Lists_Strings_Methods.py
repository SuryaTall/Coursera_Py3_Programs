#Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2,'horseback riding')

#Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
for i in trav_dest:
    if i == 'London':
        trav_dest.remove(i)
#This shows an error on Github, but works in the Runestone Environment

#Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append('Guadalajara')