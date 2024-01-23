# initialize some variables and give values to them

place = "Pune, hinjewadi"
experience = 2
company = "HCL Tech"

# All below print statements print same output

print("My place is " + place + ". I have around", experience, "years of experience at " + company)

print("My place is {}. I have around {} years of experience at {}".format(place, experience, company))

print("My place is {0}. I have around {1} years of experience at {2}".format(place, experience, company))

print("My place is {2}. I have around {1} years of experience at {0}".format(company, experience, place))

print("My place is %s. I have around %d years of experience at %s" % (place, experience, company))

_________________________________________________________________________________________________________________________
'''
output :- 
My place is Pune, hinjewadi. I have around 2 years of experience at HCL Tech
My place is Pune, hinjewadi. I have around 2 years of experience at HCL Tech
My place is Pune, hinjewadi. I have around 2 years of experience at HCL Tech
My place is Pune, hinjewadi. I have around 2 years of experience at HCL Tech
My place is Pune, hinjewadi. I have around 2 years of experience at HCL Tech
'''
