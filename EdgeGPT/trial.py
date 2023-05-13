from ast import literal_eval

a = """[
    ['French Speaking Countries', ['Belgium', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Djibouti', 'Equatorial Guinea', 'France', 'Gabon', 'Guinea', 'Haiti', 'Ivory Coast', 'Luxembourg', 'Madagascar', 'Mali', 'Monaco', 'Niger', 'Republic of the Congo', 'Rwanda', 'Senegal', 'Seychelles', 'Switzerland', 'Togo']]
    ,['Spanish Speaking Countries', ['Argentina','Bolivia','Chile','Colombia','Costa Rica','Cuba','Dominican Republic','Ecuador','El Salvador','Equatorial Guinea','Guatemala','Honduras','Mexico','Nicaragua','Panama','Paraguay','Peru','Puerto Rico','Spain','Uruguay','Venezuela']]]"""

rq = literal_eval(a)

for to_add in rq:
    print( to_add[0],to_add[1] )