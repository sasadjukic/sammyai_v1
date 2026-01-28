# Known Issues

This document tracks documented issues, behavioral tendencies, and technical limitations encountered when using SammyAI. These items are under active review for future improvements.

## LLM Behavior & Stylistic Tendencies

### Model Bias in Nominative Selection
Models such as `Gemma 3:4B` and `Gemini 2.5 Flash` exhibit a recurring preference for specific character names (e.g., Lyra, Silas, Blackwood, etc...) when generating creative content without specific guidance.

> [!TIP]
> To increase name diversity, use highly specific prompts. For example: *"Suggest 10 female names popular in 16th-century England"* provides a broader selection than a general request for character names.

### Stylistic Defaults
By default, most underlying LLMs follow these conventions:
*   **Numeric Representation:** Quantities are rendered as numerals (e.g., `0.7`) rather than words (`zero point seven`).
*   **Symbolic Notation:** Special characters are rendered as symbols (e.g., `β`) rather than spelled out (`beta`).
*   **Temporal Formatting:** Time is consistently rendered in numeric blocks (e.g., `07:34:24`).

## Language & Formatting

### Cross-Language Pollination
In extended sessions or scenarios involving very large context windows, models may occasionally inject non-English characters (frequently Chinese) into responses. This is a known phenomenon across most current LLM architectures.

### Model-Specific Variations
*   **Kimi K2-1T (Regional Spelling):** This model may utilize UK English conventions (e.g., "colour", "optimise") despite the system's US English default.
*   **Kimi K2-1T (Structural Anomalies):** Occasionally, this model may produce irregular text structures, such as rendering single-sentence paragraphs in a vertical stack.

## System & Infrastructure Errors

The following issues typically relate to external service providers or local environment configurations:

*   **Authentication Errors:** Occur when API keys for cloud providers (e.g., Gemini, DeepSeek) are missing or incorrectly configured.
*   **Connectivity & Load:** Service interruptions may occur if provider servers are overwhelmed or temporarily unavailable.
*   **Rate Limiting:** Quota exhaustion errors are common when using free tiers or reaching daily usage limits.

