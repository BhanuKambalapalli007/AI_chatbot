import React from "react";
import ChatWindow from "./components/ChatWindow";

const App = () => {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">AI Chatbot</h1>
      <ChatWindow />
    </div>
  );
};

export default App;