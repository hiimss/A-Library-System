CREATE TABLE Member(
	memberID	    VARCHAR(10)	NOT NULL,
    fName			VARCHAR(20) NOT NULL,
    lName			VARCHAR(20),
    faculty			VARCHAR(30) NOT NULL,
    phone			VARCHAR(8)  NOT NULL,
    eMail			VARCHAR(50) NOT NULL,
    fineAmount 	    VARCHAR(30) DEFAULT 0, #Whenever book is returned, fineAmount += (return_date - due_date)
    PRIMARY KEY (memberID));
    
CREATE TABLE Publisher(
	publisherName	VARCHAR(50) NOT NULL,
	PRIMARY KEY (publisherName));


CREATE TABLE Author(
	authorName VARCHAR(30) NOT NULL,
    PRIMARY KEY (authorName));
    

CREATE TABLE Book(
	accessionNumber  	 VARCHAR(15) NOT NULL,
    title 				 VARCHAR(100),
	ISBN 			 	 VARCHAR(20),
	publicationYear  	 VARCHAR(10), 
    publisherName    	 VARCHAR(50),
    memberID    	 	 VARCHAR(10), #Member that is loaning the book
    borrowDate   	 	 DATE NULL,
    dueDate     	 	 DATE NULL,
    returnDate		 	 DATE NULL,
    numOfReservations	 VARCHAR(15) DEFAULT 0, #if 0 means book can be borrowed by anyone if > 0 means it is reserved.
									 # ALTERNATIVE METHOD : COUNT the instances of accessionNumber in BookhasReservation. 
									 #Everytime a book is reserved +=1, 
                                     #Everytime it is borrowed by a reserved member or cancel reservation, -=1
    
    # Due Date will be derived attributes made using TRIGGER. 
	PRIMARY KEY (accessionNumber),
    FOREIGN KEY (memberID) references Member(memberID) ON DELETE CASCADE,
    FOREIGN KEY (publisherName) references Publisher(publisherName) ON UPDATE CASCADE
																	ON DELETE SET NULL);

#Records the Instance of reservation. Delete row once reservation fulfilled/cancelled.
#memberID can maximum appear twice in this table
#Check if member has a reservation when initiating borrow.
CREATE TABLE BookHasReservation(
	accessionNumber 	VARCHAR(15) NOT NULL,
    memberID			VARCHAR(10) NOT NULL,
    reserveDate	        DATE NOT NULL,
    
    PRIMARY KEY (accessionNumber, memberID),
    FOREIGN KEY (memberID) references Member(memberID) ON DELETE CASCADE, 
    FOREIGN KEY (accessionNumber) references Book(accessionNumber) ON DELETE CASCADE); 
    
#Many to Many Relationship so create new Table
CREATE TABLE BookHasAuthor(
	authorName    	 VARCHAR(30) NOT NULL,
    accessionNumber	 VARCHAR(15) NOT NULL,
    PRIMARY KEY (authorName, accessionNumber),
    FOREIGN KEY (authorName) references Author(authorName) ON DELETE CASCADE
														   ON UPDATE CASCADE,
    FOREIGN KEY (accessionNumber) references Book(accessionNumber) ON DELETE CASCADE
																   ON UPDATE CASCADE);
																
# When book is borrowed, UPDATE the book row with borrow_date, due_date and member id
CREATE TRIGGER DUE_DATETRIGGER BEFORE UPDATE ON Book
FOR EACH ROW SET 
	NEW.borrowDate = IFNULL(NEW.borrowDate, NOW()),
    NEW.dueDate = DATE_ADD(NEW.borrowDate, INTERVAL 14 DAY);


#Records Instance of payment ( When doing python, check if paidAmount == members fine amt )
CREATE TABLE FinePayment(
	memberID    VARCHAR(10) NOT NULL,
    paidAmount	VARCHAR(15),
    paymentDate DATE,
    PRIMARY KEY (memberID, paymentDate),
    FOREIGN KEY (memberID) references Member(memberID) ON DELETE CASCADE);
    
    
