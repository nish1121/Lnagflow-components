"""
Simple test for SOW Builder component

This test validates the basic functionality of the SOW Builder component
without requiring a full Langflow installation.
"""

import sys
import json
from datetime import datetime


class MockData:
    """Mock Data class for testing without Langflow dependency"""
    def __init__(self, text=None, data=None, **kwargs):
        self.text = text
        self.data = data or {}


class MockComponent:
    """Mock Component base class for testing"""
    pass


class MockInput:
    """Mock input classes for testing"""
    def __init__(self, name, display_name, info=None, required=False, multiline=False, 
                 options=None, value=None):
        self.name = name
        self.display_name = display_name
        self.info = info
        self.required = required
        self.multiline = multiline
        self.options = options
        self.value = value


class MockOutput:
    """Mock output class for testing"""
    def __init__(self, display_name, name, method):
        self.display_name = display_name
        self.name = name
        self.method = method


# Mock the Langflow imports
sys.modules['langflow'] = type(sys)('langflow')
sys.modules['langflow.custom'] = type(sys)('langflow.custom')
sys.modules['langflow.io'] = type(sys)('langflow.io')
sys.modules['langflow.schema'] = type(sys)('langflow.schema')

sys.modules['langflow.custom'].Component = MockComponent
sys.modules['langflow.io'].MessageTextInput = MockInput
sys.modules['langflow.io'].DropdownInput = MockInput
sys.modules['langflow.io'].Output = MockOutput
sys.modules['langflow.schema'].Data = MockData

# Now import the SOW Builder
from components.sow_builder import SOWBuilder


def test_sow_builder_markdown():
    """Test SOW Builder with Markdown format"""
    print("Testing SOW Builder - Markdown Format")
    print("=" * 60)
    
    # Create instance
    builder = SOWBuilder()
    
    # Set input values
    builder.project_name = "Test Project"
    builder.client_name = "Test Client"
    builder.project_objectives = "Deliver high-quality software solution"
    builder.scope_of_work = "Develop web application with user authentication"
    builder.deliverables = "Web app, Documentation, Training"
    builder.timeline = "Q1 2025 - Q2 2025"
    builder.resources = "2 developers, 1 designer"
    builder.location = "Remote"
    builder.payment_terms = "$50,000 total"
    builder.acceptance_criteria = "All tests pass, Client approval"
    builder.output_format = "Markdown"
    
    # Build SOW
    result = builder.build_sow()
    
    # Validate
    assert result.text is not None, "Result text should not be None"
    assert "# Statement of Work" in result.text, "Should have markdown header"
    assert "Test Project" in result.text, "Should contain project name"
    assert "Test Client" in result.text, "Should contain client name"
    assert "## 1. Project Objectives" in result.text, "Should have objectives section"
    
    print("✓ Markdown format test passed")
    print(f"Document length: {len(result.text)} characters")
    print()


def test_sow_builder_plain_text():
    """Test SOW Builder with Plain Text format"""
    print("Testing SOW Builder - Plain Text Format")
    print("=" * 60)
    
    builder = SOWBuilder()
    builder.project_name = "Test Project 2"
    builder.client_name = "Test Client 2"
    builder.project_objectives = "Complete project objectives"
    builder.scope_of_work = "Build and deploy system"
    builder.deliverables = "System, Docs"
    builder.timeline = "6 months"
    builder.resources = None  # Test optional field
    builder.location = None  # Test optional field
    builder.payment_terms = None  # Test optional field
    builder.acceptance_criteria = None  # Test optional field
    builder.output_format = "Plain Text"
    
    result = builder.build_sow()
    
    assert result.text is not None, "Result text should not be None"
    assert "STATEMENT OF WORK" in result.text, "Should have plain text header"
    assert "Test Project 2" in result.text, "Should contain project name"
    assert "1. PROJECT OBJECTIVES" in result.text, "Should have objectives section"
    
    print("✓ Plain text format test passed")
    print(f"Document length: {len(result.text)} characters")
    print()


def test_sow_builder_structured():
    """Test SOW Builder with Structured (JSON) format"""
    print("Testing SOW Builder - Structured Format")
    print("=" * 60)
    
    builder = SOWBuilder()
    builder.project_name = "Test Project 3"
    builder.client_name = "Test Client 3"
    builder.project_objectives = "Achieve project goals"
    builder.scope_of_work = "Implement features"
    builder.deliverables = "Feature A\nFeature B\nFeature C"
    builder.timeline = "Timeline details"
    builder.resources = "Resource details"
    builder.location = "On-site"
    builder.payment_terms = "Payment details"
    builder.acceptance_criteria = "Acceptance details"
    builder.output_format = "Structured"
    
    result = builder.build_sow()
    
    assert result.text is not None, "Result text should not be None"
    
    # Parse JSON to validate structure
    sow_data = json.loads(result.text)
    assert sow_data["document_type"] == "Statement of Work", "Should have document type"
    assert sow_data["metadata"]["project_name"] == "Test Project 3", "Should have project name"
    assert "sections" in sow_data, "Should have sections"
    assert "project_objectives" in sow_data["sections"], "Should have objectives"
    
    print("✓ Structured format test passed")
    print(f"JSON structure: {json.dumps(sow_data, indent=2)[:200]}...")
    print()


def test_list_formatting():
    """Test list formatting functionality"""
    print("Testing List Formatting")
    print("=" * 60)
    
    builder = SOWBuilder()
    
    # Test comma-separated list
    formatted = builder._format_list_items("Item A, Item B, Item C")
    assert "- Item A" in formatted, "Should format with bullets"
    assert "- Item B" in formatted, "Should format with bullets"
    
    # Test newline-separated list
    formatted = builder._format_list_items("Item 1\nItem 2\nItem 3")
    assert "- Item 1" in formatted, "Should format with bullets"
    assert "- Item 2" in formatted, "Should format with bullets"
    
    # Test already formatted list
    formatted = builder._format_list_items("- Already formatted\n- With bullets")
    assert "- Already formatted" in formatted, "Should preserve existing bullets"
    
    print("✓ List formatting test passed")
    print()


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("SOW BUILDER COMPONENT TEST SUITE")
    print("=" * 60 + "\n")
    
    try:
        test_sow_builder_markdown()
        test_sow_builder_plain_text()
        test_sow_builder_structured()
        test_list_formatting()
        
        print("=" * 60)
        print("ALL TESTS PASSED ✓")
        print("=" * 60)
        return True
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
