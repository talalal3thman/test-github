# 📂 Lesson: APIs in Python

This notebook introduces the fundamentals of Application Programming Interfaces (APIs) and demonstrates how to programmatically fetch and process web data using Python. 

---

## 🎯 Key Concepts Covered

*   **API Fundamentals:** Understanding what APIs are and how they allow different software applications to communicate.
*   **Making Requests:** Using the `requests` library to send HTTP `GET` requests to public API endpoints.
*   **JSON to DataFrame:** Parsing JSON responses (`response.json()`) and converting them directly into structured Pandas DataFrames using `pd.json_normalize()`.
*   **HTTP Status Codes:** Understanding common server responses (e.g., `200 OK`, `404 Not Found`, `500 Internal Server Error`).
*   **Error Handling:** Implementing `try-except` blocks to gracefully handle timeouts, connection issues, and invalid responses.
*   **Handling Pagination:** Using `while` and `for` loops with `limit` and `offset` parameters to extract multiple pages of data (applied to the Bahrain Open Data Portal).

---

## 🛠️ Required Libraries
To run the code in this notebook, ensure you have the following packages installed:
```bash
pip install requests pandas
