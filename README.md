# 8. Exercise
This is a documentation for the eighth exercise from the subject I-PPDS.

# Application
Application is taking json data from [The internet Chuck Norris Databse](http://www.icndb.com/).

The application is just changing Chuck Norris in the joke for specific name from array.

# Sync version
Application get data from the server and print them out. As I said earlier we just specify name
to replace Chuck Norris in the joke. Application even print out category of the joke

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/08/images/sync.png)

# Async version
In async version of the application we added ***async*** to the ***jokes*** function because we know
we will have to wait until we get data from the server. ***Async*** is in main too because, main will
be doing a job of a scheduler. ***Await*** is used in moments where we want to wait to finish and operation.

![Bad Release](https://raw.githubusercontent.com/Rokulus/I-PPDS_Procka/08/images/async.png)

# Compare
-   In ***sync*** version of the application the time elapsed was: ***0.7092776298522949s***
-   In ***async*** version of the application the time elapse was: ***0.16270208358764648***

The diffrence in time is because while one task is waiting for session.get, the CPU is given to other task. So while one task is wating for response from the server the other task can be done in the meantime.

