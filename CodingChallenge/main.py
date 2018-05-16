from shoe import Shoe

def main(path):
    shoe_file = open(path,'r').readlines()


    matchers = ['heel','toe','padded']
    matching = [s for s in shoe_file if any(xs in s for xs in matchers)]
    materials = shoe_file[shoe_file.index('Materials\n')+1]

    #Length is static just for the challenge
    #Can change it to apply to many cases
    if(len(matching) == 3):
        shoe = Shoe(matching[0].strip('-'),matching[1].strip('-'),materials.strip('\n'))
        print (shoe)

    if(len(matching) == 4):
        shoe = Shoe(matching[0].strip('-'),matching[2].strip('-'), materials,matching[1].strip('-').strip('\n'))
        print(shoe)

path_1 = '/Users/Cesar-Melchor/Documents/Meetup/CodingChallenge/shoes/shoe1.txt'
path_2 = '/Users/Cesar-Melchor/Documents/Meetup/CodingChallenge/shoes/shoe2.txt'
path_3 = '/Users/Cesar-Melchor/Documents/Meetup/CodingChallenge/shoes/shoe3.txt'

main(path_1)
main(path_2)
main(path_3)