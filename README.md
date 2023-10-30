# github-retriever
A kind of a crawler that fetchs info from a GitHub`s user that is inputed from Front-end

**Choice of Technology Stack:**
* Python: Python is a popular and versatile programming language, making it a good choice for web applications.
* Flask: Flask is a micro web framework for Python that is simple and easy to use, making it suitable for this small-scale application.
* MongoDB: MongoDB is a NoSQL database that's particularly useful when dealing with semi-structured data like JSON, which is common in web APIs.

**Application Structure:**
* The code follows a standard Flask application structure with routes, templates, and a MongoDB connection. This separation helps keep code organized and maintainable.

**Database Choice:**
* MongoDB was chosen as the database to store GitHub repository data. Since GitHub API responses are typically in JSON format, MongoDB's document-oriented database structure is a natural fit. It allows for flexible and efficient storage and retrieval of JSON-like data.

**GitHub API Request:**
* The code uses the requests library to make an HTTP GET request to the GitHub API. It checks for a successful response (HTTP status code 200) before proceeding. If the user is not found or if an error occurs, an appropriate message is displayed.

**User Interface:**
* Two HTML templates, index.html and repos.html, were used for the user interface. index.html contains a form to input the GitHub username, and repos.html displays the user's repositories. The use of templates allows for separation of concerns between the application logic and the presentation.

**Error Handling:**
* The code includes basic error handling to deal with situations where the user is not found or an error occurs during the GitHub API request. It provides user-friendly error messages.
