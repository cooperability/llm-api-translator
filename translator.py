from typing import Dict, List, Optional, Union
import logging

logger = logging.getLogger(__name__)

class LLMMessage:
    """Standardized message format for cross-LLM compatibility"""
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class LLMConversation:
    """Manages conversation history with token tracking and chronological ordering"""
    def __init__(self, system_instructions: List[str], max_tokens: int = 16384):
        self.system_instructions = system_instructions
        self.max_tokens = max_tokens
        self.messages: List[LLMMessage] = []
        self._system_tokens = self._count_tokens("\n\n".join(system_instructions))
        
    def add_message(self, role: str, content: str):
        self.messages.append(LLMMessage(role=role, content=content))
        
    def get_formatted_messages(self, model: str) -> Union[List[Dict], Dict]:
        """Format messages according to LLM API requirements"""
        if model.startswith("gpt"):
            return self._format_openai()
        elif model.startswith("claude"):
            return self._format_claude()
        else:
            raise ValueError(f"Unsupported model: {model}")

    def _format_openai(self) -> List[Dict]:
        """Format for OpenAI ChatGPT API"""
        formatted = [{"role": "system", "content": instr} for instr in self.system_instructions]
        formatted.extend([{"role": m.role, "content": m.content} for m in self.messages])
        return formatted

    def _format_claude(self) -> Dict:
        """Format for Anthropic Claude API"""
        if not self.messages:
            # Claude requires at least one message
            self.add_message("user", "Let's begin.")
            
        return {
            "system": "\n\n".join(self.system_instructions),
            "messages": [{"role": m.role, "content": m.content} for m in self.messages]
        }

    def _count_tokens(self, text: str) -> int:
        """Placeholder for token counting - implement with preferred tokenizer"""
        # TODO: Implement proper token counting
        return len(text.split())

class LLMAPITranslator:
    """Main interface for cross-LLM API translation"""
    def __init__(self):
        self.supported_models = {
            "openai": ["gpt-3.5-turbo", "gpt-4"],
            "anthropic": ["claude-3-opus", "claude-3-sonnet"]
        }

    def create_conversation(
        self, 
        system_instructions: List[str],
        conversation_history: Optional[Dict[str, List[Dict]]] = None,
        max_tokens: int = 16384
    ) -> LLMConversation:
        """Create a new conversation with system instructions and optional history"""
        conv = LLMConversation(system_instructions, max_tokens)
        
        if conversation_history:
            for msgs in conversation_history.values():
                for msg in msgs:
                    conv.add_message(msg["role"], msg["content"])
                    
        return conv

    def validate_model(self, model: str) -> bool:
        """Check if model is supported"""
        for provider_models in self.supported_models.values():
            if model in provider_models:
                return True
        return False