# LLM Parameter Settings

SammyAI allows you to fine-tune the behavior of your AI creation partner through advanced sampling parameters. Adjusting these settings can significantly influence the "personality" and creativity of the generated text.

![SammyAI Parameter Settings](pictures/SammyAI_v1_Parameters_Settings.png)

---

## 1. Temperature
Temperature controls the "randomness" or "creativity" of the model’s word choice.

*   **Low Temperature (e.g., 0.2 - 0.5)**: Makes the output more focused, deterministic, and conservative. Good for factual summaries or consistent technical writing.
*   **High Temperature (e.g., 0.8 - 1.0)**: Encourages the model to take risks and choose less probable words. This results in more diverse, innovative, and creative prose.
*   **Default (0.9)**: SammyAI defaults to 0.9, which provides a high degree of creative flair optimized for fiction and poetry.

## 2. Top-P (Nucleus Sampling)
Top-P is an alternative method for controlling diversity by limiting the AI to a "nucleus" of the most likely next words.

*   **How it Works**: The model considers only the top percentage of most probable words whose cumulative probability adds up to P.
*   **Effect**: Reducing Top-P can help prune away nonsensical or highly irrelevant word choices, making the AI more coherent while still allowing for creative variation.
*   **Default (0.9)**: Combined with a high temperature, a Top-P of 0.9 ensures a broad yet high-quality vocabulary for your creative drafts.

## 3. Adjusting Settings
You can access these controls via the **Settings (gear)** icon in the sidebar.

1.  Use the **Sliders** to choose your desired balance between focus and creativity.
2.  Click **Apply** to instantly update the parameters for all subsequent AI interactions in the current session.
3.  Values update in real-time on the UI labels so you can be precise with your configurations.

---

> [!TIP]
> If SammyAI feels too "repetitive," try slightly increasing the Temperature. If it feels too "unfocused" or "rambling," try slightly lowering the Top-P.
