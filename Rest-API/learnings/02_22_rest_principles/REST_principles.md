### REST Principles

1. **Resource:**
   - Everything in REST is a resource – an identifiable piece of information or service.

2. **URI (Uniform Resource Identifier):**
   - Resources are accessed and manipulated using unique URIs.

3. **HTTP Methods:**
   - Standard HTTP methods (GET, POST, PUT/PATCH, DELETE) are used for operations on resources.

4. **Statelessness:**
   - REST is stateless; each request contains all information needed, and no client state is stored on the server.

5. **Representation:**
   - Resources can have multiple representations (e.g., JSON, XML), and clients interact with them through these representations.

6. **Uniform Interface:**
   - RESTful APIs have a uniform and consistent interface for simplicity, including resource identification, manipulation through representations, self-descriptive messages, and HATEOAS.

7. **Stateless Communication:**
   - Communication between client and server is stateless, with each request being independent.

### Example

Consider a fictional bookstore API:

- **Resource:** Book
- **URI:** `/books`
- **HTTP Methods:**
  - `GET /books`: Retrieve all books.
  - `GET /books/123`: Retrieve details of Book ID 123.
  - `POST /books`: Create a new book.
  - `PUT /books/123`: Update Book ID 123.
  - `DELETE /books/123`: Delete Book ID 123.

