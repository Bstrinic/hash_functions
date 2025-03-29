# Assignment: Implement a Simple Hash Function in Python

## Introduction

Hashing is a method of mapping data of any size to fixed-size values. It is widely used in computer science, especially for fast data retrieval, password storage, data integrity checks, and more. This assignment involves implementing a simple hash function in Python, exploring collision handling, and understanding the role of salting in secure hashing.

---

## Objective

- Understand how hashing and hash functions work  
- Implement a basic hash function in Python  
- Observe and analyze hash collisions  
- Handle collisions using chaining  
- Learn about salting and its importance in secure hashing  

---

## Materials Needed

- Python programming environment or Google Colab  
- Internet access for research and collaboration  

---

## Pre-Lab Preparation

- Review the fundamentals of hashing and its real-world applications  
- Understand how hash functions work and how collisions occur  
- Learn about collision resolution techniques, especially chaining  
- Research the concept of salting and how it improves hash security  

---

## Description

In this assignment, you will create a basic hash function that maps input keys to hash values between 0 and 9. You will use a list of sample strings and examine the output of the hash function to observe collisions. To manage collisions, you'll implement a simple hash table using chaining. Additionally, you will explore salting by modifying your hash function to accept a salt and return a fixed-size, hexadecimal hash value. You'll also generate random salts and see how salting enhances security, particularly in password storage scenarios.

---

## Deliverables

- A Python script implementing:
  - A basic hash function  
  - A hash table with chaining for collision handling  
  - A salted hash function that outputs fixed-size hexadecimal values  
- A short report documenting:
  - Your observations  
  - The behavior of your hash functions  
  - The role and benefits of salting in secure hashing  

---

## Real-World Applications

- **Password Storage:** Salting prevents attackers from using precomputed hash databases (rainbow tables)  
- **Data Integrity:** Hashes verify whether data has been altered  
- **Blockchain:** Each block includes a hash of the previous block to maintain security  
- **File Verification:** Hashes are used to confirm files haven't been tampered with  
- **Caching and Indexing:** Hash tables enable fast data access in systems and databases  
