#!/usr/bin/env python
# src/deep_research_prompt_engineerer/main.py
import os

from deep_research_prompt_engineerer.crew import DeepResearchPromptEngineerer

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the crew.
    """
    inputs = {
        'research_question': 'Produce a data-driven, step-by-step market opportunity analysis for AI meeting-transcription and conversation-intelligence tools. The end-goal is to identify specific market gaps and recommend 2-3 high-conviction startup opportunities',
        'prompt_guidelines_document_content': """
            Guidance for Writing a Good Prompt for AI Deep Research:

            To get the most out of AI Deep Research tools like ChatGPT, Gemini, Perplexity, etc., crafting a well-structured and comprehensive prompt is crucial. It's not just about asking a question; it's about guiding the AI to act as a highly capable, customized research analyst.

            Here's a detailed breakdown of the key components and best practices for writing effective Deep Research prompts:

            1. Clearly State Your Goal:

            Be explicit and actionable: Don't just ask a vague question. Define the precise objective of your research.

            Specify the desired output type: Do you need an overview, a recommendation, a comparison, a detailed step-by-step guide, or a mix?

            Example (Good): "Please briefly summarize SEO best practices for AI search engines, provide a checklist of concrete steps I can take to boost visibility of my content, and recommend a specific tool that can help me with this."

            Example (Bad): "Help me understand how SEO for AI search works."

            2. Provide Comprehensive Context:
            This is arguably the most critical step, as it allows the AI to tailor the report to your specific situation, rather than providing generic information.

            Basic facts about your business/situation: Include details like your product, business model, industry, target market, or geographical location.

            Audience of the report: Who is this report for (e.g., yourself, your CEO, a technical team)? What is their level of familiarity with the topic? This influences the tone, depth, and terminology.

            Constraints: Are there any specific limitations or things your company won't consider? (e.g., "we only use open-source tools," "our budget for this is X").

            Downstream use: What decision or action are you hoping to make with this report? (e.g., "to decide on a new CRM system," "to prepare for an expert call," "to draft a new company policy").

            Proactive context gathering: If you're unsure what context is relevant, tell the AI to ask you follow-up questions for clarification before it starts the research.

            Example: "I'm planning to generate a Deep Research report on [X] in order to [Y]. What context should I provide so that I get a customized, actionable report? Pretend you have no context from any prior conversations."

            3. Specify the Desired Output Structure and Format:
            By default, AI reports can be dense walls of text. Guide the AI to present the information in a digestible and useful way.

            Content and Structure:

            Key inclusions: Dictate any specific elements you want in the deliverable (e.g., a specific comparison table, templates, code snippets, copy examples).

            Pyramid Principle: Request that the report leads with key takeaways or recommendations, both in the main summary and in each individual sub-section.

            Source overview: Ask for a summary of the sources used, including their type (government, commercial, news, blog), creation/update date, and how they were leveraged. This helps with vetting accuracy and bias.

            Format:

            Readability: Ask for bulleted lists, bolded text, and clear headings where appropriate.

            Tables: Specify a preference for tables over text summaries for comparisons or overviews.

            Summaries: For long reports, explicitly ask for a "TL;DR" summary at the beginning and/or summaries for each major section.

            4. Ask for the Research Plan and Provide Feedback:
            This is a critical iterative step to ensure the AI is on the right track before it expends significant resources.

            Request the plan: Always ask the Deep Research agent to share its proposed research plan before it starts working. Gemini does this by default, but for others (like ChatGPT), you need to explicitly ask.

            Review and provide feedback: Carefully examine the proposed plan for:

            Comprehensiveness: Is anything missing that you expected?

            Focus: Is the AI prioritizing the areas most important to you?

            Assumptions: Are there any implicit or explicit assumptions you disagree with? If so, provide clarifying context.

            Methodology: Do you agree with the evaluation or comparison criteria?

            Source prioritization: This is the time to specify if you want the AI to prioritize certain types of sources (e.g., peer-reviewed studies, official government data, independent third-party analysis, recent data only).

            Iterative refinement: Don't hesitate to refine your request based on the proposed plan. This back-and-forth ensures a much better final output.

            5. Provide Examples of Desired Output:

            If you have specific expectations for the report's look, tone, or content, provide examples. This is particularly useful if you're automating the creation of reports you used to do manually. Upload samples of best-in-class work as context.

        """
    }
    
    # Create and run the crew
    result = DeepResearchPromptEngineerer().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/deep_research_prompt.md")

if __name__ == "__main__":
    run()