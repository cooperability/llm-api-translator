# llm-api-translator
Simple script to reformat text objects passed to ChatGPT and Claude API, with the goal of achieving parity between results despite different input formats.

Addresses common challenges when working with multiple LLM providers:
- Standardizing message formats across different APIs
- Managing conversation history and system instructions
- Handling token limits and message ordering
- Providing a consistent interface regardless of the underlying LLM

## Usage
*Initialize translator*
```
translator = LLMAPITranslator()
```
*Create a conversation*
```
system_instructions = [
"You are a helpful assistant",
"Please be concise in your responses"
]
conversation = translator.create_conversation(system_instructions)
```
*Add messages*
```
conversation.add_message("user", "Hello!")
conversation.add_message("assistant", "Hi there!")
```
*Get formatted messages for different APIs*
```
openai_format = conversation.get_formatted_messages("gpt-4")
claude_format = conversation.get_formatted_messages("claude-3-opus")
```


## Features

- Unified message format
- Automatic API-specific formatting
- Token tracking and management
- Chronological message ordering
- System instruction handling
- Multi-conversation support

## PRD & Roadmap

### Current Version (1.0)
- Basic message formatting
- System instruction management
- Conversation history handling
- Support for OpenAI and Anthropic APIs

### Planned Features (2.0)
1. **Token Management**
   - Implement proper tokenizers for each LLM
   - Smart token budget allocation
   - Automatic message pruning

2. **Enhanced Conversation Management**
   - Conversation branching
   - Message threading
   - Conversation state persistence

3. **Additional Provider Support**
   - Add support for Cohere
   - Add support for Llama
   - Add support for local models

4. **Advanced Features**
   - Automatic retry handling
   - Rate limiting management
   - Streaming support
   - Async API support

5. **Monitoring & Analytics**
   - Token usage tracking
   - Response time monitoring
   - Cost estimation
   - Usage analytics

### Future Considerations
- Message validation middleware
- Custom formatting rules
- Cross-model response normalization
- Automatic model fallback
- Fine-tuning support