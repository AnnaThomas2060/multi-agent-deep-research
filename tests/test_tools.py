import pytest
from src.tools.search_tool import DuckDuckGoSearchTool
from src.tools.browse_page_tool import BrowsePageTool
from src.tools.memory_manager import CleanMemoryTool

def test_search_tool():
    tool = DuckDuckGoSearchTool()
    result = tool._run("test query")
    assert isinstance(result, str)
    assert "Title:" in result or "No results found" in result

def test_memory_manager():
    tool = CleanMemoryTool()
    long_text = "A" * 1000
    result = tool._run(long_text)
    assert len(result) < 1000
    assert "Compressed representation" in result

def test_browse_page_tool(monkeypatch):
    class MockResponse:
        content = b"<html><body><h1>Test</h1><p>Content</p></body></html>"
        def raise_for_status(self): pass

    import requests
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: MockResponse())
    
    tool = BrowsePageTool()
    result = tool._run("http://fake.com")
    assert "Test" in result
    assert "Content" in result

