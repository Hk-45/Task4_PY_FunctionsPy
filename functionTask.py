
#In this function example we combine the firstname and lastname and get result fullname
def functionNew(firstName, lastName) :
    print(f'firstName = {firstName}')
    print(f'lastName = {lastName}')
    print(f'fullName = {firstName + " " + lastName}')

functionNew('Rohit','Sharma')     
print()
functionNew('john','Abraham')     
print()   

#In this example we call function without argument so it uses the default value that we gave in function parameter. 
def functionTest(age = 24) :
    print(f'my age =', age)

functionTest(42)
functionTest(50)
functionTest()
print()

#create a bookstore function and insert some data in the function.
def bookStore(bookId, bookName, category, price, quantity) :
    print(f'bookId = {bookId}')
    print(f'bookName = {bookName}')
    print(f'category = {category}')
    print(f'price = {price}')
    print(f'quantity = {quantity}')

    return {
        'bookId' : bookId,
        'bookName' : bookName,
        'category' : category,
        'price' : price,
        'quantity': quantity
    }

bookInfo1 = bookStore(1, 'Progressive stable productivity', 'Fiction', 40, 5)
print(f'bookInfo1 = {bookInfo1}')
print()
bookInfo2 = bookStore(2, 'Re-engineered executive software', 'Mystery', 25, 2)
print(f'bookInfo2 = {bookInfo2}')
print()
bookInfo3 = bookStore(3, 'User-friendly cohesive parallelism', 'Romance', 32, 10)
print(f'bookInfo3 = {bookInfo3}')
print()
bookInfo4 = bookStore(4, 'Face-to-face upward-trending info-mediaries', 'scienceFiction', 42, 5)
print(f'bookInfo4 = {bookInfo4}')
print()


#create a Employee information function and insert data in the function
def employeeInfo(empId, empName, age, salary, experience, companyName) :
    print(f'empId = {empId}')
    print(f'empName = {empName}')
    print(f'age = {age}')
    print(f'salary = {salary}')
    print(f'experience = {experience}')
    print(f'companyName = {companyName}')

    return {
        'empId' : empId,
        'empName' : empName,
        'age' :age,
        'salary' : salary,
        'experience' : experience,
        'companyName' : companyName
    }

data = employeeInfo(1,'Rahul',24,25000,1,'google')
print(f'data = {data}')
print()
data = employeeInfo(2,'mira',30,74000,3,'infosys')
print(f'data = {data}')
print()
data = employeeInfo(3,'sam',28,250000,5,'google')
print(f'data = {data}')
print()
data = employeeInfo(4,'john',36,420000,8,'microsoft')
print(f'data = {data}')
print()