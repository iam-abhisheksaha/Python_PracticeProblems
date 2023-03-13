# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    first_letter = name[0]
    inbetween=name[1:3]
    fourth_letter = name[3]
    remainings = name[4:]

    return first_letter.upper() + inbetween+fourth_letter.upper() +remainings


print(old_macdonald('macdonald'))