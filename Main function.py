figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
              
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")
figure.show()
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
              figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()
