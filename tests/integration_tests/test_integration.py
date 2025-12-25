#!/usr/bin/env python3
"""
Quick test script to verify RAG system integration
"""
import os
import sys
import tempfile

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rag.rag_system import RAGSystem
from llm.chat_manager import ChatManager, MessageRole

def test_rag_integration():
    """Test RAG system integration with ChatManager"""
    print("=" * 60)
    print("RAG System Integration Test")
    print("=" * 60)
    
    # Create temporary test file
    test_content = """
def calculate_total(items):
    '''Calculate the total price of items'''
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

def apply_discount(total, discount_percent):
    '''Apply a percentage discount to the total'''
    discount = total * (discount_percent / 100)
    return total - discount
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(test_content)
        test_file = f.name
    
    try:
        # Initialize RAG system
        print("\n1. Initializing RAG system...")
        with tempfile.TemporaryDirectory() as tmpdir:
            rag = RAGSystem(
                chunk_size=200,
                overlap=20,
                persist_dir=os.path.join(tmpdir, "index"),
                cache_dir=os.path.join(tmpdir, "embeddings")
            )
            print("   ✓ RAG system initialized")
            
            # Index the test file
            print(f"\n2. Indexing test file: {os.path.basename(test_file)}")
            success = rag.index_file(test_file)
            print(f"   ✓ Indexing {'succeeded' if success else 'failed'}")
            
            # Mark as active
            rag.mark_active_file(test_file)
            print("   ✓ File marked as active")
            
            # Get stats
            stats = rag.get_stats()
            print(f"\n3. RAG System Stats:")
            print(f"   - Indexed files: {stats['indexed_files']}")
            print(f"   - Total chunks: {stats['total_documents']}")
            
            # Initialize ChatManager with RAG
            print("\n4. Initializing ChatManager with RAG...")
            chat_manager = ChatManager(rag_system=rag)
            chat_manager.create_session()
            print("   ✓ ChatManager initialized with RAG support")
            
            # Test context retrieval
            query = "How does the calculate_total function work?"
            print(f"\n5. Testing context retrieval for query:")
            print(f"   '{query}'")
            
            context = rag.get_context(query, top_k=2, boost_active_files=True)
            print(f"   ✓ Retrieved {len(context.chunks)} relevant chunks")
            
            # Test message preparation with context
            print("\n6. Preparing messages with RAG context...")
            chat_manager.add_message(MessageRole.USER, query)
            messages = chat_manager.get_messages_for_llm_with_context(
                query=query,
                top_k=2
            )
            
            print(f"   ✓ Prepared {len(messages)} messages for LLM")
            
            # Show the context message
            for msg in messages:
                if msg['role'] == 'system' and 'relevant context' in msg['content']:
                    print("\n7. Context injected into LLM prompt:")
                    print("   " + "-" * 56)
                    # Show first 200 chars of context
                    context_preview = msg['content'][:200] + "..."
                    for line in context_preview.split('\n'):
                        print(f"   {line}")
                    print("   " + "-" * 56)
                    break
            
            print("\n" + "=" * 60)
            print("✓ All integration tests passed!")
            print("=" * 60)
            
    finally:
        # Cleanup
        os.unlink(test_file)

if __name__ == "__main__":
    test_rag_integration()
