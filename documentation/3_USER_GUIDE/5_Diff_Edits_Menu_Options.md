# Diff-Based Editing (DBE) Options

Diff-Based Editing (DBE) is SammyAI's specialized toolkit for visual text comparison and precision editing. It bridges the gap between AI-generated suggestions and your final creative control by presenting changes in a clear, manageable diff format.

---

## 1. Enable DBE Mode
This is the core toggle for AI-assisted editing.

*   **How it Works**: When enabled, SammyAI will no longer simply "talk" to you in the chat panel about changes. Instead, it generates a proposed revision that appears in a specialized **Diff Viewer**.
*   **Workflow**: You can review exactly what the AI wants to add, remove, or modify. If you like the result, click **Accept** to update your document; otherwise, click **Reject** to keep your original text.

## 2. Global Comparison Tools
SammyAI provides robust tools for manual text comparison, essential for version control and cross-referencing.

*   **Compare with File... (Ctrl+D)**: Select an external file (e.g., an older draft or a research document) to compare against your current workspace.
*   **Compare with Clipboard (Ctrl+Shift+D)**: Instantly compare your current text with whatever snippet you have copied. This is perfect for checking revisions made in external apps.

## 3. Applying External Patches
For advanced users, SammyAI supports standard developer-grade diff tools.

*   **Apply Diff from File...**: Select a `.diff` or `.patch` file to apply its changes directly to your current document. SammyAI will parse the patch and present it in the visual viewer for your final approval.

## 4. The Visual Diff Viewer
When performing a comparison or receiving an AI suggestion, the **Diff Viewer** window opens to facilitate your review.

![Diff Edit Window](pictures/SammyAI_v1_DiffEdit_Window.png)

*   **Red Highlights**: Text that is proposed for removal.
*   **Green Highlights**: New text proposed for addition.
*   **Accept/Reject Controls**: Located at the bottom of the window, these allow you to commit or discard the proposed changes with a single click.

---

> [!TIP]
> Use DBE mode when you want SammyAI to focus on technical polish, like fixing and improving dialogue flow, or ensuring consistent character voice across a chapter.
