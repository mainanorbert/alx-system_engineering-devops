# Web infrastructure design
This project covers concepts on web infrastructure  such as:
1. [DNS](#dns)
2. [Monitoring](#monitoring)
3. [Web Server](#web-server)
4. [Network basics](network - basics)
5. [Load balancer](load-balancer)
6. [Server](server)

For each project the following concepts are covered
## DNS
NS stands for Domain Name System. It is a system used to translate human-friendly domain names, like www.example.com, into IP addresses that computers use to identify each other on the network. In essence, DNS acts as the "phone book" of the internet, allowing users to access websites and other online resources using easily memorable domain names, while the underlying network infrastructure relies on numerical IP addresses for routing and communication.
Here's how DNS works:

1. When you type a domain name (e.g., www.example.com) into your web browser, your computer needs to find the IP address associated with that domain to connect to the web server.

2. Your computer first checks its local DNS cache to see if it already knows the IP address for the requested domain. If the information is found, your computer can make the connection directly.

3. If the IP address is not in the local cache or has expired, your computer sends a DNS query to a DNS resolver (usually provided by your internet service provider or a public DNS service like Google's 8.8.8.8).

5. The DNS resolver, if it doesn't already have the IP address in its cache, will contact a series of authoritative DNS servers, starting from the root DNS servers and working its way down through a hierarchy of DNS servers. These authoritative servers provide the IP address associated with the requested domain.

5. The IP address is returned to the DNS resolver, which caches the result and sends it back to your computer.

6. Your computer now uses the obtained IP address to establish a connection to the web server associated with the domain, allowing you to access the website.

DNS is crucial for the functioning of the internet as it simplifies the process of accessing online resources and makes it more user-friendly. Without DNS, users would have to remember and use numerical IP addresses for all their internet activities, which would be impractical.
## Monitoring
Monitoring in the context of web services and websites refers to the practice of continuously observing and collecting data about the performance, availability, and security of a web application or system. It helps ensure that a website or web service is functioning correctly, performs well, and is secure for users. Monitoring is essential for maintaining a high-quality user experience and preventing or quickly addressing issues.
Here are some aspects of monitoring in the web context:

1. Performance Monitoring: This involves tracking various performance metrics, such as page load times, server response times, and resource utilization (CPU, memory, and bandwidth). Performance monitoring helps identify bottlenecks and optimize the user experience.

2. Availability Monitoring: Availability monitoring ensures that a website or web service is accessible to users. It involves checking if the web application is up and running and responding to requests. Monitoring tools can send alerts when downtime or outages occur.
3. Error Monitoring: This involves detecting and logging errors, exceptions, and issues that may occur in the application. Error monitoring helps in identifying and addressing bugs or unexpected behavior.

4. Security Monitoring: Security monitoring focuses on identifying and mitigating security threats, such as unauthorized access attempts, DDoS attacks, or suspicious activities. It helps protect sensitive data and maintain the integrity of the system.

5. Log Monitoring: Log files contain valuable information about the functioning of a web application. Log monitoring involves analyzing log data to identify issues, troubleshoot problems, and gain insights into the application's behavior.

6. User Experience Monitoring: User experience monitoring involves tracking user interactions, user journeys, and the overall satisfaction of users with the website. This can include monitoring user engagement, conversion rates, and the effectiveness of user interfaces.
## Web Server
A web server is a software application or hardware device that serves web content to users over the internet or an intranet. It is a fundamental component of the World Wide Web and plays a crucial role in the process of delivering web pages, applications, and other online resources to users' web browsers. Web servers are responsible for handling client requests, processing them, and sending the appropriate response, usually in the form of HTML pages, images, or other web content.

Key characteristics and functions of a web server include:

1. Request Handling: Web servers receive and process requests from clients, which are typically web browsers. These requests can be for specific web pages, files, or resources.

2. Content Delivery: Web servers store and serve the web content, such as HTML documents, images, CSS stylesheets, JavaScript files, and more, in response to client requests.
3. Protocol Support: Web servers support various communication protocols, with HTTP (Hypertext Transfer Protocol) being the most common. HTTPS, a secure version of HTTP, is also widely used for encrypted communication.

4. IP Address and Domain Name Mapping: Web servers are associated with IP addresses or domain names (via DNS) that allow clients to locate and connect to the server on the internet.

5. Security: Web servers implement security features to protect against common threats, including unauthorized access, DDoS attacks, and other security vulnerabilities.

6. Load Balancing: In cases of high traffic, web servers may be configured to distribute incoming requests across multiple server instances to ensure efficient load balancing and prevent server overload.
7. Protocol Support: Web servers support various communication protocols, with HTTP (Hypertext Transfer Protocol) being the most common. HTTPS, a secure version of HTTP, is also widely used for encrypted communication.

8. IP Address and Domain Name Mapping: Web servers are associated with IP addresses or domain names (via DNS) that allow clients to locate and connect to the server on the internet.
Security: Web servers implement security features to protect against common threats, including unauthorized access, DDoS attacks, and other security vulnerabilities.

9. Load Balancing: In cases of high traffic, web servers may be configured to distribute incoming requests across multiple server instances to ensure efficient load balancing and prevent server overload.
