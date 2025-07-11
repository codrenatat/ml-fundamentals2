from openai import AsyncOpenAI
from typing import List, Dict, Any, Callable
import json

class OpenAIClient:
    """Enhanced OpenAI client with function calling capabilities"""
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo", max_tokens: int = 1000, temperature: float = 0.7):
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.available_functions = {}
    
    def register_function(self, name: str, function: Callable, description: str, parameters: Dict[str, Any]):
        """Register a function that OpenAI can call"""
        self.available_functions[name] = {
            "function": function,
            "definition": {
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": parameters
                }
            }
        }
    
    def get_function_definitions(self) -> List[Dict[str, Any]]:
        """Get all registered function definitions for OpenAI"""
        return [func_data["definition"] for func_data in self.available_functions.values()]
    
    async def chat_completion(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Get chat completion from OpenAI with function calling support"""
        # Prepare the request
        request_params = {
            "model": self.model,
            "messages": messages,
            "max_tokens": kwargs.get('max_tokens', self.max_tokens),
            "temperature": kwargs.get('temperature', self.temperature)
        }
        
        # Add functions if available
        if self.available_functions:
            request_params["tools"] = self.get_function_definitions()
            request_params["tool_choice"] = "auto"
        
        response = await self.client.chat.completions.create(**request_params)
        
        # Handle function calls
        message = response.choices[0].message
        
        if message.tool_calls:
            # Add the assistant's message to conversation
            messages.append({
                "role": "assistant",
                "content": message.content,
                "tool_calls": [
                    {
                        "id": tool_call.id,
                        "type": tool_call.type,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    } for tool_call in message.tool_calls
                ]
            })
            
            # Execute function calls
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                if function_name in self.available_functions:
                    try:
                        # Execute the function
                        function_response = await self.available_functions[function_name]["function"](**function_args)
                        
                        # Add function response to messages
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": str(function_response)
                        })
                    except Exception as e:
                        # Add error response
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": f"Error: {str(e)}"
                        })
                else:
                    # Function not found
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": f"Error: Function {function_name} not found"
                    })
            
            # Get final response with function results
            final_response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=kwargs.get('max_tokens', self.max_tokens),
                temperature=kwargs.get('temperature', self.temperature)
            )
            
            return final_response.choices[0].message.content
        
        return message.content
    
    async def ask_financial_question(self, question: str, context: str = "") -> str:
        """Ask a financial question with function calling support"""
        system_message = {
            "role": "system",
            "content": """You are a helpful financial assistant with access to real-time financial data. 
            You can retrieve stock quotes, company overviews, historical data, and intraday data.
            Always use the available functions to get current, accurate financial information.
            Provide clear, helpful responses with the latest data."""
        }
        
        if context:
            user_content = f"Financial context:\n{context}\n\nQuestion: {question}"
        else:
            user_content = question
        
        user_message = {"role": "user", "content": user_content}
        
        return await self.chat_completion([system_message, user_message])
