import pytest
from src.agents.research_agents import (
    create_orchestrator,
    create_search_agent,
    create_reading_agent,
    create_citation_agent,
    create_report_generator
)

def test_agent_creation():
    orchestrator = create_orchestrator()
    assert orchestrator.role == 'Research Orchestrator'
    
    search_agent = create_search_agent()
    assert search_agent.role == 'Web Search Specialist'
    assert len(search_agent.tools) > 0

    reading_agent = create_reading_agent()
    assert reading_agent.role == 'Content Synthesizer'
    assert len(reading_agent.tools) > 0

    citation_agent = create_citation_agent()
    assert citation_agent.role == 'Citation Manager'
    
    report_generator = create_report_generator()
    assert report_generator.role == 'Lead Report Generator'

