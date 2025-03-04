from langchain_community.utilities import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///D:/sql_chatbot_api/chinook.db", sample_rows_in_table_info = 3)
print(db.table_info)


examples = [
    {   "input": "List all artists.", 
        "query": "SELECT * FROM Artist;"},
    {
        "input": "Find all albums for the artist 'AC/DC'.",
        "query": "SELECT * FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'AC/DC');",
    },
    {
        "input": "List all tracks in the 'Rock' genre.",
        "query": "SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock');",
    },
    {
        "input": "Find the total duration of all tracks.",
        "query": "SELECT SUM(Milliseconds) FROM Track;",
    },
    {
        "input": "List all customers from Canada.",
        "query": "SELECT * FROM Customer WHERE Country = 'Canada';",
    },
    {
        "input": "How many tracks are there in the album with ID 5?",
        "query": "SELECT COUNT(*) FROM Track WHERE AlbumId = 5;",
    },
    {
        "input": "Find the total number of Albums.",
        "query": "SELECT COUNT(DISTINT(AlbumId)) FROM Invoice;",
    },
    {
        "input": "List all tracks that are longer than 5 minutes.",
        "query": "SELECT * FROM Track WHERE Milliseconds > 300000;",
    },
    {
        "input": "Who are the top 5 customers by total purchase?",
        "query": "SELECT CustomerId, SUM(Total) AS TotalPurchase FROM Invoice GROUP BY CustomerId ORDER BY TotalPurchase DESC LIMIT 5;",
    },
    {
        "input": "How many employees are there",
        "query": 'SELECT COUNT(*) FROM "Employee"',
    },   
    {
        "input": "How many total artists are there?",
        "query": 'SELECT COUNT(*) FROM Artist;',
    },   
    {
        "input": "who are top 5 artists with most number of albums?",
        "query": 'SELECT artist_name, COUNT(album_id) AS album_count FROM albums GROUP BY artist_name ORDER BY album_count DESC LIMIT 5;',
    },
    {
        "input": "List all customers.",
        "query": "SELECT * FROM Customer;"
    },
    {
        "input": "Find the total number of tracks in each genre.",
        "query": "SELECT Genre.Name, COUNT(Track.TrackId) AS TotalTracks FROM Genre INNER JOIN Track ON Genre.GenreId = Track.GenreId GROUP BY Genre.Name;"
    },
    {
        "input": "Show all employees who report to a manager named 'Nancy Edwards'.",
        "query": "SELECT Employee.FirstName, Employee.LastName FROM Employee WHERE ReportsTo = (SELECT EmployeeId FROM Employee WHERE FirstName = 'Nancy' AND LastName = 'Edwards');"
    },
    {
        "input": "Find all customers in the USA.",
        "query": "SELECT FirstName, LastName, Country FROM Customer WHERE Country = 'USA';"
    },
    {
        "input": "Find all invoices for the customer with the first name 'John'.",
        "query": "SELECT * FROM Invoice WHERE CustomerId = (SELECT CustomerId FROM Customer WHERE FirstName = 'John');"
    },
    {
        "input": "List all tracks in the 'Jazz' genre.",
        "query": "SELECT * FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Jazz');"
    },
    {
        "input": "Find the artist of the album 'Let There Be Rock'.",
        "query": "SELECT Name FROM Artist WHERE ArtistId = (SELECT ArtistId FROM Album WHERE Title = 'Let There Be Rock');"
    },
    {
        "input": "Calculate the total sales amount from all invoices.",
        "query": "SELECT SUM(Total) FROM Invoice;"
    },
    {
        "input": "Find all employees who are Sales Agents.",
        "query": "SELECT * FROM Employee WHERE Title = 'Sales Support Agent';"
    },
    {
        "input": "List all albums released by the artist 'Metallica'.",
        "query": "SELECT Title FROM Album WHERE ArtistId = (SELECT ArtistId FROM Artist WHERE Name = 'Metallica');"
    },
    {
        "input": "Count the number of tracks in the 'Pop' genre.",
        "query": "SELECT COUNT(*) FROM Track WHERE GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Pop');"
    },
    {
        "input": "List all unique genres available in the database.",
        "query": "SELECT DISTINCT Name FROM Genre;"
    },
    {
        "input": "Find the name of the customer who made the largest purchase.",
        "query": "SELECT FirstName, LastName FROM Customer WHERE CustomerId = (SELECT CustomerId FROM Invoice WHERE Total = (SELECT MAX(Total) FROM Invoice));"
    },
    {
        "input": "Retrieve the names of all playlists that include tracks from the 'Classical' genre.",
        "query": "SELECT DISTINCT Playlist.Name FROM Playlist INNER JOIN PlaylistTrack ON Playlist.PlaylistId = PlaylistTrack.PlaylistId INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Track.GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Classical');"
    },
    {
        "input": "Find the top 3 artists with the most albums in the database.",
        "query": "SELECT Artist.Name, COUNT(Album.AlbumId) AS AlbumCount FROM Artist INNER JOIN Album ON Artist.ArtistId = Album.ArtistId GROUP BY Artist.Name ORDER BY AlbumCount DESC LIMIT 3;"
    },
    {
        "input": "Retrieve the names of customers who have purchased tracks from the 'Rock' genre along with the total amount they spent.",
        "query": "SELECT Customer.FirstName, Customer.LastName, SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS TotalSpent FROM Customer INNER JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId INNER JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId INNER JOIN Track ON InvoiceLine.TrackId = Track.TrackId WHERE Track.GenreId = (SELECT GenreId FROM Genre WHERE Name = 'Rock') GROUP BY Customer.CustomerId ORDER BY TotalSpent DESC;"
    },
    {
        "input": "List the names of employees who have supervised other employees along with the count of their direct reports.",
        "query": "SELECT Manager.FirstName, Manager.LastName, COUNT(Employee.EmployeeId) AS DirectReports FROM Employee INNER JOIN Employee AS Manager ON Employee.ReportsTo = Manager.EmployeeId GROUP BY Manager.EmployeeId ORDER BY DirectReports DESC;"
    },
    {
        "input": "Find the genre with the highest total track duration.",
        "query": "SELECT Genre.Name, SUM(Track.Milliseconds) AS TotalDuration FROM Genre INNER JOIN Track ON Genre.GenreId = Track.GenreId GROUP BY Genre.GenreId ORDER BY TotalDuration DESC LIMIT 1;"
    },
    {
        "input": "List the names of playlists that contain tracks by the artist 'The Beatles', and the total number of tracks in each playlist.",
        "query": "SELECT Playlist.Name, COUNT(DISTINCT PlaylistTrack.TrackId) AS TrackCount FROM Playlist INNER JOIN PlaylistTrack ON Playlist.PlaylistId = PlaylistTrack.PlaylistId INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId INNER JOIN Album ON Track.AlbumId = Album.AlbumId INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId WHERE Artist.Name = 'The Beatles' GROUP BY Playlist.Name ORDER BY TrackCount DESC;"
    }

]
print(len(examples))






