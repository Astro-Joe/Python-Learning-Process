guests = ['debbie', 'sammie', 'eniola']
for guest in guests:
    print(guest.title() + ", I'm inviting you for dinner.")


popped_guest = guests.pop()
print('\n' + popped_guest.title() + " couldn't make it for dinner.\n")
guests.append('jerry')
for new_guest in guests:
    print(new_guest.title() + ", I'm inviting you for dinner.")


print('\nI just found a bigger table, so we\'re going to have more company.\n')
guests.insert(0, 'israel')
guests.insert(2, 'moyin')
guests.append('darrell')
for latest_guest in guests:
    print(latest_guest.title() + ", I'm inviting you for dinner.")

print('\nIt seems our table won\'t arrive on time.\nSo I can only invite two guests.\n')
removed_guest = []
removed_guest_1 = guests.pop(0)
removed_guest.append(removed_guest_1)

removed_guest_2 = guests.pop(1)
removed_guest.append(removed_guest_2)

removed_guest_3 = guests.pop(2)
removed_guest.append(removed_guest_3)

removed_guest_4 = guests.pop(2)
removed_guest.append(removed_guest_4)

for peeps in removed_guest:
    print(peeps.title() + ' I can\'t invite you to dinner.\nPlan\'s changed.\n')
print("I'm inviting " + str(len(guests)) + ' guests for dinner.')
#del guests[0]
#del guests[0]
#print(guests)