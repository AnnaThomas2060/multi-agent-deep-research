import pytest
from src.main import run_research
from unittest.mock import patch, MagicMock

@patch('src.main.Crew')
@patch('src.main.Task')
@patch('src.main.Agent')
def test_run_research_workflow(mock_agent, mock_task, mock_crew):
    mock_crew_instance = mock_crew.return_value
    mock_crew_instance.kickoff.return_value = "Final Report Generated"

    result = run_research("Test Query")
    
    assert result == "Final Report Generated"
    assert mock_crew.called

