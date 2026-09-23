# Task 5: store favorite books 
def books():
    favorite_books = [
        ("To Kill a Mockingbird", "Harper Lee"),
        ("Project Hail Mary", "Andy Weir"),
        ("Pride and Prejudice", "Jane Austen"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("Jane Eyre", "Charlotte Brontë"),
    ]

    first_three = favorite_books[:3]
    print("First three books:")
    for title, author in first_three:
        print(f"{title} by {author}")
    return first_three

#Task 5: create a simple student database with names and IDs
def student_database():
    student_data = {
        "Alice Johnson": "12345",
        "Brian Smith": "56789",
        "Carla Diaz": "91011",
        "David Chen": "12131",
    }

    print("\nStudent database:")
    for name, student_id in student_data.items():
        print(f"{name}: {student_id}")
    return student_data


if __name__ == "__main__":
    books()
    student_database()