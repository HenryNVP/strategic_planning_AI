# Chat: Sync vs Streaming Mode

## 📊 Quick Comparison

| Aspect | Sync Mode | Streaming Mode |
|--------|-----------|----------------|
| **Endpoint** | `POST /chatbot/chat` | `POST /chatbot/chat/stream` |
| **Response Type** | Single JSON | Server-Sent Events (SSE) |
| **User Experience** | Wait → Complete answer | Words appear immediately |
| **Use Case** | API integrations | Interactive chat UI |
| **Latency Feel** | Feels slower (wait for all) | Feels faster (see progress) |
| **Can Cancel?** | No | Yes (close stream) |
| **File Size** | Diagram: 21K | Diagram: 24K |

---

## 🔄 Sync Mode (Standard Request/Response)

### **How it works:**
```
User: "What is strategic planning?"
         ↓
    [3-5 seconds...]
         ↓
Response: "Strategic planning is a process that organizations..."
```

### **Flow:**
1. User sends complete question
2. Backend processes (RAG + LLM)
3. **Wait for complete response**
4. Return entire answer at once
5. Display to user

### **Pros:**
- ✅ Simple to implement
- ✅ Works with any HTTP client
- ✅ Easy error handling
- ✅ Good for APIs & integrations

### **Cons:**
- ❌ User sees nothing until complete
- ❌ Feels slow for long answers
- ❌ Can't cancel mid-generation
- ❌ Poor UX for interactive chat

**Diagram:** `A4_03a_flow_chat_sync.puml`

---

## ⚡ Streaming Mode (Real-time Token Delivery)

### **How it works:**
```
User: "What is strategic planning?"
         ↓
Response appears word-by-word:
"Strategic" → "planning" → "is" → "a" → "process" → ...
```

### **Flow:**
1. User sends complete question
2. Backend starts processing
3. **LLM generates tokens one-by-one**
4. Each token sent immediately via SSE
5. UI displays each word as it arrives
6. Final "done" signal sent

### **Pros:**
- ✅ Immediate visual feedback
- ✅ Feels much faster to user
- ✅ Can cancel mid-generation
- ✅ Better UX for long answers
- ✅ Like ChatGPT experience

### **Cons:**
- ❌ More complex to implement
- ❌ Requires SSE support
- ❌ Harder error handling
- ❌ Not ideal for non-UI clients

**Diagram:** `A4_03b_flow_chat_stream.puml`

---

## 🔧 Technical Details

### **Sync Mode Response:**
```json
{
  "messages": [
    {
      "role": "user",
      "content": "What is strategic planning?"
    },
    {
      "role": "assistant",
      "content": "Strategic planning is a process that organizations use to..."
    }
  ],
  "citations": ["doc_id_1", "doc_id_2"]
}
```

### **Streaming Mode Response (SSE):**
```
data: {"content": "Strategic", "done": false}

data: {"content": " planning", "done": false}

data: {"content": " is", "done": false}

...

data: {"content": "", "done": true}
```

---

## 🎯 When to Use Each Mode

### **Use Sync Mode when:**
- Building API integrations
- Non-interactive applications
- Batch processing
- Simple clients without SSE support
- Testing & debugging

### **Use Streaming Mode when:**
- Building chat interfaces
- Interactive web applications
- Long responses expected
- User experience is priority
- Need cancellation capability

---

## 💻 Implementation Notes

### **Backend (FastAPI):**
```python
# Sync mode
@router.post("/chatbot/chat")
async def chat(request: ChatRequest):
    response = await langgraph.invoke(...)
    return ChatResponse(messages=response)

# Streaming mode
@router.post("/chatbot/chat/stream")
async def chat_stream(request: ChatRequest):
    async for chunk in langgraph.astream(...):
        yield f"data: {json.dumps(chunk)}\n\n"
```

### **Frontend (JavaScript):**
```javascript
// Sync mode
const response = await fetch('/chatbot/chat', {...});
const data = await response.json();
displayMessage(data.messages);

// Streaming mode
const eventSource = new EventSource('/chatbot/chat/stream');
eventSource.onmessage = (event) => {
  const chunk = JSON.parse(event.data);
  if (!chunk.done) {
    appendToMessage(chunk.content);
  } else {
    eventSource.close();
  }
};
```

---

## 📚 Related Diagrams

- **Sync Flow**: `A4_03a_flow_chat_sync.puml` (21K)
- **Streaming Flow**: `A4_03b_flow_chat_stream.puml` (24K)
- **History Management**: `A4_03c_flow_chat_history.puml` (19K)

---

**Last Updated**: 2025-10-29

