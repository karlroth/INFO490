--create the table named flights
CREATE TABLE flights (
	year INT,
	month INT,
	dayOfMonth INT,
	dayOfWeek INT, 
	actualDepartureTime INT,
	scheduledDepartureTime INT,
	arrivalArrivalTime INT,
	scheduledArrivalTime INT,
	uniqueCarrierCode TEXT,
	flightNumber INT,
	tailNumber TEXT,
	actualElapsedTime INT,
	scheduledElapsedTime INT,
	airTime INT,
	arrivalDelay INT,
	departureDelay INT,
	originCode TEXT,
	destinationCode TEXT,
 	distance INT,
	taxiIn INT,
	taxiOut INT,
	cancelled INT,
	cancellationCode TEXT,
	diverted TEXT,
	carrierDelay INT,
	weatherDelay INT,
	nasDelay INT,
	securityDelay INT,
	lateAircraftDelay INT
) ;

--set the separator to comma
.separator ",";

--import the 2001.csv file into flights.
.import 2001.csv flights;

--delete the headers
DELETE FROM flights WHERE Year = 'Year';

--Count the rows in flights
SELECT COUNT(*) AS COUNT FROM flights;

--Create IATA table
CREATE TABLE iata (
	airportID INT,
	name TEXT,
	city TEXT,
	country TEXT,
	iata TEXT,
	icao TEXT,
	latitude REAL,
	longitude REAL,
	altidue INT,
	timeZone TEXT,
	dst TEXT,
	tzDatabaseTimeZone TEXT
) ;

--import data
.import iata.csv iata;

--Count the rows in iata
SELECT COUNT(*) AS COUNT FROM iata;

--Join the two tables together with originCity.
CREATE TABLE myTempTable 
AS SELECT f.month, f.dayOfMonth, f.uniqueCarrierCode, f.flightNumber, f.scheduledDepartureTime, f.diverted, i.city AS originCity   
FROM flights AS f, iata AS i
	WHERE f.originCode = i.iata;

--Perform a second Join to append the destination city column
CREATE TABLE myTable
AS SELECT t.month, t.dayOfMonth, t.uniqueCarrierCode, t.flightNumber, t.scheduledDepartureTime, t.diverted, t.originCity, i.city AS destinationCity
FROM myTempTable AS t, iata AS i
	WHERE flights.destinationCode = i.iata;

--Insert a datapoint into myTable
INSERT INTO myTable
	VALUES(9,9,'INFO', 490, 0800, 1, 'Champaign', 'Chicago');

--Compute average departureDelay column.
SELECT AVG(f.departureDelay) AS Average,
	MAX(f.departureDelay) AS Max,
	MIN(f.departureDelay) AS Min
FROM flights AS f;

--Select certain flights from table.
SELECT t.month, t.dayOfMonth, t.uniqueCarrierCode, t.flightNumber	
FROM myTable AS t
WHERE t.scheduledDepartureTime > 0745 AND t.scheduledDepartureTime < 0815
	AND originCity == 'Newark' AND destinationCity == 'San Francisco' 
	AND diverted == 1;

 


