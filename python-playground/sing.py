def sing(num_bottles):
    #TODO: Add your code to achieve the desired output and pass the challenge. 
    #NOTE: The f String method of String Interpolation does not work. 
    
    output = []
    for n in reversed(range(num_bottles + 1)):
        if(n == 0) :
            break;
        output.append('{} bottles of beer on the wall, {} bottles of beer.'.format(n, n))
        output.append('Take one down and pass it around, {} bottles of beer on the wall.'.format(n - 1))
        output.append('');
        
    return output

print(sing(9))