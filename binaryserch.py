list = [34,67,23,90,12,88,96,34,56,12,566,34]
list.sort()
print(list)

user_input = int(input('Enter a number..'))

low = 0
high = len(list) - 1

def binary_serch(list,low,high):
    mid = (low + high)//2

    while list[low] <= list[high]:
        if user_input == list[mid]:
            return mid
        
        elif user_input > list[mid]:
            return binary_serch(list, mid+1 ,high)

        else:
            return binary_serch(list, low , mid-1)

serch = binary_serch(list,low,high)
print(serch)