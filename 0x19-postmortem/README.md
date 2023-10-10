## Issue Summary:

    Duration of the outage: 2 hours, from 10:00am to 12:00pm PST
    Impact: Users were unable to search for or book properties on Airbnb.com, resulting in a 30% decrease in booking activity during the outage.
    Root Cause: A sudden increase in read requests overwhelmed the database, causing it to become unresponsive.

## Timeline:

    10:00am: The developer received monitoring alerts indicating that database response times were exceeding expected thresholds.
    10:05am: The developer investigated and identified a sudden increase in read requests as the likely cause of the issue.
    10:10am: The developer attempted to mitigate the issue by adding additional read replicas, but this did not resolve the issue.
    10:20am: The developer began investigating other possible causes, including network issues or a misconfigured load balancer.
    11:00am: After further investigation, the developer identified the root cause as an issue with the database, specifically a sudden increase in read requests.
    11:10am: The developer worked to stabilize the database by reducing the number of read requests and implementing a temporary fix to prevent a similar issue from occurring in the future.
    12:00pm: The issue was resolved, and normal booking activity resumed on Airbnb.com.

## Root Cause and Resolution:

    The root cause of the issue was a sudden increase in read requests, which overwhelmed the database and caused it to become unresponsive.
    To address the issue, the developer implemented a temporary fix to prevent a similar issue from occurring in the future. This included modifying the load balancer configuration to better distribute traffic and implementing additional monitoring and alerting to detect similar issues in the future.

## Corrective and Preventative Measures:

    To prevent similar issues from occurring in the future, the developer will:
        Conduct a thorough review of the database architecture to identify any potential scalability issues.
        Increase the capacity of the database to better handle sudden spikes in traffic.
        Implement more granular monitoring and alerting to detect potential issues before they become critical.
        Conduct regular load testing to identify potential bottlenecks and scalability issues.
