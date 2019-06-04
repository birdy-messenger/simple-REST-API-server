from random import randint

first_names = "Ilya Seva Sasha Masha Alex Vladimir Tanya Kostya".split()
second_names = "Ivanov Popov Aukhertlischt Matterhorn Reyou Kiroi".split()
ages = [x for x in range(14, 35)]

ids = set()
def generateID():
	ID = randint(10e4, 10e5 - 1)
	while ID in ids:
		ID = randint(10e4, 10e5 - 1)

	ids.add(ID)
	return ID



def generate_person():
	one_of = lambda arr: arr[randint(0, len(arr)-1)]



	return {"name": one_of(first_names),
			"surname": one_of(second_names),
			"age": one_of(ages),
			"id": generateID()
		   }


def print_person(person):
	return "@%s   %s %s   %dy.o." % (person["id"], person["name"], person["surname"], person["age"])