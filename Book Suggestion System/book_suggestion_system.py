import random

books = ["The Hobbit", "The Mystery", "Animal Farm", "Brave Kingdom", "The Crash"]


def books_archive ():

	return books


def output_books_in_shelve():
	counter = 1
	for book in books_archive():

		print(f"{counter}. {book}")
		counter += 1


def add_books_to_archive(title):

	books_archive().append(title)


def remove_from_archive(title):

	books_archive().remove(title)


def suggest_book_title():

	return random.choices(books_archive(), k = 1)[0]


def suggest_page_number():

	return random.randint(1, 101)


back_to_menu = True

while (back_to_menu):
	main_menu = """

	Welcome to the Book Suggestion System!

	1. Get Suggestions
	2. Add Book
	3. Remove Book
	4. Update Book
	5. Show all books

	"""

	print(main_menu)

	main_menu_option = int(input("Enter Operation: "))

	match (main_menu_option):

		case 1:
			print("Book for the Day:")
			print(f"\tBook Title: {suggest_book_title()}")
			print(f"\tPage: {suggest_page_number()}\n")

			repetition = input("Would you like to get another suggestion? (yes/no): ")

			while (repetition.lower() == "yes"):

				print("Book for the Day:")
				print(f"\tBook Title: {suggest_book_title()}")
				print(f"\tPage: {suggest_page_number()}\n")

				repetition = input("Would you like to get another suggestion? (yes/no): ")

	
		case 2:
			book_title = input("Enter the book title: ")

			add_books_to_archive(book_title)

			print("Book added successfully!")


		case 3:
			book_removal = input("Enter book to remove: ")

			remove_from_archive(book_removal)

			print("Book added successfully!")

		case 4:
			old_title = input("Enter the old title: ")

			remove_from_archive(old_title)

			new_title = input("Enter the new title")

			add_books_to_archive(new_title)

		case 5:
			print("All Books:")
			print(output_books_in_shelve())

		case _:
			back_to_menu = False
	
	
	