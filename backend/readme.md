# AI Demo Backend

The backend service uses Flask, Docker, and a custom AI agent. The backend provides API endpoints to start an AI agent, interact with it, and adjust its parameters dynamically.

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your system.
- **Docker Compose**: Ensure Docker Compose is installed.

### Setup and Run

1. **Clone the Repository**

   <pre><code>git clone https://github.com/yourusername/your-repo-name.git

cd your-repo-name</code></pre>

2. **Build and Start the Services**

   Use Docker Compose to build and start the backend service:

   <pre><code>docker-compose up --build</code></pre>

   This command will build the Docker images and start the containers.

3. **Verify the Backend**

   You can verify that the backend is running by visiting `http://localhost:5000` or by checking the logs:

   <pre><code>docker-compose logs</code></pre>

### API Endpoints

#### **Start the AI Agent**

- **Endpoint**: `/api/start`
- **Method**: `POST`
- **Description**: Initializes and starts the AI agent.
- **Request Payload** (JSON):
  
  <pre><code>{
    "name": "agent_snd",
    "resource_path": "documents/meowsmeowing.pdf",
    "chain_of_thought_bool": true,
    "model": "facebook-dpr-ctx_encoder-multiset-base",
    "chunk_size": 200,
    "overlap": 25,
    "creativity": 0.7,
    "new_course_bool": true

}</code></pre>

#### **Chat with the AI Agent**

- **Endpoint**: `/api/chat`
- **Method**: `POST`
- **Description**: Sends a message to the AI agent and receives a response.
- **Request Payload** (JSON):
  
  <pre><code>{
    "input": "Hello, how are you?"

}</code></pre>

#### **Adjust Agent Parameters**

- **Endpoint**: `/api/adjust_parameters`
- **Method**: `POST`
- **Description**: Adjusts the AI agent’s parameters. Defaults to current parameters unless changed.
- **Request Payload** (JSON):
  
  <pre><code>{
    "creativity": 0.9

}</code></pre>

### Stopping the Services

To stop the Docker containers, use:

<pre><code>docker-compose down</code></pre>
