# data_engineer_seo_test

### 1. Data & ETL

You are given a datasets called _officer_snapshot.txt_. 

A "snapshot" captures the state of data at a given point in time. It contains a list of records describing Officers of UK companies and their roles.

An "Officer" refers to an individual who holds a specific role or position within a registered company.

The data is semi-structured with fields seperated by a mix of whitespace and `<` symbols. 
Not all fields are present in all rows.
Below is an example of how this data is structured.

![image.png](officer_snapshot.png)

Parse the raw data into a structured, tabular format, using the provided image as a reference.

### 2. Infrastructure Design

New updates are released daily and The CMA is developing an ongoing solution for applying these updates. 
These updates are released as static files on a website and can be downloaded programmatically via HTTP requests. 

Any solution must have the following requirements:
- can run on a daily schedule
- can download the relevant files and save them to local storage or the cloud
- can parse the new updates, similar to step 1, and apply them to the dataset
- can output the updated dataset to local storage or the cloud
- can notify developers of failures

Create a simple diagram (using any tooling of your choice) that expresses how this can be achieved. The diagram does not need to reference specific tools, a worklow diagram describing the process is also acceptable.

Comment on the potential advantages and disadvantages of your solution.

### 3. Scenario

The CMA is interested in developing a way to share the dataset created in steps 1 & 2. The intended audience could be technical, non-techinical, or both.   

Could you provide a solution to deliver this dataset, so that it can be used to retrieve the data filtered by company number and another field of your choosing.

You could focus on a simple web app, an API, or something else.

This solution should be deployable, and we would like it to be containerised. 
Could you please provide the Dockerfile that can run your solution. 

Note: To separate this question from question 1, a mock dataset is also acceptable.
