#1.a Create a list of integers no fewer than 10 items from 0 to 9.
one_a = [0,1,2,3,4,5,6,7,8,9]

#1.b Add 3 to the 5th indexed element.
one_b = [0,1,2,3,4,5,6,7,8,9]
one_b[5]+=3
#This instruction should add 3 to the fifth integer without affecting any other integer.

#1.c Coerce all elements in the list to floats using list comprehension.
one_c = [float(i) for i in one_b]
#This should change all the elements from one_b into floats. 

#1.d Coerce the list to a set
one_d = set(one_c)
#This should change the elements of one_c into a set, 
#which should also delete the fifth integer, since there are two 8's now. 

#1.e Using a method, append int 10 to the set
one_d.add(10)
#This should add the integer of 10 to the set we've labeled one_e. 

#1.f Using a method, pop an item from the set
one_f_popped = one_d.pop()
#By using the pop() function, we should be able to pull a random value from the set, 
#and isolate it as popped_item

#1.g Using a length counting function, count the number of items in the set.
#I was getting an error while doing this that one_a was undefined, 
# so I put all the inputs in again here and it seemed to fix it
one_a = [0,1,2,3,4,5,6,7,8,9] #answer for 1.a
one_a[5]+=3 #answer for 1.b
one_g = [float(i) for i in one_a] ####################
one_g = set(one_a)
one_g.add(10)
one_g.pop()
number_of_items = len(one_g)
#When we go through these steps, it gives us a length of 9 in the number_of_items set.

#1.h Check if the number of items in the set is the same as the number of items in the list.
one_h_same_length = len(one_g) == len(one_a)
#This command should compare the length of the two lists.
#Given that the original list was ten integers, they are not the same length.

#1.i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
set_as_list = list(one_g)
combined_list = one_a + set_as_list

#1.j Coerce 1.i to a set
combined_set = set(combined_list) 

#1.k Count the number of elements in the 1.j
number_of_elements_in_combined_set = len(combined_set)
#This should count all the values in our new combined set

#2.a Combine the three sample dictionaries (given below) into a nested dictionary
#(nested in programming means joined), named two_a, 
#ensure the key names are the same as the dictionary names.
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

#Once we have our sample dictionaries, we can combine them into a nested dictionary:
wo_a ={
    'two_patient_dictionary_kinoko': two_patient_dictionary_kinoko,
    'two_patient_dictionary_dango': two_patient_dictionary_dango,
    'two_patient_dictionary_mochi' : two_patient_dictionary_mochi
}

#2.b Using keys, retrieve the Dango's name from 2.a
dango_name = wo_a ['two_patient_dictionary_dango']['name']
# dango_name is now defined by what we've pulled from the two_patient dictionary.

#2.c Using keys, update the value of Mochi's year to 2018. This should not be a variable and should simply update 2.a.

wo_a['two_patient_dictionary_mochi']['year'] = 2018
#This should change the year value for Mochi from 2020 to 2018.

#2.d Manually create a dictionary that has a single level and contains each patient as the key and the year as the value. Set Mochi's year to 2019.'

patients_years = {
    'Kinoko': 2021,
    'Dango': 2019,
    'Mochi': 2019 
}

#since we're making this dictionary manually, we can set the new value for Mochi to 2018
#as we create it.

#2.e Coerce the keys of 2.d into a list

patient_names_list = list(patients_years.keys()) 

#2.f Coerce the values of 2.d into a list

patient_years_list = list(patients_years.values())

#We change the values of problem 2.d here into a new list.

#2.g Use the zip function to combine 2.e and 2.f into a dictionary again
patient_names_list = list(patients_years.keys()) 

combined_dict = dict(zip(patient_names_list, patient_years_list))

#3.a Is set E a subset of set A

#first we load our subsets
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}
#once we have our sets loaded, we can answer our question using the method: .issubset

is_E_subset_of_A = three_setE.issubset(three_setA)

#3.b Is set E a strict subset of set A

is_E_strict_subset_of_A = three_setE.issubset(three_setA) and three_setE !=three_setA
#The first part of the equation confirms if all elements of three_setE are in three_setA, and the second part checks to see if they're identitcal or not. In order for it to be a strict subset, both have to be true.

print(is_E_strict_subset_of_A)

#3.c Create a set that is the intersection of set A and set B

intersection_A_B = three_setA.intersection(three_setB)
#This method should give us where these two sets overlap and intersect.

print(intersection_A_B)

#3.d Create a set that is the union of sets C, D and E

union_C_D_E = three_setC.union(three_setD, three_setE)
#Using the union method, we should be able to create a new set that 
#has all the values of sets C, D, and E.

#3.e Add 9 to the set

union_C_D_E.add(9)

#There was already a 9 in the union we created in 3.d, so union_C_D_E should remain the same

#3.f Using == compare this set to the list in one_a

one_a = [0,1,2,3,4,5,6,7,8,9]
set_one_a = set(one_a)

#First, we need to make list one_a into a set.

three_f_are_sets_equal = union_C_D_E == set_one_a

#since the data from 1.a starts at 0, we should get False as the answer

#3.g Explain why they are not the same. What would you need to change if you wanted this to be True?

#As mentioned in the previous problem, one_a starts at 0, while union_C_D_E starts at 1.
#If we wanted to make them equal, we need to do the following:

union_C_D_E.add(0)
#With the added 0, the two sets now match. Now we just repeat the final step of  3.f

three_g_are_sets_equal = union_C_D_E == set_one_a

#4.a Create a variable of type int with the value of 8

four_a = 8

type_list = []

type_list.append(type(four_a)) 

# 4.b Create an empty list.

four_b= [ ]

type_list.append(type(four_b))

#4.c Using type(), add the type of 4.a to this list.

type_list.append(type(four_a))#?

#4.d Add 0.39 to 4.c

four_a += 0.39 

#4.e append the type of 0.39 to the list.

type_list.append(type(four_a))

#4.f exponentiate to the -10, ie: 4.d^-10,round it to no decimal places, and append to list.

four_a= round(four_a ** -10)

#4.g append the type to the list.

type_list.append(type(four_a))

#5.a Manually create a dictionary... 

five_a = {index:value for index, value in enumerate (type_list)}
print(five_a)

#5.b Add 300 and coerce it into a string.

three_hundred_str = str(300)

#5.c append the type to the list.

type_list.append(type(three_hundred_str))

#5.d Slice the string up to the 2nd element

sliced_string = three_hundred_str[:2]

#5.e Append the type of sliced string to the list

type_list.append(type (sliced_string))

#5.f Use list comprehension to convert this into a new list of integers

new_integer_list = [int(char) for char in sliced_string]

#5.g append the type to the list
type_list.append(type(new_integer_list))

#5.h append the type of three_setA to the list.

type_list.append(type(three_setA))
