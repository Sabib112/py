import array as arr

array_num=arr.array('i',[1,2,3,5,3,6,8,9,4,8])
print("Original array: ",str(array_num))

print ('count of the array: '+str(array_num.count(3)))

array_num.reverse()
print("Reverse the array: ",str(array_num))

int_array = arr.array('i', [1, 2, 3, 3, 4])
print('integer array: ', int_array)

print('first element: ',int_array[0])
print('last element: ',int_array[-1])

int_array[2]=10
print('modified array: ',int_array)


int_array.append(6)
print('array after appending 6: ',int_array)

int_array.remove(4)
print('array after removing 4: ',int_array)

slice_array = int_array[1:4]
print('sliced array (1:4): ',slice_array)

print('length of the array: ',len(int_array))

print('iterate of the array: ')
for element in int_array:
    print(element)

array_list=int_array.tolist()
print('convert array to list: ',array_list)