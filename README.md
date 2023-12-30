# RabbitMQ Distributed Task Queue Demo

## Introduction

### What is RabbitMQ?
RabbitMQ is an open-source message broker that enables applications to communicate with each other using messages. It helps in decoupling the system's components, managing the workload distribution, and ensuring the reliability and scalability of your application. RabbitMQ supports multiple messaging protocols and can be easily integrated into various architectures.

### Objective of This Project
The objective of this project is to demonstrate the basic capabilities of RabbitMQ by setting up a distributed task queue system. We'll create a simple producer that sends messages representing tasks and a consumer that processes these tasks. The project aims to showcase message queuing, durability, fair message dispatch, and basic error handling using RabbitMQ.

## Installation and Setup

### Prerequisites
- Windows, Linux, or macOS -- I used windows/vscode
- Python 3.x -- I used 3.10, and of course use a venv
- Access to a terminal or command prompt as admin

### Installation Steps
1. **Install Erlang:**
   - Download and install the Erlang v 26.2.1 runtime from the official Erlang website.
2. **Install RabbitMQ Server:**
   - Download and install RabbitMQ Server v 3.12.11 from the official RabbitMQ website.
3. **Install pika:**
   
     ```bash
     pip install pika
     ```
4. **Enable RabbitMQ Management Plugin (Optional):**
   - Run the following command in the RabbitMQ Command Prompt:
     ```bash
     rabbitmq-plugins enable rabbitmq_management
     ```
5. **Test Your Installation:**
   - Access the RabbitMQ Management Console at http://localhost:15672/ (default login: guest/guest).

## Project Structure
- `producer/producer.py`: The script to publish messages (tasks) to the queue.
- `consumer/consumer.py`: The script to consume and process the messages from the queue.

## Code Explanation

### Producer Script (`producer.py`)
The producer script connects to the RabbitMQ server, creates a queue, and sends a series of task messages. It demonstrates how to declare a queue, create a persistent message, and publish it to the queue. Of course we used our industry standard "Hello World!" 

### Consumer Script (`consumer.py`)
The consumer script waits for messages from the RabbitMQ queue and processes them upon arrival. It showcases message acknowledgment, ensuring that messages are only removed from the queue after they have been fully processed.

## Testing and Demonstration

### What We Tested
- Message Queuing: Tested how messages are enqueued and dequeued in RabbitMQ.
- Durability: Ensured that messages persist even if the RabbitMQ service restarts.
- Fair Dispatch: Demonstrated how RabbitMQ distributes messages evenly among multiple consumers.

### Running the Scripts
1. **Start RabbitMQ Service:**
   - Ensure the RabbitMQ server is running.
2. **Run the Consumer Script:**
   - Execute `python consumer.py` to start the consumer.
3. **Run the Producer Script:**
   - Execute `python producer.py "Your message"` to send a new task.
4. **Observe the Results:**
   - Watch how messages are processed by the consumer script.

## Further Exercises
To further explore the capabilities of RabbitMQ and practice on your own, try the following exercises:
- Multiple Producers and Consumers:
  - Create multiple producer scripts sending different types of tasks and multiple consumers each handling a specific type of task.
- Priority Queuing:
  - Modify the queue to prioritize certain messages.
- Advanced Message Properties:
  - Experiment with different message properties like timestamps and headers.
- Integrate with a Real Application:
  - Apply what you've learned to integrate RabbitMQ into a real-world application you're working on or familiar with.

## Conclusion
This project provides a hands-on approach to understanding RabbitMQ and the principles of message queuing. By building and observing a simple distributed task queue, you've gained insights into how RabbitMQ operates and how it can be used to improve the scalability and reliability of applications.
