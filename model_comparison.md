# Ollama Model Comparison: Deep Semantic Analysis

This comparison evaluates the models based *strictly* on their ability to perform deep semantic abstraction.

**The Test Prompts:**
1. **File Names:** Invoices, receipts, resumes, cover letters, and photos.
2. **File Content:** Finance summary, budget review, expense report, cooking recipe, baking guide.

The true test of a taxonomist AI is whether it groups literal items (like "resume" and "cover letter") into higher-level abstract concepts (like "Career Documents" or "Professional Materials"), or if it simply parrots back literal groups (a bucket for resumes, a bucket for cover letters).

## Comparison Table

| Model | Semantic Abstraction Quality | Depth Analysis & Notes |
| :--- | :--- | :--- |
| **gemma4:e4b** | **Excellent** | **High Abstraction:** Grouped invoices & receipts into "Financial Records"; resumes & cover letters into "Professional Documents". For content, grouped all money-related text into "Financial Records" and food into "Recipes and Cooking Guides". Perfect abstraction. |
| **gemma_4_12b** | **Excellent** | **High Abstraction:** Created "Financial Records", "Photos", and "Career Documents". For content, abstracted everything into "Finance" and "Culinary". Outstanding semantic reasoning. |
| **qwen_3.5_4b** | **Excellent** | **High Abstraction:** Grouped into "Financial Documents", "Personal Photos", and "Career Documents". For content, used "Financial Documents" and "Culinary Guides". Excellent grasp of underlying concepts. |
| **qwen_3_4b** | **Good** | **Moderate Abstraction:** Successfully combined "Resume and Cover Letters" and abstracted content into "Finance" and "Cooking". However, it left Invoices and Receipts as separate literal buckets. |
| **gemma4:e2b** | **Good** | **Literal but Logical:** Created literal buckets (Invoices, Photos, Receipts) and grouped resumes/letters into "Personal Documents". For content, slightly granular ("Finance and Budgeting" separate from "Expense Reports"). |
| **qwen_3_8b** | **Poor (Too Literal)** | **Overly Granular:** Failed to abstract. It created separate buckets for "Resumes" and "Cover Letters", and separate buckets for "Finance" and "Budgeting". It thinks like a keyword-matcher, not a taxonomist. |
| **gemma_3_4b** | **Poor (Redundant)**| **Flawed:** Separated "Resumes" and "Letters". For content, it redundantly separated "Recipes" and "Food Preparation Guides", showing a lack of semantic understanding that baking and cooking fall under the same domain. |
| **gemma_3_12b** | **Poor (Vague)** | **Flawed:** Created separate literal buckets, but grouped cover letters into a highly vague "Documents" category. |
| **qwen_3.5_9b**| **Failed** | Did not produce any output. |

## Key Observations

> [!TIP]
> **The True Intelligence Test: Abstraction**
> The best models (**`gemma4:e4b`**, **`gemma_4_12b`**, and **`qwen_3.5_4b`**) realized that a resume and a cover letter belong to a single parent concept: **Career/Professional Documents**. They also realized that an invoice and a receipt are both **Financial Records**. They didn't just group identical words; they grouped identical *concepts*.

> [!WARNING]
> **The Trap of Literal Matching**
> Models like **`qwen_3_8b`** and the **`gemma_3` family** fell into the trap of literal matching. They saw resumes and made a "Resumes" folder. They saw cover letters and made a "Cover Letters" folder. This is poor taxonomy design, as it fails to reduce clutter through abstraction.

### Conclusion on Semantic Depth
When testing for actual "intelligence" (the ability to generalize and abstract concepts rather than just matching keywords):
- The `gemma4` family (especially `e4b` and `12b`) and `qwen_3.5_4b` excel at true semantic categorization.
- Larger models do not necessarily mean smarter abstractions. Ironically, `qwen_3_8b` was *worse* at abstracting concepts than its smaller `qwen_3.5_4b` counterpart, getting bogged down in overly granular, literal categories.
