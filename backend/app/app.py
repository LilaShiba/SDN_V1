from flask import Flask, request, jsonify
from agent import Agent as AiAgent

'''
Example Call
curl -X POST http://localhost:8008/api/start -H "Content-Type: application/json" -d '{
  "name": "agent_snd",
  "resource_path": "documents/meowsmeowing.pdf",
  "chain_of_thought_bool": true,
  "model": "facebook-dpr-ctx_encoder-multiset-base",
  "chunk_size": 200,
  "overlap": 25,
  "creativity": 0.7,
  "new_course_bool": true
}'



'''

app = Flask(__name__)

# Initialize a global agent variable to store the AiAgent instance
agent = None

@app.route('/api/start', methods=['POST'])
def start_agent():
    global agent
    data = request.json
    
    # Extract parameters from the JSON payload
    name = data.get('name')
    resource_path = data.get('resource_path')
    chain_of_thought_bool = data.get('chain_of_thought_bool')
    model = data.get('model')
    chunk_size = data.get('chunk_size')
    overlap = data.get('overlap')
    creativity = data.get('creativity')
    new_course_bool = data.get('new_course_bool')
    
    # Initialize the AiAgent with the provided parameters
    agent = AiAgent(
        name=name,
        resource_path=resource_path,
        chain_of_thought_bool=chain_of_thought_bool,
        model=model,
        chunk_size=chunk_size,
        overlap=overlap,
        creativity=creativity,
        new_course_bool=new_course_bool
    )
    
    result = agent.start_chat()
    return jsonify({"message": result})

@app.route('/api/chat', methods=['POST'])
def chat():
    global agent
    if agent is None:
        return jsonify({"error": "Agent not started"}), 400

    data = request.json
    input_str = data.get('input')
    
    result = agent.chat(input_str)
    return jsonify({"message": result})

@app.route('/api/adjust_parameters', methods=['POST'])
def adjust_parameters():
    global agent
    if agent is None:
        return jsonify({"error": "Agent not started"}), 400
    
    data = request.json
    
    # Adjust parameters only if they are provided in the request
    result = agent.adjust_parameters(
        name=data.get('name'),
        resource_path=data.get('resource_path'),
        chain_of_thought_bool=data.get('chain_of_thought_bool'),
        model=data.get('model'),
        chunk_size=data.get('chunk_size'),
        overlap=data.get('overlap'),
        creativity=data.get('creativity'),
        new_course_bool=data.get('new_course_bool')
    )
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(debug=True)
