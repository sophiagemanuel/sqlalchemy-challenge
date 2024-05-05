# sqlalchemy-challenge
Module 10 Challenge
For this module assignment I created a climate analysis of the Honolulu, Hawaii area.
In the file 'SurfsUp' is both files of my code.
The first part of my analysis is found in the Jupyter notebook file "climate_starter.ipynb" where I create an engine, reflect the database, save references to measurement and station, and create our session. I then created an Exploratory percipitaion Analysis by first finding the most recent date and then calculating a year from that date (2017-8-23 to 2016-8-23). With this, I preformed a query to retrieve the data and percipitation and ordered by the date and then saved these reults into a dataframe (sorting it by date). I then used Pandas with Matplotlib to plot the data, shown in this graph: 
![image](https://github.com/sophiagemanuel/sqlalchemy-challenge/assets/157437098/bf8de635-792c-4730-b7c2-4fa4c39e9484)

I then began my Exploratory Station Analysis by designing a query to find the number of stations and then find the most active station. With the most acticve station id (USC00519281) we found the lowest, highest, and average temperature and then plotted it as a histogram: 
![image](https://github.com/sophiagemanuel/sqlalchemy-challenge/assets/157437098/7e1dfb09-caa2-4a16-957e-85408a545112)

The second part of my analysis is found in the python file "app.py" where I imported my dependencies and then, like the previous part, reflected the database, save references to measurement and station, and create our session. I then setup our Flak and created app routes for the welcome page, percipitation, stations, start, and start/end. At the end of my code I made sure to finish by adding " If __name__ == "__main": app.run(debug=True)" to make sure everything worked. 
