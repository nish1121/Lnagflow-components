"""
Example Usage of SOW Builder Component

This file demonstrates how to use the SOW Builder component programmatically.
In Langflow, you would typically use the visual editor to configure these inputs.
"""

# Example inputs for the SOW Builder
example_sow_inputs = {
    "project_name": "AI-Powered Customer Service Platform",
    "client_name": "TechCorp Inc.",
    "project_objectives": """
    - Implement an AI-powered customer service platform to improve response times
    - Reduce customer support costs by 30%
    - Enhance customer satisfaction scores
    - Provide 24/7 automated support capabilities
    """,
    "scope_of_work": """
    **Inclusions:**
    - Design and development of conversational AI chatbot
    - Integration with existing CRM system
    - Training data preparation and model fine-tuning
    - Dashboard for monitoring and analytics
    - Knowledge base setup and management
    - Initial training for support staff
    
    **Exclusions:**
    - Hardware procurement
    - Third-party API costs
    - Ongoing maintenance beyond initial 3-month period
    - Custom integrations not specified in this document
    """,
    "deliverables": """
    Functional AI chatbot deployed on company website
    Mobile app integration (iOS and Android)
    Admin dashboard for monitoring conversations
    Documentation and user guides
    Training sessions for support team (2 sessions)
    30-day post-launch support
    """,
    "timeline": """
    - Week 1-2: Requirements gathering and design
    - Week 3-6: Development and initial testing
    - Week 7-8: Integration with CRM
    - Week 9-10: User acceptance testing
    - Week 11: Staff training and documentation
    - Week 12: Deployment and go-live
    - Week 13-24: Post-launch support and optimization
    """,
    "resources": """
    - 2 AI/ML Engineers
    - 1 Full-stack Developer
    - 1 UX/UI Designer
    - 1 Project Manager
    - Access to company CRM system
    - Cloud infrastructure (AWS/Azure)
    - Training data from historical support tickets
    """,
    "location": "Remote work with bi-weekly on-site meetings at TechCorp headquarters",
    "payment_terms": """
    Total Project Cost: $150,000
    
    Payment Schedule:
    - 30% ($45,000) upon contract signing
    - 40% ($60,000) upon completion of development and testing (Week 8)
    - 30% ($45,000) upon final delivery and go-live (Week 12)
    
    Payment method: Wire transfer within 15 days of invoice
    """,
    "acceptance_criteria": """
    - Chatbot achieves 85% accuracy on test queries
    - Response time under 2 seconds for 95% of queries
    - Successful integration with CRM system
    - All deliverables completed as specified
    - User acceptance testing sign-off by client
    - Staff training completed with feedback forms
    """,
}


def print_example_sow():
    """
    Print an example SOW document using the sample inputs above.
    
    Note: This is a simplified example. In actual Langflow usage, 
    the component would be connected to other components in a flow.
    """
    print("=" * 80)
    print("SOW BUILDER COMPONENT - EXAMPLE OUTPUT")
    print("=" * 80)
    print("\n")
    print("SAMPLE INPUTS:")
    print("-" * 80)
    for key, value in example_sow_inputs.items():
        print(f"\n{key.upper()}:")
        print(value[:200] if len(str(value)) > 200 else value)
        if len(str(value)) > 200:
            print("... (truncated)")
    
    print("\n" + "=" * 80)
    print("\nTo use this component in Langflow:")
    print("1. Import the component into your Langflow instance")
    print("2. Drag the 'SOW Builder' component onto the canvas")
    print("3. Connect input sources (text inputs, prompts, or other components)")
    print("4. Configure the required fields")
    print("5. Select your preferred output format (Markdown, Plain Text, or Structured)")
    print("6. Run the flow to generate your SOW document")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    print_example_sow()
    
    # Note: To actually instantiate and run the component, you would need
    # Langflow installed and properly configured. This example just shows
    # the expected inputs and usage pattern.
