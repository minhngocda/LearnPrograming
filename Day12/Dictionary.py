def firstFunc():
    alien_0 = {'color': 'green', 'point': 5}
    print(alien_0['color'])
    new_point = alien_0['point']
    print("You just earned " + str(new_point) + " points!")
    print(alien_0)
    #to put more key-value in a dictionary, also put in a empy one, like alien_0={}
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)
    #to modify a value in a dictionary
    alien_0['color'] = 'yellow'
    print(alien_0)

def secondFunc() :
    alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
    print("Original x-position: " + str(alien_0['x_position']))
    alien_0['speed']= 'fast'
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
    # This must be a fast alien.
        x_increment = 3
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print("New x-position: " + str(alien_0['x_position']))   
secondFunc()  
firstFunc() 




 