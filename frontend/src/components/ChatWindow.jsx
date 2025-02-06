import React, { useState } from "react";
import axios from "axios";

const ChatWindow = () => {
  const [query, setQuery] = useState("");
  const [responses, setResponses] = useState([]);

  const handleQuery = async () => {
    const response = await axios.post("http://localhost:8000/query/", { query });
    setResponses([...responses, { query, response: response.data.results }]);
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleQuery}>Send</button>
      <div>
        {responses.map((res, idx) => (
          <div key={idx}>
            <p><strong>You:</strong> {res.query}</p>
            <p><strong>Chatbot:</strong> {JSON.stringify(res.response)}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChatWindow;